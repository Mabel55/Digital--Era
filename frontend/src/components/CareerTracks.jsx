import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Code, Database, LineChart, Server, Layout, Shield, ArrowRight, PlayCircle, Briefcase, ChevronDown, ChevronUp, Clock, BookOpen, Star } from 'lucide-react';
import PublicNavbar from './PublicNavbar';
import { Helmet } from 'react-helmet-async';

const tracks = [
  {
    id: 'python-dev',
    title: 'Python Developer',
    icon: <Code size={24} color="#3b82f6" />,
    color: '#3b82f6',
    category: 'Backend',
    courses: 8,
    hours: 45,
    description: 'Master Python from basics to advanced applications, including web scraping, automation, and API development.',
    salary: '$110,000+',
    steps: [
      { name: 'Python Basics', type: 'Course', hours: 6 },
      { name: 'Object-Oriented Programming', type: 'Course', hours: 8 },
      { name: 'Data Structures', type: 'Course', hours: 7 },
      { name: 'Python Web Scraping', type: 'Project', hours: 5 },
      { name: 'Building REST APIs', type: 'Course', hours: 10 },
    ]
  },
  {
    id: 'data-scientist',
    title: 'Data Scientist',
    icon: <LineChart size={24} color="var(--accent)" />,
    color: '#00e5a0',
    category: 'Data',
    courses: 12,
    hours: 60,
    description: 'Learn data manipulation, visualization, and machine learning using Python, pandas, scikit-learn, and more.',
    salary: '$125,000+',
    steps: [
      { name: 'Intro to Data Science', type: 'Course', hours: 5 },
      { name: 'Data Manipulation with Pandas', type: 'Course', hours: 8 },
      { name: 'Data Visualization', type: 'Course', hours: 7 },
      { name: 'Predictive Modeling', type: 'Project', hours: 10 },
      { name: 'Machine Learning', type: 'Course', hours: 12 },
    ]
  },
  {
    id: 'backend-engineer',
    title: 'Backend Engineer',
    icon: <Server size={24} color="#f59e0b" />,
    color: '#f59e0b',
    category: 'Backend',
    courses: 10,
    hours: 55,
    description: 'Build scalable backend systems with Python, FastAPI, Node.js, and databases.',
    salary: '$130,000+',
    steps: [
      { name: 'Backend Fundamentals', type: 'Course', hours: 6 },
      { name: 'Database Design (SQL)', type: 'Course', hours: 8 },
      { name: 'FastAPI Masterclass', type: 'Course', hours: 10 },
      { name: 'Authentication & Security', type: 'Course', hours: 7 },
      { name: 'E-commerce API', type: 'Project', hours: 12 },
    ]
  },
  {
    id: 'frontend-engineer',
    title: 'Frontend Engineer',
    icon: <Layout size={24} color="#ec4899" />,
    color: '#ec4899',
    category: 'Frontend',
    courses: 9,
    hours: 50,
    description: 'Create beautiful, responsive user interfaces with HTML, CSS, JavaScript, and React.',
    salary: '$105,000+',
    steps: [
      { name: 'HTML & CSS Basics', type: 'Course', hours: 5 },
      { name: 'JavaScript Deep Dive', type: 'Course', hours: 10 },
      { name: 'React Fundamentals', type: 'Course', hours: 8 },
      { name: 'State Management', type: 'Course', hours: 6 },
      { name: 'Portfolio Website', type: 'Project', hours: 8 },
    ]
  },
  {
    id: 'ai-engineer',
    title: 'AI Engineer',
    icon: <Database size={24} color="#a78bfa" />,
    color: '#a78bfa',
    category: 'AI',
    courses: 11,
    hours: 65,
    description: 'Build intelligent systems with LLMs, RAG, agents, computer vision, and production ML pipelines.',
    salary: '$145,000+',
    steps: [
      { name: 'Python for AI', type: 'Course', hours: 6 },
      { name: 'Machine Learning Fundamentals', type: 'Course', hours: 12 },
      { name: 'Deep Learning with PyTorch', type: 'Course', hours: 10 },
      { name: 'LLMs & Prompt Engineering', type: 'Course', hours: 8 },
      { name: 'AI Chatbot with RAG', type: 'Project', hours: 14 },
    ]
  },
];

