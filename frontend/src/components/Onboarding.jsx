import React, { useState } from 'react';
import { useAuth } from '../AuthContext';
import { useNavigate } from 'react-router-dom';
import { GraduationCap, Rocket, ArrowLeft, Sparkles, LogIn, Award, Target } from 'lucide-react';

const Onboarding = () => {
  const [isLogin, setIsLogin] = useState(false);
  const [isForgotPassword, setIsForgotPassword] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [oldPassword, setOldPassword] = useState('');
  const [name, setName] = useState('');
  const [level, setLevel] = useState('Beginner');
  const [goal, setGoal] = useState('get a job');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  
  const { login, signup } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    
    try {
      if (isForgotPassword) {
        const res = await fetch('/users/forgot-password', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email })
        });
        const data = await res.json();
        if (res.ok) {
          setError(data.message || "If that email exists, a reset link has been sent.");
        } else {
          setError(data.detail || "An error occurred.");
        }
      } else if (isLogin) {
        await login(email, password);
        navigate('/');
      } else {
        await signup(name, email, password, level, goal);
        navigate('/');
      }
    } catch (err) {
      setError(err.message || "An error occurred");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div id="onboarding" className="screen active">
      <div className="onboard-card">
        <div className="logo-row">
          <div className="logo-icon"><GraduationCap size={24} /></div>
          <div className="logo-text">Digital <span>Era</span></div>
        </div>
        
        <div className="onboard-title">{isForgotPassword ? "Reset Password" : (isLogin ? "Welcome Back" : "Start Your Coding Journey")}</div>
        <div className="onboard-sub">
          {isForgotPassword ? "Enter your email address to receive a password reset link." : (isLogin ? "Log in to continue your personalized learning path." : "Tell us about yourself so we can personalize your learning experience.")}
        </div>

        {error && <div style={{ color: error.includes("link has been sent") ? 'var(--accent)' : 'var(--danger)', marginBottom: '16px', fontSize: '13px', textAlign: 'center' }}>{error}</div>}

        <form onSubmit={handleSubmit}>
          {!isLogin && !isForgotPassword && (
            <div className="field-row">
              <label className="field-label">Your Full Name</label>
              <input 
                type="text" 
                placeholder="e.g. Ada Okonkwo" 
                value={name}
                onChange={(e) => setName(e.target.value)}
                required={!isLogin && !isForgotPassword}
              />
            </div>
          )}

          <div className="field-row">
            <label className="field-label">Email</label>
            <input 
              type="email" 
              placeholder="ada@example.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>

          {!isForgotPassword && (
            <div className="field-row">
              <label className="field-label">Password</label>
              <input 
                type="password" 
                placeholder="••••••••"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
          )}

          {!isLogin && !isForgotPassword && (
            <div className="two-col">
              <div className="field-row">
                <label className="field-label" style={{ display: 'flex', alignItems: 'center', gap: '6px' }}><Award size={14} /> Experience Level</label>
                <select value={level} onChange={(e) => setLevel(e.target.value)}>
                  <option value="Beginner">Beginner</option>
                  <option value="Intermediate">Intermediate</option>
                  <option value="Advanced">Advanced</option>
                </select>
              </div>
              <div className="field-row">
                <label className="field-label" style={{ display: 'flex', alignItems: 'center', gap: '6px' }}><Target size={14} /> Goal</label>
                <select value={goal} onChange={(e) => setGoal(e.target.value)}>
                  <option value="get a job">Get a Job</option>
                  <option value="build projects">Build Projects</option>
                  <option value="learn AI/ML">Learn AI/ML</option>
                  <option value="freelance">Freelance</option>
                </select>
              </div>
            </div>
          )}

          <button type="submit" className="btn-primary" disabled={loading}>
            {loading ? "Processing..." : (isForgotPassword ? "Send Reset Link" : (isLogin ? "Login" : <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px' }}><Rocket size={18} /> Initialize My Learning Path</div>))}
          </button>
        </form>

        {isLogin && !isForgotPassword && (
          <div style={{ textAlign: 'center', marginTop: '16px' }}>
            <a href="#" onClick={(e) => { e.preventDefault(); setIsForgotPassword(true); setError(''); }} style={{ color: 'var(--text-muted)', fontSize: '14px', textDecoration: 'none' }}>Forgot Password?</a>
          </div>
        )}

        <div className="divider">
          <hr /><span>{isForgotPassword ? "Or" : (isLogin ? "New here?" : "Already enrolled?")}</span><hr />
        </div>
        
        <button 
          className="returning-btn" 
          onClick={() => { 
            if (isForgotPassword) {
              setIsForgotPassword(false);
              setIsLogin(true);
              setOldPassword('');
            } else {
              setIsLogin(!isLogin); 
            }
            setError(''); 
          }}
        >
          {isForgotPassword ? <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '6px' }}><ArrowLeft size={16} /> Back to Login</div> : (isLogin ? <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '6px' }}><Sparkles size={16} /> Create a new account</div> : <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '6px' }}><LogIn size={16} /> Continue where I left off</div>)}
        </button>
      </div>
    </div>
  );
};

export default Onboarding;
