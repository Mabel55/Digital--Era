import React, { useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { useAuth } from '../AuthContext';
import { useNavigate } from 'react-router-dom';
import { curriculum, courseManifest } from '../data/courses';
import { projectsManifest } from '../data/projects';
import CertificateModal from './CertificateModal';
import NotificationCenter from './NotificationCenter';
import { GraduationCap, Sun, Moon, Trophy, Flame, Users, User, Target, Scroll, Rocket, Brain, Wrench, Hammer, BookOpen, Terminal, Crown, ArrowRight, Star, Zap, Globe, Menu, X, Search, Play, Calendar, MessageSquare, Code2 } from 'lucide-react';

const Dashboard = () => {
  const { user, token, logout, subscription } = useAuth();
  const navigate = useNavigate();
  const [activeTab, setActiveTab] = useState('Beginner');
  const [overviewCourse, setOverviewCourse] = useState(null);
  const [certCourse, setCertCourse] = useState(null);
  const [theme, setTheme] = useState(localStorage.getItem('theme') || 'dark');
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [dailyChallenge, setDailyChallenge] = useState(null);
  const [unreadNotifs, setUnreadNotifs] = useState(0);
  const [notifications, setNotifications] = useState([]);
  const [learningGoal, setLearningGoal] = useState(null);
  const { t, i18n } = useTranslation();

  const fetchNotifications = async () => {
    try {
      const res = await fetch('/notifications', { headers: { Authorization: `Bearer ${token}` }});
      if (res.ok) setNotifications(await res.json());
    } catch (e) {
      console.error(e);
    }
  };

  const markNotificationsRead = () => { setUnreadNotifs(0); };
  const clearAllNotifications = () => { setNotifications([]); setUnreadNotifs(0); };

  useEffect(() => {
    if (token) fetchNotifications();
  }, [token]);

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
    if (token) {
      fetchEngagementData();
    }
  }, [token]);

  const fetchEngagementData = async () => {
    try {
      // Fetch Daily Challenge
      const dcRes = await fetch('/daily-challenge/', { headers: { Authorization: `Bearer ${token}` }});
      if (dcRes.ok) setDailyChallenge(await dcRes.json());
      
      // Fetch Unread Notifications Count
      const notifRes = await fetch('/notifications/unread-count', { headers: { Authorization: `Bearer ${token}` }});
      if (notifRes.ok) {
        const data = await notifRes.json();
        setUnreadNotifs(data.count);
      }
      
      // Fetch Learning Goal
      const goalRes = await fetch('/users/me/goals/current', { headers: { Authorization: `Bearer ${token}` }});
      if (goalRes.ok) setLearningGoal(await goalRes.json());
    } catch (e) {
      console.error('Failed to fetch engagement data:', e);
    }
  };

  const handleSearch = (e) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      navigate(`/catalog?search=${encodeURIComponent(searchQuery)}`);
    }
  };

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
            const completed = getCourseProgress(courseName);
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
          
          <button 
            className="mobile-menu-btn" 
            onClick={() => setIsMenuOpen(!isMenuOpen)}
            aria-label="Toggle mobile menu"
          >
            {isMenuOpen ? <X size={20} /> : <Menu size={20} />}
          </button>

        <div className={`nav-right ${isMenuOpen ? 'open' : ''}`} style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          {/* Search Bar */}
          <form onSubmit={handleSearch} style={{ position: 'relative', display: 'flex', alignItems: 'center', marginRight: '10px' }}>
            <Search size={16} color="var(--text-dim)" style={{ position: 'absolute', left: '12px' }} />
            <input 
              type="text" 
              placeholder={t('dashboard.search') || "Search courses, topics..."} 
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              style={{
                padding: '8px 12px 8px 36px',
                background: 'var(--surface)',
                color: 'var(--text)',
                border: '1px solid var(--border)',
                borderRadius: '20px',
                fontSize: '13px',
                outline: 'none',
                width: '180px'
              }}
            />
          </form>

          {/* Language Switcher */}
          <div style={{ position: 'relative', display: 'flex', alignItems: 'center' }}>
            <Globe size={16} color="var(--text2)" style={{ position: 'absolute', left: '10px', pointerEvents: 'none' }} />
            <select
              value={i18n.language}
              onChange={(e) => changeLanguage(e.target.value)}
              style={{
                padding: '8px 12px 8px 30px',
                background: 'var(--surface)',
                color: 'var(--text)',
                border: '1px solid var(--border)',
                borderRadius: '20px',
                cursor: 'pointer',
                fontSize: '13px',
                fontWeight: 600,
                fontFamily: 'inherit',
                outline: 'none',
                appearance: 'none',
                WebkitAppearance: 'none',
                MozAppearance: 'none',
                paddingRight: '24px',
                backgroundImage: `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%239ca3af' stroke-width='2'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E")`,
                backgroundRepeat: 'no-repeat',
                backgroundPosition: 'right 8px center'
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
          <button 
            onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
            style={{ padding: '8px 12px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border)', borderRadius: '20px', cursor: 'pointer', display: 'flex', alignItems: 'center' }}
            title="Toggle Light/Dark Mode"
            aria-label="Toggle theme"
          >
            {theme === 'dark' ? <Sun size={18} /> : <Moon size={18} />}
          </button>
          
          <button 
            onClick={() => navigate('/community')}
            style={{ padding: '8px 16px', background: 'var(--surface2)', color: '#3b82f6', border: '1px solid var(--border)', borderRadius: '20px', cursor: 'pointer', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '6px' }}
          >
            <MessageSquare size={16} /> Forum
          </button>
          
          <button 
            onClick={() => navigate('/sandbox')}
            style={{ padding: '8px 16px', background: 'var(--surface2)', color: 'var(--accent)', border: '1px solid var(--border)', borderRadius: '20px', cursor: 'pointer', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '6px' }}
          >
            <Code2 size={16} /> Sandbox
          </button>

          <button 
            onClick={() => navigate('/leaderboard')}
            style={{ padding: '8px 16px', background: 'var(--surface2)', color: 'var(--accent3)', border: '1px solid var(--border)', borderRadius: '20px', cursor: 'pointer', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '6px' }}
          >
            <Trophy size={16} /> {t('dashboard.leaderboard') || 'Leaderboard'}
          </button>
          <div className="streak-badge">
            <Flame 
              size={16} 
              color="var(--accent3)" 
              style={{ animation: user?.streak > 0 ? 'pulse 2s infinite' : 'none' }} 
            /> 
            <span>{user?.streak || 0}</span> day streak
          </div>
          
          <NotificationCenter 
            notifications={notifications} 
            markAsRead={markNotificationsRead} 
            clearAll={clearAllNotifications} 
          />

          {((user?.role || '').toLowerCase() === 'admin' || (user?.role || '').toLowerCase() === 'teacher' || user?.email === 'nasaadanna@gmail.com') && (
            <button 
              onClick={() => navigate('/teacher')}
              style={{ padding: '8px 16px', background: 'var(--accent)', color: 'black', border: 'none', borderRadius: '20px', cursor: 'pointer', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '6px' }}
            >
              <Users size={16} /> Admin Portal
            </button>
          )}
          <button 
            onClick={() => navigate('/profile')}
            style={{ padding: '8px 16px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border)', borderRadius: '20px', cursor: 'pointer', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '6px' }}
          >
            <User size={16} /> Profile
          </button>
          <button 
            onClick={handleLogout}
            style={{ padding: '8px 16px', background: 'transparent', color: 'var(--text-dim)', border: '1px solid var(--border)', borderRadius: '20px', cursor: 'pointer', fontWeight: 'bold' }}
          >
            {t('dashboard.logout') || 'Logout'}
          </button>
        </div>
      </nav>

      <div className="dash-body">
        <div className="dash-hero">
          <div className="hero-left">
            <h2>{t('dashboard.welcome')}, <span>{user?.full_name?.split(' ')?.[0] || user?.email?.split('@')?.[0] || 'Student'}</span>!</h2>
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
              <div className="stat-item" style={{ animation: 'pulse 2s infinite' }}>
                <div className="stat-num" style={{ display: 'flex', alignItems: 'center', gap: '8px', justifyContent: 'center' }}>
                  <Zap size={24} color="var(--accent)" /> {user?.xp || 0}
                </div>
                <div className="stat-label">Total XP</div>
              </div>
              <div className="stat-item">
                <div className="stat-num">{user?.level || 'Beginner'}</div>
                <div className="stat-label">Current Level</div>
              </div>
            </div>

            {/* Badges Section */}
            <div style={{ display: 'flex', gap: '12px', marginTop: '24px', flexWrap: 'wrap' }}>
              {user?.streak >= 7 && (
                <div style={{ display: 'flex', alignItems: 'center', gap: '6px', padding: '6px 12px', background: 'rgba(245,158,11,0.1)', border: '1px solid rgba(245,158,11,0.2)', borderRadius: '20px', color: 'var(--accent3)', fontSize: '12px', fontWeight: 'bold' }}>
                  <Flame size={14} /> 7-Day Streak
                </div>
              )}
              {user?.level === 'Master' && (
                <div style={{ display: 'flex', alignItems: 'center', gap: '6px', padding: '6px 12px', background: 'rgba(234,179,8,0.1)', border: '1px solid rgba(234,179,8,0.2)', borderRadius: '20px', color: '#eab308', fontSize: '12px', fontWeight: 'bold' }}>
                  <Star size={14} /> Python Master
                </div>
              )}
              {user?.xp >= 100 && (
                <div style={{ display: 'flex', alignItems: 'center', gap: '6px', padding: '6px 12px', background: 'rgba(59,130,246,0.1)', border: '1px solid rgba(59,130,246,0.2)', borderRadius: '20px', color: 'var(--accent2)', fontSize: '12px', fontWeight: 'bold' }}>
                  <Trophy size={14} /> Century Club (100+ XP)
                </div>
              )}
            </div>
          </div>
        </div>

        {/* Engagement Row: Continue Learning, Daily Challenge, Weekly Goal */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '20px', marginBottom: '40px' }}>
          
          {/* Continue Learning */}
          {user?.last_active_course && (
            <div className="track-card" onClick={() => startCourse(user.last_active_course)} style={{ background: 'linear-gradient(145deg, var(--surface), var(--surface2))', border: '1px solid var(--accent)', cursor: 'pointer' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '12px' }}>
                <Play size={20} color="var(--accent)" fill="var(--accent)" />
                <h3 style={{ margin: 0, fontSize: '16px' }}>Continue Learning</h3>
              </div>
              <div style={{ fontWeight: 'bold', fontSize: '18px', marginBottom: '8px' }}>{user.last_active_course}</div>
              <div style={{ color: 'var(--text-dim)', fontSize: '14px', marginBottom: '16px' }}>
                Resume from Lesson {user.last_active_lesson_idx + 1}
              </div>
              <div className="track-progress-bar">
                <div className="bar-bg">
                  <div className="bar-fill" style={{ width: `${(getCourseProgress(user.last_active_course) / (courseManifest[user.last_active_course]?.lessons.length || 1)) * 100}%` }}></div>
                </div>
              </div>
            </div>
          )}

          {/* Daily Challenge */}
          {dailyChallenge && (
            <div className="track-card" onClick={() => navigate('/daily-challenge')} style={{ background: 'linear-gradient(145deg, var(--surface), rgba(59, 130, 246, 0.1))', border: '1px solid var(--accent2)', cursor: 'pointer' }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '12px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                  <Calendar size={20} color="var(--accent2)" />
                  <h3 style={{ margin: 0, fontSize: '16px' }}>Daily Practice</h3>
                </div>
                {dailyChallenge.already_completed ? (
                  <span style={{ fontSize: '12px', background: 'rgba(0,229,160,0.2)', color: 'var(--accent)', padding: '4px 8px', borderRadius: '12px', fontWeight: 'bold' }}>Completed</span>
                ) : (
                  <span style={{ fontSize: '12px', background: 'rgba(245,158,11,0.2)', color: '#f59e0b', padding: '4px 8px', borderRadius: '12px', fontWeight: 'bold' }}>Pending</span>
                )}
              </div>
              <div style={{ fontWeight: 'bold', fontSize: '16px', marginBottom: '8px' }}>{dailyChallenge.title}</div>
              <div style={{ color: 'var(--text-dim)', fontSize: '14px', marginBottom: '16px' }}>
                Earn +{dailyChallenge.xp_reward} XP and extend your streak!
              </div>
              <button style={{ width: '100%', padding: '8px', background: dailyChallenge.already_completed ? 'var(--surface2)' : 'var(--accent2)', color: dailyChallenge.already_completed ? 'var(--text-dim)' : '#fff', border: 'none', borderRadius: '8px', fontWeight: 'bold', cursor: 'pointer' }}>
                {dailyChallenge.already_completed ? 'Review Solution' : 'Solve Challenge'}
              </button>
            </div>
          )}

          {/* Weekly Goal */}
          {learningGoal && (
            <div className="track-card" onClick={() => navigate('/profile')} style={{ background: 'linear-gradient(145deg, var(--surface), rgba(245, 158, 11, 0.1))', border: '1px solid var(--accent3)', cursor: 'pointer' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '12px' }}>
                <Target size={20} color="var(--accent3)" />
                <h3 style={{ margin: 0, fontSize: '16px' }}>Weekly Goal</h3>
              </div>
              <div style={{ fontWeight: 'bold', fontSize: '18px', marginBottom: '8px' }}>
                {learningGoal.actual_days} / {learningGoal.target_days} Days
              </div>
              <div style={{ color: 'var(--text-dim)', fontSize: '14px', marginBottom: '16px' }}>
                You're on track! Keep learning to hit your goal.
              </div>
              <div className="track-progress-bar">
                <div className="bar-bg">
                  <div className="bar-fill" style={{ background: 'var(--accent3)', width: `${Math.min(100, (learningGoal.actual_days / learningGoal.target_days) * 100)}%` }}></div>
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Upgrade Banner for Free Users */}
        {subscription && !subscription.is_pro && (
          <div 
            onClick={() => navigate('/pricing')}
            role="button"
            tabIndex={0}
            onKeyDown={(e) => e.key === 'Enter' && navigate('/pricing')}
            style={{
              background: 'linear-gradient(135deg, rgba(0,229,160,0.08), rgba(59,130,246,0.08))',
              border: '1px solid var(--accent)',
              borderRadius: '16px',
              padding: '20px 28px',
              marginBottom: '32px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              cursor: 'pointer',
              transition: 'transform 0.2s, box-shadow 0.2s',
              flexWrap: 'wrap',
              gap: '16px'
            }}
            onMouseEnter={(e) => { e.currentTarget.style.transform = 'translateY(-2px)'; e.currentTarget.style.boxShadow = '0 8px 30px rgba(0,229,160,0.15)'; }}
            onMouseLeave={(e) => { e.currentTarget.style.transform = 'translateY(0)'; e.currentTarget.style.boxShadow = 'none'; }}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
              <div style={{
                width: '44px', height: '44px', borderRadius: '12px',
                background: 'rgba(0,229,160,0.15)',
                display: 'flex', alignItems: 'center', justifyContent: 'center'
              }}>
                <Crown size={22} color="var(--accent)" />
              </div>
              <div>
                <div style={{ fontWeight: 700, fontSize: '15px', marginBottom: '4px' }}>Upgrade to Pro</div>
                <div style={{ color: 'var(--text2)', fontSize: '13px' }}>Unlock all courses, unlimited AI tutor, certificates & more</div>
              </div>
            </div>
            <div style={{
              display: 'flex', alignItems: 'center', gap: '8px',
              background: 'var(--accent)', color: '#0d0f14',
              padding: '10px 20px', borderRadius: '100px',
              fontWeight: 700, fontSize: '13px', whiteSpace: 'nowrap'
            }}>
              See Plans <ArrowRight size={14} />
            </div>
          </div>
        )}

        {/* Pro Badge */}
        {subscription?.is_pro && (
          <div style={{
            background: 'rgba(0,229,160,0.08)',
            border: '1px solid rgba(0,229,160,0.2)',
            borderRadius: '12px',
            padding: '12px 20px',
            marginBottom: '24px',
            display: 'flex',
            alignItems: 'center',
            gap: '10px',
            fontSize: '13px',
            color: 'var(--accent)'
          }}>
            <Crown size={16} /> <strong>Pro Member</strong> — You have full access to all features
          </div>
        )}

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
          studentName={user?.full_name || user?.email?.split('@')?.[0] || 'Student'}
          onClose={() => setCertCourse(null)}
        />
      )}
    </div>
  );
};

export default Dashboard;
