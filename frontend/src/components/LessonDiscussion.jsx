import React, { useState, useEffect } from 'react';
import { useAuth } from '../AuthContext';

const LessonDiscussion = ({ lessonName }) => {
  const { token, user } = useAuth();
  const [threads, setThreads] = useState([]);
  const [newThreadTitle, setNewThreadTitle] = useState('');
  const [newComment, setNewComment] = useState({});

  useEffect(() => {
    if (lessonName) {
      fetchThreads();
    }
  }, [lessonName]);

  const fetchThreads = async () => {
    try {
      const res = await fetch(`/forum/lesson/${encodeURIComponent(lessonName)}`);
      if (res.ok) {
        const data = await res.json();
        setThreads(data);
      }
    } catch (e) {
      console.error("Failed to fetch threads", e);
    }
  };

  const createThread = async () => {
    if (!newThreadTitle.trim()) return;
    try {
      const res = await fetch('/forum/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ title: newThreadTitle, lesson_name: lessonName })
      });
      if (res.ok) {
        setNewThreadTitle('');
        fetchThreads();
      }
    } catch (e) {
      console.error(e);
    }
  };

  const addComment = async (threadId) => {
    const commentContent = newComment[threadId];
    if (!commentContent || !commentContent.trim()) return;
    
    try {
      const res = await fetch(`/forum/${threadId}/comments`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ content: commentContent })
      });
      if (res.ok) {
        setNewComment({ ...newComment, [threadId]: '' });
        fetchThreads();
      }
    } catch (e) {
      console.error(e);
    }
  };

  return (
    <div style={{ marginTop: '40px', padding: '20px', background: 'var(--surface)', borderRadius: '12px', border: '1px solid var(--border)' }}>
      <h3 style={{ marginTop: 0, color: 'white', display: 'flex', alignItems: 'center', gap: '8px' }}>
        💬 Community Discussion
      </h3>
      <p style={{ color: 'var(--text-dim)', fontSize: '14px', marginBottom: '20px' }}>
        Stuck on {lessonName}? Ask a question or help out a fellow student!
      </p>

      <div style={{ display: 'flex', gap: '10px', marginBottom: '30px' }}>
        <input 
          type="text" 
          value={newThreadTitle}
          onChange={(e) => setNewThreadTitle(e.target.value)}
          placeholder="Start a new discussion thread..."
          style={{ flex: 1, padding: '10px', borderRadius: '8px', border: '1px solid var(--border)', background: 'var(--surface2)', color: 'var(--text)' }}
        />
        <button 
          onClick={createThread}
          style={{ padding: '10px 20px', background: 'var(--accent)', color: 'black', fontWeight: 'bold', border: 'none', borderRadius: '8px', cursor: 'pointer' }}
        >
          Post Thread
        </button>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
        {threads.map(thread => (
          <div key={thread.id} style={{ background: 'var(--surface2)', padding: '16px', borderRadius: '8px', border: '1px solid var(--border)' }}>
            <h4 style={{ margin: '0 0 16px 0', color: 'var(--text)' }}>{thread.title}</h4>
            
            {/* Comments */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', marginBottom: '16px', paddingLeft: '16px', borderLeft: '2px solid var(--border)' }}>
              {thread.comments?.map(c => (
                <div key={c.id} style={{ color: 'var(--text-dim)', fontSize: '14px', background: 'var(--surface)', padding: '8px 12px', borderRadius: '6px' }}>
                  {c.content}
                </div>
              ))}
            </div>

            {/* Add Comment */}
            <div style={{ display: 'flex', gap: '10px' }}>
              <input 
                type="text" 
                value={newComment[thread.id] || ''}
                onChange={(e) => setNewComment({ ...newComment, [thread.id]: e.target.value })}
                placeholder="Reply..."
                style={{ flex: 1, padding: '8px', borderRadius: '6px', border: '1px solid var(--border)', background: 'var(--surface)', color: 'var(--text)' }}
              />
              <button 
                onClick={() => addComment(thread.id)}
                style={{ padding: '8px 16px', background: 'var(--accent2)', color: 'white', fontWeight: 'bold', border: 'none', borderRadius: '6px', cursor: 'pointer' }}
              >
                Reply
              </button>
            </div>
          </div>
        ))}
        {threads.length === 0 && (
          <div style={{ color: 'var(--text-dim)', fontStyle: 'italic', textAlign: 'center', padding: '20px' }}>
            No discussions yet for this lesson. Be the first to start one!
          </div>
        )}
      </div>
    </div>
  );
};

export default LessonDiscussion;
