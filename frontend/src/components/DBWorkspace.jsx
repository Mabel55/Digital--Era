import React, { useState, useEffect, useRef } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';
import Editor from '@monaco-editor/react';
import { marked } from 'marked';

const DBWorkspace = () => {
  const { courseId } = useParams();
  const navigate = useNavigate();
  const { token, user } = useAuth();
  
  const [course, setCourse] = useState(null);
  const [lessons, setLessons] = useState([]);
  const [currentLessonIdx, setCurrentLessonIdx] = useState(0);
  const [activeTab, setActiveTab] = useState('theory');
  const [code, setCode] = useState('');
  const [terminalOutput, setTerminalOutput] = useState('');
  const [terminalClass, setTerminalClass] = useState('');
  const [isRunning, setIsRunning] = useState(false);
  const [messages, setMessages] = useState([]);
  const [chatInput, setChatInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const [hasError, setHasError] = useState(false);
  
  const chatEndRef = useRef(null);

  useEffect(() => {
    fetchCourseData();
  }, [courseId]);

  const fetchCourseData = async () => {
    try {
      const cRes = await fetch(`/courses/${courseId}`);
      if (cRes.ok) {
        const cData = await cRes.json();
        setCourse(cData);
        
        const lRes = await fetch(`/courses/${courseId}/lessons`);
        if (lRes.ok) {
          const lData = await lRes.json();
          setLessons(lData);
          if (lData.length > 0) {
            loadLesson(0, lData);
          }
        }
      }
    } catch(e) {
      console.error(e);
    }
  };

  useEffect(() => {
    if (course) {
      setMessages([
        { sender: 'ai', text: `Hi ${user?.name?.split(' ')[0] || 'there'}! I'm your AI Tutor for **${course.title}**. Ask me anything!` }
      ]);
    }
  }, [course]);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isTyping]);

  const loadLesson = (idx, lessonList = lessons) => {
    setCurrentLessonIdx(idx);
    const lesson = lessonList[idx];
    if (!lesson) return;
    setCode('# Write your code here\n');
    setTerminalOutput('');
    setActiveTab('theory');
  };

  const handleRunCode = async () => {
    setIsRunning(true);
    setTerminalOutput('Evaluating...');
    setTerminalClass('');
    setHasError(false);
    
    const lesson = lessons[currentLessonIdx];
    if (!lesson) return;
    
    try {
      // Feature 2: Call auto-grading endpoint
      const res = await fetch(`/lessons/${lesson.id}/submit`, {
        method: "POST",
        headers: { 
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}` 
        },
        body: JSON.stringify({ code })
      });
      const data = await res.json();
      
      if (!res.ok) {
        setTerminalOutput(`Error: ${data.detail}`);
        setTerminalClass('error');
        setHasError(true);
      } else {
        setTerminalOutput(data.feedback || "No feedback.");
        const codeHasError = !data.passed;
        setTerminalClass(codeHasError ? 'error' : 'success');
        setHasError(codeHasError);
        
        if (!codeHasError) {
          // Feature 3: Grant XP and Progress via DB lesson_id
          if (token) {
            try {
              const progressRes = await fetch('/users/me/progress', {
                method: 'POST',
                headers: { 
                  'Content-Type': 'application/json',
                  'Authorization': `Bearer ${token}` 
                },
                body: JSON.stringify({ 
                  course_name: course.title, 
                  lesson_id: lesson.id
                })
              });
              
              if (progressRes.ok) {
                const userData = await progressRes.json();
                setTerminalOutput(prev => prev + `\n\n🎉 Lesson Passed! +10 XP Awarded! You are now level: ${userData.level}`);
              }
            } catch (e) {
              console.error("Failed to update progress", e);
            }
          }
        }
      }
    } catch (err) {
      setTerminalOutput("Execution failed. Server error.");
      setTerminalClass('error');
      setHasError(true);
    } finally {
      setIsRunning(false);
    }
  };

  const sendChat = async (e, directMessage = null) => {
    e?.preventDefault();
    const userMsg = directMessage || chatInput;
    if (!userMsg.trim()) return;

    setMessages(prev => [...prev, { sender: 'user', text: userMsg }]);
    if (!directMessage) setChatInput('');
    setIsTyping(true);
    
    const currentLesson = lessons[currentLessonIdx];

    try {
      const res = await fetch(`/chat`, {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}` 
        },
        // Feature 1: Context-Aware AI Chat sends lesson_id
        body: JSON.stringify({ message: userMsg, course: course?.title || "", lesson_id: currentLesson?.id })
      });
      const data = await res.json();
      setMessages(prev => [...prev, { sender: 'ai', text: data.answer || data.response || data.detail || "No response" }]);
    } catch (err) {
      setMessages(prev => [...prev, { sender: 'ai', text: "Sorry, I'm having trouble connecting to my brain right now." }]);
    } finally {
      setIsTyping(false);
    }
  };

  if (!course || lessons.length === 0) {
    return <div style={{color:'white', padding: '20px'}}>Loading Live Course...</div>;
  }

  const lesson = lessons[currentLessonIdx];
  const progressPct = ((currentLessonIdx + 1) / lessons.length) * 100;

  return (
    <div id="workspace" className="screen active" style={{ height: '100vh', display: 'flex', flexDirection: 'column' }}>
      <div className="ws-topbar">
        <div className="ws-topbar-left">
          <button className="ws-back-btn" onClick={() => navigate('/')}>
            ← Dashboard
          </button>
          <div className="ws-course-title">{course.title}</div>
          <div className="ws-lesson-nav">
            Lesson {currentLessonIdx + 1} of {lessons.length}
          </div>
        </div>
        <div className="ws-topbar-right">
          <button className="btn-run" onClick={handleRunCode} disabled={isRunning}>
            ▶ {isRunning ? 'Evaluating...' : 'AI Auto-Grade'}
          </button>
          <button className="btn-submit" onClick={() => {
            if (currentLessonIdx < lessons.length - 1) {
              loadLesson(currentLessonIdx + 1);
            } else {
              alert("Course completed!");
              navigate('/');
            }
          }}>
            {currentLessonIdx < lessons.length - 1 ? 'Next Lesson' : 'Finish Course'}
          </button>
        </div>
      </div>
      <div className="progress-strip">
        <div className="progress-strip-fill" style={{ width: `${progressPct}%` }}></div>
      </div>

      <div className="ws-layout">
        {/* Left Panel - Exercise */}
        <div className="ws-exercise">
          <div className="exercise-tabs">
            <div className={`ex-tab ${activeTab === 'theory' ? 'active' : ''}`} onClick={() => setActiveTab('theory')}>Lesson Content</div>
          </div>
          <div className="ex-tab-content">
            <div className="exercise-title">{lesson.title}</div>
            <div className="exercise-body" dangerouslySetInnerHTML={{ __html: marked(lesson.content || "No content") }}></div>
          </div>
        </div>

        {/* Middle Panel - Editor & Terminal */}
        <div className="ws-editor-panel">
            <div className="editor-toolbar">
            <div className="file-tab"><div className="dot"></div> solution.py</div>
          </div>
          <div style={{ flex: 1, minHeight: 0 }}>
            <Editor
              height="100%"
              defaultLanguage="python"
              theme="vs-dark"
              value={code}
              onChange={(value) => setCode(value)}
              options={{ minimap: { enabled: false }, fontSize: 14 }}
            />
          </div>
          <div className="terminal-panel">
            <div className="terminal-header" style={{ display: 'flex', justifyContent: 'space-between', width: '100%' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <div className="terminal-dot dot-red"></div>
                <div className="terminal-dot dot-yellow"></div>
                <div className="terminal-dot dot-green"></div>
                <span style={{ marginLeft: '8px' }}>AI Feedback Terminal</span>
              </div>
            </div>
            <div id="terminal-output" className={terminalClass}>
              {terminalOutput}
            </div>
          </div>
        </div>

        {/* Right Panel - AI Chat */}
        <div className="ws-chat">
          <div className="chat-header-bar">
            <div className="ai-avatar">🤖</div>
            <div className="ai-info">
              <div className="ai-name">Mabel Tutor</div>
              <div className="ai-status"><div className="status-dot"></div> Online (Context-Aware)</div>
            </div>
          </div>
          <div className="chat-messages">
            {messages.map((msg, i) => (
              <div key={i} className={`chat-msg ${msg.sender}`}>
                <div className="msg-bubble" dangerouslySetInnerHTML={{ __html: marked(msg.text) }}></div>
              </div>
            ))}
            {isTyping && (
              <div className="chat-msg ai">
                <div className="msg-bubble typing-indicator">
                  <span></span><span></span><span></span>
                </div>
              </div>
            )}
            <div ref={chatEndRef}></div>
          </div>
          <form className="chat-input-row" onSubmit={sendChat}>
            <textarea 
              className="chat-textarea" 
              placeholder="Ask for help..." 
              value={chatInput}
              onChange={e => setChatInput(e.target.value)}
              onKeyDown={e => {
                if (e.key === 'Enter' && !e.shiftKey) {
                  e.preventDefault();
                  sendChat();
                }
              }}
            />
            <button type="submit" className="chat-send-btn">↑</button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default DBWorkspace;
