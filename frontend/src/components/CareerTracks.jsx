import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Code, Database, LineChart, Server, Layout, Shield, ArrowRight, PlayCircle, Briefcase, ChevronRight } from 'lucide-react';
import PublicNavbar from './PublicNavbar';

const CareerTracks = () => {
  const navigate = useNavigate();
  
  const tracks = [
    {
      id: 'python-dev',
      title: 'Python Developer',
      icon: <Code size={24} color="#3b82f6" />,
      color: '#3b82f6',
      courses: 8,
      hours: 45,
      description: 'Master Python from basics to advanced applications, including web scraping, automation, and API development.',
      salary: '$110,000+',
      steps: [
        { name: 'Python Basics', type: 'Course' },
        { name: 'Object-Oriented Programming', type: 'Course' },
        { name: 'Data Structures', type: 'Course' },
        { name: 'Python Web Scraping', type: 'Project' },
        { name: 'Building REST APIs', type: 'Course' },
      ]
    },
    {
      id: 'data-scientist',
      title: 'Data Scientist',
      icon: <LineChart size={24} color="var(--accent)" />,
      color: 'var(--accent)',
      courses: 12,
      hours: 60,
      description: 'Learn data manipulation, visualization, and machine learning using Python, pandas, scikit-learn, and more.',
      salary: '$125,000+',
      steps: [
        { name: 'Intro to Data Science', type: 'Course' },
        { name: 'Data Manipulation with Pandas', type: 'Course' },
        { name: 'Data Visualization', type: 'Course' },
        { name: 'Predictive Modeling', type: 'Project' },
        { name: 'Machine Learning', type: 'Course' },
      ]
    },
    {
      id: 'backend-engineer',
      title: 'Backend Engineer',
      icon: <Server size={24} color="#f59e0b" />,
      color: '#f59e0b',
      courses: 10,
      hours: 55,
      description: 'Build scalable backend systems with Python, FastAPI, Node.js, and databases.',
      salary: '$130,000+',
      steps: [
        { name: 'Backend Fundamentals', type: 'Course' },
        { name: 'Database Design (SQL)', type: 'Course' },
        { name: 'FastAPI Masterclass', type: 'Course' },
        { name: 'Authentication & Security', type: 'Course' },
        { name: 'E-commerce API', type: 'Project' },
      ]
    },
    {
      id: 'frontend-engineer',
      title: 'Frontend Engineer',
      icon: <Layout size={24} color="#ec4899" />,
      color: '#ec4899',
      courses: 9,
      hours: 50,
      description: 'Create beautiful, responsive user interfaces with HTML, CSS, JavaScript, and React.',
      salary: '$105,000+',
      steps: [
        { name: 'HTML & CSS Basics', type: 'Course' },
        { name: 'JavaScript Deep Dive', type: 'Course' },
        { name: 'React Fundamentals', type: 'Course' },
        { name: 'State Management', type: 'Course' },
        { name: 'Portfolio Website', type: 'Project' },
      ]
    }
  ];

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      <PublicNavbar />
      
      <main style={{ flex: 1, padding: '40px 24px', maxWidth: '1200px', margin: '0 auto', width: '100%' }}>
        <div style={{ textAlign: 'center', marginBottom: '60px' }}>
          <div style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', padding: '6px 16px', background: 'rgba(0,229,160,0.1)', border: '1px solid var(--accent)', borderRadius: '100px', color: 'var(--accent)', fontWeight: 600, fontSize: '14px', marginBottom: '24px' }}>
            <Briefcase size={16} /> Career Tracks
          </div>
          <h1 style={{ fontFamily: 'var(--font-display)', fontSize: 'clamp(32px, 5vw, 48px)', fontWeight: 800, marginBottom: '16px', color: 'var(--text)' }}>
            Your Roadmap to a <span style={{ color: 'var(--accent)' }}>Tech Career</span>
          </h1>
          <p style={{ color: 'var(--text2)', fontSize: '18px', maxWidth: '600px', margin: '0 auto', lineHeight: 1.6 }}>
            Curated learning paths designed by industry experts. Go from absolute beginner to job-ready professional.
          </p>
        </div>

        <div style={{ display: 'grid', gap: '32px' }}>
          {tracks.map((track) => (
            <div key={track.id} style={{ background: 'var(--surface)', border: '1px solid var(--border)', borderRadius: '24px', overflow: 'hidden' }}>
              <div style={{ display: 'flex', flexWrap: 'wrap' }}>
                
                {/* Track Info */}
                <div style={{ flex: '1 1 400px', padding: '40px', borderRight: '1px solid var(--border)' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '16px', marginBottom: '24px' }}>
                    <div style={{ width: '56px', height: '56px', borderRadius: '16px', background: `${track.color}15`, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                      {track.icon}
                    </div>
                    <div>
                      <h2 style={{ fontSize: '28px', fontWeight: 800, color: 'var(--text)', fontFamily: 'var(--font-display)', marginBottom: '4px' }}>{track.title}</h2>
                      <div style={{ display: 'flex', gap: '16px', color: 'var(--text3)', fontSize: '14px', fontWeight: 600 }}>
                        <span>{track.courses} Courses</span>
                        <span>•</span>
                        <span>{track.hours} Hours</span>
                      </div>
                    </div>
                  </div>
                  
                  <p style={{ color: 'var(--text2)', fontSize: '16px', lineHeight: 1.6, marginBottom: '32px' }}>
                    {track.description}
                  </p>
                  
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '16px', background: 'var(--surface2)', borderRadius: '12px', marginBottom: '32px' }}>
                    <div>
                      <div style={{ fontSize: '13px', color: 'var(--text3)', fontWeight: 600, textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '4px' }}>Avg. Starting Salary</div>
                      <div style={{ fontSize: '24px', fontWeight: 800, color: 'var(--text)', fontFamily: 'var(--font-mono)' }}>{track.salary}</div>
                    </div>
                  </div>
                  
                  <button 
                    onClick={() => navigate('/courses')}
                    style={{ width: '100%', padding: '16px', background: 'var(--accent)', color: '#000', border: 'none', borderRadius: '12px', fontWeight: 'bold', fontSize: '16px', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px' }}
                  >
                    Start Track <ArrowRight size={20} />
                  </button>
                </div>
                
                {/* Track Roadmap */}
                <div style={{ flex: '2 1 500px', padding: '40px', background: 'var(--surface2)' }}>
                  <h3 style={{ fontSize: '18px', fontWeight: 700, color: 'var(--text)', marginBottom: '32px' }}>Track Syllabus</h3>
                  
                  <div style={{ position: 'relative' }}>
                    {/* Vertical Line */}
                    <div style={{ position: 'absolute', left: '20px', top: '24px', bottom: '24px', width: '2px', background: 'var(--border)' }}></div>
                    
                    {track.steps.map((step, idx) => (
                      <div key={idx} style={{ display: 'flex', alignItems: 'flex-start', gap: '24px', marginBottom: idx === track.steps.length - 1 ? 0 : '32px', position: 'relative' }}>
                        <div style={{ width: '42px', height: '42px', borderRadius: '50%', background: 'var(--surface)', border: `2px solid ${track.color}`, display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 1, flexShrink: 0, fontWeight: 'bold', color: 'var(--text)' }}>
                          {idx + 1}
                        </div>
                        <div style={{ background: 'var(--surface)', border: '1px solid var(--border)', padding: '20px', borderRadius: '12px', flex: 1 }}>
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                            <div style={{ fontSize: '12px', fontWeight: 600, color: step.type === 'Course' ? 'var(--text2)' : 'var(--accent)', textTransform: 'uppercase', letterSpacing: '1px', padding: '4px 8px', background: 'var(--surface2)', borderRadius: '4px' }}>
                              {step.type}
                            </div>
                          </div>
                          <h4 style={{ fontSize: '16px', fontWeight: 600, color: 'var(--text)' }}>{step.name}</h4>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
};

export default CareerTracks;
