import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';
import PublicNavbar from './PublicNavbar';
import { useCurriculum } from '../hooks/useCurriculum';
import { Code2, BarChart2, Bot, Palette, Terminal, GraduationCap, Star, Clock, BookOpen } from 'lucide-react';
import { Helmet } from 'react-helmet-async';

const TRACK_ICONS = {
  Python:   <Code2 size={32} />,
  Data:     <BarChart2 size={32} />,
  AI:       <Bot size={32} />,
  Frontend: <Palette size={32} />,
};

const getIcon = (name) => {
  for (const [key, icon] of Object.entries(TRACK_ICONS)) {
    if (name.includes(key)) return icon;
  }
  return <Terminal size={32} />;
};

const CourseCatalog = () => {
  const navigate = useNavigate();
  const { token } = useAuth();
  const [searchTerm, setSearchTerm] = React.useState('');
  const [filterLevel, setFilterLevel] = React.useState('All');
  
  const { data, isLoading, error } = useCurriculum();
  const curriculum = data?.curriculum || {};

  const filteredCurriculum = Object.entries(curriculum).filter(([categoryName, levels]) => {
    const matchesSearch = categoryName.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesLevel = filterLevel === 'All' || Object.keys(levels).includes(filterLevel);
    return matchesSearch && matchesLevel;
  });

  const handleCardClick = () => {
    // Smart navigation: logged-in users go to dashboard, guests to onboarding
    navigate(token ? '/dashboard' : '/onboarding');
  };

  return (
    <div style={{ backgroundColor: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column', overflowX: 'hidden' }}>
      <Helmet>
        <title>Course Catalog | Digital Era Academy \u2014 Python, AI, Data Science &amp; Frontend</title>
        <meta name="description" content="Browse 10+ expert-designed learning tracks at Digital Era. Master Python, Data Science, AI Engineering, Frontend, Backend development with hands-on interactive projects and a built-in AI tutor." />
        <meta name="keywords" content="python course Nigeria, data science course Lagos, AI course Africa, frontend course online, learn to code Nigeria, digital era courses, coding curriculum Lagos" />
        <link rel="canonical" href="https://digital-era.live/catalog" />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="https://digital-era.live/catalog" />
        <meta property="og:title" content="Course Catalog | Digital Era Academy" />
        <meta property="og:description" content="10+ learning tracks. Python, AI, Data Science, Frontend & Backend — all with interactive projects and AI tutoring." />
        <meta property="og:image" content="https://digital-era.live/og-image.png" />
        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "ItemList",
          "name": "Digital Era Course Catalog",
          "description": "Comprehensive tech learning tracks from Digital Era Academy",
          "url": "https://digital-era.live/catalog",
          "itemListElement": [
            { "@type": "Course", "position": 1, "name": "Python Core", "provider": { "@type": "Organization", "name": "Digital Era" } },
            { "@type": "Course", "position": 2, "name": "Data Science", "provider": { "@type": "Organization", "name": "Digital Era" } },
            { "@type": "Course", "position": 3, "name": "AI Engineering", "provider": { "@type": "Organization", "name": "Digital Era" } },
            { "@type": "Course", "position": 4, "name": "Frontend Development", "provider": { "@type": "Organization", "name": "Digital Era" } },
            { "@type": "Course", "position": 5, "name": "Backend Engineering", "provider": { "@type": "Organization", "name": "Digital Era" } }
          ]
        })}</script>
      </Helmet>
      <PublicNavbar />
      
      <main style={{ flex: 1, padding: '60px 32px', maxWidth: '1400px', margin: '0 auto', width: '100%' }}>
        <div style={{ textAlign: 'center', marginBottom: '40px' }}>
          <div style={{
            display: 'inline-flex', alignItems: 'center', gap: '8px',
            padding: '6px 16px', background: 'var(--surface)', border: '1px solid var(--border)',
            borderRadius: '100px', marginBottom: '24px'
          }}>
            <BookOpen size={14} color="var(--accent)" />
            <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--accent)' }}>
              {Object.keys(curriculum).length || '10'}+ Learning Tracks
            </span>
          </div>
          <h1 style={{ fontFamily: 'var(--font-display)', fontSize: 'clamp(32px, 5vw, 48px)', fontWeight: 800, marginBottom: '16px' }}>
            Course <span style={{ color: 'var(--accent)' }}>Catalog</span>
          </h1>
          <p style={{ color: 'var(--text2)', fontSize: '16px', maxWidth: '600px', margin: '0 auto', lineHeight: 1.6 }}>
            Browse our comprehensive curriculum. From beginner basics to advanced AI orchestration, build your skills with interactive, real-world projects.
          </p>
        </div>

        {/* Search & Filter Bar */}
        <div style={{ 
          display: 'flex', flexWrap: 'wrap', gap: '16px', justifyContent: 'center', 
          marginBottom: '40px', background: 'var(--surface)', padding: '20px', 
          borderRadius: '16px', border: '1px solid var(--border)' 
        }}>
          <input 
            type="text" 
            placeholder="Search tracks..." 
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            style={{ 
              padding: '12px 20px', borderRadius: '100px', border: '1px solid var(--border)', 
              background: 'var(--bg)', color: 'var(--text)', width: '100%', maxWidth: '300px',
              fontSize: '14px', outline: 'none', transition: 'border-color 0.2s'
            }}
            onFocus={e => e.target.style.borderColor = 'var(--accent)'}
            onBlur={e => e.target.style.borderColor = 'var(--border)'}
          />
          <div style={{ display: 'flex', gap: '8px', overflowX: 'auto', paddingBottom: '4px' }}>
            {['All', 'Beginner', 'Intermediate', 'Advanced'].map(level => (
              <button 
                key={level}
                onClick={() => setFilterLevel(level)}
                style={{ 
                  padding: '10px 20px', borderRadius: '100px', cursor: 'pointer',
                  border: filterLevel === level ? '1px solid var(--accent)' : '1px solid var(--border)',
                  background: filterLevel === level ? 'rgba(0, 229, 160, 0.1)' : 'var(--bg)',
                  color: filterLevel === level ? 'var(--accent)' : 'var(--text)',
                  fontWeight: filterLevel === level ? 'bold' : 'normal',
                  whiteSpace: 'nowrap', minHeight: '44px',
                  transition: 'all 0.2s'
                }}
              >
                {level}
              </button>
            ))}
          </div>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))', gap: '24px' }}>
          {isLoading ? (
            Array(6).fill(0).map((_, i) => (
              <div key={i} style={{ 
                background: 'var(--surface)', borderRadius: '16px', padding: '24px', 
                height: '240px', border: '1px solid var(--border)',
                animation: 'pulse 1.5s infinite', display: 'flex', flexDirection: 'column'
              }}>
                <div style={{ background: 'var(--surface2)', height: '48px', width: '48px', borderRadius: '12px', marginBottom: '16px' }}></div>
                <div style={{ background: 'var(--surface2)', height: '24px', width: '70%', borderRadius: '4px', marginBottom: '16px' }}></div>
                <div style={{ background: 'var(--surface2)', height: '16px', width: '40%', borderRadius: '4px', marginTop: 'auto' }}></div>
              </div>
            ))
          ) : filteredCurriculum.length === 0 ? (
            <div style={{ gridColumn: '1 / -1', textAlign: 'center', padding: '80px 0', color: 'var(--text2)' }}>
              <div style={{ fontSize: '48px', marginBottom: '16px' }}>🔍</div>
              <h3 style={{ fontFamily: 'var(--font-display)', fontSize: '20px', marginBottom: '8px', color: 'var(--text)' }}>
                No tracks found
              </h3>
              <p style={{ marginBottom: '20px' }}>
                {searchTerm ? `No results for "${searchTerm}"` : `No ${filterLevel} courses available`} — try adjusting your filters.
              </p>
              <button
                onClick={() => { setSearchTerm(''); setFilterLevel('All'); }}
                style={{
                  padding: '10px 24px', background: 'var(--accent)', color: '#000',
                  border: 'none', borderRadius: '100px', cursor: 'pointer',
                  fontWeight: 'bold', fontSize: '14px'
                }}
              >
                Clear Filters
              </button>
            </div>
          ) : filteredCurriculum.map(([categoryName, levels], idx) => {
            const totalLessons = Object.values(levels).flat().length;
            const delayClass = `card-enter card-enter-${Math.min(idx + 1, 6)}`;

            return (
              <div 
                key={idx} 
                className={`track-card ${delayClass}`}
                onClick={handleCardClick}
                style={{ display: 'flex', flexDirection: 'column' }}
                role="button"
                tabIndex={0}
                onKeyDown={e => e.key === 'Enter' && handleCardClick()}
                aria-label={`${categoryName} — ${totalLessons} lessons. ${token ? 'Go to dashboard' : 'Sign up to start'}`}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '16px' }}>
                  <div style={{ fontSize: '32px', color: 'var(--accent)' }}>
                    {getIcon(categoryName)}
                  </div>
                  <div style={{ 
                    background: 'var(--surface2)', padding: '4px 10px', 
                    borderRadius: '100px', fontSize: '11px', fontWeight: 600, color: 'var(--text2)' 
                  }}>
                    {totalLessons} Lessons
                  </div>
                </div>
                
                <h3 className="track-card-name" style={{ fontSize: '20px', marginBottom: '8px' }}>{categoryName}</h3>
                
                <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', marginTop: 'auto', paddingTop: '16px', marginBottom: '12px' }}>
                  {levels['Beginner'] && <span className="track-tag tag-beginner">Beginner</span>}
                  {levels['Intermediate'] && <span className="track-tag tag-intermediate">Intermediate</span>}
                  {levels['Advanced'] && <span className="track-tag tag-advanced">Advanced</span>}
                </div>
                
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', color: 'var(--text2)', fontSize: '12px', marginBottom: '16px' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                    <Star size={14} color="#f59e0b" fill="#f59e0b" />
                    <span style={{ fontWeight: 'bold', color: 'var(--text)' }}>4.{8 + (idx % 2)}</span>
                    <span>({1200 + (idx * 342)} reviews)</span>
                  </div>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                    <Clock size={14} />
                    <span>~{totalLessons * 2} hours</span>
                  </div>
                </div>

                <div style={{ 
                  borderTop: '1px solid var(--border)', paddingTop: '16px',
                  display: 'flex', justifyContent: 'space-between', alignItems: 'center'
                }}>
                  <span style={{ fontSize: '13px', color: 'var(--text3)', fontWeight: 600 }}>Included in Pro</span>
                  <span style={{ 
                    color: 'var(--accent)', fontSize: '13px', fontWeight: 700, 
                    display: 'flex', alignItems: 'center', gap: '4px' 
                  }}>
                    {token ? 'Open Dashboard →' : 'Start Learning →'}
                  </span>
                </div>
              </div>
            );
          })}
        </div>
      </main>

      <footer style={{ 
        padding: '32px', borderTop: '1px solid var(--border)', 
        display: 'flex', justifyContent: 'space-between', alignItems: 'center',
        background: 'var(--surface)', flexWrap: 'wrap', gap: '12px'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span style={{ display: 'flex', alignItems: 'center', gap: '6px' }}><GraduationCap size={18} /> Digital Era</span>
        </div>
        <p style={{ color: 'var(--text2)', fontSize: '13px' }}>© 2026 Digital Era Academy. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default CourseCatalog;
