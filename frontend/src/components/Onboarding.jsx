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
  
  const { login, signup, resetPassword } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    
    try {
      if (isForgotPassword) {
        await resetPassword(email, oldPassword, password);
        setIsForgotPassword(false);
        setIsLogin(true);
        setOldPassword('');
        setError("Password reset successfully. Please log in with your new password.");
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
          {isForgotPassword ? "Enter your email, current password, and new password." : (isLogin ? "Log in to continue your personalized learning path." : "Tell us about yourself so we can personalize your learning experience.")}
        </div>

        {error && <div style={{ color: error.includes("successfully") ? 'var(--success)' : 'var(--danger)', marginBottom: '16px', fontSize: '13px' }}>{error}</div>}

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

          {isForgotPassword && (
            <div className="field-row">
              <label className="field-label">Current Password</label>
              <input 
                type="password" 
                placeholder="••••••••"
                value={oldPassword}
                onChange={(e) => setOldPassword(e.target.value)}
                required
              />
            </div>
          )}

          <div className="field-row">
            <label className="field-label">{isForgotPassword ? "New Password" : "Password"}</label>
            <input 
              type="password" 
              placeholder="••••••••"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>

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
            {loading ? "Processing..." : (isForgotPassword ? "Reset Password" : (isLogin ? "Login" : <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px' }}><Rocket size={18} /> Initialize My Learning Path</div>))}
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
