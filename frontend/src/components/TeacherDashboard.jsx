import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';
import { Users, BookOpen, Flame, CheckCircle2, XCircle, DollarSign, Bot, Crown, Activity } from 'lucide-react';

const TeacherDashboard = () => {
  const { token, user } = useAuth();
  const navigate = useNavigate();
  const [students, setStudents] = useState([]);
  const [metrics, setMetrics] = useState(null);
  const [uploadFile, setUploadFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState('');
  const [courseTitle, setCourseTitle] = useState('');
  const [courseLevel, setCourseLevel] = useState('Beginner');
  const [courseTrack, setCourseTrack] = useState('General');
  const [isUploading, setIsUploading] = useState(false);

  useEffect(() => {
    // Basic protection
    if (user && (user.role || '').toLowerCase() !== 'admin' && (user.role || '').toLowerCase() !== 'teacher' && user.email !== 'nasaadanna@gmail.com') {
      navigate('/');
    }
  }, [user, navigate]);

  useEffect(() => {
    fetchStudents();
    fetchMetrics();
  }, []);

  const fetchMetrics = async () => {
    try {
      const res = await fetch('/admin/analytics', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        setMetrics(data);
      }
    } catch (e) {
      console.error(e);
    }
  };

  const fetchStudents = async () => {
    try {
      const res = await fetch('/users/', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        setStudents(data);
      }
    } catch (e) {
      console.error(e);
    }
  };

  const handleGrantPro = async (userId) => {
    if (!window.confirm("Grant this user lifetime Pro access for free?")) return;
    try {
      const res = await fetch(`/admin/users/${userId}/grant-pro`, {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (res.ok) {
        fetchStudents();
        fetchMetrics();
      } else {
        const err = await res.json();
        alert(err.detail || "Failed to grant Pro");
      }
    } catch (e) {
      console.error(e);
    }
  };

  const handleToggleBlock = async (userId) => {
    if (!window.confirm("Are you sure you want to toggle the block status of this user?")) return;
    try {
      const res = await fetch(`/admin/users/${userId}/toggle-block`, {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (res.ok) {
        fetchStudents();
      } else {
         const err = await res.json();
         alert(err.detail || "Failed to toggle block");
      }
    } catch (e) {
      console.error(e);
    }
  };

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!uploadFile || !courseTitle) {
      setUploadStatus('Please select a file and enter a course title.');
      return;
    }

    setUploadStatus('Uploading and training AI Brain... this may take a minute.');
    setIsUploading(true);
    
    const formData = new FormData();
    formData.append('file', uploadFile);
    formData.append('course_title', courseTitle);
    formData.append('course_level', courseLevel);
    formData.append('course_track', courseTrack);

    try {
      const res = await fetch('/teachers/upload-pdf/', {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${token}` }, // if endpoint is protected
        body: formData
      });
      
      if (res.ok) {
        const data = await res.json();
        setUploadStatus(`Success: ${data.message}`);
        setUploadFile(null);
        setCourseTitle('');
      } else {
        const errorData = await res.json();
        setUploadStatus(`Error: ${errorData.detail || 'Upload failed'}`);
      }
    } catch (e) {
      setUploadStatus(`Error: ${e.message}`);
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <div style={{ padding: '40px', maxWidth: '1200px', margin: '0 auto', color: 'var(--text-bright)' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '40px' }}>
        <h1 style={{ display: 'flex', alignItems: 'center', gap: '12px' }}><Activity size={32} /> Admin Dashboard</h1>
        <button 
          onClick={() => navigate('/')}
          style={{ padding: '10px 20px', background: 'var(--surface)', color: 'white', borderRadius: '8px', border: '1px solid var(--border)', cursor: 'pointer' }}
          aria-label="Back to Home"
        >
          ← Back to Dashboard
        </button>
      </div>

      {metrics && (
        <div className="admin-metrics-grid">
          <div className="admin-metric-card">
            <div className="admin-metric-title"><DollarSign size={16} color="var(--accent)" /> Paystack MRR</div>
            <div className="admin-metric-value">${metrics.mrr}</div>
          </div>
          <div className="admin-metric-card">
            <div className="admin-metric-title"><Users size={16} color="var(--accent2)" /> Total Users</div>
            <div className="admin-metric-value">{metrics.total_users}</div>
          </div>
          <div className="admin-metric-card">
            <div className="admin-metric-title"><Crown size={16} color="var(--accent3)" /> Active Pro Users</div>
            <div className="admin-metric-value">{metrics.active_pro_users}</div>
          </div>
          <div className="admin-metric-card">
            <div className="admin-metric-title"><Bot size={16} color="var(--accent)" /> AI Msgs Today</div>
            <div className="admin-metric-value">{metrics.ai_messages_today}</div>
          </div>
        </div>
      )}

      <div className="admin-panels-grid">
        {/* PDF Uploader Section */}
        <div style={{ background: 'var(--surface)', padding: '30px', borderRadius: '12px', border: '1px solid var(--border)' }}>
          <h2 style={{ marginBottom: '20px', color: 'var(--accent)', display: 'flex', alignItems: 'center', gap: '8px' }}><BookOpen size={24} /> Upload Course Material</h2>
          <p style={{ marginBottom: '20px', color: 'var(--text-dim)' }}>Upload a PDF textbook or syllabus. The AI Brain will automatically ingest this document to provide highly context-aware tutoring to your students.</p>
          
          <form onSubmit={handleUpload} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            <div>
              <label style={{ display: 'block', marginBottom: '8px', fontWeight: 'bold' }}>Course Title:</label>
              <input 
                type="text" 
                value={courseTitle} 
                onChange={(e) => setCourseTitle(e.target.value)} 
                placeholder="e.g. Intro to Data Science"
                style={{ width: '100%', padding: '12px', borderRadius: '8px', background: 'var(--bg)', border: '1px solid var(--border)', color: 'white' }}
              />
            </div>
            
            <div style={{ display: 'flex', gap: '16px' }}>
              <div style={{ flex: 1 }}>
                <label style={{ display: 'block', marginBottom: '8px', fontWeight: 'bold' }}>Level:</label>
                <select 
                  value={courseLevel} 
                  onChange={(e) => setCourseLevel(e.target.value)}
                  style={{ width: '100%', padding: '12px', borderRadius: '8px', background: 'var(--bg)', border: '1px solid var(--border)', color: 'white' }}
                >
                  <option value="Beginner">Beginner</option>
                  <option value="Intermediate">Intermediate</option>
                  <option value="Advanced">Advanced</option>
                </select>
              </div>
              <div style={{ flex: 1 }}>
                <label style={{ display: 'block', marginBottom: '8px', fontWeight: 'bold' }}>Track:</label>
                <select 
                  value={courseTrack} 
                  onChange={(e) => setCourseTrack(e.target.value)}
                  style={{ width: '100%', padding: '12px', borderRadius: '8px', background: 'var(--bg)', border: '1px solid var(--border)', color: 'white' }}
                >
                  <option value="General">General</option>
                  <option value="Backend">Backend</option>
                  <option value="Data Science">Data Science</option>
                  <option value="Frontend">Frontend</option>
                </select>
              </div>
            </div>

            <div>
              <label style={{ display: 'block', marginBottom: '8px', fontWeight: 'bold' }}>PDF File:</label>
              <input 
                type="file" 
                accept="application/pdf"
                onChange={(e) => setUploadFile(e.target.files[0])} 
                style={{ width: '100%', padding: '12px', borderRadius: '8px', background: 'var(--bg)', border: '1px solid var(--border)', color: 'white' }}
              />
            </div>

            <button 
              type="submit" 
              disabled={isUploading || !uploadFile}
              style={{ marginTop: '10px', padding: '14px', background: 'var(--accent)', color: 'black', fontWeight: 'bold', fontSize: '16px', borderRadius: '8px', border: 'none', cursor: isUploading || !uploadFile ? 'not-allowed' : 'pointer', opacity: isUploading || !uploadFile ? 0.5 : 1 }}
              aria-label={isUploading ? "Uploading course material" : "Upload Course Material"}
              aria-busy={isUploading}
            >
              Upload & Train AI
            </button>
            
            {uploadStatus && (
              <div style={{ marginTop: '16px', padding: '16px', background: uploadStatus.includes('Success') ? 'rgba(34, 197, 94, 0.1)' : 'rgba(56, 189, 248, 0.1)', color: uploadStatus.includes('Success') ? '#22c55e' : 'var(--text-bright)', borderRadius: '8px', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '8px' }}>
                {uploadStatus.includes('Success') ? <CheckCircle2 size={18} /> : uploadStatus.includes('Error') ? <XCircle size={18} /> : null} {uploadStatus}
              </div>
            )}
          </form>
        </div>

        {/* Student Progress Section */}
        <div style={{ background: 'var(--surface)', padding: '30px', borderRadius: '12px', border: '1px solid var(--border)', overflowY: 'auto', maxHeight: '600px' }}>
          <h2 style={{ marginBottom: '20px', color: 'var(--accent)', display: 'flex', alignItems: 'center', gap: '8px' }}><Users size={24} /> Student Roster & Progress</h2>
          
          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            {students.length === 0 ? (
              <div style={{ color: 'var(--text-dim)' }}>Loading students...</div>
            ) : (
              students.map(student => (
                <div key={student.id} style={{ padding: '16px', background: 'var(--bg)', borderRadius: '8px', border: '1px solid var(--border)' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
                    <div>
                      <div style={{ fontWeight: 'bold', fontSize: '18px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                        {student.full_name || student.email}
                        {!student.is_active && (
                          <span style={{ background: '#ef4444', color: 'white', padding: '2px 6px', borderRadius: '4px', fontSize: '10px' }}>BLOCKED</span>
                        )}
                      </div>
                      <div style={{ fontSize: '12px', color: 'var(--text-dim)', marginTop: '4px', display: 'flex', gap: '6px' }}>
                        {student.subscription?.is_pro ? (
                           <span style={{ color: 'var(--accent)', fontWeight: 'bold' }}>PRO TIER</span>
                        ) : (
                           <span>Free Tier</span>
                        )}
                        {student.subscription?.paystack_customer_code && (
                           <span style={{ color: '#059669', background: '#d1fae5', padding: '2px 6px', borderRadius: '4px', fontWeight: 'bold' }}>Paystack Customer</span>
                        )}
                      </div>
                    </div>
                    <div style={{ background: 'rgba(56, 189, 248, 0.2)', color: 'var(--accent)', padding: '4px 8px', borderRadius: '4px', fontSize: '12px', fontWeight: 'bold' }}>
                      {student.level || 'Beginner'} • Lvl {Math.floor((student.xp || 0) / 100) + 1}
                    </div>
                  </div>
                  
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '14px', color: 'var(--text-dim)', marginBottom: '8px' }}>
                    <span>XP: {student.xp || 0}</span>
                    <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}><Flame size={14} color="var(--accent3)" /> {student.streak || 0} Day Streak</span>
                  </div>

                  <div style={{ marginTop: '12px', borderTop: '1px solid var(--border)', paddingTop: '12px' }}>
                    <div style={{ fontSize: '12px', fontWeight: 'bold', color: 'var(--text-dim)', marginBottom: '8px', textTransform: 'uppercase' }}>Course Progress</div>
                    {student.progress && Object.keys(student.progress).length > 0 ? (
                      Object.keys(student.progress).map(course => (
                        <div key={course} style={{ display: 'flex', justifyContent: 'space-between', fontSize: '14px', marginBottom: '4px' }}>
                          <span>{course}</span>
                          <span style={{ color: 'var(--accent)' }}>{student.progress[course].completed_lessons} lessons</span>
                        </div>
                      ))
                    ) : (
                      <div style={{ fontSize: '14px', color: 'var(--text-dim)' }}>No active courses yet.</div>
                    )}
                  </div>
                  
                  <div style={{ marginTop: '16px', borderTop: '1px solid var(--border)', paddingTop: '16px', display: 'flex', gap: '8px', justifyContent: 'flex-end' }}>
                    {!student.subscription?.is_pro && (
                      <button 
                        onClick={() => handleGrantPro(student.id)}
                        style={{ padding: '6px 12px', background: 'var(--surface2)', color: 'var(--accent)', borderRadius: '6px', border: '1px solid var(--border)', cursor: 'pointer', fontSize: '12px', fontWeight: 'bold' }}
                      >
                        Grant Pro
                      </button>
                    )}
                    <button 
                      onClick={() => handleToggleBlock(student.id)}
                      style={{ padding: '6px 12px', background: student.is_active ? 'var(--surface2)' : '#ef4444', color: student.is_active ? '#ef4444' : 'white', borderRadius: '6px', border: '1px solid var(--border)', cursor: 'pointer', fontSize: '12px', fontWeight: 'bold' }}
                    >
                      {student.is_active ? 'Block User' : 'Unblock User'}
                    </button>
                  </div>
                </div>
              ))
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default TeacherDashboard;
