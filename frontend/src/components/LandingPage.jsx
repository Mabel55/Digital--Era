import React, { useEffect, useRef, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import PublicNavbar from './PublicNavbar';
import { Rocket, Zap, Bot, Trophy, User, GraduationCap, Star, ArrowRight, Briefcase } from 'lucide-react';
import { Helmet } from 'react-helmet-async';
import mabelFounderImg from '../../public/mabel-founder.jpg';
import CustomerSupportChat from './CustomerSupportChat';

const LandingPage = () => {
  const navigate = useNavigate();
  const statsRef = useRef(null);
  const [statsVisible, setStatsVisible] = useState(false);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => { if (entry.isIntersecting) { setStatsVisible(true); observer.disconnect(); } },
      { threshold: 0.3 }
    );
    if (statsRef.current) observer.observe(statsRef.current);
    return () => observer.disconnect();
  }, []);

  return (
    <div style={{ backgroundColor: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column', overflowX: 'hidden' }}>
      <Helmet>
        <title>Digital Era | Tech Training Centre in Ikorodu, Lagos | AI, Data &amp; Code</title>
        <meta name="description" content="Digital Era is a tech training centre in Ikorodu, Lagos, founded by Arua Mabel Chinasa. Learn Python, Data Science, AI, and Coding with hands-on interactive projects. Enroll today!" />
        <meta name="keywords" content="tech training Lagos, coding school Ikorodu, AI course Lagos, data science Nigeria, Python training Lagos, Digital Era Mabel Chinasa, software development school Lagos" />
        <meta name="geo.region" content="NG-LA" />
        <meta name="geo.placename" content="Ikorodu, Lagos, Nigeria" />
        <meta name="geo.position" content="6.6194;3.5106" />
        <meta name="ICBM" content="6.6194, 3.5106" />
        {/* Open Graph */}
        <meta property="og:type" content="website" />
        <meta property="og:url" content="https://digital-era.app" />
        <meta property="og:title" content="Digital Era | Master AI & Code in Lagos" />
        <meta property="og:description" content="Hands-on Python, Data Science, AI &amp; Coding school in Ikorodu, Lagos. Interactive projects, AI tutor, and real certificates." />
        <meta property="og:image" content="/mabel-founder.jpg" />
        {/* Twitter Card */}
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Digital Era | Master AI & Code" />
        <meta name="twitter:description" content="Learn Python, Data Science and AI in Lagos with hands-on interactive projects." />
      </Helmet>
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
          
          <div
            className="hero-badge-pulse"
            style={{ 
              display: 'inline-flex', alignItems: 'center', gap: '8px',
              padding: '6px 16px', background: 'var(--surface)', border: '1px solid rgba(0,229,160,0.4)',
              borderRadius: '100px', marginBottom: '32px',
            }}
          >
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
              onClick={() => navigate('/careers')}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}><Briefcase size={18} /> View Careers</div>
            </button>
            <button 
              className="returning-btn" 
              style={{ padding: '16px 36px', fontSize: '16px', borderRadius: '100px', width: 'auto', background: 'transparent', color: 'var(--text2)', border: '1px solid var(--border)' }}
              onClick={() => navigate('/pricing')}
            >
              View Pricing
            </button>
          </div>

          {/* Tech Logos */}
          <div style={{ marginTop: '60px', opacity: 0.6, width: '100%', maxWidth: '800px', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <div style={{ fontSize: '12px', textTransform: 'uppercase', letterSpacing: '2px', fontWeight: 'bold', marginBottom: '20px' }}>Learn Top Technologies</div>
            <div style={{ display: 'flex', gap: '40px', flexWrap: 'wrap', justifyContent: 'center', fontSize: '20px', fontWeight: 'bold', fontFamily: 'var(--font-mono)' }}>
              <span>Python</span>
              <span>React</span>
              <span>SQL</span>
              <span>Docker</span>
              <span>TensorFlow</span>
              <span>FastAPI</span>
            </div>
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
          {/* How It Works Section */}
          <div style={{ marginTop: '100px', width: '100%', textAlign: 'center' }}>
            <h2 style={{ fontFamily: 'var(--font-display)', fontSize: '32px', fontWeight: 800, marginBottom: '40px' }}>How Digital Era Works</h2>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '20px', justifyContent: 'center' }}>
              {[
                { step: '1', title: 'Choose Your Track', desc: 'Select from Frontend, Backend, Data Science or AI.' },
                { step: '2', title: 'Learn by Doing', desc: 'Read concise theory and jump straight into our built-in code editor.' },
                { step: '3', title: 'Get Instant Feedback', desc: 'Run your code, pass tests, and ask the AI Tutor for hints if stuck.' },
                { step: '4', title: 'Earn Certificates', desc: 'Complete courses to earn verifiable certificates for your resume.' }
              ].map((s, i) => (
                <div key={i} style={{ flex: '1 1 200px', background: 'var(--surface2)', padding: '24px', borderRadius: '16px', border: '1px solid var(--border)' }}>
                  <div style={{ width: '40px', height: '40px', borderRadius: '50%', background: 'var(--accent)', color: 'black', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '20px', fontWeight: 'bold', margin: '0 auto 16px' }}>{s.step}</div>
                  <h3 style={{ fontSize: '18px', marginBottom: '8px' }}>{s.title}</h3>
                  <p style={{ color: 'var(--text2)', fontSize: '14px', lineHeight: 1.5 }}>{s.desc}</p>
                </div>
              ))}
            </div>
          </div>
          {/* Social Proof Section */}
          <div style={{ marginTop: '80px', width: '100%', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '16px', marginBottom: '40px' }}>
              <div style={{ display: 'flex', position: 'relative' }}>
                {[1, 2, 3, 4, 5].map((i) => (
                  <div key={i} style={{ 
                    width: '32px', height: '32px', borderRadius: '50%', background: 'var(--surface2)', 
                    border: '2px solid var(--bg)', marginLeft: i > 1 ? '-12px' : '0', zIndex: 6 - i,
                    display: 'flex', alignItems: 'center', justifyContent: 'center'
                  }}>
                    <User size={16} color="var(--text2)" />
                  </div>
                ))}
              </div>
              <div style={{ color: 'var(--text)', fontWeight: 'bold' }}>
                Join <span style={{ color: 'var(--accent)' }}>500+</span> students learning to code
              </div>
            </div>

            <div className="testimonials-scroll">
              {[
                { name: 'Emeka U.', role: 'Frontend Developer', text: '"The interactive React workspace helped me land my first tech job in Lagos. Way better than just watching videos!"' },
                { name: 'Sarah O.', role: 'Data Analyst', text: '"The AI tutor is incredible. It explains Python concepts perfectly when I get stuck on the data science track."' },
                { name: 'David I.', role: 'Student', text: '"Earning certificates as I complete courses keeps me motivated. The platform is super easy to use on my phone too."' }
              ].map((t, i) => (
                <div key={i} style={{ background: 'var(--surface)', padding: '24px', borderRadius: '16px', border: '1px solid var(--border)', textAlign: 'left' }}>
                  <div style={{ color: 'var(--accent3)', marginBottom: '12px', display: 'flex', gap: '4px' }}>
                    {[1,2,3,4,5].map(star => <Star key={star} size={16} fill="currentColor" />)}
                  </div>
                  <p style={{ color: 'var(--text)', fontStyle: 'italic', marginBottom: '20px', lineHeight: 1.6 }}>{t.text}</p>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                    <div style={{ width: '40px', height: '40px', borderRadius: '50%', background: 'var(--surface2)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                      <User size={20} color="var(--text2)" />
                    </div>
                    <div>
                      <div style={{ fontWeight: 'bold', color: 'var(--text)' }}>{t.name}</div>
                      <div style={{ fontSize: '12px', color: 'var(--text2)' }}>{t.role}</div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
            
            <div ref={statsRef} style={{ display: 'flex', gap: '24px', marginTop: '60px', flexWrap: 'wrap', justifyContent: 'center' }}>
               {[
                 { value: '500+', label: 'Active Students', color: 'var(--accent)' },
                 { value: '1,200+', label: 'Lessons Completed', color: 'var(--accent2)' },
                 { value: '24/7', label: 'AI Tutoring', color: 'var(--accent3)' },
               ].map((stat, i) => (
                 <div
                   key={i}
                   className={statsVisible ? 'stat-count-animate' : ''}
                   style={{
                     background: 'var(--surface2)', padding: '20px 40px', borderRadius: '16px',
                     border: '1px solid var(--border)', display: 'flex', flexDirection: 'column',
                     alignItems: 'center', animationDelay: `${i * 0.12}s`,
                     transition: 'border-color 0.3s', cursor: 'default'
                   }}
                   onMouseEnter={e => e.currentTarget.style.borderColor = stat.color}
                   onMouseLeave={e => e.currentTarget.style.borderColor = 'var(--border)'}
                 >
                   <div style={{ fontSize: '36px', fontWeight: 'bold', color: stat.color, fontFamily: 'var(--font-mono)' }}>
                     {stat.value}
                   </div>
                   <div style={{ color: 'var(--text2)', fontSize: '14px', textTransform: 'uppercase', letterSpacing: '1px', marginTop: '4px' }}>
                     {stat.label}
                   </div>
                 </div>
               ))}
            </div>

            <div style={{ display: 'flex', gap: '24px', marginTop: '40px', opacity: 0.6, flexWrap: 'wrap', justifyContent: 'center' }}>
               <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontWeight: 'bold' }}>Powered by Google Gemini</div>
               <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontWeight: 'bold' }}>Deployed on Azure</div>
               <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontWeight: 'bold' }}>Made in Nigeria</div>
            </div>
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
                width: '140px', height: '140px', borderRadius: '50%', 
                flexShrink: 0, overflow: 'hidden',
                boxShadow: '0 0 0 4px var(--accent), 0 10px 40px rgba(0,229,160,0.35)'
              }}>
                <img
                  src={mabelFounderImg}
                  alt="Arua Mabel Chinasa – Founder of Digital Era"
                  style={{ width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center top' }}
                />
              </div>
              <div>
                <h3 style={{ fontFamily: 'var(--font-display)', fontSize: '28px', fontWeight: 700, marginBottom: '8px' }}>Meet the Founder</h3>
                <p style={{ color: 'var(--accent)', fontSize: '18px', fontWeight: 700, marginBottom: '16px' }}>Arua Mabel Chinasa</p>
                <p style={{ color: 'var(--text2)', fontSize: '15px', lineHeight: 1.6 }}>
                  Arua Mabel Chinasa founded Digital Era to empower the next generation of builders. With a passion for AI, data science, and modern web technologies, she designed this curriculum to provide the ultimate interactive learning experience. Her vision is to make elite tech education accessible, practical, and highly engaging for everyone.
                </p>
                <div style={{ display: 'flex', gap: '12px', marginTop: '20px', flexWrap: 'wrap' }}>
                  <a
                    href="https://www.linkedin.com/in/adanna-mabel-8310b725b"
                    target="_blank" rel="noopener noreferrer"
                    style={{
                      display: 'inline-flex', alignItems: 'center', gap: '8px',
                      padding: '8px 18px', borderRadius: '100px',
                      background: 'linear-gradient(135deg, #0077b5, #00a0dc)',
                      color: '#fff', fontSize: '13px', fontWeight: 600,
                      textDecoration: 'none', transition: 'opacity 0.2s'
                    }}
                    onMouseEnter={e => e.currentTarget.style.opacity = '0.85'}
                    onMouseLeave={e => e.currentTarget.style.opacity = '1'}
                  >
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                    LinkedIn
                  </a>
                  <a
                    href="https://wa.me/2347037197261"
                    target="_blank" rel="noopener noreferrer"
                    style={{
                      display: 'inline-flex', alignItems: 'center', gap: '8px',
                      padding: '8px 18px', borderRadius: '100px',
                      background: 'linear-gradient(135deg, #25D366, #128C7E)',
                      color: '#fff', fontSize: '13px', fontWeight: 600,
                      textDecoration: 'none', transition: 'opacity 0.2s'
                    }}
                    onMouseEnter={e => e.currentTarget.style.opacity = '0.85'}
                    onMouseLeave={e => e.currentTarget.style.opacity = '1'}
                  >
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                    WhatsApp
                  </a>
                </div>
              </div>
            </div>
          </div>

        </div>

        {/* ── Contact Section ── */}
        <div id="contact" style={{
          width: '100%', maxWidth: '1200px', padding: '0 32px',
          marginTop: '80px', marginBottom: '20px'
        }}>
          <div style={{ textAlign: 'center', marginBottom: '48px' }}>
            <h2 style={{ fontFamily: 'var(--font-display)', fontSize: '36px', fontWeight: 800 }}>
              Contact <span style={{ color: 'var(--accent)' }}>Digital Era</span>
            </h2>
            <p style={{ color: 'var(--text2)', fontSize: '16px', marginTop: '12px' }}>
              Reach out to enroll, ask questions, or visit our training centre in Ikorodu, Lagos.
            </p>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '32px' }}>

            {/* Info cards */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>

              {/* Phone */}
              <a href="tel:+2347037197261" style={{ textDecoration: 'none' }}>
                <div style={{
                  display: 'flex', alignItems: 'center', gap: '16px',
                  background: 'var(--surface)', border: '1px solid var(--border)',
                  borderRadius: '16px', padding: '20px 24px',
                  transition: 'border-color 0.2s, transform 0.2s',
                  cursor: 'pointer'
                }}
                  onMouseEnter={e => { e.currentTarget.style.borderColor = 'var(--accent)'; e.currentTarget.style.transform = 'translateY(-2px)'; }}
                  onMouseLeave={e => { e.currentTarget.style.borderColor = 'var(--border)'; e.currentTarget.style.transform = 'none'; }}
                >
                  <div style={{ width: '48px', height: '48px', borderRadius: '12px', background: 'rgba(0,229,160,0.1)', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81a19.79 19.79 0 01-3.07-8.63A2 2 0 012 1h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 8.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>
                  </div>
                  <div>
                    <div style={{ fontSize: '12px', color: 'var(--text2)', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '4px' }}>Phone</div>
                    <div style={{ color: 'var(--text)', fontWeight: 600, fontSize: '15px' }}>+234 703 719 7261</div>
                  </div>
                </div>
              </a>

              {/* Email */}
              <a href="mailto:nasaadanna@gmail.com" style={{ textDecoration: 'none' }}>
                <div style={{
                  display: 'flex', alignItems: 'center', gap: '16px',
                  background: 'var(--surface)', border: '1px solid var(--border)',
                  borderRadius: '16px', padding: '20px 24px',
                  transition: 'border-color 0.2s, transform 0.2s', cursor: 'pointer'
                }}
                  onMouseEnter={e => { e.currentTarget.style.borderColor = 'var(--accent)'; e.currentTarget.style.transform = 'translateY(-2px)'; }}
                  onMouseLeave={e => { e.currentTarget.style.borderColor = 'var(--border)'; e.currentTarget.style.transform = 'none'; }}
                >
                  <div style={{ width: '48px', height: '48px', borderRadius: '12px', background: 'rgba(0,229,160,0.1)', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                  </div>
                  <div>
                    <div style={{ fontSize: '12px', color: 'var(--text2)', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '4px' }}>Email</div>
                    <div style={{ color: 'var(--text)', fontWeight: 600, fontSize: '15px' }}>nasaadanna@gmail.com</div>
                  </div>
                </div>
              </a>

              {/* WhatsApp */}
              <a href="https://wa.me/2347037197261" target="_blank" rel="noopener noreferrer" style={{ textDecoration: 'none' }}>
                <div style={{
                  display: 'flex', alignItems: 'center', gap: '16px',
                  background: 'var(--surface)', border: '1px solid var(--border)',
                  borderRadius: '16px', padding: '20px 24px',
                  transition: 'border-color 0.2s, transform 0.2s', cursor: 'pointer'
                }}
                  onMouseEnter={e => { e.currentTarget.style.borderColor = '#25D366'; e.currentTarget.style.transform = 'translateY(-2px)'; }}
                  onMouseLeave={e => { e.currentTarget.style.borderColor = 'var(--border)'; e.currentTarget.style.transform = 'none'; }}
                >
                  <div style={{ width: '48px', height: '48px', borderRadius: '12px', background: 'rgba(37,211,102,0.1)', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="#25D366"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                  </div>
                  <div>
                    <div style={{ fontSize: '12px', color: 'var(--text2)', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '4px' }}>WhatsApp</div>
                    <div style={{ color: 'var(--text)', fontWeight: 600, fontSize: '15px' }}>+234 703 719 7261</div>
                  </div>
                </div>
              </a>

              {/* Address */}
              <a
                href="https://www.google.com/maps/search/Abule+Onimalu+road+Selewu+Igbogbo+Ikorodu+Lagos"
                target="_blank" rel="noopener noreferrer" style={{ textDecoration: 'none' }}
              >
                <div style={{
                  display: 'flex', alignItems: 'center', gap: '16px',
                  background: 'var(--surface)', border: '1px solid var(--border)',
                  borderRadius: '16px', padding: '20px 24px',
                  transition: 'border-color 0.2s, transform 0.2s', cursor: 'pointer'
                }}
                  onMouseEnter={e => { e.currentTarget.style.borderColor = 'var(--accent)'; e.currentTarget.style.transform = 'translateY(-2px)'; }}
                  onMouseLeave={e => { e.currentTarget.style.borderColor = 'var(--border)'; e.currentTarget.style.transform = 'none'; }}
                >
                  <div style={{ width: '48px', height: '48px', borderRadius: '12px', background: 'rgba(0,229,160,0.1)', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
                  </div>
                  <div>
                    <div style={{ fontSize: '12px', color: 'var(--text2)', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '4px' }}>Training Centre</div>
                    <div style={{ color: 'var(--text)', fontWeight: 600, fontSize: '14px', lineHeight: 1.4 }}>Abule, Onimalu Road Selewu,<br/>Igbogbo Ikorodu, Lagos State</div>
                  </div>
                </div>
              </a>

              {/* LinkedIn */}
              <a href="https://www.linkedin.com/in/adanna-mabel-8310b725b" target="_blank" rel="noopener noreferrer" style={{ textDecoration: 'none' }}>
                <div style={{
                  display: 'flex', alignItems: 'center', gap: '16px',
                  background: 'var(--surface)', border: '1px solid var(--border)',
                  borderRadius: '16px', padding: '20px 24px',
                  transition: 'border-color 0.2s, transform 0.2s', cursor: 'pointer'
                }}
                  onMouseEnter={e => { e.currentTarget.style.borderColor = '#0077b5'; e.currentTarget.style.transform = 'translateY(-2px)'; }}
                  onMouseLeave={e => { e.currentTarget.style.borderColor = 'var(--border)'; e.currentTarget.style.transform = 'none'; }}
                >
                  <div style={{ width: '48px', height: '48px', borderRadius: '12px', background: 'rgba(0,119,181,0.12)', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="#0077b5"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                  </div>
                  <div>
                    <div style={{ fontSize: '12px', color: 'var(--text2)', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '4px' }}>LinkedIn</div>
                    <div style={{ color: 'var(--text)', fontWeight: 600, fontSize: '14px' }}>Adanna Mabel</div>
                  </div>
                </div>
              </a>
            </div>

            {/* Contact Form */}
            <div style={{
              background: 'var(--surface)', border: '1px solid var(--border)',
              borderRadius: '20px', padding: '32px',
            }}>
              <h3 style={{ fontFamily: 'var(--font-display)', fontSize: '20px', fontWeight: 700, marginBottom: '24px' }}>Send a Message</h3>
              <form
                id="contact-form"
                onSubmit={e => {
                  e.preventDefault();
                  const d = new FormData(e.target);
                  const wa = `https://wa.me/2347037197261?text=${encodeURIComponent(`Hi Mabel! My name is ${d.get('name')}. ${d.get('message')} — ${d.get('email')}`)}` ;
                  window.open(wa, '_blank');
                }}
                style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}
              >
                <div>
                  <label style={{ fontSize: '13px', color: 'var(--text2)', marginBottom: '6px', display: 'block' }}>Your Name</label>
                  <input
                    name="name" required
                    placeholder="e.g. John Okafor"
                    style={{
                      width: '100%', padding: '12px 16px', borderRadius: '10px',
                      background: 'var(--bg)', border: '1px solid var(--border)',
                      color: 'var(--text)', fontSize: '14px', outline: 'none', boxSizing: 'border-box'
                    }}
                    onFocus={e => e.target.style.borderColor = 'var(--accent)'}
                    onBlur={e => e.target.style.borderColor = 'var(--border)'}
                  />
                </div>
                <div>
                  <label style={{ fontSize: '13px', color: 'var(--text2)', marginBottom: '6px', display: 'block' }}>Email Address</label>
                  <input
                    name="email" type="email" required
                    placeholder="you@example.com"
                    style={{
                      width: '100%', padding: '12px 16px', borderRadius: '10px',
                      background: 'var(--bg)', border: '1px solid var(--border)',
                      color: 'var(--text)', fontSize: '14px', outline: 'none', boxSizing: 'border-box'
                    }}
                    onFocus={e => e.target.style.borderColor = 'var(--accent)'}
                    onBlur={e => e.target.style.borderColor = 'var(--border)'}
                  />
                </div>
                <div>
                  <label style={{ fontSize: '13px', color: 'var(--text2)', marginBottom: '6px', display: 'block' }}>Message</label>
                  <textarea
                    name="message" required rows={5}
                    placeholder="I'd like to enroll in..."
                    style={{
                      width: '100%', padding: '12px 16px', borderRadius: '10px',
                      background: 'var(--bg)', border: '1px solid var(--border)',
                      color: 'var(--text)', fontSize: '14px', outline: 'none',
                      resize: 'vertical', fontFamily: 'inherit', boxSizing: 'border-box'
                    }}
                    onFocus={e => e.target.style.borderColor = 'var(--accent)'}
                    onBlur={e => e.target.style.borderColor = 'var(--border)'}
                  />
                </div>
                <button
                  type="submit"
                  className="btn-primary"
                  style={{ padding: '14px', borderRadius: '12px', fontSize: '15px', fontWeight: 700, width: '100%' }}
                >
                  Send via WhatsApp
                </button>
                <p style={{ fontSize: '12px', color: 'var(--text2)', textAlign: 'center', marginTop: '-4px' }}>
                  Your message will open in WhatsApp for a quick reply.
                </p>
              </form>
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
              onClick={() => navigate('/catalog')}
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
        <p style={{ color: 'var(--text2)', fontSize: '14px', marginTop: '30px' }}>
          &copy; {new Date().getFullYear()} Digital Era. All rights reserved.
        </p>
      </footer>
      
      <CustomerSupportChat />
    </div>
  );
};

export default LandingPage;
