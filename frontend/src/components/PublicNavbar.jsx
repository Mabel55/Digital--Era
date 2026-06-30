import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';

const PublicNavbar = () => {
  const { token } = useAuth();
  const navigate = useNavigate();

  return (
    <nav className="dash-nav" style={{ position: 'sticky', top: 0, zIndex: 100, borderBottom: '1px solid var(--border)' }}>
      <Link to="/" style={{ textDecoration: 'none', color: 'inherit' }}>
        <div className="logo-row" style={{ marginBottom: 0 }}>
          <div className="logo-icon">🎓</div>
          <div className="logo-text">Digital <span>Era</span></div>
        </div>
      </Link>
      <div className="nav-right" style={{ display: 'flex', gap: '24px', alignItems: 'center' }}>
        <Link to="/courses" style={{ color: 'var(--text)', textDecoration: 'none', fontWeight: 500, fontSize: '14px', transition: 'color 0.2s' }} onMouseOver={e => e.target.style.color = 'var(--accent)'} onMouseOut={e => e.target.style.color = 'var(--text)'}>Courses</Link>
        <Link to="/public-leaderboard" style={{ color: 'var(--text)', textDecoration: 'none', fontWeight: 500, fontSize: '14px', transition: 'color 0.2s' }} onMouseOver={e => e.target.style.color = 'var(--accent)'} onMouseOut={e => e.target.style.color = 'var(--text)'}>Leaderboard</Link>
        
        {token ? (
          <button 
            className="btn-primary" 
            style={{ padding: '8px 20px', margin: 0, width: 'auto' }}
            onClick={() => navigate('/dashboard')}
          >
            Go to Dashboard
          </button>
        ) : (
          <button 
            className="btn-primary" 
            style={{ padding: '8px 20px', margin: 0, width: 'auto' }}
            onClick={() => navigate('/onboarding')}
          >
            Log In / Sign Up
          </button>
        )}
      </div>
    </nav>
  );
};

export default PublicNavbar;
