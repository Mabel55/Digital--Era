import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';

const TeacherDashboard = () => {
  const { token, user } = useAuth();
  const navigate = useNavigate();
  const [students, setStudents] = useState([]);
  const [uploadFile, setUploadFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState('');
  const [courseTitle, setCourseTitle] = useState('');
  const [courseLevel, setCourseLevel] = useState('Beginner');
  const [courseTrack, setCourseTrack] = useState('General');

  useEffect(() => {
    // Basic protection
    if (user && user.role !== 'admin' && user.role !== 'teacher') {
      navigate('/');
    }
  }, [user, navigate]);

  useEffect(() => {
    fetchStudents();
  }, []);

  const fetchStudents = async () => {
    try {
      const res = await fetch('/users/', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        // Filter out admins if you want, or just show everyone
        setStudents(data);
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
        setUploadStatus(`✅ Success: ${data.message}`);
        setUploadFile(null);
        setCourseTitle('');
      } else {
        const errorData = await res.json();
        setUploadStatus(`❌ Error: ${errorData.detail || 'Upload failed'}`);
      }
    } catch (e) {
      setUploadStatus(`❌ Error: ${e.message}`);
    }
  };

  return (
    <div style={{ padding: '40px', maxWidth: '1200px', margin: '0 auto', color: 'var(--text-bright)' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '40px' }}>
        <h1>👨‍🏫 Teacher Portal</h1>
        <button 
          onClick={() => navigate('/')}
          style={{ padding: '10px 20px', background: 'var(--surface)', color: 'white', borderRadius: '8px', border: '1px solid var(--border)', cursor: 'pointer' }}
        >
          ← Back to Dashboard
        </button>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '40px' }}>
        {/* PDF Uploader Section */}
        <div style={{ background: 'var(--surface)', padding: '30px', borderRadius: '12px', border: '1px solid var(--border)' }}>
          <h2 style={{ marginBottom: '20px', color: 'var(--accent)' }}>📚 Upload Course Material</h2>
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
              style={{ marginTop: '10px', padding: '14px', background: 'var(--accent)', color: 'black', fontWeight: 'bold', fontSize: '16px', borderRadius: '8px', border: 'none', cursor: 'pointer' }}
            >
              Upload & Train AI
            </button>
            
            {uploadStatus && (
              <div style={{ marginTop: '16px', padding: '16px', background: uploadStatus.includes('✅') ? 'rgba(34, 197, 94, 0.1)' : 'rgba(56, 189, 248, 0.1)', color: uploadStatus.includes('✅') ? '#22c55e' : 'var(--text-bright)', borderRadius: '8px', fontWeight: 'bold' }}>
                {uploadStatus}
              </div>
            )}
          </form>
        </div>

        {/* Student Progress Section */}
        <div style={{ background: 'var(--surface)', padding: '30px', borderRadius: '12px', border: '1px solid var(--border)', overflowY: 'auto', maxHeight: '600px' }}>
          <h2 style={{ marginBottom: '20px', color: 'var(--accent)' }}>👥 Student Roster & Progress</h2>
          
          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            {students.length === 0 ? (
              <div style={{ color: 'var(--text-dim)' }}>Loading students...</div>
            ) : (
              students.map(student => (
                <div key={student.id} style={{ padding: '16px', background: 'var(--bg)', borderRadius: '8px', border: '1px solid var(--border)' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
                    <div style={{ fontWeight: 'bold', fontSize: '18px' }}>{student.full_name || student.email}</div>
                    <div style={{ background: 'rgba(56, 189, 248, 0.2)', color: 'var(--accent)', padding: '4px 8px', borderRadius: '4px', fontSize: '12px', fontWeight: 'bold' }}>
                      {student.level || 'Beginner'} • Lvl {Math.floor((student.xp || 0) / 100) + 1}
                    </div>
                  </div>
                  
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '14px', color: 'var(--text-dim)', marginBottom: '8px' }}>
                    <span>XP: {student.xp || 0}</span>
                    <span>🔥 {student.streak || 0} Day Streak</span>
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
