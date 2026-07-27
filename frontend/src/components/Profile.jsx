import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';
import { User, Flame, Trophy, Award, Edit3, ArrowLeft, CheckCircle2, TrendingUp, Target, Calendar } from 'lucide-react';
import { AreaChart, Area, XAxis, YAxis, Tooltip, ResponsiveContainer, Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis } from 'recharts';

const mockChartData = [
  { day: 'Mon', xp: 20 },
  { day: 'Tue', xp: 45 },
  { day: 'Wed', xp: 30 },
  { day: 'Thu', xp: 80 },
  { day: 'Fri', xp: 120 },
  { day: 'Sat', xp: 50 },
  { day: 'Sun', xp: 150 },
];

const mockSkillsData = [
  { subject: 'Python', A: 120, fullMark: 150 },
  { subject: 'Data Science', A: 98, fullMark: 150 },
  { subject: 'SQL', A: 86, fullMark: 150 },
  { subject: 'Machine Learning', A: 65, fullMark: 150 },
  { subject: 'Web Dev', A: 85, fullMark: 150 },
  { subject: 'Git', A: 110, fullMark: 150 },
];

const Profile = () => {
  const { user, token, refreshUser } = useAuth();
  const navigate = useNavigate();
  
  const [isEditing, setIsEditing] = useState(false);
  const [fullName, setFullName] = useState(user?.full_name || '');
  const [goal, setGoal] = useState(user?.goal || 'Build Projects');
  const [level, setLevel] = useState(user?.level || 'Beginner');
  const [successMsg, setSuccessMsg] = useState('');
  const [activityData, setActivityData] = useState([]);
  const [completions, setCompletions] = useState([]);

  useEffect(() => {
    const fetchProfileData = async () => {
      try {
        const actRes = await fetch('/users/me/activity?days=30', { headers: { Authorization: `Bearer ${token}` } });
        if (actRes.ok) {
           const data = await actRes.json();
           const formatted = data.map(d => ({
              day: new Date(d.activity_date).toLocaleDateString('en-US', {weekday: 'short'}),
              fullDate: d.activity_date,
              xp: d.xp_earned,
              lessons: d.lessons_completed
           }));
           // Only keep last 7 days for the chart
           setActivityData(formatted.slice(-7));
        }
        
        const compRes = await fetch('/users/me/completions', { headers: { Authorization: `Bearer ${token}` } });
        if (compRes.ok) setCompletions(await compRes.json());
      } catch (e) {
        console.error("Failed to load profile data", e);
      }
    };
    if (token) fetchProfileData();
  }, [token]);

  const handleSave = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch('/users/me', {
        method: 'PUT',
        headers: {
           'Content-Type': 'application/json',
           'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
           full_name: fullName,
           goal: goal,
           preferred_language: 'en'
        })
      });
      if (res.ok) {
        if (refreshUser) await refreshUser();
        setSuccessMsg('Profile updated successfully!');
        setTimeout(() => { setSuccessMsg(''); setIsEditing(false); }, 2000);
      } else {
        alert("Failed to update profile.");
      }
    } catch (e) {
      alert("Error saving profile");
    }
  };

  const getBadges = () => {
    const badges = [];
    if (user?.streak >= 3) badges.push({ name: '3-Day Streak', icon: <Flame size={20} color="var(--accent3)" /> });
    if (user?.streak >= 7) badges.push({ name: '7-Day Streak', icon: <Flame size={20} color="var(--accent3)" /> });
    if (user?.xp >= 100) badges.push({ name: 'Century Club', icon: <Trophy size={20} color="#fbbf24" /> });
    if (user?.progress && Object.keys(user.progress).length > 0) badges.push({ name: 'First Steps', icon: <CheckCircle2 size={20} color="var(--accent)" /> });
    return badges;
  };

  const badges = getBadges();

  return (
    <div style={{ backgroundColor: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column', color: 'var(--text)' }}>
      {/* Top Nav */}
      <nav style={{ padding: '16px 24px', borderBottom: '1px solid var(--border)', display: 'flex', alignItems: 'center' }}>
        <button onClick={() => navigate('/dashboard')} style={{ background: 'transparent', border: 'none', color: 'var(--text2)', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '8px' }}>
          <ArrowLeft size={20} /> Back to Dashboard
        </button>
      </nav>

      <div style={{ maxWidth: '800px', margin: '40px auto', padding: '0 24px', width: '100%', paddingBottom: '80px' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '32px' }}>
          <div>
            <h1 style={{ fontSize: '32px', fontWeight: 800, margin: '0 0 8px 0', fontFamily: 'var(--font-display)' }}>Your Profile</h1>
            <p style={{ color: 'var(--text2)', margin: 0 }}>Manage your personal details and view your progress.</p>
          </div>
          {!isEditing && (
            <button onClick={() => setIsEditing(true)} style={{ padding: '8px 16px', background: 'var(--surface2)', color: 'var(--text)', border: '1px solid var(--border)', borderRadius: '8px', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '8px', fontWeight: 'bold' }}>
              <Edit3 size={16} /> Edit Profile
            </button>
          )}
        </div>

        {successMsg && (
          <div style={{ background: 'rgba(0, 229, 160, 0.1)', color: 'var(--accent)', padding: '12px 16px', borderRadius: '8px', marginBottom: '24px', display: 'flex', alignItems: 'center', gap: '8px', border: '1px solid rgba(0, 229, 160, 0.2)' }}>
            <CheckCircle2 size={18} /> {successMsg}
          </div>
        )}

        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '24px', marginBottom: '24px' }}>
          {/* Main Info Card */}
          <div style={{ background: 'var(--surface)', padding: '32px', borderRadius: '16px', border: '1px solid var(--border)', gridColumn: isEditing ? '1 / -1' : '1' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '24px', marginBottom: '32px' }}>
              <div style={{ width: '80px', height: '80px', borderRadius: '50%', background: 'linear-gradient(135deg, var(--accent), var(--accent2))', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
                <User size={40} color="white" />
              </div>
              <div>
                <h2 style={{ margin: '0 0 4px 0', fontSize: '24px' }}>{user?.full_name || user?.email?.split('@')?.[0] || 'Student'}</h2>
                <div style={{ color: 'var(--text2)' }}>{user?.email}</div>
                <div style={{ display: 'inline-block', marginTop: '8px', padding: '4px 12px', background: 'var(--surface2)', borderRadius: '100px', fontSize: '12px', fontWeight: 'bold', color: 'var(--accent)' }}>
                  Level: {user?.level || 'Beginner'}
                </div>
              </div>
            </div>

            {isEditing ? (
              <form onSubmit={handleSave} style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '13px', color: 'var(--text2)', marginBottom: '8px' }}>Full Name</label>
                  <input type="text" value={fullName} onChange={e => setFullName(e.target.value)} style={{ width: '100%', padding: '12px', background: 'var(--bg)', border: '1px solid var(--border)', borderRadius: '8px', color: 'var(--text)' }} />
                </div>
                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '16px' }}>
                  <div>
                    <label style={{ display: 'block', fontSize: '13px', color: 'var(--text2)', marginBottom: '8px' }}>Experience Level</label>
                    <select value={level} onChange={e => setLevel(e.target.value)} style={{ width: '100%', padding: '12px', background: 'var(--bg)', border: '1px solid var(--border)', borderRadius: '8px', color: 'var(--text)' }}>
                      <option value="Beginner">Beginner</option>
                      <option value="Intermediate">Intermediate</option>
                      <option value="Advanced">Advanced</option>
                    </select>
                  </div>
                  <div>
                    <label style={{ display: 'block', fontSize: '13px', color: 'var(--text2)', marginBottom: '8px' }}>Learning Goal</label>
                    <select value={goal} onChange={e => setGoal(e.target.value)} style={{ width: '100%', padding: '12px', background: 'var(--bg)', border: '1px solid var(--border)', borderRadius: '8px', color: 'var(--text)' }}>
                      <option value="get a job">Get a Job</option>
                      <option value="build projects">Build Projects</option>
                      <option value="learn AI/ML">Learn AI/ML</option>
                      <option value="freelance">Freelance</option>
                    </select>
                  </div>
                </div>
                <div style={{ display: 'flex', gap: '12px', marginTop: '16px' }}>
                  <button type="submit" style={{ padding: '12px 24px', background: 'var(--accent)', color: 'black', border: 'none', borderRadius: '8px', fontWeight: 'bold', cursor: 'pointer' }}>Save Changes</button>
                  <button type="button" onClick={() => setIsEditing(false)} style={{ padding: '12px 24px', background: 'transparent', color: 'var(--text)', border: '1px solid var(--border)', borderRadius: '8px', fontWeight: 'bold', cursor: 'pointer' }}>Cancel</button>
                </div>
              </form>
            ) : (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '16px', color: 'var(--text2)', fontSize: '14px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', paddingBottom: '16px', borderBottom: '1px solid var(--border)' }}>
                  <span>Learning Goal</span>
                  <span style={{ color: 'var(--text)', fontWeight: 500, textTransform: 'capitalize' }}>{user?.goal || 'Build Projects'}</span>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between', paddingBottom: '16px', borderBottom: '1px solid var(--border)' }}>
                  <span>Total XP Earned</span>
                  <span style={{ color: 'var(--accent)', fontWeight: 'bold', fontFamily: 'var(--font-mono)' }}>{user?.xp || 0} XP</span>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                  <span>Current Streak</span>
                  <span style={{ color: 'var(--accent3)', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '6px' }}>
                    <Flame size={16} /> {user?.streak || 0} Days
                  </span>
                </div>
              </div>
            )}
          </div>

          {/* Badges / Achievements */}
          {!isEditing && (
            <div style={{ background: 'var(--surface)', padding: '32px', borderRadius: '16px', border: '1px solid var(--border)' }}>
              <h3 style={{ margin: '0 0 24px 0', fontSize: '18px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                <Award size={20} color="var(--accent)" /> Badges & Achievements
              </h3>
              
              {badges.length > 0 ? (
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(100px, 1fr))', gap: '16px' }}>
                  {badges.map((b, i) => (
                    <div key={i} style={{ background: 'var(--surface2)', padding: '16px', borderRadius: '12px', textAlign: 'center', border: '1px solid var(--border)', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '12px' }}>
                      <div style={{ width: '48px', height: '48px', borderRadius: '50%', background: 'var(--bg)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                        {b.icon}
                      </div>
                      <span style={{ fontSize: '12px', fontWeight: 'bold' }}>{b.name}</span>
                    </div>
                  ))}
                </div>
              ) : (
                <div style={{ textAlign: 'center', padding: '40px 0', color: 'var(--text3)' }}>
                  <Award size={48} style={{ opacity: 0.2, marginBottom: '16px' }} />
                  <p>Complete courses and build your streak to earn badges!</p>
                </div>
              )}
            </div>
          )}
        </div>

        {/* Analytics Chart & Referrals */}
        {!isEditing && (
          <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '24px' }}>
            <div style={{ background: 'var(--surface)', padding: '32px', borderRadius: '16px', border: '1px solid var(--border)' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '24px' }}>
                <h3 style={{ margin: 0, fontSize: '18px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <TrendingUp size={20} color="var(--accent)" /> XP Earned (Last 7 Days)
                </h3>
              </div>
              
              <div style={{ height: '300px', width: '100%' }}>
                <ResponsiveContainer width="100%" height="100%">
                  <AreaChart data={activityData.length > 0 ? activityData : mockChartData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                    <defs>
                      <linearGradient id="colorXp" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="var(--accent)" stopOpacity={0.3}/>
                        <stop offset="95%" stopColor="var(--accent)" stopOpacity={0}/>
                      </linearGradient>
                    </defs>
                    <XAxis dataKey="day" stroke="var(--text3)" fontSize={12} tickLine={false} axisLine={false} />
                    <YAxis stroke="var(--text3)" fontSize={12} tickLine={false} axisLine={false} />
                    <Tooltip 
                      contentStyle={{ backgroundColor: 'var(--surface2)', border: '1px solid var(--border)', borderRadius: '8px', color: 'var(--text)' }}
                      itemStyle={{ color: 'var(--accent)' }}
                    />
                    <Area type="monotone" dataKey="xp" stroke="var(--accent)" strokeWidth={3} fillOpacity={1} fill="url(#colorXp)" />
                  </AreaChart>
                </ResponsiveContainer>
              </div>
            </div>


            <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
              
              {/* Skills Radar */}
              <div style={{ background: 'var(--surface)', padding: '32px', borderRadius: '16px', border: '1px solid var(--border)' }}>
                <h3 style={{ margin: '0 0 16px 0', fontSize: '18px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <Target size={20} color="var(--accent2)" /> Skill Assessment
                </h3>
                <div style={{ height: '220px', width: '100%' }}>
                  <ResponsiveContainer width="100%" height="100%">
                    <RadarChart cx="50%" cy="50%" outerRadius="80%" data={mockSkillsData}>
                      <PolarGrid stroke="var(--border)" />
                      <PolarAngleAxis dataKey="subject" tick={{ fill: 'var(--text2)', fontSize: 11 }} />
                      <PolarRadiusAxis angle={30} domain={[0, 150]} tick={false} axisLine={false} />
                      <Radar name="Skills" dataKey="A" stroke="var(--accent2)" fill="var(--accent2)" fillOpacity={0.5} />
                    </RadarChart>
                  </ResponsiveContainer>
                </div>
              </div>

              {/* Certificates */}
              <div style={{ background: 'var(--surface)', padding: '32px', borderRadius: '16px', border: '1px solid var(--border)' }}>
                <h3 style={{ margin: '0 0 16px 0', fontSize: '18px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <CheckCircle2 size={20} color="var(--accent)" /> Certificates
                </h3>
                {completions.length > 0 ? (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                    {completions.map(c => (
                      <div key={c.id} style={{ display: 'flex', alignItems: 'center', gap: '12px', padding: '12px', background: 'var(--surface2)', borderRadius: '8px', border: '1px solid var(--border)' }}>
                        <div style={{ width: '40px', height: '40px', background: 'rgba(0, 229, 160, 0.1)', borderRadius: '8px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                          <Award size={20} color="var(--accent)" />
                        </div>
                        <div>
                          <div style={{ fontWeight: 'bold', fontSize: '14px' }}>{c.course_name}</div>
                          <div style={{ fontSize: '12px', color: 'var(--text-dim)' }}>Completed {new Date(c.completed_at).toLocaleDateString()}</div>
                        </div>
                      </div>
                    ))}
                  </div>
                ) : (
                  <p style={{ color: 'var(--text2)', margin: 0, fontSize: '14px', lineHeight: '1.6' }}>
                    No certificates earned yet. Complete your first course to get certified!
                  </p>
                )}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Profile;
