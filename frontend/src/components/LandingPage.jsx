import React from 'react';
import { useNavigate } from 'react-router-dom';
import PublicNavbar from './PublicNavbar';
import { Rocket, Zap, Bot, Trophy, User, GraduationCap } from 'lucide-react';

const LandingPage = () => {
  const navigate = useNavigate();

  return (
    <div style={{ backgroundColor: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column', overflowX: 'hidden' }}>
      <PublicNavbar />
      
      {/* Hero Section */}
      <main style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', position: 'relative' }}>
        
        {/* Decorative background elements */}
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

          <h1 className="landing-hero-title">
            Master <span style={{ color: 'var(--accent)', textShadow: '0 0 30px var(--accent-glow)' }}>AI & Code</span><br />
            by Building Real Projects.
          </h1>
          
          <p className="landing-hero-subtitle">
            Stop watching tutorials and start typing. Digital Era gives you interactive environments to learn Python, React, Data Science, and AI.
          </p>
          
          <div className="landing-cta-row">
            <button 
              className="btn-primary" 
              style={{ padding: '16px 36px', fontSize: '16px', borderRadius: '100px', width: 'auto' }}
              onClick={() => navigate('/onboarding')}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>Start Coding for Free <Rocket size={20} /></div>
            </button>
            <button 
              className="returning-btn" 
              style={{ padding: '16px 36px', fontSize: '16px', borderRadius: '100px', width: 'auto', background: 'var(--surface)', color: 'var(--text)' }}
              onClick={() => navigate('/pricing')}
            >
              View Pricing
            </button>
          </div>

          {/* Feature Highlights Grid */}
          <div className="landing-features-grid">
            {[
              { icon: <Zap size={40} strokeWidth={1.5} color="var(--accent)" />, title: 'Interactive Workspaces', desc: 'Code right in your browser with real-time feedback and terminals.' },
              { icon: <Bot size={40} strokeWidth={1.5} color="var(--accent)" />, title: 'AI Assistant Included', desc: 'Get unstuck immediately with your personal AI coding tutor.' },
              { icon: <Trophy size={40} strokeWidth={1.5} color="var(--accent)" />, title: 'Earn Certifications', desc: 'Build a portfolio and earn recognized certificates as you learn.' }
            ].map((feat, i) => (
              <div key={i} className="landing-feature-card">
                <div style={{ marginBottom: '16px' }}>{feat.icon}</div>
                <h3 style={{ fontFamily: 'var(--font-display)', fontSize: '20px', fontWeight: 700, marginBottom: '12px' }}>{feat.title}</h3>
                <p style={{ color: 'var(--text2)', fontSize: '14px', lineHeight: 1.6 }}>{feat.desc}</p>
              </div>
            ))}
          </div>

          {/* About & Founder Section */}
          <div className="landing-about-section">
            <div style={{
              position: 'absolute', top: 0, right: 0, width: '300px', height: '300px',
              background: 'radial-gradient(circle, rgba(0,229,160,0.1), transparent 70%)',
              pointerEvents: 'none'
            }}></div>
            
            <h2 style={{ fontFamily: 'var(--font-display)', fontSize: '36px', fontWeight: 800, marginBottom: '24px' }}>
              About <span style={{ color: 'var(--accent)' }}>Digital Era</span>
            </h2>
            <p style={{ color: 'var(--text)', fontSize: '18px', maxWidth: '800px', lineHeight: 1.7, marginBottom: '48px' }}>
              Digital Era was built with a single mission: to bridge the gap between theoretical knowledge and real-world tech skills. We believe that the best way to master AI, Data Science, Product Management, and Coding is by getting your hands dirty and building actual projects.
            </p>

            <div className="landing-founder-card">
              <div style={{ 
                width: '120px', height: '120px', borderRadius: '50%', 
                background: 'linear-gradient(135deg, var(--accent), #3b82f6)', 
                flexShrink: 0, display: 'flex', alignItems: 'center', justifyContent: 'center',
                boxShadow: '0 10px 30px rgba(0,229,160,0.3)'
              }}>
                <User size={64} color="white" />
              </div>
              <div>
                <h3 style={{ fontFamily: 'var(--font-display)', fontSize: '28px', fontWeight: 700, marginBottom: '8px' }}>Meet the Founder</h3>
                <p style={{ color: 'var(--accent)', fontSize: '18px', fontWeight: 700, marginBottom: '16px' }}>Arua Mabel Chinasa</p>
                <p style={{ color: 'var(--text2)', fontSize: '15px', lineHeight: 1.6 }}>
                  Arua Mabel Chinasa founded Digital Era to empower the next generation of builders. With a passion for AI, data science, and modern web technologies, she designed this curriculum to provide the ultimate interactive learning experience. Her vision is to make elite tech education accessible, practical, and highly engaging for everyone.
                </p>
              </div>
            </div>
          </div>

        </div>

        {/* Pricing CTA */}
        <div style={{
          textAlign: 'center', padding: '60px 32px', margin: '60px 0',
          background: 'var(--surface)', border: '1px solid var(--border)',
          borderRadius: '24px', position: 'relative', overflow: 'hidden'
        }}>
          <div style={{
            position: 'absolute', top: 0, left: 0, right: 0, height: '3px',
            background: 'linear-gradient(90deg, var(--accent), #3b82f6, var(--accent3))'
          }}></div>
          <h2 style={{ fontFamily: 'var(--font-display)', fontSize: '32px', fontWeight: 800, marginBottom: '16px' }}>
            Ready to Go <span style={{ color: 'var(--accent)' }}>Pro</span>?
          </h2>
          <p style={{ color: 'var(--text2)', fontSize: '16px', maxWidth: '500px', margin: '0 auto 28px', lineHeight: 1.6 }}>
            Unlock all courses, unlimited AI tutoring, certificates, and more starting at just $9.99/month.
          </p>
          <div style={{ display: 'flex', gap: '12px', justifyContent: 'center', flexWrap: 'wrap' }}>
            <button 
              className="btn-primary" 
              style={{ padding: '14px 32px', fontSize: '15px', borderRadius: '100px', width: 'auto' }}
              onClick={() => navigate('/pricing')}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>See Plans & Pricing <Rocket size={18} /></div>
            </button>
            <button 
              className="returning-btn" 
              style={{ padding: '14px 32px', fontSize: '15px', borderRadius: '100px', width: 'auto', background: 'transparent', color: 'var(--text)', border: '1px solid var(--border)' }}
              onClick={() => navigate('/courses')}
            >
              Browse Free Courses
            </button>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="landing-footer">
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span style={{ display: 'flex', alignItems: 'center', gap: '6px' }}><GraduationCap size={18} /> Digital Era</span>
        </div>
        <p style={{ color: 'var(--text2)', fontSize: '13px' }}>© 2026 Digital Era. Founded by Arua Mabel Chinasa.</p>
      </footer>
    </div>
  );
};

export default LandingPage;
