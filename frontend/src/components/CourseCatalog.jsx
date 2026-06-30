import React from 'react';
import { useNavigate } from 'react-router-dom';
import PublicNavbar from './PublicNavbar';
import { curriculum } from '../data/courses';

const CourseCatalog = () => {
  const navigate = useNavigate();

  return (
    <div style={{ backgroundColor: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column', overflowX: 'hidden' }}>
      <PublicNavbar />
      
      <main style={{ flex: 1, padding: '60px 32px', maxWidth: '1400px', margin: '0 auto', width: '100%' }}>
        <div style={{ textAlign: 'center', marginBottom: '60px' }}>
          <h1 style={{ fontFamily: 'var(--font-display)', fontSize: '48px', fontWeight: 800, marginBottom: '16px' }}>
            Course <span style={{ color: 'var(--accent)' }}>Catalog</span>
          </h1>
          <p style={{ color: 'var(--text2)', fontSize: '16px', maxWidth: '600px', margin: '0 auto', lineHeight: 1.6 }}>
            Browse our comprehensive curriculum. From beginner basics to advanced AI orchestration, build your skills with interactive, real-world projects.
          </p>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))', gap: '24px' }}>
          {Object.entries(curriculum).map(([categoryName, levels], idx) => {
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
                    {/* Just some generic icons based on name */}
                    {categoryName.includes('Python') ? '🐍' : 
                     categoryName.includes('Data') ? '📊' : 
                     categoryName.includes('AI') ? '🤖' : 
                     categoryName.includes('Frontend') ? '🎨' : '💻'}
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
          <span style={{ fontSize: '18px' }}>🎓</span>
          <span style={{ fontFamily: 'var(--font-display)', fontWeight: 700, fontSize: '16px' }}>Digital Era</span>
        </div>
        <p style={{ color: 'var(--text2)', fontSize: '13px' }}>© 2026 Digital Era Academy. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default CourseCatalog;
