import React, { useState, useEffect, useRef } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';
import Editor from '@monaco-editor/react';
import { marked } from 'marked';
import { courseManifest } from '../data/courses';

const Workspace = () => {
  const { courseId } = useParams();
  const navigate = useNavigate();
  const { token, user } = useAuth();
  const courseName = decodeURIComponent(courseId);
  const manifest = courseManifest[courseName];

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
  const [selectedOption, setSelectedOption] = useState(null);
  const [quizResult, setQuizResult] = useState(null);
  
  const chatEndRef = useRef(null);

  useEffect(() => {
    if (manifest && manifest.lessons.length > 0) {
      loadLesson(0);
    }
    // Initialize chat with welcome message
    setMessages([
      { sender: 'ai', text: `Hi ${user?.name?.split(' ')[0] || 'there'}! I'm your AI Tutor for **${courseName}**. Ask me anything!` }
    ]);
  }, [courseName]);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isTyping]);

  const loadLesson = (idx) => {
    setCurrentLessonIdx(idx);
    const lesson = manifest.lessons[idx];
    setCode(lesson.starterCode || '');
    setTerminalOutput('');
    setActiveTab('theory');
    setSelectedOption(null);
    setQuizResult(null);
  };

  const handleRunCode = async () => {
    setIsRunning(true);
    setTerminalOutput('Executing...');
    setTerminalClass('');
    setHasError(false);
    
    try {
      const res = await fetch('/run-python/', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code })
      });
      const data = await res.json();
      
      if (!res.ok) {
        setTerminalOutput(`Error: ${data.detail}`);
        setTerminalClass('error');
        setHasError(true);
      } else {
        setTerminalOutput(data.output || "No output.");
        const codeHasError = data.output.toLowerCase().includes('error') || data.exit_code !== 0 || data.output.toLowerCase().includes('traceback');
        setTerminalClass(codeHasError ? 'error' : 'success');
        setHasError(codeHasError);
        
        if (!codeHasError) {
          // Grant XP and Progress
          const token = localStorage.getItem('token');
          if (token) {
            try {
              const progressRes = await fetch('/users/me/progress', {
                method: 'POST',
                headers: { 
                  'Content-Type': 'application/json',
                  'Authorization': `Bearer ${token}` 
                },
                body: JSON.stringify({ 
                  course_name: courseName, 
                  lesson_index: currentLessonIdx 
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
      setTerminalOutput("Execution failed. Ensure Docker is running.");
      setTerminalClass('error');
      setHasError(true);
    } finally {
      setIsRunning(false);
    }
  };

  const handleFixMyCode = () => {
    const prompt = `I am getting an error. Can you find the bug in my code **without giving me the full solution**? Tell me what line it is on, and give me a hint.\n\nHere is my code:\n\`\`\`python\n${code}\n\`\`\`\n\nError output:\n\`\`\`\n${terminalOutput}\n\`\`\``;
    sendChat(null, prompt);
  };

  const handleQuizSubmit = async () => {
    const lesson = manifest.lessons[currentLessonIdx];
    if (selectedOption === lesson.correctAnswer) {
      setQuizResult('correct');
      const token = localStorage.getItem('token');
      if (token) {
        try {
          const progressRes = await fetch('/users/me/progress', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
            body: JSON.stringify({ course_name: courseName, lesson_index: currentLessonIdx })
          });
          if (progressRes.ok) {
            const userData = await progressRes.json();
            setQuizResult(`correct_xp_${userData.level}`);
          }
        } catch (e) { console.error(e); }
      }
    } else {
      setQuizResult('incorrect');
    }
  };

  const sendChat = async (e, directMessage = null) => {
    e?.preventDefault();
    const userMsg = directMessage || chatInput;
    if (!userMsg.trim()) return;

    setMessages(prev => [...prev, { sender: 'user', text: userMsg }]);
    if (!directMessage) setChatInput('');
    setIsTyping(true);

    try {
      const res = await fetch(`/chat`, {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}` 
        },
        body: JSON.stringify({ message: userMsg, course: courseName })
      });
      const data = await res.json();
      setMessages(prev => [...prev, { sender: 'ai', text: data.answer || data.response || "No response" }]);
    } catch (err) {
      setMessages(prev => [...prev, { sender: 'ai', text: "Sorry, I'm having trouble connecting to my brain right now." }]);
    } finally {
      setIsTyping(false);
    }
  };

  if (!manifest) {
    return <div style={{color:'white', padding: '20px'}}>Course not found</div>;
  }

  const lesson = manifest.lessons[currentLessonIdx];
  const progressPct = ((currentLessonIdx + 1) / manifest.lessons.length) * 100;

  return (
    <div id="workspace" className="screen active" style={{ height: '100vh', display: 'flex', flexDirection: 'column' }}>
      <div className="ws-topbar">
        <div className="ws-topbar-left">
          <button className="ws-back-btn" onClick={() => navigate('/')}>
            ← Dashboard
          </button>
          <div className="ws-course-title">{courseName}</div>
          <div className="ws-lesson-nav">
            Lesson {currentLessonIdx + 1} of {manifest.lessons.length}
          </div>
        </div>
        <div className="ws-topbar-right">
          <button className="btn-run" onClick={handleRunCode} disabled={isRunning}>
            ▶ {isRunning ? 'Running...' : 'Run Code'}
          </button>
          <button className="btn-submit" onClick={() => {
            if (currentLessonIdx < manifest.lessons.length - 1) {
              loadLesson(currentLessonIdx + 1);
            } else {
              alert("Course completed!");
              navigate('/');
            }
          }}>
            {currentLessonIdx < manifest.lessons.length - 1 ? 'Next Lesson' : 'Finish Course'}
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
            <div className={`ex-tab ${activeTab === 'theory' ? 'active' : ''}`} onClick={() => setActiveTab('theory')}>Theory</div>
            <div className={`ex-tab ${activeTab === 'instructions' ? 'active' : ''}`} onClick={() => setActiveTab('instructions')}>Instructions</div>
            <div className={`ex-tab ${activeTab === 'solution' ? 'active' : ''}`} onClick={() => setActiveTab('solution')}>Solution</div>
          </div>
          <div className="ex-tab-content">
            <div className="exercise-title">{lesson.title}</div>
            <div className="exercise-body" dangerouslySetInnerHTML={{ __html: marked(
              activeTab === 'theory' ? lesson.theory : 
              activeTab === 'instructions' ? lesson.instructions : 
              '### Solution Code\n\n```python\n' + (lesson.solution || 'No solution provided.') + '\n```'
            ) }}></div>
            
            {(activeTab === 'theory' || activeTab === 'solution') && (
              <button 
                onClick={() => sendChat(null, `Please give me a detailed technical explanation of this lesson: "${lesson.title}". Explain the concepts and how the code works step-by-step.`)}
                style={{ 
                  marginTop: '20px', padding: '10px 16px', background: 'var(--surface)', 
                  color: 'var(--accent)', border: '1px solid var(--border)', 
                  borderRadius: '8px', cursor: 'pointer', fontWeight: 'bold',
                  display: 'flex', alignItems: 'center', gap: '8px'
                }}
              >
                Get Detail Explanation
              </button>
            )}
          </div>
        </div>

        {/* Middle Panel - Editor & Terminal OR Quiz */}
        {lesson.type === 'quiz' ? (
          <div className="ws-quiz-panel" style={{ flex: 1, padding: '40px', background: 'var(--surface)', margin: '20px', borderRadius: '12px', display: 'flex', flexDirection: 'column', gap: '20px', overflowY: 'auto' }}>
            <h2 style={{ color: 'var(--text-bright)' }}>{lesson.question}</h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
              {lesson.options.map((opt, i) => (
                <div 
                  key={i}
                  onClick={() => setSelectedOption(i)}
                  style={{
                    padding: '16px', borderRadius: '8px', border: `2px solid ${selectedOption === i ? 'var(--accent)' : 'var(--border)'}`,
                    background: selectedOption === i ? 'rgba(56, 189, 248, 0.1)' : 'transparent',
                    cursor: 'pointer', color: 'var(--text-bright)', fontSize: '16px', transition: 'all 0.2s'
                  }}
                >
                  {String.fromCharCode(65 + i)}. {opt}
                </div>
              ))}
            </div>
            <button 
              onClick={handleQuizSubmit}
              disabled={selectedOption === null}
              style={{
                marginTop: '20px', padding: '14px', background: 'var(--accent)', color: 'black', 
                fontWeight: 'bold', fontSize: '16px', borderRadius: '8px', border: 'none', 
                cursor: selectedOption === null ? 'not-allowed' : 'pointer', opacity: selectedOption === null ? 0.5 : 1
              }}
            >
              Submit Answer
            </button>
            {quizResult && quizResult.startsWith('correct') && (
              <div style={{ padding: '16px', background: 'rgba(34, 197, 94, 0.1)', color: '#22c55e', borderRadius: '8px', fontWeight: 'bold' }}>
                🎉 Correct! {quizResult.includes('xp') && `+10 XP Awarded! You are now level: ${quizResult.split('_')[2]}`}
              </div>
            )}
            {quizResult === 'incorrect' && (
              <div style={{ padding: '16px', background: 'rgba(239, 68, 68, 0.1)', color: '#ef4444', borderRadius: '8px', fontWeight: 'bold' }}>
                ❌ Incorrect. Try again!
              </div>
            )}
          </div>
        ) : (
          <div className="ws-editor-panel">
            <div className="editor-toolbar">
            <div className="file-tab"><div className="dot"></div> main.py</div>
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
                <span style={{ marginLeft: '8px' }}>Terminal Output</span>
              </div>
              {hasError && (
                <button 
                  onClick={handleFixMyCode}
                  style={{ 
                    background: 'rgba(239,68,68,0.15)', color: '#ef4444', 
                    border: '1px solid rgba(239,68,68,0.3)', borderRadius: '4px', 
                    padding: '3px 10px', fontSize: '11px', fontWeight: 'bold', 
                    cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '4px' 
                  }}
                >
                  🐛 Fix My Code
                </button>
              )}
            </div>
            <div id="terminal-output" className={terminalClass}>
              {terminalOutput}
            </div>
          </div>
          </div>
        )}

        {/* Right Panel - AI Chat */}
        <div className="ws-chat">
          <div className="chat-header-bar">
            <div className="ai-avatar">🤖</div>
            <div className="ai-info">
              <div className="ai-name">Mabel Tutor</div>
              <div className="ai-status"><div className="status-dot"></div> Online</div>
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

export default Workspace;
