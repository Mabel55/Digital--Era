import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';

const Leaderboard = () => {
  const { user } = useAuth();
  const navigate = useNavigate();
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchLeaderboard();
  }, []);

  const fetchLeaderboard = async () => {
    try {
      const res = await fetch('/leaderboard');
      const data = await res.json();
      if (res.ok) {
        setUsers(data);
      }
    } catch (e) {
      console.error(e);
    }
    setLoading(false);
  };

  if (loading) {
    return <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', color: 'white' }}>Loading Leaderboard...</div>;
  }

  return (
    <div className="screen active" style={{ flexDirection: 'column', background: 'var(--bg)', minHeight: '100vh', overflowY: 'auto' }}>
      <nav className="dash-nav">
        <div className="logo-row">
          <div className="logo-icon">🏆</div>
          <div className="logo-text">Global <span>Leaderboard</span></div>
        </div>
        <button onClick={() => navigate('/dashboard')} className="ws-back-btn">← Back to Dashboard</button>
      </nav>
      
      <div className="dash-body" style={{ maxWidth: '900px', margin: '0 auto', width: '100%' }}>
        
        <div className="dash-hero" style={{ padding: '30px 40px', marginBottom: '40px', background: 'linear-gradient(120deg, rgba(37,42,58,0.8), rgba(26,29,39,0.9))' }}>
          <div className="hero-left">
            <h2>Climb the <span>Leagues</span></h2>
            <p>Earn XP by completing courses, running code, and passing AI skill assessments. Can you reach the Gold League?</p>
            <div style={{ display: 'flex', gap: '20px', marginTop: '20px' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}><div className="lb-rank gold" style={{ fontSize: '18px' }}>🥇</div> Gold League (Top 3)</div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}><div className="lb-rank silver" style={{ fontSize: '18px' }}>🥈</div> Silver League</div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}><div className="lb-rank bronze" style={{ fontSize: '18px' }}>🥉</div> Bronze League</div>
            </div>
          </div>
        </div>

        <div className="leaderboard-table" style={{ background: 'var(--surface)', backdropFilter: 'blur(16px)', WebkitBackdropFilter: 'blur(16px)', border: '1px solid var(--border)' }}>
          {users.map((u, index) => {
            let rankClass = '';
            let medal = `#${index + 1}`;
            
            if (index === 0) { rankClass = 'gold'; medal = '🥇'; }
            else if (index === 1) { rankClass = 'silver'; medal = '🥈'; }
            else if (index === 2) { rankClass = 'bronze'; medal = '🥉'; }
            
            const isMe = user?.email === u.email;

            return (
              <div key={u.id} className="lb-row" style={{ backgroundColor: isMe ? 'rgba(0, 229, 160, 0.1)' : 'transparent', borderLeft: isMe ? '4px solid var(--accent)' : '4px solid transparent' }}>
                <div className={`lb-rank ${rankClass}`} style={{ fontSize: index < 3 ? '24px' : '16px' }}>
                  {medal}
                </div>
                <div className="lb-name">
                  {u.full_name.split(' ')[0]} {isMe && <span style={{ color: 'var(--accent)', marginLeft: '8px', fontSize: '12px' }}>(You)</span>}
                </div>
                <div className="lb-xp">{u.xp} XP</div>
                <div className="lb-badge">
                  {u.level === 'Master' ? '👑' : u.level === 'Advanced' ? '🔥' : u.level === 'Intermediate' ? '🚀' : '🌱'}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

export default Leaderboard;
