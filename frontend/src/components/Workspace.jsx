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
    setCode(lesson.starterCode);
    setTerminalOutput('');
    setActiveTab('theory');
  };

  const handleRunCode = async () => {
    setIsRunning(true);
    setTerminalOutput('Executing...');
    setTerminalClass('');
    
    try {
      const res = await fetch('http://127.0.0.1:8000/run-python/', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code })
      });
      const data = await res.json();
      
      if (!res.ok) {
        setTerminalOutput(`Error: ${data.detail}`);
        setTerminalClass('error');
      } else {
        setTerminalOutput(data.output || "No output.");
        setTerminalClass(data.output.toLowerCase().includes('error') ? 'error' : 'success');
      }
    } catch (err) {
      setTerminalOutput("Execution failed. Ensure Docker is running.");
      setTerminalClass('error');
    } finally {
      setIsRunning(false);
    }
  };

  const sendChat = async (e) => {
    e?.preventDefault();
    if (!chatInput.trim()) return;

    const userMsg = chatInput;
    setMessages(prev => [...prev, { sender: 'user', text: userMsg }]);
    setChatInput('');
    setIsTyping(true);

    try {
      const res = await fetch(`http://127.0.0.1:8000/chat?message=${encodeURIComponent(userMsg)}&course_name=${encodeURIComponent(courseName)}`, {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await res.json();
      setMessages(prev => [...prev, { sender: 'ai', text: data.response }]);
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
          </div>
          <div className="ex-tab-content">
            <div className="exercise-title">{lesson.title}</div>
            <div className="exercise-body" dangerouslySetInnerHTML={{ __html: marked(activeTab === 'theory' ? lesson.theory : lesson.instructions) }}></div>
          </div>
        </div>

        {/* Middle Panel - Editor & Terminal */}
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
            <div className="terminal-header">
              <div className="terminal-dot dot-red"></div>
              <div className="terminal-dot dot-yellow"></div>
              <div className="terminal-dot dot-green"></div>
              <span style={{ marginLeft: '8px' }}>Terminal Output</span>
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
