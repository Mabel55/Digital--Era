import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';

const Assessment = () => {
  const { topic } = useParams();
  const { user, token } = useAuth();
  const navigate = useNavigate();
  
  const [questions, setQuestions] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  
  const [score, setScore] = useState(0);
  const [isFinished, setIsFinished] = useState(false);
  const [finalResult, setFinalResult] = useState(null);
  
  useEffect(() => {
    fetchQuestions();
  }, [topic]);
  
  const fetchQuestions = async () => {
    setLoading(true);
    try {
      const res = await fetch('/assessments/generate', {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          topic: topic,
          level: user?.level || 'Beginner'
        })
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || 'Failed to fetch assessment');
      
      setQuestions(data.questions);
    } catch (e) {
      setError(e.message);
    }
    setLoading(false);
  };
  
  const handleAnswer = (optionIndex) => {
    const isCorrect = optionIndex === questions[currentIndex].correctAnswer;
    if (isCorrect) {
      setScore(s => s + 1);
    }
    
    if (currentIndex < questions.length - 1) {
      setCurrentIndex(i => i + 1);
    } else {
      submitAssessment(score + (isCorrect ? 1 : 0));
    }
  };
  
  const submitAssessment = async (finalScore) => {
    setIsFinished(true);
    try {
      const res = await fetch('/assessments/submit', {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          score: finalScore,
          max_score: questions.length,
          topic: topic
        })
      });
      const data = await res.json();
      setFinalResult(data);
      // Data contains skill_score, xp_gained, new_level
    } catch (e) {
      console.error(e);
    }
  };
  
  if (loading) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100vh', background: 'var(--bg)' }}>
        <div style={{ fontSize: '40px', animation: 'spin 1s linear infinite' }}>⚙️</div>
        <h2 style={{ color: 'var(--text)', marginTop: '20px' }}>Generating AI Assessment...</h2>
        <p style={{ color: 'var(--text-dim)' }}>Analyzing '{topic}' curriculum...</p>
      </div>
    );
  }
  
  if (error) {
    return (
      <div style={{ padding: '40px', color: 'red', textAlign: 'center' }}>
        <h2>Error</h2>
        <p>{error}</p>
        <button onClick={() => navigate('/dashboard')} className="btn-run">Go Back</button>
      </div>
    );
  }
  
  if (isFinished) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyItems: 'center', justifyContent: 'center', height: '100vh', background: 'var(--bg)' }}>
        <div className="onboard-card" style={{ textAlign: 'center', maxWidth: '600px', width: '100%' }}>
          <h1 style={{ color: 'var(--accent)', fontSize: '32px', marginBottom: '10px' }}>Assessment Complete!</h1>
          <p style={{ color: 'var(--text-dim)', fontSize: '18px', marginBottom: '30px' }}>Your DataCamp-style Skill Score</p>
          
          <div style={{
            width: '200px', height: '200px', margin: '0 auto 30px',
            borderRadius: '50%', border: '10px solid var(--surface2)',
            display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
            background: 'var(--bg)', boxShadow: '0 0 30px rgba(0,229,160,0.2)'
          }}>
            <span style={{ fontSize: '48px', fontWeight: 'bold', color: 'var(--text)' }}>
              {finalResult ? finalResult.skill_score : '...'}
            </span>
            <span style={{ fontSize: '14px', color: 'var(--text-dim)' }}>out of 300</span>
          </div>
          
          {finalResult && (
            <div style={{ background: 'var(--surface2)', padding: '20px', borderRadius: '12px', marginBottom: '30px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '10px' }}>
                <span style={{ color: 'var(--text-dim)' }}>XP Earned:</span>
                <span style={{ color: 'var(--accent3)', fontWeight: 'bold' }}>+{finalResult.xp_gained} XP</span>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                <span style={{ color: 'var(--text-dim)' }}>Current Level:</span>
                <span style={{ color: 'var(--accent2)', fontWeight: 'bold' }}>{finalResult.new_level}</span>
              </div>
            </div>
          )}
          
          <button onClick={() => navigate('/dashboard')} className="btn-submit" style={{ width: '100%', justifyContent: 'center', padding: '15px' }}>
            Return to Dashboard
          </button>
        </div>
      </div>
    );
  }
  
  const currentQ = questions[currentIndex];
  const progressPct = ((currentIndex) / questions.length) * 100;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100vh', background: 'var(--bg)' }}>
      {/* Topbar */}
      <div className="ws-topbar">
        <button onClick={() => navigate('/dashboard')} className="ws-back-btn">← Quit Assessment</button>
        <div style={{ color: 'var(--text)', fontWeight: 'bold' }}>{topic} Assessment</div>
        <div style={{ color: 'var(--text-dim)' }}>Question {currentIndex + 1} of {questions.length}</div>
      </div>
      
      {/* Progress Bar */}
      <div className="progress-strip">
        <div className="progress-strip-fill" style={{ width: `${progressPct}%` }}></div>
      </div>
      
      {/* Question Container */}
      <div style={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
        <div className="onboard-card" style={{ width: '100%', maxWidth: '700px' }}>
          <h2 style={{ fontSize: '22px', lineHeight: '1.5', marginBottom: '40px', color: 'var(--text)' }}>
            {currentQ?.question}
          </h2>
          
          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            {currentQ?.options.map((opt, i) => (
              <button 
                key={i}
                onClick={() => handleAnswer(i)}
                style={{
                  padding: '20px',
                  background: 'var(--surface2)',
                  border: '1px solid var(--border)',
                  borderRadius: '12px',
                  color: 'var(--text)',
                  fontSize: '16px',
                  textAlign: 'left',
                  cursor: 'pointer',
                  transition: 'all 0.2s',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '15px'
                }}
                onMouseOver={(e) => { e.currentTarget.style.borderColor = 'var(--accent)'; e.currentTarget.style.transform = 'translateY(-2px)'; }}
                onMouseOut={(e) => { e.currentTarget.style.borderColor = 'var(--border)'; e.currentTarget.style.transform = 'none'; }}
              >
                <div style={{ 
                  width: '30px', height: '30px', borderRadius: '50%', 
                  background: 'var(--surface)', display: 'flex', alignItems: 'center', justifyContent: 'center',
                  fontWeight: 'bold', color: 'var(--text-dim)'
                }}>
                  {String.fromCharCode(65 + i)}
                </div>
                {opt}
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Assessment;
