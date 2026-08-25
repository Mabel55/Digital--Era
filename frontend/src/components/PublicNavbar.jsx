import React, { useState } from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../AuthContext';
import { useTranslation } from 'react-i18next';
import { GraduationCap, Menu, X, Globe } from 'lucide-react';

const PublicNavbar = () => {
  const { token, user } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const { i18n } = useTranslation();

  const changeLanguage = (e) => {
    i18n.changeLanguage(e.target.value);
  };

  const navLinks = [
    { to: '/catalog', label: 'Courses' },
    { to: '/careers', label: 'Careers' },
    { to: '/pricing', label: 'Pricing' },
    { to: '/public-leaderboard', label: 'Leaderboard' },
  ];

  const isActive = (path) => location.pathname === path;

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
        aria-expanded={isMenuOpen}
      >
        {isMenuOpen ? <X size={20} /> : <Menu size={20} />}
      </button>

      <div className={`nav-right ${isMenuOpen ? 'open' : ''}`}>
        {/* Nav Links */}
        {navLinks.map(({ to, label }) => (
          <Link
            key={to}
            to={to}
            onClick={() => setIsMenuOpen(false)}
            style={{
              color: isActive(to) ? 'var(--accent)' : 'var(--text)',
              textDecoration: 'none',
              fontWeight: isActive(to) ? 700 : 500,
              fontSize: '14px',
              transition: 'color 0.2s',
              borderBottom: isActive(to) ? '2px solid var(--accent)' : '2px solid transparent',
              paddingBottom: '2px',
            }}
            onMouseOver={e => { if (!isActive(to)) e.currentTarget.style.color = 'var(--accent)'; }}
            onMouseOut={e => { if (!isActive(to)) e.currentTarget.style.color = 'var(--text)'; }}
          >
            {label}
          </Link>
        ))}
        
        {/* Language Selector — use native select for mobile compatibility */}
        <div style={{ position: 'relative', display: 'flex', alignItems: 'center' }}>
          <Globe size={16} color="var(--text2)" style={{ position: 'absolute', left: '10px', pointerEvents: 'none', zIndex: 1 }} />
          <select 
            onChange={changeLanguage}
            value={i18n.language}
            style={{
              padding: '8px 14px 8px 32px',
              background: 'var(--surface)', color: 'var(--text)',
              border: '1px solid var(--border)', borderRadius: '20px',
              cursor: 'pointer', fontSize: '14px', fontWeight: 600,
              fontFamily: 'inherit', outline: 'none',
              minHeight: '44px',
              touchAction: 'manipulation',
            }}
            aria-label="Select language"
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
            style={{ padding: '10px 20px', margin: 0, width: 'auto', minHeight: '44px' }}
            onClick={() => { navigate('/dashboard'); setIsMenuOpen(false); }}
          >
            Go to Dashboard
          </button>
        ) : (
          <button 
            className="btn-primary" 
            style={{ padding: '10px 20px', margin: 0, width: 'auto', minHeight: '44px' }}
            onClick={() => { navigate('/onboarding'); setIsMenuOpen(false); }}
          >
            Log In / Sign Up
          </button>
        )}
      </div>
    </nav>
  );
};

export default PublicNavbar;
