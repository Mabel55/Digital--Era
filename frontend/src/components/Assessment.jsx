import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';
import { Helmet } from 'react-helmet-async';
import { CheckCircle2, XCircle, Clock } from 'lucide-react';

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
  
  // New State variables for enhancements
  const [timeLeft, setTimeLeft] = useState(600); // 10 minutes total
  const [selectedOption, setSelectedOption] = useState(null);
  const [isAnswerRevealed, setIsAnswerRevealed] = useState(false);
  const [userAnswers, setUserAnswers] = useState([]);
  const [showReview, setShowReview] = useState(false);
  
  useEffect(() => {
    fetchQuestions();
  }, [topic]);

  useEffect(() => {
    if (loading || isFinished || error) return;
    const timer = setInterval(() => {
      setTimeLeft(prev => {
        if (prev <= 1) {
          clearInterval(timer);
          // Handle timeout by forcing submit
          submitAssessment(score); 
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
    return () => clearInterval(timer);
  }, [loading, isFinished, error, score]);
  
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
    if (isAnswerRevealed) return; // Prevent clicking after revealed
    const currentQ = questions[currentIndex];
    const isCorrect = optionIndex === currentQ.correctAnswer;
    
    setSelectedOption(optionIndex);
    setIsAnswerRevealed(true);
    
    if (isCorrect) {
      setScore(s => s + 1);
    }
    
    setUserAnswers(prev => [...prev, {
      question: currentQ.question,
      options: currentQ.options,
      userChoice: optionIndex,
      correctChoice: currentQ.correctAnswer,
      isCorrect,
      explanation: currentQ.explanation
    }]);
  };

  const handleNextQuestion = () => {
    setIsAnswerRevealed(false);
    setSelectedOption(null);
    if (currentIndex < questions.length - 1) {
      setCurrentIndex(i => i + 1);
    } else {
      // Safe way since handleNextQuestion is called via button click *after* state updated:
      submitAssessment(score);
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
          topic: topic,
          questions_data: userAnswers // Will lack the last answer if timeout, but ok for now
        })
      });
      const data = await res.json();
      setFinalResult(data);
    } catch (e) {
      console.error(e);
    }
  };

  const formatTime = (seconds) => {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${m}:${s < 10 ? '0' : ''}${s}`;
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

  // REVIEW SCREEN
  if (showReview) {
    return (
      <div style={{ background: 'var(--bg)', minHeight: '100vh', padding: '40px 24px', color: 'var(--text)' }}>
        <Helmet>
          <title>Assessment | Digital Era Academy</title>
          <meta name="robots" content="noindex, nofollow" />
        </Helmet>
        <div style={{ maxWidth: '800px', margin: '0 auto' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '40px' }}>
            <h1 style={{ fontSize: '28px', margin: 0 }}>Review Assessment: {topic}</h1>
            <button onClick={() => navigate('/dashboard')} className="btn-submit" style={{ padding: '10px 20px' }}>Return to Dashboard</button>
          </div>
          
          <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
            {userAnswers.map((ans, idx) => (
              <div key={idx} style={{ background: 'var(--surface)', padding: '24px', borderRadius: '16px', border: `1px solid ${ans.isCorrect ? 'rgba(0,229,160,0.5)' : 'rgba(239,68,68,0.5)'}` }}>
                <div style={{ display: 'flex', gap: '12px', marginBottom: '16px', alignItems: 'flex-start' }}>
                  {ans.isCorrect ? <CheckCircle2 size={24} color="var(--accent)" /> : <XCircle size={24} color="#ef4444" />}
                  <h3 style={{ fontSize: '18px', margin: 0, lineHeight: 1.5 }}>{idx + 1}. {ans.question}</h3>
                </div>
                
                <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', paddingLeft: '36px', marginBottom: '20px' }}>
                  {ans.options.map((opt, optIdx) => {
                    let bgColor = 'var(--surface2)';
                    let borderColor = 'var(--border)';
                    if (optIdx === ans.correctChoice) {
                      bgColor = 'rgba(0,229,160,0.1)';
                      borderColor = 'var(--accent)';
                    } else if (optIdx === ans.userChoice && !ans.isCorrect) {
                      bgColor = 'rgba(239,68,68,0.1)';
                      borderColor = '#ef4444';
                    }
                    
                    return (
                      <div key={optIdx} style={{ padding: '12px 16px', borderRadius: '8px', background: bgColor, border: `1px solid ${borderColor}`, fontSize: '15px' }}>
                        {String.fromCharCode(65 + optIdx)}. {opt}
                      </div>
                    );
                  })}
                </div>
                
                <div style={{ background: 'var(--bg)', padding: '16px', borderRadius: '8px', borderLeft: '4px solid var(--accent3)', marginLeft: '36px' }}>
                  <div style={{ fontSize: '12px', color: 'var(--text-dim)', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '8px', fontWeight: 'bold' }}>Explanation</div>
                  <div style={{ fontSize: '14px', lineHeight: 1.6 }}>{ans.explanation}</div>
                </div>
              </div>
            ))}
          </div>
        </div>
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
          
          <div style={{ display: 'flex', gap: '16px' }}>
            <button onClick={() => setShowReview(true)} style={{ flex: 1, padding: '15px', background: 'var(--surface2)', color: 'var(--text)', border: '1px solid var(--border)', borderRadius: '8px', cursor: 'pointer', fontWeight: 'bold' }}>
              Review Answers
            </button>
            <button onClick={() => navigate('/dashboard')} className="btn-submit" style={{ flex: 1, justifyContent: 'center', padding: '15px' }}>
              Return to Dashboard
            </button>
          </div>
        </div>
      </div>
    );
  }
  
  const currentQ = questions[currentIndex];
  const progressPct = ((currentIndex) / questions.length) * 100;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100vh', background: 'var(--bg)' }}>
      {/* Topbar */}
      <div className="ws-topbar" style={{ padding: '12px 24px' }}>
        <button onClick={() => navigate('/dashboard')} className="ws-back-btn">← Quit Assessment</button>
        <div style={{ color: 'var(--text)', fontWeight: 'bold', fontSize: '16px' }}>{topic} Assessment</div>
        
        <div style={{ display: 'flex', alignItems: 'center', gap: '24px' }}>
          <div style={{ color: 'var(--text-dim)' }}>Question {currentIndex + 1} of {questions.length}</div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: timeLeft < 60 ? '#ef4444' : 'var(--text2)', fontWeight: 'bold', background: 'var(--surface2)', padding: '6px 12px', borderRadius: '100px' }}>
            <Clock size={16} />
            {formatTime(timeLeft)}
          </div>
        </div>
      </div>
      
      {/* Progress Bar */}
      <div className="progress-strip">
        <div className="progress-strip-fill" style={{ width: `${progressPct}%` }}></div>
      </div>
      
      {/* Question Container */}
      <div style={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px', overflowY: 'auto' }}>
        <div className="onboard-card" style={{ width: '100%', maxWidth: '700px', padding: '40px' }}>
          <h2 style={{ fontSize: '22px', lineHeight: '1.5', marginBottom: '40px', color: 'var(--text)' }}>
            {currentQ?.question}
          </h2>
          
          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            {currentQ?.options.map((opt, i) => {
              let isCorrectOpt = i === currentQ.correctAnswer;
              let isSelectedOpt = i === selectedOption;
              
              let bgColor = 'var(--surface2)';
              let borderColor = 'var(--border)';
              let color = 'var(--text)';
              
              if (isAnswerRevealed) {
                if (isCorrectOpt) {
                  bgColor = 'rgba(0, 229, 160, 0.1)';
                  borderColor = 'var(--accent)';
                } else if (isSelectedOpt) {
                  bgColor = 'rgba(239, 68, 68, 0.1)';
                  borderColor = '#ef4444';
                }
              }

              return (
                <button 
                  key={i}
                  onClick={() => handleAnswer(i)}
                  disabled={isAnswerRevealed}
                  style={{
                    padding: '20px',
                    background: bgColor,
                    border: `2px solid ${borderColor}`,
                    borderRadius: '12px',
                    color: color,
                    fontSize: '16px',
                    textAlign: 'left',
                    cursor: isAnswerRevealed ? 'default' : 'pointer',
                    transition: 'all 0.2s',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '15px'
                  }}
                  onMouseOver={(e) => { if (!isAnswerRevealed) { e.currentTarget.style.borderColor = 'var(--accent)'; e.currentTarget.style.transform = 'translateY(-2px)'; } }}
                  onMouseOut={(e) => { if (!isAnswerRevealed) { e.currentTarget.style.borderColor = borderColor; e.currentTarget.style.transform = 'none'; } }}
                >
                  <div style={{ 
                    width: '30px', height: '30px', borderRadius: '50%', 
                    background: isAnswerRevealed && isCorrectOpt ? 'var(--accent)' : isAnswerRevealed && isSelectedOpt ? '#ef4444' : 'var(--surface)', 
                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                    fontWeight: 'bold', color: (isAnswerRevealed && (isCorrectOpt || isSelectedOpt)) ? '#000' : 'var(--text-dim)'
                  }}>
                    {String.fromCharCode(65 + i)}
                  </div>
                  {opt}
                </button>
              );
            })}
          </div>

          {/* Explanation Area */}
          {isAnswerRevealed && (
            <div style={{ marginTop: '32px', animation: 'fadeIn 0.3s' }}>
              <div style={{ 
                padding: '20px', borderRadius: '12px', 
                background: selectedOption === currentQ.correctAnswer ? 'rgba(0,229,160,0.1)' : 'rgba(239,68,68,0.1)',
                border: `1px solid ${selectedOption === currentQ.correctAnswer ? 'var(--accent)' : '#ef4444'}`
              }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontWeight: 'bold', fontSize: '18px', marginBottom: '12px', color: selectedOption === currentQ.correctAnswer ? 'var(--accent)' : '#ef4444' }}>
                  {selectedOption === currentQ.correctAnswer ? <CheckCircle2 size={24} /> : <XCircle size={24} />}
                  {selectedOption === currentQ.correctAnswer ? 'Correct!' : 'Incorrect'}
                </div>
                <div style={{ color: 'var(--text)', lineHeight: 1.6 }}>
                  {currentQ.explanation}
                </div>
              </div>
              
              <button 
                onClick={handleNextQuestion}
                className="btn-submit"
                style={{ width: '100%', padding: '16px', marginTop: '24px', fontSize: '16px' }}
              >
                {currentIndex < questions.length - 1 ? 'Next Question' : 'Finish Assessment'}
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Assessment;
