import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';
import { ArrowLeft, Play, CheckCircle2, XCircle, Loader2 } from 'lucide-react';
import Editor from '@monaco-editor/react';
import ReactMarkdown from 'react-markdown';

const DailyChallenge = () => {
  const { token, user } = useAuth();
  const navigate = useNavigate();
  
  const [challenge, setChallenge] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  const [code, setCode] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [feedback, setFeedback] = useState(null);

  useEffect(() => {
    fetchChallenge();
  }, []);

  const fetchChallenge = async () => {
    setLoading(true);
    try {
      const res = await fetch('/daily-challenge/', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (!res.ok) throw new Error('Failed to load challenge');
      const data = await res.json();
      setChallenge(data);
      setCode(data.starter_code);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async () => {
    if (!code.trim()) return;
    setIsSubmitting(true);
    setFeedback(null);
    try {
      const res = await fetch('/daily-challenge/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          challenge_id: challenge.id,
          code: code
        })
      });
      const data = await res.json();
      setFeedback({
        passed: data.passed,
        message: data.message || data.feedback,
        xp: data.xp_gained
      });
      
      if (data.passed) {
        setChallenge(prev => ({ ...prev, already_completed: true }));
      }
    } catch (e) {
      setFeedback({ passed: false, message: 'Connection error. Try again.', xp: 0 });
    } finally {
      setIsSubmitting(false);
    }
  };

  if (loading) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100vh', background: 'var(--bg)' }}>
        <Loader2 size={40} color="var(--accent)" className="spinner" style={{ animation: 'spin 1s linear infinite' }} />
        <h2 style={{ color: 'var(--text)', marginTop: '20px' }}>Loading Daily Challenge...</h2>
      </div>
    );
  }

  if (error || !challenge) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100vh', background: 'var(--bg)' }}>
        <h2 style={{ color: '#ef4444' }}>Error</h2>
        <p style={{ color: 'var(--text-dim)' }}>{error || "Could not load challenge"}</p>
        <button onClick={() => navigate('/dashboard')} className="btn-run" style={{ marginTop: '20px' }}>Go Back</button>
      </div>
    );
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100vh', background: 'var(--bg)' }}>
      {/* Topbar */}
      <div className="ws-topbar" style={{ display: 'flex', justifyContent: 'space-between', padding: '12px 24px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
          <button onClick={() => navigate('/dashboard')} className="ws-back-btn" style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <ArrowLeft size={16} /> Dashboard
          </button>
          <div style={{ fontWeight: 'bold', color: 'var(--text)', fontSize: '16px' }}>
            Daily Challenge
          </div>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
          <span style={{ color: 'var(--accent2)', fontWeight: 'bold' }}>+{challenge.xp_reward} XP</span>
          {challenge.already_completed && <span style={{ color: 'var(--accent)', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '4px' }}><CheckCircle2 size={16} /> Completed</span>}
        </div>
      </div>

      <div style={{ display: 'flex', flex: 1, overflow: 'hidden' }}>
        {/* Left Side: Instructions */}
        <div style={{ width: '40%', borderRight: '1px solid var(--border)', display: 'flex', flexDirection: 'column', background: 'var(--surface)' }}>
          <div style={{ padding: '24px', overflowY: 'auto', flex: 1 }}>
            <div style={{ display: 'inline-block', padding: '4px 10px', background: 'var(--surface2)', borderRadius: '4px', fontSize: '12px', color: 'var(--text-dim)', marginBottom: '16px', fontWeight: 'bold', textTransform: 'uppercase' }}>
              {challenge.difficulty}
            </div>
            <h1 style={{ fontSize: '24px', color: 'var(--text)', marginBottom: '24px', fontWeight: 'bold' }}>{challenge.title}</h1>
            
            <div className="markdown-body" style={{ color: 'var(--text2)', lineHeight: 1.6 }}>
              <ReactMarkdown>{challenge.description}</ReactMarkdown>
            </div>
            
            {challenge.hint && (
              <div style={{ marginTop: '32px', padding: '16px', background: 'rgba(59, 130, 246, 0.1)', borderLeft: '4px solid #3b82f6', borderRadius: '4px' }}>
                <h4 style={{ color: '#3b82f6', marginBottom: '8px', fontSize: '14px', textTransform: 'uppercase', letterSpacing: '1px' }}>💡 Hint</h4>
                <p style={{ color: 'var(--text2)', fontSize: '14px' }}>{challenge.hint}</p>
              </div>
            )}
            
            {feedback && (
              <div style={{ marginTop: '24px', padding: '16px', background: feedback.passed ? 'rgba(0,229,160,0.1)' : 'rgba(239,68,68,0.1)', border: `1px solid ${feedback.passed ? 'var(--accent)' : '#ef4444'}`, borderRadius: '8px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontWeight: 'bold', color: feedback.passed ? 'var(--accent)' : '#ef4444', marginBottom: '8px' }}>
                  {feedback.passed ? <CheckCircle2 size={20} /> : <XCircle size={20} />}
                  {feedback.passed ? 'Success!' : 'Keep Trying'}
                </div>
                <p style={{ color: 'var(--text)', fontSize: '14px' }}>{feedback.message}</p>
                {feedback.passed && feedback.xp > 0 && (
                  <div style={{ marginTop: '8px', color: 'var(--accent2)', fontWeight: 'bold', fontSize: '14px' }}>
                    You earned +{feedback.xp} XP!
                  </div>
                )}
              </div>
            )}
          </div>
        </div>

        {/* Right Side: Editor */}
        <div style={{ width: '60%', display: 'flex', flexDirection: 'column' }}>
          <div style={{ padding: '12px 24px', borderBottom: '1px solid var(--border)', background: 'var(--surface2)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div style={{ color: 'var(--text)', fontWeight: 'bold', fontSize: '14px' }}>solution.py</div>
            <button 
              onClick={handleSubmit}
              disabled={isSubmitting || challenge.already_completed}
              className="btn-run"
              style={{ padding: '8px 16px', display: 'flex', alignItems: 'center', gap: '8px', opacity: (isSubmitting || challenge.already_completed) ? 0.6 : 1 }}
            >
              {isSubmitting ? <Loader2 size={16} style={{ animation: 'spin 1s linear infinite' }} /> : <Play size={16} fill="currentColor" />} 
              {challenge.already_completed ? 'Completed' : 'Submit Code'}
            </button>
          </div>
          <div style={{ flex: 1 }}>
            <Editor
              height="100%"
              theme="vs-dark"
              language={challenge.language || 'python'}
              value={code}
              onChange={(val) => setCode(val)}
              options={{
                minimap: { enabled: false },
                fontSize: 15,
                padding: { top: 20 },
                readOnly: challenge.already_completed,
                scrollBeyondLastLine: false,
                lineHeight: 24,
                fontFamily: 'JetBrains Mono, monospace'
              }}
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default DailyChallenge;
