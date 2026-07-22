import React, { useState, useEffect, useRef } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';
import Editor from '@monaco-editor/react';
import { marked } from 'marked';
import { courseManifest } from '../data/courses';
import LessonDiscussion from './LessonDiscussion';
import { ArrowLeft, Play, Terminal, CheckCircle2, XCircle, Bug, Bot, ArrowUp, PartyPopper, Home, RotateCcw } from 'lucide-react';

const Workspace = () => {
  const { courseId } = useParams();
  const navigate = useNavigate();
  const { token, user, subscription } = useAuth();
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
  const [showCelebration, setShowCelebration] = useState(false);
  const [showStory, setShowStory] = useState(true); // Story Mode State
  const [pyodide, setPyodide] = useState(null);
  
  // AI Limits State
  const [aiUsage, setAiUsage] = useState({ remaining: -1, limit: -1, isLimited: false });
  const isPro = subscription?.is_pro;
  
  const chatEndRef = useRef(null);

  useEffect(() => {
    const loadPyodideScript = async () => {
      if (!document.getElementById('pyodide-script')) {
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js';
        script.id = 'pyodide-script';
        script.async = true;
        document.body.appendChild(script);
        
        script.onload = async () => {
          try {
            const pyodideInstance = await window.loadPyodide();
            pyodideInstance.runPython(`
              import sys
              import io
              sys.stdout = io.StringIO()
            `);
            setPyodide(pyodideInstance);
            console.log("Pyodide loaded successfully.");
          } catch (e) {
            console.error("Pyodide load failed", e);
          }
        };
      }
    };
    loadPyodideScript();
  }, []);

  useEffect(() => {
    if (manifest && manifest.lessons.length > 0) {
      loadLesson(0);
    }
    setMessages([
      { sender: 'ai', text: `Hi ${user?.name?.split(' ')[0] || 'there'}! I'm your AI Tutor for **${courseName}**. Ask me anything!` }
    ]);
  }, [courseName]);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isTyping]);

  useEffect(() => {
    // Fetch initial AI usage limits for free users
    if (token && !isPro) {
      fetch('/ai-usage', { headers: { 'Authorization': `Bearer ${token}` } })
        .then(res => res.json())
        .then(data => {
          if (data.is_limited) {
            setAiUsage({
              remaining: Math.max(0, data.daily_limit - data.messages_used),
              limit: data.daily_limit,
              isLimited: true
            });
          }
        })
        .catch(e => console.error("Failed to fetch AI usage:", e));
    }
  }, [token, isPro]);

  const loadLesson = (idx) => {
    setCurrentLessonIdx(idx);
    const lesson = manifest.lessons[idx];
    setCode(lesson.starterCode || '');
    setTerminalOutput('');
    setActiveTab('theory');
    setSelectedOption(null);
    setQuizResult(null);
    setShowStory(true); // Always start in story mode for a new lesson
  };

  const determineLanguage = () => {
    const c = courseName.toLowerCase();
    if (c.includes('sql') || c.includes('database')) return 'sql';
    if (c.includes('frontend') || c.includes('javascript') || c.includes('react')) return 'javascript';
    return 'python'; // Default
  };

  const triggerProgressUpdate = async () => {
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
  };

  const handleRunCode = async () => {
    setIsRunning(true);
    setTerminalOutput('Executing...');
    setTerminalClass('');
    setHasError(false);
    
    const lang = determineLanguage();

    try {
      // 1. PYTHON CLIENT-SIDE (PYODIDE)
      if (lang === 'python' && pyodide) {
        try {
          pyodide.runPython("sys.stdout = io.StringIO()");
          pyodide.runPython(code);
          const stdout = pyodide.runPython("sys.stdout.getvalue()");
          setTerminalOutput(stdout || "No output.");
          setTerminalClass('success');
          triggerProgressUpdate();
        } catch (err) {
          setTerminalOutput(err.toString());
          setTerminalClass('error');
          setHasError(true);
        }
        setIsRunning(false);
        return;
      }
      
      // 2. JAVASCRIPT CLIENT-SIDE
      if (lang === 'javascript') {
        try {
            // Run JS in a sandboxed iframe to prevent access to parent page
            const result = await new Promise((resolve, reject) => {
              const iframe = document.createElement('iframe');
              iframe.sandbox = 'allow-scripts';
              iframe.style.display = 'none';
              document.body.appendChild(iframe);

              const timeout = setTimeout(() => {
                document.body.removeChild(iframe);
                reject(new Error('Execution timed out (5s limit)'));
              }, 5000);

              window.addEventListener('message', function handler(e) {
                if (e.source === iframe.contentWindow) {
                  clearTimeout(timeout);
                  window.removeEventListener('message', handler);
                  document.body.removeChild(iframe);
                  if (e.data.error) reject(new Error(e.data.error));
                  else resolve(e.data.logs || 'No output.');
                }
              });

              const sandboxedCode = `
                <script>
                  try {
                    const __logs = [];
                    const console = { log: (...a) => __logs.push(a.join(' ')), error: (...a) => __logs.push('Error: ' + a.join(' ')), warn: (...a) => __logs.push('Warning: ' + a.join(' ')) };
                    ${code}
                    parent.postMessage({ logs: __logs.join('\\n') }, '*');
                  } catch(e) {
                    parent.postMessage({ error: e.toString() }, '*');
                  }
                <\/script>
              `;
              iframe.srcdoc = sandboxedCode;
            });
            setTerminalOutput(result || "No output.");
            setTerminalClass('success');
            triggerProgressUpdate();
        } catch (err) {
            setTerminalOutput(err.toString());
            setTerminalClass('error');
            setHasError(true);
        }
        setIsRunning(false);
        return;
      }

      // 3. FALLBACK TO BACKEND DOCKER (C, SQL, Go, etc.)
      const res = await fetch('/run-code/', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code, language: lang })
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
          triggerProgressUpdate();
        }
      }
    } catch (err) {
      setTerminalOutput("Execution failed. Ensure backend/Docker is running.");
      setTerminalClass('error');
      setHasError(true);
    } finally {
      setIsRunning(false);
    }
  };

  const handleFixMyCode = () => {
    const prompt = `I am getting an error. Can you find the bug in my code **without giving me the full solution**? Tell me what line it is on, and give me a hint.\n\nHere is my code:\n\`\`\`${determineLanguage()}\n${code}\n\`\`\`\n\nError output:\n\`\`\`\n${terminalOutput}\n\`\`\``;
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

    if (aiUsage.isLimited && aiUsage.remaining <= 0 && !isPro) {
      setMessages(prev => [...prev, { sender: 'ai', text: "You've used all your free AI tutor messages for today. Upgrade to Pro for unlimited access!" }]);
      return;
    }

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
      
      if (res.status === 429) {
         setMessages(prev => [...prev, { sender: 'ai', text: "You've reached your daily AI limit. Please upgrade to Pro." }]);
         setAiUsage(prev => ({ ...prev, remaining: 0 }));
         return;
      }
      
      const data = await res.json();
      setMessages(prev => [...prev, { sender: 'ai', text: data.answer || data.response || data.detail || "No response" }]);
      
      // Update remaining messages if provided
      if (data.remaining_messages !== undefined && data.daily_limit !== undefined) {
        setAiUsage({
          remaining: Math.max(0, data.remaining_messages),
          limit: data.daily_limit,
          isLimited: data.daily_limit > 0
        });
      }
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
          <button 
            className="ws-back-btn" 
            onClick={() => navigate('/dashboard')} 
            style={{ display: 'flex', alignItems: 'center', gap: '6px' }}
            aria-label="Go back to Dashboard"
          >
            <ArrowLeft size={16} /> Dashboard
          </button>
          <div className="ws-course-title">{courseName}</div>
          <div className="ws-lesson-nav">
            Lesson {currentLessonIdx + 1} of {manifest.lessons.length}
          </div>
        </div>
        <div className="ws-topbar-right">
          {!showStory && lesson.type !== 'quiz' && (
            <button 
              className="btn-run" 
              onClick={handleRunCode} 
              disabled={isRunning} 
              style={{ display: 'flex', alignItems: 'center', gap: '6px' }}
              aria-label="Run Code"
            >
              <Play size={16} /> {isRunning ? 'Running...' : 'Run Code'}
            </button>
          )}
          <button className="btn-submit" onClick={() => {
            if (currentLessonIdx < manifest.lessons.length - 1) {
              loadLesson(currentLessonIdx + 1);
            } else {
              setShowCelebration(true);
            }
          }}>
            {currentLessonIdx < manifest.lessons.length - 1 ? 'Next Lesson' : 'Finish Course'}
          </button>
        </div>
      </div>
      <div className="progress-strip">
        <div className="progress-strip-fill" style={{ width: `${progressPct}%` }}></div>
      </div>

      {showStory ? (
        <div className="story-mode-container" style={{ flex: 1, display: 'flex', justifyContent: 'center', alignItems: 'center', background: 'var(--bg)', padding: '40px', overflowY: 'auto' }}>
          <div className="story-card" style={{ maxWidth: '800px', width: '100%', background: 'var(--surface)', padding: '60px', borderRadius: '16px', border: '1px solid var(--border)', boxShadow: '0 20px 60px rgba(0,0,0,0.5)', animation: 'slideUp 0.5s ease' }}>
            <h1 style={{ fontFamily: 'var(--font-display)', fontSize: '32px', color: 'var(--accent)', marginBottom: '24px' }}>{lesson.title}</h1>
            <div className="exercise-body story-body" dangerouslySetInnerHTML={{ __html: marked(lesson.theory || "No theory provided.") }} style={{ fontSize: '16px', lineHeight: '1.8', color: 'var(--text)', marginBottom: '40px' }}></div>
            <button 
              onClick={() => { setShowStory(false); if(lesson.starterCode) setCode(lesson.starterCode); }}
              className="btn-submit"
              style={{ width: '100%', padding: '16px', fontSize: '18px', display: 'flex', justifyContent: 'center', gap: '10px' }}
              aria-label="Start Practice"
            >
              <Terminal size={20} /> I'm Ready to Practice
            </button>
          </div>
        </div>
      ) : (
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
                `### Solution Code\n\n\`\`\`${determineLanguage()}\n` + (lesson.solution || 'No solution provided.') + '\n```'
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
              
              <LessonDiscussion lessonName={lesson.title} />
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
                  <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}><CheckCircle2 size={18} /> Correct!</div> {quizResult.includes('xp') && `+10 XP Awarded! You are now level: ${quizResult.split('_')[2]}`}
                </div>
              )}
              {quizResult === 'incorrect' && (
                <div style={{ padding: '16px', background: 'rgba(239, 68, 68, 0.1)', color: '#ef4444', borderRadius: '8px', fontWeight: 'bold' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}><XCircle size={18} /> Incorrect. Try again!</div>
                </div>
              )}
            </div>
          ) : (
            <div className="ws-editor-panel">
              <div className="editor-toolbar">
              <div className="file-tab"><div className="dot"></div> code.{determineLanguage() === 'javascript' ? 'js' : determineLanguage() === 'sql' ? 'sql' : 'py'}</div>
            </div>
            <div style={{ flex: 1, minHeight: 0 }}>
              <Editor
                height="100%"
                defaultLanguage={determineLanguage()}
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
                    <Bug size={14} /> Fix My Code
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
              <div className="ai-avatar" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}><Bot size={24} /></div>
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
            
            {/* AI Limits Banner */}
            {aiUsage.isLimited && !isPro && (
              <div style={{
                padding: '8px 12px', fontSize: '12px', textAlign: 'center',
                background: aiUsage.remaining === 0 ? 'rgba(239,68,68,0.1)' : 'rgba(245,158,11,0.1)',
                color: aiUsage.remaining === 0 ? 'var(--danger)' : 'var(--accent3)',
                borderTop: '1px solid var(--border)'
              }}>
                {aiUsage.remaining === 0 
                  ? "Daily AI limit reached. Upgrade to Pro for unlimited."
                  : `${aiUsage.remaining} free AI messages remaining today.`
                }
                <span 
                  onClick={() => navigate('/pricing')} 
                  style={{ fontWeight: 'bold', marginLeft: '6px', cursor: 'pointer', textDecoration: 'underline' }}
                >
                  Upgrade
                </span>
              </div>
            )}
            
            <form className="chat-input-row" onSubmit={sendChat}>
              <textarea 
                className="chat-textarea" 
                placeholder={aiUsage.isLimited && aiUsage.remaining === 0 && !isPro ? "Limit reached..." : "Ask for help..."} 
                value={chatInput}
                onChange={e => setChatInput(e.target.value)}
                disabled={aiUsage.isLimited && aiUsage.remaining === 0 && !isPro}
                onKeyDown={e => {
                  if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    sendChat();
                  }
                }}
              />
              <button 
                type="submit" 
                className="chat-send-btn"
                disabled={aiUsage.isLimited && aiUsage.remaining === 0 && !isPro}
                aria-label="Send message to AI Tutor"
              >
                <ArrowUp size={16} />
              </button>
            </form>
          </div>
        </div>
      )}

      {/* Course Completion Celebration */}
      {showCelebration && (
        <div 
          className="celebration-overlay" 
          onClick={() => { setShowCelebration(false); navigate('/dashboard'); }}
          role="dialog"
          aria-modal="true"
          aria-label="Course Completed Celebration"
        >
          <div className="celebration-card" onClick={e => e.stopPropagation()}>
            <div className="celebration-emoji"><PartyPopper size={64} color="var(--accent)" /></div>
            <div className="celebration-title">Course Complete!</div>
            <div className="celebration-subtitle">
              Congratulations! You've finished <strong>{courseName}</strong>. Keep the momentum going!
            </div>
            <div className="celebration-actions">
              <button 
                className="btn-primary" 
                style={{ padding: '12px 28px', borderRadius: '100px', width: 'auto' }}
                onClick={() => { setShowCelebration(false); navigate('/dashboard'); }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}><Home size={18} /> Back to Dashboard</div>
              </button>
              <button 
                className="returning-btn" 
                style={{ padding: '12px 28px', borderRadius: '100px', width: 'auto' }}
                onClick={() => { setShowCelebration(false); loadLesson(0); }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}><RotateCcw size={18} /> Review Course</div>
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Workspace;
