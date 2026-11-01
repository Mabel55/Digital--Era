import React, { memo } from 'react';
import { Clock, Bug, CheckCircle2, XCircle, Terminal, Globe } from 'lucide-react';
import Editor from '@monaco-editor/react';

const getPreviewDoc = (userCode, language) => {
  if (language === 'css') {
    return `<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body { font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; padding: 24px; background: #ffffff; color: #0f172a; line-height: 1.6; }
    h1 { margin-top: 0; }
    .demo-divider { border: 0; border-top: 1px solid #e2e8f0; margin: 20px 0; }
    ${userCode}
  </style>
</head>
<body>
  <h1>Heading 1 (&lt;h1&gt;)</h1>
  <h2>Heading 2 (&lt;h2&gt;)</h2>
  <p>This paragraph demonstrates your custom CSS styles in action.</p>
  <hr class="demo-divider" />
  <div class="box card my-box">
    <h3>Box / Card Element</h3>
    <p>Testing margin, padding, borders, and colors.</p>
    <button class="btn">Styled Button</button>
  </div>
  <hr class="demo-divider" />
  <nav class="navbar">
    <div class="logo"><strong>Brand Logo</strong></div>
    <div class="nav-links"><a href="#home">Home</a> &bull; <a href="#courses">Courses</a> &bull; <a href="#contact">Contact</a></div>
  </nav>
</body>
</html>`;
  }

  // HTML mode
  if (userCode.toLowerCase().includes('<!doctype') || userCode.toLowerCase().includes('<html')) {
    return userCode;
  }
  return `<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body { 
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
      padding: 24px; 
      background: #ffffff; 
      color: #0f172a; 
      line-height: 1.6; 
    }
    img { max-width: 100%; height: auto; }
  </style>
</head>
<body>
  ${userCode}
</body>
</html>`;
};

const CodeEditorArea = ({
  lesson,
  mobileTab,
  determineLanguage,
  editorRef,
  code,
  handleCodeChange,
  hasError,
  handleFixMyCode,
  terminalClass,
  terminalOutput,
  executionTime,
  selectedOption,
  setSelectedOption,
  handleQuizSubmit,
  quizResult,
  outputTab = 'terminal',
  setOutputTab,
}) => {
  const lang = determineLanguage ? determineLanguage() : 'python';
  const isWeb = lang === 'html' || lang === 'css';

  const getFileName = () => {
    switch (lang) {
      case 'html': return 'index.html';
      case 'css': return 'styles.css';
      case 'javascript': return 'code.js';
      case 'sql': return 'code.sql';
      case 'c': return 'main.c';
      case 'go': return 'main.go';
      case 'rust': return 'main.rs';
      default: return 'code.py';
    }
  };

  if (lesson.type === 'quiz') {
    return (
      <div className={`ws-quiz-panel ${mobileTab === 'editor' ? 'mobile-active' : ''}`} style={{ flex: 1, padding: '40px', background: 'var(--surface)', margin: '20px', borderRadius: '12px', display: 'flex', flexDirection: 'column', gap: '20px', overflowY: 'auto' }}>
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
    );
  }

  return (
    <div className={`ws-editor-panel ${mobileTab === 'editor' ? 'mobile-active' : ''}`}>
      <div className="editor-toolbar" style={{ display: 'flex', justifyContent: 'space-between', padding: '8px 16px', borderBottom: '1px solid var(--border)' }}>
        <div className="file-tab">
          <div className="dot"></div> {getFileName()}
        </div>
        <button 
          onClick={() => { if(editorRef.current) editorRef.current.getAction('editor.action.formatDocument')?.run(); }}
          style={{ background: 'none', border: 'none', color: 'var(--text-dim)', cursor: 'pointer', fontSize: '12px' }}
        >
          Format Code
        </button>
      </div>
      <div style={{ flex: 1, minHeight: 0 }}>
        <Editor
          height="100%"
          language={lang}
          defaultLanguage={lang}
          theme="vs-dark"
          value={code}
          onChange={handleCodeChange}
          onMount={(editor) => editorRef.current = editor}
          options={{ minimap: { enabled: false }, fontSize: 14 }}
        />
      </div>
      <div className="terminal-panel">
        <div className="terminal-header" style={{ display: 'flex', justifyContent: 'space-between', width: '100%', alignItems: 'center' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <div className="terminal-dot dot-red"></div>
            <div className="terminal-dot dot-yellow"></div>
            <div className="terminal-dot dot-green"></div>

            {isWeb ? (
              <div style={{ display: 'flex', marginLeft: '10px', background: 'rgba(255,255,255,0.06)', borderRadius: '6px', padding: '2px', border: '1px solid var(--border)' }}>
                <button
                  type="button"
                  onClick={() => setOutputTab && setOutputTab('terminal')}
                  style={{
                    padding: '3px 10px',
                    fontSize: '11px',
                    borderRadius: '4px',
                    border: 'none',
                    background: outputTab === 'terminal' ? 'var(--accent)' : 'transparent',
                    color: outputTab === 'terminal' ? '#000000' : 'var(--text-dim)',
                    fontWeight: outputTab === 'terminal' ? 'bold' : 'normal',
                    cursor: 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '4px',
                    transition: 'all 0.15s ease'
                  }}
                >
                  <Terminal size={12} /> Terminal Output
                </button>
                <button
                  type="button"
                  onClick={() => setOutputTab && setOutputTab('preview')}
                  style={{
                    padding: '3px 10px',
                    fontSize: '11px',
                    borderRadius: '4px',
                    border: 'none',
                    background: outputTab === 'preview' ? 'var(--accent)' : 'transparent',
                    color: outputTab === 'preview' ? '#000000' : 'var(--text-dim)',
                    fontWeight: outputTab === 'preview' ? 'bold' : 'normal',
                    cursor: 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '4px',
                    transition: 'all 0.15s ease'
                  }}
                >
                  <Globe size={12} /> Browser Preview
                </button>
              </div>
            ) : (
              <span style={{ marginLeft: '8px' }}>Terminal Output</span>
            )}

            {executionTime > 0 && <span style={{ marginLeft: '12px', color: 'var(--text-dim)', fontSize: '11px', display: 'flex', alignItems: 'center', gap: '4px' }}><Clock size={12}/> {executionTime}ms</span>}
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
        {outputTab === 'preview' && isWeb ? (
          <div style={{ flex: 1, minHeight: 0, background: '#ffffff', overflow: 'hidden' }}>
            <iframe
              title="Browser Preview"
              srcDoc={getPreviewDoc(code, lang)}
              sandbox="allow-scripts"
              style={{ width: '100%', height: '100%', border: 'none', background: '#ffffff' }}
            />
          </div>
        ) : (
          <div id="terminal-output" className={terminalClass}>
            {terminalOutput}
          </div>
        )}
      </div>
    </div>
  );
};

export default memo(CodeEditorArea);