const FILTERS = ['All', 'Frontend', 'Backend', 'Data', 'AI'];

const CareerTracks = () => {
  const navigate = useNavigate();
  const [activeFilter, setActiveFilter] = useState('All');
  const [expandedTracks, setExpandedTracks] = useState({});

  const toggleTrack = (id) => {
    setExpandedTracks(prev => ({ ...prev, [id]: !prev[id] }));
  };

  const filtered = activeFilter === 'All'
    ? tracks
    : tracks.filter(t => t.category === activeFilter);

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      <Helmet>
        <title>Career Tracks | Digital Era Academy</title>
        <meta name="description" content="Explore curated career paths — Python Developer, Data Scientist, Backend Engineer, Frontend Engineer, AI Engineer. Go from beginner to job-ready." />
        <meta property="og:title" content="Career Tracks | Digital Era Academy" />
        <meta property="og:description" content="Structured, expert-designed learning paths from Digital Era to launch your tech career." />
      </Helmet>
      <PublicNavbar />
      
      <main style={{ flex: 1, padding: '40px 24px', maxWidth: '1200px', margin: '0 auto', width: '100%' }}>
        {/* Header */}
        <div style={{ textAlign: 'center', marginBottom: '48px' }}>
          <div style={{
            display: 'inline-flex', alignItems: 'center', gap: '8px',
            padding: '6px 16px', background: 'rgba(0,229,160,0.1)', border: '1px solid var(--accent)',
            borderRadius: '100px', color: 'var(--accent)', fontWeight: 600, fontSize: '14px', marginBottom: '24px'
          }}>
            <Briefcase size={16} /> Career Tracks
          </div>
          <h1 style={{ fontFamily: 'var(--font-display)', fontSize: 'clamp(32px, 5vw, 48px)', fontWeight: 800, marginBottom: '16px', color: 'var(--text)' }}>
            Your Roadmap to a <span style={{ color: 'var(--accent)' }}>Tech Career</span>
          </h1>
          <p style={{ color: 'var(--text2)', fontSize: '18px', maxWidth: '600px', margin: '0 auto', lineHeight: 1.6 }}>
            Curated learning paths designed by industry experts. Go from absolute beginner to job-ready professional.
          </p>
        </div>

        {/* Filter Tabs */}
        <div style={{
          display: 'flex', gap: '10px', justifyContent: 'center',
          flexWrap: 'wrap', marginBottom: '48px'
        }}>
          {FILTERS.map(f => (
            <button
              key={f}
              onClick={() => setActiveFilter(f)}
              style={{
                padding: '10px 24px', borderRadius: '100px', cursor: 'pointer',
                fontWeight: 700, fontSize: '14px', minHeight: '44px',
                border: activeFilter === f ? '1px solid var(--accent)' : '1px solid var(--border)',
                background: activeFilter === f ? 'rgba(0,229,160,0.12)' : 'var(--surface)',
                color: activeFilter === f ? 'var(--accent)' : 'var(--text)',
                transition: 'all 0.2s',
              }}
            >
              {f}
            </button>
          ))}
        </div>

        {/* Track Cards */}
        <div style={{ display: 'grid', gap: '28px' }}>
          {filtered.map((track, idx) => {
            const isOpen = !!expandedTracks[track.id];
            return (
              <div
                key={track.id}
                className="card-enter"
                style={{
                  background: 'var(--surface)', border: '1px solid var(--border)',
                  borderRadius: '24px', overflow: 'hidden',
                  animationDelay: `${idx * 0.08}s`,
                  transition: 'border-color 0.3s'
                }}
                onMouseEnter={e => e.currentTarget.style.borderColor = track.color + '66'}
                onMouseLeave={e => e.currentTarget.style.borderColor = 'var(--border)'}
              >
                {/* Top accent bar */}
                <div style={{ height: '3px', background: `linear-gradient(90deg, ${track.color}, transparent)` }} />

                <div style={{ display: 'flex', flexWrap: 'wrap' }}>
                  {/* ── Left: Track Info ── */}
                  <div style={{ flex: '1 1 320px', padding: '36px 40px', borderRight: '1px solid var(--border)' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '16px', marginBottom: '20px' }}>
                      <div style={{
                        width: '56px', height: '56px', borderRadius: '16px',
                        background: `${track.color}18`, display: 'flex', alignItems: 'center', justifyContent: 'center',
                        border: `1px solid ${track.color}33`
                      }}>
                        {track.icon}
                      </div>
                      <div>
                        <h2 style={{ fontSize: '24px', fontWeight: 800, color: 'var(--text)', fontFamily: 'var(--font-display)', marginBottom: '4px' }}>
                          {track.title}
                        </h2>
                        <div style={{ display: 'flex', gap: '12px', color: 'var(--text3)', fontSize: '13px', fontWeight: 600 }}>
                          <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}><BookOpen size={12} /> {track.courses} Courses</span>
                          <span>•</span>
                          <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}><Clock size={12} /> {track.hours}h total</span>
                        </div>
                      </div>
                    </div>
                    
                    <p style={{ color: 'var(--text2)', fontSize: '15px', lineHeight: 1.6, marginBottom: '24px' }}>
                      {track.description}
                    </p>
                    
                    {/* Salary */}
                    <div style={{
                      display: 'flex', alignItems: 'center', justifyContent: 'space-between',
                      padding: '14px 16px', background: 'var(--surface2)', borderRadius: '12px',
                      border: `1px solid ${track.color}22`, marginBottom: '24px'
                    }}>
                      <div>
                        <div style={{ fontSize: '11px', color: 'var(--text3)', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '4px' }}>
                          Avg. Starting Salary
                        </div>
                        <div style={{ fontSize: '22px', fontWeight: 800, color: track.color, fontFamily: 'var(--font-mono)' }}>
                          {track.salary}
                        </div>
                      </div>
                      <div style={{ display: 'flex', gap: '2px' }}>
                        {[1,2,3,4,5].map(s => <Star key={s} size={14} color="#f59e0b" fill="#f59e0b" />)}
                      </div>
                    </div>

                    <button 
                      onClick={() => navigate('/catalog')}
                      style={{
                        width: '100%', padding: '14px', background: track.color,
                        color: track.color === '#00e5a0' || track.color === '#f59e0b' ? '#000' : '#fff',
                        border: 'none', borderRadius: '12px', fontWeight: 'bold', fontSize: '15px',
                        cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px',
                        transition: 'opacity 0.2s', minHeight: '44px'
                      }}
                      onMouseEnter={e => e.currentTarget.style.opacity = '0.85'}
                      onMouseLeave={e => e.currentTarget.style.opacity = '1'}
                    >
                      Start Track <ArrowRight size={18} />
                    </button>
                  </div>
                  
                  {/* ── Right: Roadmap ── */}
                  <div style={{ flex: '2 1 400px', padding: '36px 40px', background: 'var(--surface2)' }}>
                    {/* Mobile: collapsible toggle */}
                    <button
                      onClick={() => toggleTrack(track.id)}
                      style={{
                        display: 'none',
                        width: '100%', padding: '12px 16px', marginBottom: '16px',
                        background: 'var(--surface)', border: '1px solid var(--border)',
                        borderRadius: '10px', cursor: 'pointer', color: 'var(--text)',
                        fontWeight: 600, fontSize: '14px', alignItems: 'center',
                        justifyContent: 'space-between', gap: '8px'
                      }}
                      className="track-syllabus-toggle"
                      aria-expanded={isOpen}
                    >
                      Track Syllabus ({track.steps.length} steps)
                      {isOpen ? <ChevronUp size={18} /> : <ChevronDown size={18} />}
                    </button>

                    <h3 style={{ fontSize: '16px', fontWeight: 700, color: 'var(--text)', marginBottom: '28px' }}>
                      Track Syllabus
                    </h3>
                    
                    <div style={{ position: 'relative' }} className={`track-syllabus-content ${isOpen ? 'open' : ''}`}>
                      {/* Animated vertical connector */}
                      <div style={{
                        position: 'absolute', left: '20px', top: '21px', bottom: '21px', width: '2px',
                        background: `linear-gradient(180deg, ${track.color} 0%, var(--border) 100%)`,
                      }} />
                      
                      {track.steps.map((step, idx2) => (
                        <div
                          key={idx2}
                          className={`card-enter card-enter-${Math.min(idx2 + 1, 6)}`}
                          style={{
                            display: 'flex', alignItems: 'flex-start', gap: '20px',
                            marginBottom: idx2 === track.steps.length - 1 ? 0 : '20px',
                            position: 'relative'
                          }}
                        >
                          {/* Step number bubble */}
                          <div style={{
                            width: '42px', height: '42px', borderRadius: '50%',
                            background: idx2 === 0 ? track.color : 'var(--surface)',
                            border: `2px solid ${track.color}`,
                            display: 'flex', alignItems: 'center', justifyContent: 'center',
                            zIndex: 1, flexShrink: 0,
                            fontWeight: 'bold', fontSize: '14px',
                            color: idx2 === 0 ? (track.color === '#00e5a0' || track.color === '#f59e0b' ? '#000' : '#fff') : 'var(--text)',
                            transition: 'background 0.3s'
                          }}>
                            {idx2 + 1}
                          </div>

                          {/* Step content */}
                          <div style={{
                            background: 'var(--surface)', border: '1px solid var(--border)',
                            padding: '16px 20px', borderRadius: '12px', flex: 1,
                            transition: 'border-color 0.2s',
                          }}
                            onMouseEnter={e => e.currentTarget.style.borderColor = track.color + '66'}
                            onMouseLeave={e => e.currentTarget.style.borderColor = 'var(--border)'}
                          >
                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                              <span style={{
                                fontSize: '11px', fontWeight: 700,
                                color: step.type === 'Project' ? track.color : 'var(--text3)',
                                textTransform: 'uppercase', letterSpacing: '1px',
                                padding: '3px 8px', background: step.type === 'Project' ? `${track.color}18` : 'var(--surface2)',
                                borderRadius: '4px'
                              }}>
                                {step.type}
                              </span>
                              <span style={{ fontSize: '12px', color: 'var(--text3)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                                <Clock size={11} /> {step.hours}h
                              </span>
                            </div>
                            <h4 style={{ fontSize: '15px', fontWeight: 600, color: 'var(--text)' }}>{step.name}</h4>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>

        {/* Bottom CTA */}
        <div style={{
          textAlign: 'center', marginTop: '64px', padding: '48px 32px',
          background: 'var(--surface)', borderRadius: '24px',
          border: '1px solid var(--border)', position: 'relative', overflow: 'hidden'
        }}>
          <div style={{
            position: 'absolute', top: 0, left: 0, right: 0, height: '3px',
            background: 'linear-gradient(90deg, var(--accent), #3b82f6, var(--accent3))'
          }} />
          <h2 style={{ fontFamily: 'var(--font-display)', fontSize: '28px', fontWeight: 800, marginBottom: '12px' }}>
            Not sure which track? <span style={{ color: 'var(--accent)' }}>Take the Quiz!</span>
          </h2>
          <p style={{ color: 'var(--text2)', marginBottom: '24px', maxWidth: '480px', margin: '0 auto 24px' }}>
            Answer 5 quick questions and we'll recommend the perfect career path for your goals.
          </p>
          <button
            onClick={() => navigate('/onboarding')}
            className="btn-primary"
            style={{ padding: '14px 36px', borderRadius: '100px', width: 'auto', fontSize: '15px' }}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              Find My Track <ArrowRight size={18} />
            </div>
          </button>
        </div>
      </main>

      {/* Inline style for mobile toggle visibility */}
      <style>{`
        @media (max-width: 768px) {
          .track-syllabus-toggle { display: flex !important; }
          .track-syllabus-content { display: none; }
          .track-syllabus-content.open { display: block; }
        }
      `}</style>
    </div>
  );
};

export default CareerTracks;
