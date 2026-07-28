import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';
import { useTranslation } from 'react-i18next';
import { GraduationCap, Menu, X, Globe } from 'lucide-react';

const PublicNavbar = () => {
  const { token, user } = useAuth();
  const navigate = useNavigate();
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const { i18n } = useTranslation();

  const changeLanguage = (e) => {
    i18n.changeLanguage(e.target.value);
  };

  return (
    <nav className="dash-nav" style={{ position: 'sticky', top: 0, zIndex: 100, borderBottom: '1px solid var(--border)' }}>
      <Link to="/" style={{ textDecoration: 'none', color: 'inherit' }}>
        <div className="logo-row" style={{ marginBottom: 0 }}>
          <div className="logo-icon"><GraduationCap size={24} /></div>
          <div className="logo-text">Digital <span>Era</span></div>
        </div>
      </Link>
      
      <button 
        className="mobile-menu-btn" 
        onClick={() => setIsMenuOpen(!isMenuOpen)}
        aria-label="Toggle mobile menu"
      >
        {isMenuOpen ? <X size={20} /> : <Menu size={20} />}
      </button>

      <div className={`nav-right ${isMenuOpen ? 'open' : ''}`} style={{ display: 'flex', gap: '24px', alignItems: 'center' }}>
        <Link to="/catalog" style={{ color: 'var(--text)', textDecoration: 'none', fontWeight: 500, fontSize: '14px', transition: 'color 0.2s' }} onMouseOver={e => e.target.style.color = 'var(--accent)'} onMouseOut={e => e.target.style.color = 'var(--text)'}>Courses</Link>
        <Link to="/pricing" style={{ color: 'var(--text)', textDecoration: 'none', fontWeight: 500, fontSize: '14px', transition: 'color 0.2s' }} onMouseOver={e => e.target.style.color = 'var(--accent)'} onMouseOut={e => e.target.style.color = 'var(--text)'}>Pricing</Link>
        <Link to="/public-leaderboard" style={{ color: 'var(--text)', textDecoration: 'none', fontWeight: 500, fontSize: '14px', transition: 'color 0.2s' }} onMouseOver={e => e.target.style.color = 'var(--accent)'} onMouseOut={e => e.target.style.color = 'var(--text)'}>Leaderboard</Link>
        
        {/* Language Selector */}
        <div style={{ position: 'relative', display: 'flex', alignItems: 'center' }}>
          <Globe size={16} color="var(--text2)" style={{ position: 'absolute', left: '10px', pointerEvents: 'none' }} />
          <select 
            onChange={changeLanguage}
            value={i18n.language}
            style={{
              padding: '6px 12px 6px 32px',
              background: 'var(--surface)', color: 'var(--text)',
              border: '1px solid var(--border)', borderRadius: '20px',
              cursor: 'pointer', fontSize: '13px', fontWeight: 600,
              fontFamily: 'inherit', outline: 'none', appearance: 'none',
              WebkitAppearance: 'none', MozAppearance: 'none'
            }}
          >
            <option value="en">EN</option>
            <option value="es">ES</option>
            <option value="fr">FR</option>
            <option value="ig">IG</option>
            <option value="yo">YO</option>
            <option value="ha">HA</option>
            <option value="sw">SW</option>
            <option value="ar">AR</option>
          </select>
        </div>

        {user && ((user.role || '').toLowerCase() === 'admin' || user.email === 'nasaadanna@gmail.com') && (
          <Link to="/teacher" style={{ color: 'var(--accent)', textDecoration: 'none', fontWeight: 'bold', fontSize: '14px' }}>Admin Portal</Link>
        )}
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
