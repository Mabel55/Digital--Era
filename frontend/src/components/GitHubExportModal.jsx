import React, { useState, useEffect } from 'react';
import { X, Github, ExternalLink, Loader, CheckCircle, AlertCircle } from 'lucide-react';
import api from '../api';

const GitHubExportModal = ({ isOpen, onClose, code, language, courseName }) => {
  const [token, setToken] = useState('');
  const [repoName, setRepoName] = useState('');
  const [status, setStatus] = useState('idle'); // idle, loading, success, error
  const [errorMessage, setErrorMessage] = useState('');
  const [repoUrl, setRepoUrl] = useState('');

  useEffect(() => {
    // Pre-fill repo name
    if (courseName) {
      const sanitized = courseName.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
      setRepoName(`digital-era-${sanitized}-capstone`);
    }
    // Load saved token
    const savedToken = localStorage.getItem('github_pat');
    if (savedToken) setToken(savedToken);
  }, [courseName]);

  const handleExport = async (e) => {
    e.preventDefault();
    if (!token || !repoName) return;

    setStatus('loading');
    setErrorMessage('');

    try {
      // Save token for future use
      localStorage.setItem('github_pat', token);

      const response = await api.post('/github/export', {
        token,
        repo_name: repoName,
        code,
        language
      });
      
      setRepoUrl(response.data.url);
      setStatus('success');
    } catch (error) {
      setStatus('error');
      setErrorMessage(error.response?.data?.detail || 'Failed to export to GitHub');
    }
  };

  if (!isOpen) return null;

  return (
    <div className="modal-overlay">
      <div className="modal-content github-modal">
        <button className="close-btn" onClick={onClose}><X size={20} /></button>
        
        <div className="modal-header">
          <div className="github-icon-wrapper">
            <Github size={28} />
          </div>
          <h2>Push to GitHub</h2>
          <p>Export your Capstone project directly to your GitHub portfolio.</p>
        </div>

        {status === 'success' ? (
          <div className="github-success-state">
            <CheckCircle size={48} className="success-icon" />
            <h3>Export Successful!</h3>
            <p>Your repository has been created with your code and a README.</p>
            <a href={repoUrl} target="_blank" rel="noopener noreferrer" className="btn btn-primary view-repo-btn">
              View on GitHub <ExternalLink size={16} />
            </a>
          </div>
        ) : (
          <div className="github-form-container">
            <div className="github-instructions">
              <h4>How to get a Token</h4>
              <ol>
                <li>Go to <a href="https://github.com/settings/tokens/new" target="_blank" rel="noopener noreferrer">GitHub Settings</a></li>
                <li>Write any Note (e.g. "Digital Era")</li>
                <li>Check the <strong>repo</strong> scope checkbox</li>
                <li>Click <strong>Generate token</strong> at the bottom</li>
              </ol>
            </div>

            <form onSubmit={handleExport} className="github-form">
              <div className="form-group">
                <label>Personal Access Token</label>
                <input 
                  type="password" 
                  value={token} 
                  onChange={(e) => setToken(e.target.value)}
                  placeholder="ghp_xxxxxxxxxxxxxxxxxxxx"
                  required
                />
              </div>

              <div className="form-group">
                <label>Repository Name</label>
                <input 
                  type="text" 
                  value={repoName} 
                  onChange={(e) => setRepoName(e.target.value)}
                  placeholder="my-cool-project"
                  required
                />
              </div>

              {status === 'error' && (
                <div className="error-message">
                  <AlertCircle size={16} />
                  <span>{errorMessage}</span>
                </div>
              )}

              <button 
                type="submit" 
                className="btn btn-primary submit-export-btn"
                disabled={status === 'loading'}
              >
                {status === 'loading' ? (
                  <><Loader className="spin" size={18} /> Pushing...</>
                ) : (
                  <><Github size={18} /> Create Repository</>
                )}
              </button>
            </form>
          </div>
        )}
      </div>
    </div>
  );
};

export default GitHubExportModal;
