import React from 'react';
import { useNavigate } from 'react-router-dom';
import PublicNavbar from './PublicNavbar';
import { curriculum } from '../data/courses';
import { Code2, BarChart2, Bot, Palette, Terminal, GraduationCap } from 'lucide-react';

const CourseCatalog = () => {
  const navigate = useNavigate();
  const [searchTerm, setSearchTerm] = React.useState('');
  const [filterLevel, setFilterLevel] = React.useState('All');

  const filteredCurriculum = Object.entries(curriculum).filter(([categoryName, levels]) => {
    const matchesSearch = categoryName.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesLevel = filterLevel === 'All' || Object.keys(levels).includes(filterLevel);
    return matchesSearch && matchesLevel;
  });

  return (
    <div style={{ backgroundColor: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column', overflowX: 'hidden' }}>
      <PublicNavbar />
      
      <main style={{ flex: 1, padding: '60px 32px', maxWidth: '1400px', margin: '0 auto', width: '100%' }}>
        <div style={{ textAlign: 'center', marginBottom: '40px' }}>
          <h1 style={{ fontFamily: 'var(--font-display)', fontSize: '48px', fontWeight: 800, marginBottom: '16px' }}>
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
              background: 'var(--bg)', color: 'var(--text)', width: '100%', maxWidth: '300px'
            }}
          />
          <div style={{ display: 'flex', gap: '8px', overflowX: 'auto', paddingBottom: '4px' }}>
            {['All', 'Beginner', 'Intermediate', 'Advanced'].map(level => (
              <button 
                key={level}
                onClick={() => setFilterLevel(level)}
                style={{ 
                  padding: '8px 20px', borderRadius: '100px', cursor: 'pointer',
                  border: filterLevel === level ? '1px solid var(--accent)' : '1px solid var(--border)',
                  background: filterLevel === level ? 'rgba(0, 229, 160, 0.1)' : 'var(--bg)',
                  color: filterLevel === level ? 'var(--accent)' : 'var(--text)',
                  fontWeight: filterLevel === level ? 'bold' : 'normal',
                  whiteSpace: 'nowrap'
                }}
              >
                {level}
              </button>
            ))}
          </div>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))', gap: '24px' }}>
          {filteredCurriculum.length === 0 ? (
            <div style={{ gridColumn: '1 / -1', textAlign: 'center', padding: '60px 0', color: 'var(--text2)' }}>
              <h3>No courses found matching your criteria.</h3>
              <button onClick={() => { setSearchTerm(''); setFilterLevel('All'); }} style={{ marginTop: '16px', padding: '8px 16px', background: 'var(--surface2)', border: 'none', color: 'var(--text)', borderRadius: '8px', cursor: 'pointer' }}>Clear Filters</button>
            </div>
          ) : filteredCurriculum.map(([categoryName, levels], idx) => {
            // Count total lessons
            const totalLessons = Object.values(levels).flat().length;

            return (
              <div 
                key={idx} 
                className="track-card"
                onClick={() => navigate('/onboarding')}
                style={{ display: 'flex', flexDirection: 'column' }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '16px' }}>
                  <div className="track-card-icon" style={{ fontSize: '36px', margin: 0 }}>
                    <div style={{ fontSize: '32px', marginBottom: '16px', color: 'var(--accent)' }}>
                      {categoryName.includes('Python') ? <Code2 size={32} /> : 
                       categoryName.includes('Data') ? <BarChart2 size={32} /> : 
                       categoryName.includes('AI') ? <Bot size={32} /> : 
                       categoryName.includes('Frontend') ? <Palette size={32} /> : <Terminal size={32} />}
                    </div>
                  </div>
                  <div style={{ 
                    background: 'var(--surface2)', padding: '4px 10px', 
                    borderRadius: '100px', fontSize: '11px', fontWeight: 600, color: 'var(--text2)' 
                  }}>
                    {totalLessons} Lessons
                  </div>
                </div>
                
                <h3 className="track-card-name" style={{ fontSize: '20px', marginBottom: '8px' }}>{categoryName}</h3>
                
                <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', marginTop: 'auto', paddingTop: '16px' }}>
                  {levels['Beginner'] && <span className="track-tag tag-beginner">Beginner</span>}
                  {levels['Intermediate'] && <span className="track-tag tag-intermediate">Intermediate</span>}
                  {levels['Advanced'] && <span className="track-tag tag-advanced">Advanced</span>}
                </div>
                
                <div style={{ 
                  marginTop: '20px', borderTop: '1px solid var(--border)', paddingTop: '16px',
                  display: 'flex', justifyContent: 'space-between', alignItems: 'center'
                }}>
                  <span style={{ fontSize: '13px', color: 'var(--text3)', fontWeight: 600 }}>Included in Pro</span>
                  <span style={{ 
                    color: 'var(--accent)', fontSize: '13px', fontWeight: 700, 
                    display: 'flex', alignItems: 'center', gap: '4px' 
                  }}>
                    Start Learning →
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
        background: 'var(--surface)'
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
