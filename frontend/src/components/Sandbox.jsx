import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Helmet } from 'react-helmet-async';
import { ArrowLeft, Play, Terminal, Loader2, Code2 } from 'lucide-react';
import Editor from '@monaco-editor/react';

const Sandbox = () => {
  const navigate = useNavigate();
  const [language, setLanguage] = useState('python');
  const [code, setCode] = useState('# Welcome to the Sandbox!\n# Write and test your code here.\n\nprint("Hello from Digital Era Sandbox!")\n');
  const [output, setOutput] = useState('');
  const [isRunning, setIsRunning] = useState(false);

  const handleRun = async () => {
    setIsRunning(true);
    setOutput('Running code...');
    
    try {
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
      setOutput(data.output || 'No output.');
    } catch (e) {
      setOutput(`Error: ${e.message}`);
    } finally {
      setIsRunning(false);
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
            onClick={handleRun}
            disabled={isRunning}
            className="btn-run"
            style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '8px 16px', opacity: isRunning ? 0.7 : 1 }}
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

        {/* Terminal Area */}
        <div style={{ width: '40%', display: 'flex', flexDirection: 'column', background: '#0d1117' }}>
          <div style={{ padding: '12px 16px', borderBottom: '1px solid var(--border)', display: 'flex', alignItems: 'center', gap: '8px', background: 'var(--surface2)' }}>
            <Terminal size={16} color="var(--text2)" />
            <span style={{ fontSize: '13px', fontWeight: 'bold', color: 'var(--text)' }}>Terminal</span>
          </div>
          <div style={{ flex: 1, padding: '16px', overflowY: 'auto' }}>
            <pre style={{ margin: 0, fontFamily: 'JetBrains Mono, monospace', fontSize: '14px', color: 'var(--text-bright)', whiteSpace: 'pre-wrap', wordBreak: 'break-all' }}>
              {output || 'Run your code to see output here.'}
            </pre>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Sandbox;
