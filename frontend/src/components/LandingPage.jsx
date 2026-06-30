import React from 'react';
import { useNavigate } from 'react-router-dom';
import PublicNavbar from './PublicNavbar';

const LandingPage = () => {
  const navigate = useNavigate();

  return (
    <div style={{ backgroundColor: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column', overflowX: 'hidden' }}>
      <PublicNavbar />
      
      {/* Hero Section */}
      <main style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', position: 'relative' }}>
        
        {/* Decorative background elements (glassmorphism/glow) */}
        <div style={{ 
          position: 'absolute', top: '-150px', left: '50%', transform: 'translateX(-50%)',
          width: '800px', height: '800px', 
          background: 'radial-gradient(circle, rgba(0, 229, 160, 0.1) 0%, transparent 70%)',
          borderRadius: '50%', pointerEvents: 'none', zIndex: 0
        }}></div>
        <div style={{ 
          position: 'absolute', top: '200px', right: '-200px',
          width: '600px', height: '600px', 
          background: 'radial-gradient(circle, rgba(59, 130, 246, 0.08) 0%, transparent 70%)',
          borderRadius: '50%', pointerEvents: 'none', zIndex: 0
        }}></div>

        <div style={{ 
          maxWidth: '1200px', width: '100%', padding: '100px 32px', 
          display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center',
          position: 'relative', zIndex: 1
        }}>
          
          <div style={{ 
            display: 'inline-flex', alignItems: 'center', gap: '8px',
            padding: '6px 16px', background: 'var(--surface)', border: '1px solid var(--border)',
            borderRadius: '100px', marginBottom: '32px',
            boxShadow: '0 4px 20px rgba(0,0,0,0.2)'
          }}>
            <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--accent)' }}>NEW</span>
            <span style={{ fontSize: '12px', color: 'var(--text2)' }}>AI-Powered Learning Paths are live!</span>
          </div>

          <h1 style={{ 
            fontFamily: 'var(--font-display)', fontSize: '64px', fontWeight: 800, 
            lineHeight: 1.1, marginBottom: '24px', letterSpacing: '-1px'
          }}>
            Master <span style={{ color: 'var(--accent)', textShadow: '0 0 30px var(--accent-glow)' }}>AI & Code</span><br />
            by Building Real Projects.
          </h1>
          
          <p style={{ 
            fontSize: '18px', color: 'var(--text2)', maxWidth: '600px', 
            lineHeight: 1.6, marginBottom: '48px'
          }}>
            Stop watching tutorials and start typing. Digital Era gives you interactive environments to learn Python, React, Data Science, and AI.
          </p>
          
          <div style={{ display: 'flex', gap: '20px' }}>
            <button 
              className="btn-primary" 
              style={{ padding: '16px 36px', fontSize: '16px', borderRadius: '100px', width: 'auto' }}
              onClick={() => navigate('/onboarding')}
            >
              Start Coding for Free 🚀
            </button>
            <button 
              className="returning-btn" 
              style={{ padding: '16px 36px', fontSize: '16px', borderRadius: '100px', width: 'auto', background: 'var(--surface)', color: 'var(--text)' }}
              onClick={() => navigate('/courses')}
            >
              Browse Curriculum
            </button>
          </div>

          {/* Feature Highlights Grid */}
          <div style={{ 
            display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '24px', 
            marginTop: '100px', width: '100%'
          }}>
            {[
              { icon: '⚡', title: 'Interactive Workspaces', desc: 'Code right in your browser with real-time feedback and terminals.' },
              { icon: '🤖', title: 'AI Assistant Included', desc: 'Get unstuck immediately with your personal AI coding tutor.' },
              { icon: '🏆', title: 'Earn Certifications', desc: 'Build a portfolio and earn recognized certificates as you learn.' }
            ].map((feat, i) => (
              <div key={i} style={{ 
                background: 'var(--surface)', padding: '32px', borderRadius: 'var(--radius)',
                border: '1px solid var(--border)', textAlign: 'left',
                transition: 'transform 0.3s, box-shadow 0.3s', cursor: 'default'
              }} onMouseOver={e => {
                e.currentTarget.style.transform = 'translateY(-5px)';
                e.currentTarget.style.boxShadow = '0 10px 30px rgba(0,0,0,0.3)';
                e.currentTarget.style.borderColor = 'var(--accent)';
              }} onMouseOut={e => {
                e.currentTarget.style.transform = 'translateY(0)';
                e.currentTarget.style.boxShadow = 'none';
                e.currentTarget.style.borderColor = 'var(--border)';
              }}>
                <div style={{ fontSize: '32px', marginBottom: '16px' }}>{feat.icon}</div>
                <h3 style={{ fontFamily: 'var(--font-display)', fontSize: '20px', fontWeight: 700, marginBottom: '12px' }}>{feat.title}</h3>
                <p style={{ color: 'var(--text2)', fontSize: '14px', lineHeight: 1.6 }}>{feat.desc}</p>
              </div>
            ))}
          </div>

        </div>
      </main>

      {/* Footer */}
      <footer style={{ 
        padding: '32px', borderTop: '1px solid var(--border)', 
        display: 'flex', justifyContent: 'space-between', alignItems: 'center',
        background: 'var(--surface)'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span style={{ fontSize: '18px' }}>🎓</span>
          <span style={{ fontFamily: 'var(--font-display)', fontWeight: 700, fontSize: '16px' }}>Digital Era</span>
        </div>
        <p style={{ color: 'var(--text2)', fontSize: '13px' }}>© 2026 Digital Era Academy. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default LandingPage;
