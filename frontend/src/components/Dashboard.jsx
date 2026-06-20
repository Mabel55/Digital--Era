import React, { useState, useEffect } from 'react';
import { useAuth } from '../AuthContext';
import { useNavigate } from 'react-router-dom';
import { curriculum, courseManifest } from '../data/courses';

const Dashboard = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const [activeTab, setActiveTab] = useState('Beginner');

  // Find user's track based on goal, default to "Python Core"
  const getTrack = () => {
    if (!user) return "Python Core";
    const g = user.goal?.toLowerCase() || '';
    if (g.includes('frontend') || g.includes('ui')) return "Frontend";
    if (g.includes('backend') || g.includes('api')) return "Backend";
    if (g.includes('data') || g.includes('ml')) return "Data Science";
    if (g.includes('ai')) return "AI Engineering";
    if (g.includes('job') || g.includes('freelance')) return "Python Core";
    return "Python Core";
  };

  const currentTrack = getTrack();

  const handleLogout = () => {
    logout();
    navigate('/onboarding');
  };

  const getCourseProgress = (courseName) => {
    // Determine progress from user.progress object or similar
    if (!user || !user.progress || !user.progress[courseName]) return 0;
    return user.progress[courseName].completed_lessons || 0;
  };

  const openCourse = (courseName) => {
    navigate(`/workspace/${encodeURIComponent(courseName)}`);
  };

  return (
    <div id="dashboard" className="screen active">
      <nav className="dash-nav">
        <div className="logo-row">
          <div className="logo-icon">🎓</div>
          <div className="logo-text">Digital <span>Era</span></div>
        </div>
        <div className="nav-right">
          <div className="streak-badge">🔥 <span>{user?.streak || 0}</span> day streak</div>
          <button className="avatar-btn" onClick={handleLogout}>
            {user?.name ? user.name.charAt(0).toUpperCase() : 'U'}
          </button>
        </div>
      </nav>

      <div className="dash-body">
        <div className="dash-hero">
          <div className="hero-left">
            <h2>Welcome back, <span>{user?.name?.split(' ')[0] || 'Student'}</span>!</h2>
            <p>Your custom track is focused on: <strong>{currentTrack}</strong>.</p>
            <div className="hero-stats">
              <div className="stat-item">
                <div className="stat-num">{user?.xp || 0}</div>
                <div className="stat-label">Total XP</div>
              </div>
              <div className="stat-item">
                <div className="stat-num">{user?.level || 'Beginner'}</div>
                <div className="stat-label">Current Level</div>
              </div>
            </div>
          </div>
        </div>

        <div className="section-title">
          📚 Learning Path <span>Select your difficulty level</span>
        </div>

        <div style={{ display: 'flex', gap: '10px', marginBottom: '24px' }}>
          {['Beginner', 'Intermediate', 'Advanced'].map(lvl => (
            <button 
              key={lvl}
              onClick={() => setActiveTab(lvl)}
              style={{
                padding: '8px 16px',
                background: activeTab === lvl ? 'var(--accent)' : 'var(--surface)',
                color: activeTab === lvl ? '#0d0f14' : 'var(--text)',
                border: '1px solid var(--border)',
                borderRadius: '20px',
                cursor: 'pointer',
                fontWeight: 600,
                fontSize: '13px'
              }}
            >
              {lvl}
            </button>
          ))}
        </div>

        <div className="track-grid">
          {curriculum[currentTrack] && curriculum[currentTrack][activeTab]?.map((courseName, i) => {
            const manifest = courseManifest[courseName];
            const totalLessons = manifest ? manifest.lessons.length : 0;
            const completed = getCourseProgress(courseName);
            const progressPct = totalLessons > 0 ? (completed / totalLessons) * 100 : 0;

            return (
              <div key={courseName} className="track-card" onClick={() => openCourse(courseName)}>
                <div className="track-card-icon">💻</div>
                <div className="track-card-name">{courseName}</div>
                <div className="track-card-desc">
                  {totalLessons} lessons • {completed} completed
                </div>
                <div className="track-card-meta">
                  <span className={`track-tag tag-${activeTab.toLowerCase()}`}>{activeTab}</span>
                </div>
                <div className="track-progress-bar">
                  <div className="bar-bg">
                    <div className="bar-fill" style={{ width: `${progressPct}%` }}></div>
                  </div>
                  <div className="bar-label">{Math.round(progressPct)}% Complete</div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
