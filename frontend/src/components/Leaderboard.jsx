import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Medal, Trophy, Home, ArrowLeft, Flame, User as UserIcon } from 'lucide-react';

export default function Leaderboard({ isPublic = false }) {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();
  
  const token = localStorage.getItem('token');

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        const response = await fetch('/leaderboard');
        if (!response.ok) throw new Error('Failed to fetch leaderboard');
        const data = await response.json();
        setUsers(data);
      } catch (error) {
        console.error("Error fetching leaderboard:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchLeaderboard();
  }, []);

  const getRankStyle = (index) => {
    if (index === 0) return { borderColor: '#eab308', boxShadow: '0 0 20px rgba(234,179,8,0.15)' };
    if (index === 1) return { borderColor: '#9ca3af', boxShadow: '0 0 20px rgba(156,163,175,0.15)' };
    if (index === 2) return { borderColor: '#d97706', boxShadow: '0 0 20px rgba(217,119,6,0.15)' };
    return {};
  };

  const getRankBadge = (index) => {
    if (index === 0) return <Medal size={20} color="#fbbf24" />;
    if (index === 1) return <Medal size={20} color="#9ca3af" />;
    if (index === 2) return <Medal size={20} color="#b45309" />;
    return <span style={{ color: 'var(--text-dim)', fontWeight: 600 }}>#{index + 1}</span>;
  };

  const podiumStyles = {
    container: {
      display: 'flex', justifyContent: 'center', alignItems: 'flex-end',
      gap: '24px', marginBottom: '48px', padding: '0 16px'
    },
    podiumItem: (height, color) => ({
      display: 'flex', flexDirection: 'column', alignItems: 'center', width: '200px'
    }),
    podiumBar: (height, color) => ({
      width: '100%', height: `${height}px`,
      background: `linear-gradient(to top, ${color}33, ${color}11)`,
      borderRadius: '16px 16px 0 0',
      borderTop: `4px solid ${color}`,
      display: 'flex', justifyContent: 'center', paddingTop: '16px',
      backdropFilter: 'blur(8px)',
    }),
    name: (color) => ({
      fontFamily: 'var(--font-display)', fontWeight: 700, fontSize: '16px',
      color: color, marginBottom: '4px', textAlign: 'center'
    }),
    xp: { color: 'var(--accent2)', fontWeight: 600, fontSize: '14px', marginBottom: '12px' }
  };

  return (
    <div style={{ minHeight: '100vh', background: 'var(--bg)', color: 'var(--text)', overflow: 'hidden', position: 'relative' }}>
      {/* Background glow */}
      <div style={{ position: 'absolute', top: '-10%', left: '-10%', width: '40%', height: '40%', borderRadius: '50%', background: 'rgba(0,229,160,0.05)', filter: 'blur(120px)', pointerEvents: 'none' }} />
      <div style={{ position: 'absolute', bottom: '-10%', right: '-10%', width: '40%', height: '40%', borderRadius: '50%', background: 'rgba(59,130,246,0.05)', filter: 'blur(120px)', pointerEvents: 'none' }} />

      <div style={{ maxWidth: '900px', margin: '0 auto', padding: '48px 16px', position: 'relative', zIndex: 1 }}>
        
        <div style={{ display: 'flex', alignItems: 'center', gap: '16px', marginBottom: '48px' }}>
          <button 
             onClick={() => navigate(token && !isPublic ? '/dashboard' : '/')}
             style={{ padding: '8px 12px', background: 'var(--surface)', borderRadius: '8px', border: '1px solid var(--border)', cursor: 'pointer', color: 'var(--text2)', fontSize: '16px', display: 'flex', alignItems: 'center', gap: '6px', transition: 'all 0.2s' }}
             title="Go Back"
          >
             {token && !isPublic ? <Home size={18} /> : <ArrowLeft size={18} />} {token && !isPublic ? 'Dashboard' : 'Home'}
          </button>
          <div>
            <h1 style={{ fontFamily: 'var(--font-display)', fontSize: '36px', fontWeight: 800, background: 'linear-gradient(90deg, var(--accent), var(--accent2))', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent', marginBottom: '4px' }}>
              Global Leaderboard
            </h1>
            <p style={{ color: 'var(--text2)', fontSize: '15px' }}>Top 100 students ranked by total XP.</p>
          </div>
        </div>

        {loading ? (
          <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '250px' }}>
            <div style={{ width: '48px', height: '48px', border: '4px solid var(--border)', borderTopColor: 'var(--accent)', borderRadius: '50%', animation: 'spin 1s linear infinite' }} />
            <style>{`@keyframes spin { to { transform: rotate(360deg); } }`}</style>
          </div>
        ) : (
          <>
            {/* Top 3 Podium */}
            {users.length >= 3 && (
              <div style={podiumStyles.container}>
                {/* 2nd place */}
                <div style={podiumStyles.podiumItem(160, '#9ca3af')}>
                  <div style={podiumStyles.name('#9ca3af')}>{users[1].full_name || users[1].email?.split('@')[0] || 'User'}</div>
                  <div style={podiumStyles.xp}>{users[1].xp} XP</div>
                  <div style={podiumStyles.podiumBar(160, '#9ca3af')}>
                    <span style={{ fontSize: '24px' }}><Medal size={24} color="#9ca3af" /></span>
                  </div>
                </div>

                {/* 1st place */}
                <div style={podiumStyles.podiumItem(224, '#eab308')}>
                  <div style={{ fontSize: '32px', marginBottom: '8px', animation: 'pulse 2s infinite' }}><Trophy size={40} color="#eab308" /></div>
                  <div style={{ ...podiumStyles.name('#eab308'), fontSize: '20px' }}>{users[0].full_name || users[0].email?.split('@')[0] || 'User'}</div>
                  <div style={podiumStyles.xp}>{users[0].xp} XP</div>
                  <div style={podiumStyles.podiumBar(224, '#eab308')}>
                    <span style={{ fontSize: '36px', fontWeight: 900, color: 'white', opacity: 0.8 }}>1</span>
                  </div>
                </div>

                {/* 3rd place */}
                <div style={podiumStyles.podiumItem(128, '#d97706')}>
                  <div style={podiumStyles.name('#d97706')}>{users[2].full_name || users[2].email?.split('@')[0] || 'User'}</div>
                  <div style={podiumStyles.xp}>{users[2].xp} XP</div>
                  <div style={podiumStyles.podiumBar(128, '#d97706')}>
                    <span style={{ fontSize: '24px' }}><Medal size={24} color="#d97706" /></span>
                  </div>
                </div>
              </div>
            )}

            {/* Full List */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              {users.map((user, index) => (
                <div 
                  key={user.id}
                  style={{
                    display: 'flex', alignItems: 'center', justifyContent: 'space-between',
                    padding: '16px 20px', borderRadius: '12px',
                    border: '1px solid var(--border)',
                    background: index < 3 ? 'var(--surface2)' : 'var(--surface)',
                    transition: 'all 0.2s',
                    cursor: 'default',
                    ...getRankStyle(index)
                  }}
                  onMouseOver={e => { e.currentTarget.style.transform = 'translateX(4px)'; }}
                  onMouseOut={e => { e.currentTarget.style.transform = 'translateX(0)'; }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
                    <div style={{ width: '48px', textAlign: 'center', fontSize: index < 3 ? '24px' : '14px', fontWeight: 700, color: 'var(--text2)', fontFamily: 'var(--font-mono)' }}>
                      {getRankBadge(index)}
                    </div>
                    
                    <div style={{ width: '40px', height: '40px', borderRadius: '50%', background: 'var(--surface3)', display: 'flex', alignItems: 'center', justifyContent: 'center', border: '1px solid var(--border)', flexShrink: 0 }}>
                      <span style={{ fontWeight: 700, fontSize: '16px', color: 'var(--accent)' }}>
                        <UserIcon size={20} />
                      </span>
                    </div>

                    <div>
                      <div style={{ fontWeight: 700, fontSize: '15px', color: 'var(--text)' }}>
                        {user.full_name || user.email?.split('@')[0] || 'User'}
                      </div>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginTop: '4px' }}>
                        <span style={{ fontSize: '12px', color: 'var(--text3)', fontWeight: 600, padding: '2px 8px', background: 'var(--surface3)', borderRadius: '4px' }}>
                          {user.level || 'Novice'}
                        </span>
                        {user.streak > 0 && (
                          <div style={{ display: 'flex', alignItems: 'center', gap: '4px', fontSize: '12px', color: 'var(--accent3)', fontWeight: 600 }}>
                            <Flame size={14} color="var(--accent3)" /> {user.streak} day streak
                          </div>
                        )}
                      </div>
                    </div>
                  </div>

                  <div style={{ display: 'flex', alignItems: 'center', gap: '6px', padding: '8px 16px', background: 'var(--surface3)', borderRadius: '8px', border: '1px solid var(--border)' }}>
                    <span style={{ color: 'var(--accent)', fontSize: '14px' }}>⭐</span>
                    <span style={{ fontSize: '18px', fontWeight: 900, color: 'var(--text)', fontFamily: 'var(--font-mono)', letterSpacing: '-0.5px' }}>{user.xp.toLocaleString()}</span>
                    <span style={{ fontSize: '12px', color: 'var(--accent2)', fontWeight: 700, marginLeft: '2px' }}>XP</span>
                  </div>
                </div>
              ))}
            </div>
          </>
        )}
      </div>
    </div>
  );
}
