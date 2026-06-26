import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';
import Editor from '@monaco-editor/react';
import { marked } from 'marked';
import { projectsManifest } from '../data/projects';

const ProjectWorkspace = () => {
  const { projectId } = useParams();
  const navigate = useNavigate();
  const { token, user } = useAuth();
  
  const project = projectsManifest[projectId];

  const [files, setFiles] = useState({});
  const [activeFile, setActiveFile] = useState('');
  const [terminalOutput, setTerminalOutput] = useState('');
  const [terminalClass, setTerminalClass] = useState('');
  const [isRunning, setIsRunning] = useState(false);

  useEffect(() => {
    if (project) {
      setFiles({ ...project.files });
      setActiveFile(project.entrypoint);
    }
  }, [project]);

  if (!project) {
    return <div style={{ color: 'white', padding: '20px' }}>Project not found</div>;
  }

  const handleRunProject = async () => {
    setIsRunning(true);
    setTerminalOutput('Executing Project...');
    setTerminalClass('');
    
    try {
      const res = await fetch('/run-code/', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          language: project.language,
          files: files,
          entrypoint: project.entrypoint
        })
      });
      const data = await res.json();
      
      if (!res.ok) {
        setTerminalOutput(`Error: ${data.detail || data.output}`);
        setTerminalClass('error');
      } else {
        setTerminalOutput(data.output || "No output.");
        setTerminalClass(data.exit_code !== 0 ? 'error' : 'success');
      }
    } catch (err) {
      setTerminalOutput("Execution failed. Ensure Docker is running.");
      setTerminalClass('error');
    } finally {
      setIsRunning(false);
    }
  };

  const determineLanguage = (filename) => {
    if (filename.endsWith('.py')) return 'python';
    if (filename.endsWith('.js')) return 'javascript';
    if (filename.endsWith('.md')) return 'markdown';
    return 'plaintext';
  };

  return (
    <div id="project-workspace" className="screen active" style={{ height: '100vh', display: 'flex', flexDirection: 'column' }}>
      <div className="ws-topbar" style={{ background: '#0f172a', padding: '10px 20px', display: 'flex', justifyContent: 'space-between', borderBottom: '1px solid #1e293b' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '20px' }}>
          <button className="ws-back-btn" onClick={() => navigate('/')} style={{ background: 'none', border: 'none', color: '#94a3b8', cursor: 'pointer', fontSize: '14px' }}>
            ← Dashboard
          </button>
          <div className="ws-course-title" style={{ color: 'white', fontWeight: 'bold' }}>{project.title}</div>
        </div>
        <div>
          <button 
            className="btn-run" 
            onClick={handleRunProject} 
            disabled={isRunning}
            style={{ padding: '8px 16px', background: '#22c55e', border: 'none', borderRadius: '4px', fontWeight: 'bold', cursor: isRunning ? 'not-allowed' : 'pointer' }}
          >
            ▶ {isRunning ? 'Running...' : 'Run Project'}
          </button>
        </div>
      </div>

      <div style={{ display: 'flex', flex: 1, overflow: 'hidden' }}>
        {/* File Explorer */}
        <div style={{ width: '250px', background: '#1e293b', borderRight: '1px solid #334155', display: 'flex', flexDirection: 'column' }}>
          <div style={{ padding: '15px', color: '#94a3b8', fontSize: '12px', fontWeight: 'bold', textTransform: 'uppercase', letterSpacing: '1px' }}>
            Explorer
          </div>
          <div style={{ flex: 1, overflowY: 'auto' }}>
            {Object.keys(files).map((filename) => (
              <div 
                key={filename}
                onClick={() => setActiveFile(filename)}
                style={{
                  padding: '10px 20px', 
                  color: activeFile === filename ? '#38bdf8' : '#e2e8f0',
                  background: activeFile === filename ? 'rgba(56, 189, 248, 0.1)' : 'transparent',
                  cursor: 'pointer',
                  borderLeft: activeFile === filename ? '3px solid #38bdf8' : '3px solid transparent',
                  display: 'flex', alignItems: 'center', gap: '10px', fontSize: '14px'
                }}
              >
                📄 {filename}
              </div>
            ))}
          </div>
        </div>

        {/* Editor & Terminal */}
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
          <div style={{ background: '#0f172a', padding: '10px 20px', display: 'flex', borderBottom: '1px solid #1e293b' }}>
            <div style={{ color: '#38bdf8', fontSize: '14px' }}>
              {activeFile}
            </div>
          </div>
          
          <div style={{ flex: 2, position: 'relative' }}>
            {determineLanguage(activeFile) === 'markdown' ? (
              <div style={{ padding: '30px', color: 'white', overflowY: 'auto', height: '100%' }} dangerouslySetInnerHTML={{ __html: marked(files[activeFile] || '') }}></div>
            ) : (
              <Editor
                height="100%"
                language={determineLanguage(activeFile)}
                theme="vs-dark"
                value={files[activeFile]}
                onChange={(value) => setFiles({ ...files, [activeFile]: value })}
                options={{ minimap: { enabled: false }, fontSize: 14 }}
              />
            )}
          </div>

          {/* Terminal */}
          <div style={{ flex: 1, background: '#020617', borderTop: '1px solid #1e293b', display: 'flex', flexDirection: 'column' }}>
            <div style={{ padding: '10px 20px', color: '#94a3b8', fontSize: '12px', borderBottom: '1px solid #1e293b', display: 'flex', alignItems: 'center', gap: '8px' }}>
              <div style={{ width: 10, height: 10, borderRadius: '50%', background: '#ef4444' }}></div>
              <div style={{ width: 10, height: 10, borderRadius: '50%', background: '#f59e0b' }}></div>
              <div style={{ width: 10, height: 10, borderRadius: '50%', background: '#22c55e' }}></div>
              <span style={{ marginLeft: '10px' }}>Terminal Output</span>
            </div>
            <div style={{ padding: '20px', color: terminalClass === 'error' ? '#ef4444' : '#22c55e', fontFamily: 'monospace', flex: 1, overflowY: 'auto', whiteSpace: 'pre-wrap' }}>
              {terminalOutput || '> Ready.'}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProjectWorkspace;
