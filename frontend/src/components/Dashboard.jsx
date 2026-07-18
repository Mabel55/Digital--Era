import React, { useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { useAuth } from '../AuthContext';
import { useNavigate } from 'react-router-dom';
import { curriculum, courseManifest } from '../data/courses';
import { projectsManifest } from '../data/projects';
import CertificateModal from './CertificateModal';
import { GraduationCap, Sun, Moon, Trophy, Flame, Users, Target, Scroll, Rocket, Brain, Wrench, Hammer, BookOpen, Terminal } from 'lucide-react';

const Dashboard = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const [activeTab, setActiveTab] = useState('Beginner');
  const [overviewCourse, setOverviewCourse] = useState(null);
  const [certCourse, setCertCourse] = useState(null);
  const [theme, setTheme] = useState(localStorage.getItem('theme') || 'dark');
  const { t, i18n } = useTranslation();

  const changeLanguage = (lng) => {
    i18n.changeLanguage(lng);
  };

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
  }, [theme]);

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

  const [currentTrack, setCurrentTrack] = useState(() => getTrack());

  const handleLogout = () => {
    logout();
    navigate('/onboarding');
  };

  const getCourseProgress = (courseName) => {
    // Determine progress from user.progress object or similar
    if (!user || !user.progress || !user.progress[courseName]) return 0;
    return user.progress[courseName].completed_lessons || 0;
  };

  const openOverview = (courseName) => {
    setOverviewCourse(courseName);
  };

  const startCourse = (courseName) => {
    navigate(`/workspace/${encodeURIComponent(courseName)}`);
  };

  const [dbCourses, setDbCourses] = useState([]);
  const [dbCoursesLoading, setDbCoursesLoading] = useState(true);
  const [dbCoursesError, setDbCoursesError] = useState(null);

  useEffect(() => {
    fetchDBCourses();
  }, []);

  const fetchDBCourses = async () => {
    setDbCoursesLoading(true);
    setDbCoursesError(null);
    try {
      const res = await fetch('/courses/');
      if (res.ok) {
        const data = await res.json();
        setDbCourses(data);
      } else {
        setDbCoursesError('Failed to load courses. Please try again.');
      }
    } catch (e) {
      console.error(e);
      setDbCoursesError('Could not connect to the server.');
    } finally {
      setDbCoursesLoading(false);
    }
  };

  const startDBCourse = (courseId) => {
    navigate(`/db-workspace/${courseId}`);
  };

  const getDBCourseProgress = (courseName) => {
    if (!user || !user.progress || !user.progress[courseName]) return 0;
    return user.progress[courseName].completed_lesson_ids?.length || 0;
  };

    const completedCourses = [];
    Object.keys(curriculum).forEach(track => {
      Object.keys(curriculum[track]).forEach(level => {
        curriculum[track][level].forEach(courseName => {
          const manifest = courseManifest[courseName];
          if (manifest) {
            const totalLessons = manifest.lessons.length;
            // Fake 100% completion for testing purposes if it's Python Fundamentals
            const completed = courseName === 'Python Fundamentals' ? totalLessons : getCourseProgress(courseName);
            if (totalLessons > 0 && completed === totalLessons) {
              completedCourses.push(courseName);
            }
          }
        });
      });
    });
    const uniqueCompletedCourses = [...new Set(completedCourses)];

  return (
    <div id="dashboard" className="screen active">
      <nav className="dash-nav">
          <div 
            className="logo-row" 
            onClick={() => navigate('/')} 
            role="button" 
            tabIndex={0} 
            onKeyDown={(e) => e.key === 'Enter' && navigate('/')}
            style={{ cursor: 'pointer' }}
            aria-label="Go to Home"
          >
            <div className="logo-icon"><GraduationCap size={24} aria-hidden="true" /></div>
            <div className="logo-text">Digital <span>Era</span></div>
          </div>
        <div className="nav-right" style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <button 
            onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
            style={{ padding: '8px 12px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border)', borderRadius: '20px', cursor: 'pointer', display: 'flex', alignItems: 'center' }}
            title="Toggle Light/Dark Mode"
            aria-label="Toggle theme"
          >
            {theme === 'dark' ? <Sun size={18} /> : <Moon size={18} />}
          </button>
          <button 
            onClick={() => navigate('/leaderboard')}
            style={{ padding: '8px 16px', background: 'var(--surface2)', color: 'var(--accent3)', border: '1px solid var(--border)', borderRadius: '20px', cursor: 'pointer', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '6px' }}
          >
            <Trophy size={16} /> Leaderboard
          </button>
          <div className="streak-badge"><Flame size={16} color="var(--accent3)" /> <span>{user?.streak || 0}</span> day streak</div>
          {((user?.role || '').toLowerCase() === 'admin' || (user?.role || '').toLowerCase() === 'teacher') && (
            <button 
              onClick={() => navigate('/teacher')}
              style={{ padding: '8px 16px', background: 'var(--accent)', color: 'black', border: 'none', borderRadius: '20px', cursor: 'pointer', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '6px' }}
            >
              <Users size={16} /> Teacher Portal
            </button>
          )}
          <button 
            onClick={handleLogout}
            style={{ padding: '8px 16px', background: 'transparent', color: 'var(--text-dim)', border: '1px solid var(--border)', borderRadius: '20px', cursor: 'pointer', fontWeight: 'bold' }}
          >
            Logout
          </button>
        </div>
      </nav>

      <div className="dash-body">
        <div className="dash-hero">
          <div className="hero-left">
            <h2>{t('dashboard.welcome')}, <span>{user?.name?.split(' ')[0] || 'Student'}</span>!</h2>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '16px', color: 'var(--text-dim)' }}>
              Your current track:
              <select 
                value={currentTrack} 
                onChange={(e) => setCurrentTrack(e.target.value)}
                style={{
                  padding: '6px 12px',
                  borderRadius: '6px',
                  background: 'var(--surface)',
                  color: 'var(--accent)',
                  border: '1px solid var(--border)',
                  outline: 'none',
                  fontFamily: 'inherit',
                  fontSize: '14px',
                  fontWeight: '600',
                  cursor: 'pointer'
                }}
                aria-label="Select your learning track"
              >
                {Object.keys(curriculum).map(trackName => (
                  <option key={trackName} value={trackName}>{trackName}</option>
                ))}
              </select>
              <button 
                onClick={() => navigate(`/assessment/${encodeURIComponent(currentTrack)}`)}
                style={{
                  padding: '6px 12px',
                  borderRadius: '6px',
                  background: 'var(--accent3)',
                  color: 'black',
                  border: 'none',
                  outline: 'none',
                  fontFamily: 'inherit',
                  fontSize: '13px',
                  fontWeight: 'bold',
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '6px'
                }}
              >
                <Target size={14} /> Test Your Skills
              </button>
            </div>
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

        {uniqueCompletedCourses.length > 0 && (
          <>
            <div className="section-title">
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}><Trophy size={20} color="var(--accent3)" /> Your Certificates <span>({uniqueCompletedCourses.length})</span></div>
            </div>
            <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap', marginBottom: '40px' }}>
              {uniqueCompletedCourses.map(c => (
                <div 
                  key={c}
                  onClick={() => setCertCourse(c)}
                  role="button"
                  tabIndex={0}
                  onKeyDown={(e) => e.key === 'Enter' && setCertCourse(c)}
                  aria-label={`View Certificate for ${c}`}
                  style={{
                    padding: '12px 20px', background: 'rgba(0, 229, 160, 0.08)',
                    border: '1px solid var(--accent)', borderRadius: '12px',
                    color: 'white', cursor: 'pointer', display: 'flex',
                    alignItems: 'center', gap: '8px', fontWeight: 'bold'
                  }}
                >
                  <Scroll size={16} /> {c}
                </div>
              ))}
            </div>
          </>
        )}

        <div className="section-title">
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}><Rocket size={20} color="var(--accent)" /> Live AI Courses</div> <span>Created by your teachers</span>
        </div>
        {dbCoursesLoading ? (
          <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text2)' }}>
            <div style={{ fontSize: '24px', marginBottom: '12px', animation: 'pulse 2s infinite' }}>⏳</div>
            Loading courses...
          </div>
        ) : dbCoursesError ? (
          <div style={{ padding: '24px', textAlign: 'center', background: 'rgba(239,68,68,0.06)', border: '1px solid rgba(239,68,68,0.2)', borderRadius: 'var(--radius)', marginBottom: '40px' }}>
            <p style={{ color: 'var(--danger)', marginBottom: '12px' }}>⚠️ {dbCoursesError}</p>
            <button onClick={fetchDBCourses} style={{ padding: '8px 20px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border)', borderRadius: '8px', cursor: 'pointer', fontWeight: 600 }}>🔄 Retry</button>
          </div>
        ) : dbCourses.length > 0 ? (
          <div className="track-grid" style={{ marginBottom: '40px' }}>
            {dbCourses.map(course => {
              const totalLessons = course.lessons?.length || 0;
              const completed = getDBCourseProgress(course.title);
              const progressPct = totalLessons > 0 ? (completed / totalLessons) * 100 : 0;
              return (
                <div 
                  key={course.id} 
                  className="track-card" 
                  onClick={() => startDBCourse(course.id)} 
                  role="button"
                  tabIndex={0}
                  onKeyDown={(e) => e.key === 'Enter' && startDBCourse(course.id)}
                  aria-label={`Live Course: ${course.title}`}
                  style={{ border: '1px solid var(--accent)' }}
                >
                  <div className="track-card-icon"><Brain size={32} strokeWidth={1.5} /></div>
                  <div className="track-card-name">{course.title}</div>
                  <div className="track-card-desc">
                    {totalLessons} lessons • {completed} completed
                  </div>
                  <div className="track-card-meta">
                    <span className={`track-tag tag-advanced`}>Live</span>
                  </div>
                  <div className="track-progress-bar">
                    <div className="bar-bg">
                      <div className="bar-fill" style={{ width: `${progressPct}%`, background: 'var(--accent)' }}></div>
                    </div>
                    <div className="bar-label">{Math.round(progressPct)}% Complete</div>
                  </div>
                </div>
              );
            })}
          </div>
        ) : (
          <div style={{ padding: '24px', textAlign: 'center', color: 'var(--text3)', marginBottom: '40px' }}>
            No live courses available yet.
          </div>
        )}

        <div className="section-title">
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}><Wrench size={20} color="var(--accent)" /> Guided Projects</div> <span>Build real-world applications</span>
        </div>
        <div className="track-grid" style={{ marginBottom: '40px' }}>
          {Object.values(projectsManifest).map(project => (
            <div 
              key={project.id} 
              className="track-card" 
              onClick={() => navigate(`/project/${project.id}`)} 
              role="button"
              tabIndex={0}
              onKeyDown={(e) => e.key === 'Enter' && navigate(`/project/${project.id}`)}
              aria-label={`Project: ${project.title}`}
              style={{ border: '1px solid var(--accent3)' }}
            >
              <div className="track-card-icon"><Hammer size={32} strokeWidth={1.5} /></div>
              <div className="track-card-name">{project.title}</div>
              <div className="track-card-desc">{project.description}</div>
              <div className="track-card-meta">
                <span className={`track-tag tag-intermediate`}>{project.difficulty}</span>
                <span className="track-tag tag-beginner" style={{ marginLeft: '10px' }}>+{project.xp} XP</span>
              </div>
            </div>
          ))}
        </div>

        <div className="section-title">
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}><BookOpen size={20} color="var(--accent)" /> Learning Path</div> <span>Select your difficulty level</span>
        </div>

        <div style={{ display: 'flex', gap: '10px', marginBottom: '24px' }}>
          {['Beginner', 'Intermediate', 'Advanced'].map(lvl => (
            <button 
              key={lvl}
              onClick={() => setActiveTab(lvl)}
              aria-pressed={activeTab === lvl}
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
              <div 
                key={courseName} 
                className="track-card" 
                onClick={() => openOverview(courseName)}
                role="button"
                tabIndex={0}
                onKeyDown={(e) => e.key === 'Enter' && openOverview(courseName)}
                aria-label={`Course: ${courseName}`}
              >
                <div className="track-card-icon"><Terminal size={32} strokeWidth={1.5} /></div>
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

      {overviewCourse && (
        <div 
          style={{
            position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, 
            backgroundColor: 'rgba(0,0,0,0.8)', display: 'flex', 
            justifyContent: 'center', alignItems: 'center', zIndex: 1000
          }}
          role="dialog"
          aria-modal="true"
          aria-label="Course Overview"
        >
          <div style={{
            background: 'var(--surface)', padding: '30px', borderRadius: '16px',
            width: '100%', maxWidth: '500px', border: '1px solid var(--border)'
          }}>
            <h2 style={{ marginTop: 0, color: 'white' }}>{overviewCourse}</h2>
            <p style={{ color: 'var(--text-dim)', marginBottom: '20px' }}>What you will learn in this course:</p>
            <ul style={{ color: 'var(--text)', paddingLeft: '20px', marginBottom: '30px', lineHeight: '1.6' }}>
              {courseManifest[overviewCourse]?.lessons.map((lesson, idx) => (
                <li key={idx}><strong>{lesson.title}</strong></li>
              ))}
            </ul>
            <div style={{ display: 'flex', gap: '12px', justifyContent: 'flex-end' }}>
              <button 
                onClick={() => setOverviewCourse(null)}
                style={{ padding: '10px 20px', background: 'transparent', color: 'var(--text)', border: '1px solid var(--border)', borderRadius: '8px', cursor: 'pointer', fontWeight: 'bold' }}
              >
                Cancel
              </button>
              <button 
                onClick={() => startCourse(overviewCourse)}
                style={{ padding: '10px 20px', background: 'var(--accent)', color: '#000', border: 'none', borderRadius: '8px', cursor: 'pointer', fontWeight: 'bold' }}
              >
                Start Course
              </button>
            </div>
          </div>
        </div>
      )}

      {certCourse && (
        <CertificateModal
          courseName={certCourse}
          studentName={user?.name || 'Student'}
          onClose={() => setCertCourse(null)}
        />
      )}
    </div>
  );
};

export default Dashboard;
