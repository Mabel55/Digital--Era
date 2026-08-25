import React, { useState, useEffect } from 'react';
import { useAuth } from '../AuthContext';
import { Helmet } from 'react-helmet-async';
import PublicNavbar from './PublicNavbar';
import { MessageSquare, Plus, MessageCircle, ChevronDown, ChevronUp, User, Loader2 } from 'lucide-react';

const Forum = () => {
  const { token, user } = useAuth();
  const [threads, setThreads] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // New thread state
  const [showNewThread, setShowNewThread] = useState(false);
  const [newThreadTitle, setNewThreadTitle] = useState('');
  const [newThreadContent, setNewThreadContent] = useState(''); // We use the first comment as the body
  const [isSubmitting, setIsSubmitting] = useState(false);

  // Expanded threads (to show comments)
  const [expandedThreads, setExpandedThreads] = useState({});
  const [commentInputs, setCommentInputs] = useState({});

  useEffect(() => {
    fetchThreads();
  }, []);

  const fetchThreads = async () => {
    setLoading(true);
    try {
      const res = await fetch('/forum/');
      if (res.ok) {
        const data = await res.json();
        setThreads(data.reverse()); // Newest first
      } else {
        setError('Failed to fetch forum threads.');
      }
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };

  const handleCreateThread = async (e) => {
    e.preventDefault();
    if (!token) {
      alert("You must be logged in to post.");
      return;
    }
    if (!newThreadTitle.trim() || !newThreadContent.trim()) return;

    setIsSubmitting(true);
    try {
      // 1. Create thread
      const tRes = await fetch('/forum/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
        body: JSON.stringify({ title: newThreadTitle, lesson_name: 'Global' })
      });
      if (!tRes.ok) throw new Error("Failed to create thread");
      const threadData = await tRes.json();

      // 2. Add first comment (the body)
      await fetch(`/forum/${threadData.id}/comments`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
        body: JSON.stringify({ content: newThreadContent })
      });

      setShowNewThread(false);
      setNewThreadTitle('');
      setNewThreadContent('');
      fetchThreads();
    } catch (e) {
      alert(e.message);
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleAddComment = async (threadId) => {
    if (!token) {
      alert("You must be logged in to comment.");
      return;
    }
    const content = commentInputs[threadId];
    if (!content || !content.trim()) return;

    try {
      const res = await fetch(`/forum/${threadId}/comments`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
        body: JSON.stringify({ content })
      });
      
      if (res.ok) {
        setCommentInputs(prev => ({ ...prev, [threadId]: '' }));
        fetchThreads(); // Refresh threads
      }
    } catch (e) {
      console.error(e);
    }
  };

  const toggleExpand = (threadId) => {
    setExpandedThreads(prev => ({ ...prev, [threadId]: !prev[threadId] }));
  };

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      <Helmet>
        <title>Community Forum | Digital Era Academy — Ask &amp; Learn Together</title>
        <meta name="description" content="Join the Digital Era community forum. Ask coding questions, share Python and AI tips, and learn from fellow developers in Nigeria and beyond." />
        <meta name="keywords" content="coding forum Nigeria, Python help Lagos, developer community Africa, AI questions, Digital Era forum" />
        <link rel="canonical" href="https://digital-era.live/community" />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="https://digital-era.live/community" />
        <meta property="og:title" content="Community Forum | Digital Era Academy" />
        <meta property="og:description" content="Ask questions, share ideas and learn with 500+ students on the Digital Era forum." />
        <meta property="og:image" content="https://digital-era.live/og-image.png" />
      </Helmet>
      <PublicNavbar />
      
      <main style={{ flex: 1, padding: '40px 24px', maxWidth: '1000px', margin: '0 auto', width: '100%' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end', marginBottom: '40px' }}>
          <div>
            <div style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', padding: '6px 16px', background: 'rgba(59, 130, 246, 0.1)', border: '1px solid #3b82f6', borderRadius: '100px', color: '#3b82f6', fontWeight: 600, fontSize: '14px', marginBottom: '16px' }}>
              <MessageSquare size={16} /> Community Forum
            </div>
            <h1 style={{ fontFamily: 'var(--font-display)', fontSize: 'clamp(28px, 4vw, 40px)', fontWeight: 800, color: 'var(--text)' }}>
              Ask questions. <span style={{ color: 'var(--accent)' }}>Share ideas.</span>
            </h1>
          </div>
          
          <button 
            onClick={() => setShowNewThread(!showNewThread)}
            style={{ padding: '12px 24px', background: 'var(--accent)', color: '#000', border: 'none', borderRadius: '12px', fontWeight: 'bold', fontSize: '16px', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '8px' }}
          >
            {showNewThread ? <ChevronUp size={20} /> : <Plus size={20} />} 
            {showNewThread ? 'Cancel' : 'New Discussion'}
          </button>
        </div>

        {/* New Thread Form */}
        {showNewThread && (
          <div style={{ background: 'var(--surface)', border: '1px solid var(--border)', borderRadius: '16px', padding: '24px', marginBottom: '32px', animation: 'fadeIn 0.3s' }}>
            <h3 style={{ marginTop: 0, color: 'var(--text)', fontSize: '18px', marginBottom: '16px' }}>Start a New Discussion</h3>
            <form onSubmit={handleCreateThread}>
              <div style={{ marginBottom: '16px' }}>
                <input 
                  type="text" 
                  placeholder="Discussion Title (e.g. How do I sort a dictionary in Python?)" 
                  value={newThreadTitle}
                  onChange={(e) => setNewThreadTitle(e.target.value)}
                  style={{ width: '100%', padding: '12px', background: 'var(--bg)', border: '1px solid var(--border)', borderRadius: '8px', color: 'var(--text)', fontSize: '16px' }}
                  required
                />
              </div>
              <div style={{ marginBottom: '16px' }}>
                <textarea 
                  placeholder="Provide more details or code snippets here..." 
                  value={newThreadContent}
                  onChange={(e) => setNewThreadContent(e.target.value)}
                  style={{ width: '100%', padding: '12px', background: 'var(--bg)', border: '1px solid var(--border)', borderRadius: '8px', color: 'var(--text)', fontSize: '15px', minHeight: '120px', resize: 'vertical' }}
                  required
                />
              </div>
              <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
                <button 
                  type="submit" 
                  disabled={isSubmitting}
                  style={{ padding: '10px 24px', background: 'var(--accent2)', color: '#fff', border: 'none', borderRadius: '8px', fontWeight: 'bold', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '8px', opacity: isSubmitting ? 0.7 : 1 }}
                >
                  {isSubmitting ? <Loader2 size={16} className="spinner" /> : <MessageCircle size={16} />}
                  Post Discussion
                </button>
              </div>
            </form>
          </div>
        )}

        {/* Threads List */}
        {loading ? (
          <div style={{ display: 'flex', justifyContent: 'center', padding: '60px 0' }}>
            <Loader2 size={32} color="var(--accent)" className="spinner" />
          </div>
        ) : error ? (
          <div style={{ textAlign: 'center', padding: '40px', color: '#ef4444' }}>{error}</div>
        ) : threads.length === 0 ? (
          <div style={{ textAlign: 'center', padding: '60px', background: 'var(--surface2)', borderRadius: '16px', color: 'var(--text-dim)' }}>
            <MessageSquare size={48} style={{ opacity: 0.2, marginBottom: '16px' }} />
            <h3>No discussions yet</h3>
            <p>Be the first to start a conversation in the community!</p>
          </div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            {threads.map(thread => (
              <div key={thread.id} style={{ background: 'var(--surface)', border: '1px solid var(--border)', borderRadius: '12px', overflow: 'hidden' }}>
                
                {/* Thread Header (Click to expand) */}
                <div 
                  onClick={() => toggleExpand(thread.id)}
                  style={{ padding: '20px', cursor: 'pointer', display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', background: expandedThreads[thread.id] ? 'var(--surface2)' : 'transparent', transition: 'background 0.2s' }}
                >
                  <div style={{ flex: 1 }}>
                    <h3 style={{ margin: '0 0 8px 0', fontSize: '18px', color: 'var(--text)', fontWeight: 600 }}>{thread.title}</h3>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '12px', fontSize: '13px', color: 'var(--text-dim)' }}>
                      <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}><User size={14} /> {thread.author_name}</span>
                      <span>•</span>
                      <span>{new Date(thread.created_at).toLocaleDateString()}</span>
                      <span>•</span>
                      <span style={{ display: 'flex', alignItems: 'center', gap: '4px', color: thread.comments.length > 0 ? 'var(--accent)' : 'inherit' }}>
                        <MessageCircle size={14} /> {thread.comments.length} replies
                      </span>
                    </div>
                  </div>
                  <div style={{ color: 'var(--text3)', marginLeft: '16px' }}>
                    {expandedThreads[thread.id] ? <ChevronUp size={20} /> : <ChevronDown size={20} />}
                  </div>
                </div>

                {/* Thread Comments (Expanded state) */}
                {expandedThreads[thread.id] && (
                  <div style={{ padding: '20px', borderTop: '1px solid var(--border)' }}>
                    {thread.comments.length === 0 ? (
                      <p style={{ color: 'var(--text-dim)', fontStyle: 'italic', margin: '0 0 20px 0' }}>No replies yet.</p>
                    ) : (
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '16px', marginBottom: '24px' }}>
                        {thread.comments.map((comment, idx) => (
                          <div key={comment.id} style={{ display: 'flex', gap: '16px', background: idx === 0 ? 'rgba(59, 130, 246, 0.05)' : 'var(--bg)', padding: '16px', borderRadius: '12px', border: idx === 0 ? '1px solid rgba(59,130,246,0.2)' : '1px solid var(--border)' }}>
                            <div style={{ width: '40px', height: '40px', borderRadius: '50%', background: 'var(--surface2)', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0, fontWeight: 'bold', color: 'var(--text2)' }}>
                              {comment.author_name.charAt(0).toUpperCase()}
                            </div>
                            <div style={{ flex: 1 }}>
                              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '8px' }}>
                                <span style={{ fontWeight: 'bold', color: 'var(--text)', fontSize: '14px' }}>{comment.author_name}</span>
                                <span style={{ color: 'var(--text-dim)', fontSize: '12px' }}>{new Date(comment.created_at).toLocaleString()}</span>
                              </div>
                              <div style={{ color: 'var(--text2)', fontSize: '15px', lineHeight: 1.5, whiteSpace: 'pre-wrap' }}>
                                {comment.content}
                              </div>
                            </div>
                          </div>
                        ))}
                      </div>
                    )}

                    {/* Add Comment Input */}
                    {token ? (
                      <div style={{ display: 'flex', gap: '12px' }}>
                        <input 
                          type="text" 
                          placeholder="Write a reply..." 
                          value={commentInputs[thread.id] || ''}
                          onChange={(e) => setCommentInputs(prev => ({ ...prev, [thread.id]: e.target.value }))}
                          onKeyDown={(e) => e.key === 'Enter' && handleAddComment(thread.id)}
                          style={{ flex: 1, padding: '12px 16px', background: 'var(--bg)', border: '1px solid var(--border)', borderRadius: '24px', color: 'var(--text)' }}
                        />
                        <button 
                          onClick={() => handleAddComment(thread.id)}
                          disabled={!commentInputs[thread.id]?.trim()}
                          style={{ padding: '0 20px', background: 'var(--accent)', color: '#000', border: 'none', borderRadius: '24px', fontWeight: 'bold', cursor: commentInputs[thread.id]?.trim() ? 'pointer' : 'not-allowed', opacity: commentInputs[thread.id]?.trim() ? 1 : 0.5 }}
                        >
                          Reply
                        </button>
                      </div>
                    ) : (
                      <div style={{ padding: '12px', background: 'var(--surface2)', borderRadius: '8px', textAlign: 'center', color: 'var(--text-dim)', fontSize: '14px' }}>
                        Please log in to participate in this discussion.
                      </div>
                    )}
                  </div>
                )}
              </div>
            ))}
          </div>
        )}
      </main>
    </div>
  );
};

export default Forum;
