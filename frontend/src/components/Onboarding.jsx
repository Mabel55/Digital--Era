import React, { useState } from 'react';
import { useAuth } from '../AuthContext';
import { useNavigate } from 'react-router-dom';

const Onboarding = () => {
  const [isLogin, setIsLogin] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
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
      if (isLogin) {
        await login(email, password);
      } else {
        await signup(name, email, password, level, goal);
      }
      navigate('/');
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
          <div className="logo-icon">🎓</div>
          <div className="logo-text">Digital <span>Era</span></div>
        </div>
        
        <div className="onboard-title">{isLogin ? "Welcome Back" : "Start Your Coding Journey"}</div>
        <div className="onboard-sub">
          {isLogin ? "Log in to continue your personalized learning path." : "Tell us about yourself so we can personalize your learning experience."}
        </div>

        {error && <div style={{ color: 'var(--danger)', marginBottom: '16px', fontSize: '13px' }}>{error}</div>}

        <form onSubmit={handleSubmit}>
          {!isLogin && (
            <div className="field-row">
              <label className="field-label">Your Full Name</label>
              <input 
                type="text" 
                placeholder="e.g. Ada Okonkwo" 
                value={name}
                onChange={(e) => setName(e.target.value)}
                required={!isLogin}
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

          {!isLogin && (
            <div className="two-col">
              <div className="field-row">
                <label className="field-label">Experience Level</label>
                <select value={level} onChange={(e) => setLevel(e.target.value)}>
                  <option value="Beginner">🟢 Beginner</option>
                  <option value="Intermediate">🟡 Intermediate</option>
                  <option value="Advanced">🔴 Advanced</option>
                </select>
              </div>
              <div className="field-row">
                <label className="field-label">Goal</label>
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
            {loading ? "Processing..." : (isLogin ? "Login" : "🚀 Initialize My Learning Path")}
          </button>
        </form>

        <div className="divider">
          <hr /><span>{isLogin ? "New here?" : "Already enrolled?"}</span><hr />
        </div>
        
        <button 
          className="returning-btn" 
          onClick={() => { setIsLogin(!isLogin); setError(''); }}
        >
          {isLogin ? "✨ Create a new account" : "📂 Continue where I left off"}
        </button>
      </div>
    </div>
  );
};

export default Onboarding;
