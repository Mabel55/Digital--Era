import React, { useState, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import { Helmet } from 'react-helmet-async';
import { ArrowLeft, Play, Terminal, Loader2, Code2, Sparkles, MessageSquare } from 'lucide-react';
import Editor from '@monaco-editor/react';
import ReactMarkdown from 'react-markdown';
import { useAuth } from '../AuthContext';

const Sandbox = () => {
  const navigate = useNavigate();
  const [language, setLanguage] = useState('python');
  const [code, setCode] = useState('# Welcome to the Sandbox!\n# Write and test your code here.\n\nprint("Hello from Digital Era Sandbox!")\n');
  const [output, setOutput] = useState('');
  const [feedback, setFeedback] = useState(null);
  const [isRunning, setIsRunning] = useState(false);
  const [isReviewing, setIsReviewing] = useState(false);
  const [activeTab, setActiveTab] = useState('terminal'); // 'terminal' | 'review'
  const { token } = useAuth();

  // Pyodide loader for browser-based Python execution
  const loadPyodideRuntime = useCallback(async () => {
    if (!window.pyodide) {
      if (document.getElementById('pyodide-script') && window.loadPyodide) {
        window.pyodide = await window.loadPyodide({
          indexURL: "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/"
        });
      } else {
        const script = document.createElement('script');
        script.src = "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js";
        script.id = 'pyodide-script';
        document.head.appendChild(script);
        await new Promise(resolve => {
          script.onload = resolve;
        });
        window.pyodide = await window.loadPyodide({
          indexURL: "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/"
        });
      }
    }
    return window.pyodide;
  }, []);

  const handleRun = async () => {
    setIsRunning(true);
    setOutput('Executing...');
    setActiveTab('terminal'); // Automatically switch to terminal view
    
    try {
      if (language === 'python') {
        let pyodideInstance = window.pyodide;
        if (!pyodideInstance) {
          setOutput('⚡ Loading Python engine (first run)...');
          pyodideInstance = await loadPyodideRuntime();
        }
        
        pyodideInstance.runPython("import sys; import io; sys.stdout = io.StringIO()");
        pyodideInstance.runPython(code);
        const stdout = pyodideInstance.runPython("sys.stdout.getvalue()");
        setOutput(stdout || "No output.");
        
      } else if (language === 'javascript' || language === 'js') {
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
        setOutput(result || "No output.");
      } else {
        // Fallback for SQL
        const res = await fetch('/run-code/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            language,
            code,
            files: {},
            entrypoint: "solution.py"
          })
        });
        
        const data = await res.json();
        if (!res.ok) throw new Error(data.detail || "Server error");
        setOutput(data.output || 'No output.');
      }
    } catch (e) {
      setOutput(`Error: ${e.message}`);
    } finally {
      setIsRunning(false);
    }
  };

  const handleReviewCode = async () => {
    setIsReviewing(true);
    setFeedback('Analyzing your code...');
    setActiveTab('review'); // Automatically switch to review tab
    
    try {
      const res = await fetch('/review-code/', {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}` 
        },
        body: JSON.stringify({ code, language })
      });
      
      const data = await res.json();
      if (res.ok) {
        setFeedback(data.feedback);
      } else {
        setFeedback(`Error: ${data.detail}`);
      }
    } catch (e) {
      setFeedback(`Error: ${e.message}`);
    } finally {
      setIsReviewing(false);
    }
  };

  const handleLanguageChange = (e) => {
    const newLang = e.target.value;
    setLanguage(newLang);
    if (newLang === 'python') {
      setCode('# Python Sandbox\nprint("Hello World!")');
    } else if (newLang === 'javascript') {
      setCode('// JavaScript Sandbox\nconsole.log("Hello World!");');
    } else if (newLang === 'sql') {
      setCode('-- SQL Sandbox\nCREATE TABLE test (id INT, name TEXT);\nINSERT INTO test VALUES (1, "Alice");\nSELECT * FROM test;');
    }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100vh', background: 'var(--bg)' }}>
      <Helmet>
        <title>Sandbox | Digital Era Academy</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>
      {/* Topbar */}
      <div className="ws-topbar" style={{ display: 'flex', justifyContent: 'space-between', padding: '12px 24px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
          <button onClick={() => navigate('/dashboard')} className="ws-back-btn" style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <ArrowLeft size={16} /> Dashboard
          </button>
          <div style={{ fontWeight: 'bold', color: 'var(--text)', fontSize: '16px', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Code2 size={20} color="var(--accent)" /> Code Sandbox
          </div>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
          <select 
            value={language}
            onChange={handleLanguageChange}
            style={{ padding: '8px 12px', background: 'var(--surface2)', color: 'var(--text)', border: '1px solid var(--border)', borderRadius: '8px', cursor: 'pointer' }}
          >
            <option value="python">Python 3</option>
            <option value="javascript">JavaScript (Node)</option>
            <option value="sql">SQL (SQLite)</option>
          </select>
          <button 
            onClick={handleReviewCode}
            disabled={isReviewing || isRunning}
            style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '8px 16px', background: 'rgba(0, 229, 160, 0.1)', color: 'var(--accent)', border: '1px solid var(--accent)', borderRadius: '8px', fontWeight: 'bold', cursor: (isReviewing || isRunning) ? 'default' : 'pointer', opacity: (isReviewing || isRunning) ? 0.7 : 1 }}
          >
            {isReviewing ? <Loader2 size={16} className="spinner" style={{ animation: 'spin 1s linear infinite' }} /> : <Sparkles size={16} />}
            AI Review
          </button>
          <button 
            onClick={handleRun}
            disabled={isRunning || isReviewing}
            className="btn-run"
            style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '8px 16px', opacity: (isRunning || isReviewing) ? 0.7 : 1 }}
          >
            {isRunning ? <Loader2 size={16} className="spinner" style={{ animation: 'spin 1s linear infinite' }} /> : <Play size={16} fill="currentColor" />}
            Run Code
          </button>
        </div>
      </div>

      <div style={{ display: 'flex', flex: 1, overflow: 'hidden' }}>
        {/* Editor Area */}
        <div style={{ width: '60%', borderRight: '1px solid var(--border)' }}>
          <Editor
            height="100%"
            theme="vs-dark"
            language={language === 'js' ? 'javascript' : language}
            value={code}
            onChange={(val) => setCode(val)}
            options={{
              minimap: { enabled: false },
              fontSize: 16,
              padding: { top: 20 },
              scrollBeyondLastLine: false,
              fontFamily: 'JetBrains Mono, monospace'
            }}
          />
        </div>

        {/* Output & AI Review Area */}
        <div style={{ width: '40%', display: 'flex', flexDirection: 'column', background: '#0d1117' }}>
          
          {/* Tabs */}
          <div style={{ display: 'flex', background: 'var(--surface2)', borderBottom: '1px solid var(--border)' }}>
            <button 
              onClick={() => setActiveTab('terminal')}
              style={{ 
                flex: 1, padding: '12px', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px',
                background: activeTab === 'terminal' ? 'transparent' : 'rgba(0,0,0,0.2)',
                borderBottom: activeTab === 'terminal' ? '2px solid var(--accent)' : '2px solid transparent',
                color: activeTab === 'terminal' ? 'var(--text)' : 'var(--text2)',
                fontWeight: activeTab === 'terminal' ? 'bold' : 'normal',
                cursor: 'pointer'
              }}
            >
              <Terminal size={16} /> Terminal
            </button>
            <button 
              onClick={() => setActiveTab('review')}
              style={{ 
                flex: 1, padding: '12px', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px',
                background: activeTab === 'review' ? 'transparent' : 'rgba(0,0,0,0.2)',
                borderBottom: activeTab === 'review' ? '2px solid var(--accent)' : '2px solid transparent',
                color: activeTab === 'review' ? 'var(--text)' : 'var(--text2)',
                fontWeight: activeTab === 'review' ? 'bold' : 'normal',
                cursor: 'pointer'
              }}
            >
              <Sparkles size={16} /> AI Code Review
            </button>
          </div>

          <div style={{ flex: 1, padding: '20px', overflowY: 'auto' }}>
            {activeTab === 'terminal' ? (
              <pre style={{ margin: 0, fontFamily: 'JetBrains Mono, monospace', fontSize: '14px', color: 'var(--text-bright)', whiteSpace: 'pre-wrap', wordBreak: 'break-all' }}>
                {output || 'Run your code to see output here.'}
              </pre>
            ) : (
              <div style={{ color: 'var(--text)', fontSize: '15px', lineHeight: '1.6', fontFamily: 'Inter, sans-serif' }}>
                {feedback ? (
                  <ReactMarkdown>{feedback}</ReactMarkdown>
                ) : (
                  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100%', color: 'var(--text2)', marginTop: '40px' }}>
                    <MessageSquare size={48} style={{ marginBottom: '16px', opacity: 0.5 }} />
                    <p>Click "AI Review" in the top bar to get instant, AI-powered feedback on your code.</p>
                  </div>
                )}
              </div>
            )}
          </div>

        </div>
      </div>
    </div>
  );
};

export default Sandbox;
