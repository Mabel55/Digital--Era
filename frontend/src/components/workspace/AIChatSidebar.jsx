import React, { memo } from 'react';
import { Bot, ArrowUp, RotateCcw } from 'lucide-react';
import DOMPurify from 'dompurify';
import { marked } from 'marked';

const AIChatSidebar = ({
  mobileTab,
  messages,
  isTyping,
  chatEndRef,
  aiUsage,
  isPro,
  navigate,
  chatInput,
  setChatInput,
  sendChat,
  persona,
  setPersona,
  lastFailedMsg,
}) => {
  const handleRetry = (e) => {
    e?.preventDefault();
    if (lastFailedMsg) {
      sendChat(null, lastFailedMsg);
    }
  };

  return (
    <div className={`ws-chat ${mobileTab === 'chat' ? 'mobile-active' : ''}`}>
      <div className="chat-header-bar">
        <div className="ai-avatar" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}><Bot size={24} /></div>
        <div className="ai-info" style={{ display: 'flex', flexDirection: 'column', gap: '4px', width: '100%' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div className="ai-name">Mabel Tutor</div>
            <select 
              value={persona || 'study_buddy'} 
              onChange={e => setPersona && setPersona(e.target.value)}
              style={{ background: 'var(--bg-lighter)', color: 'var(--text)', border: '1px solid var(--border)', borderRadius: '4px', fontSize: '11px', padding: '2px 4px' }}
            >
              <option value="study_buddy">Study Buddy</option>
              <option value="code_reviewer">Code Reviewer</option>
            </select>
          </div>
          <div className="ai-status"><div className="status-dot"></div> Online</div>
        </div>
      </div>
      <div className="chat-messages">
        {messages.map((msg, i) => (
          <div key={i} className={`chat-msg ${msg.sender}`}>
            <div className="msg-bubble" style={msg.isError ? { borderLeft: '3px solid var(--danger, #ef4444)' } : {}}>
              {msg.thought_process && (
                <details style={{ marginBottom: '8px', fontSize: '11px', background: 'rgba(0,0,0,0.1)', padding: '6px', borderRadius: '4px' }}>
                  <summary style={{ cursor: 'pointer', color: 'var(--text-dim)' }}>Thought Process</summary>
                  <div style={{ marginTop: '4px', color: 'var(--text-dim)', whiteSpace: 'pre-wrap' }}>{msg.thought_process}</div>
                </details>
              )}
              <div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(marked(msg.text)) }}></div>
              {/* Retry button for error messages */}
              {msg.isError && lastFailedMsg && i === messages.length - 1 && (
                <button
                  onClick={handleRetry}
                  style={{
                    marginTop: '10px',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '6px',
                    padding: '6px 14px',
                    fontSize: '12px',
                    fontWeight: 'bold',
                    color: 'var(--accent)',
                    background: 'rgba(0, 229, 160, 0.1)',
                    border: '1px solid rgba(0, 229, 160, 0.3)',
                    borderRadius: '6px',
                    cursor: 'pointer',
                    transition: 'all 0.2s ease',
                  }}
                  onMouseEnter={e => { e.target.style.background = 'rgba(0, 229, 160, 0.2)'; }}
                  onMouseLeave={e => { e.target.style.background = 'rgba(0, 229, 160, 0.1)'; }}
                  aria-label="Retry last message"
                >
                  <RotateCcw size={14} /> Try Again
                </button>
              )}
            </div>
          </div>
        ))}
        {isTyping && (
          <div className="chat-msg ai">
            <div className="msg-bubble typing-indicator">
              <span></span><span></span><span></span>
            </div>
          </div>
        )}
        <div ref={chatEndRef}></div>
      </div>
      
      {/* AI Limits Banner */}
      {aiUsage.isLimited && !isPro && (
        <div style={{
          padding: '8px 12px', fontSize: '12px', textAlign: 'center',
          background: aiUsage.remaining === 0 ? 'rgba(239,68,68,0.1)' : 'rgba(245,158,11,0.1)',
          color: aiUsage.remaining === 0 ? 'var(--danger)' : 'var(--accent3)',
          borderTop: '1px solid var(--border)'
        }}>
          {aiUsage.remaining === 0 
            ? "Daily AI limit reached. Upgrade to Pro for unlimited."
            : `${aiUsage.remaining} free AI messages remaining today.`
          }
          <span 
            onClick={() => navigate('/pricing')} 
            style={{ fontWeight: 'bold', marginLeft: '6px', cursor: 'pointer', textDecoration: 'underline' }}
          >
            Upgrade
          </span>
        </div>
      )}
      
      <form className="chat-input-row" onSubmit={sendChat}>
        <textarea 
          className="chat-textarea" 
          placeholder={aiUsage.isLimited && aiUsage.remaining === 0 && !isPro ? "Limit reached..." : "Ask for help..."} 
          value={chatInput}
          onChange={e => setChatInput(e.target.value)}
          disabled={aiUsage.isLimited && aiUsage.remaining === 0 && !isPro}
          onKeyDown={e => {
            if (e.key === 'Enter' && !e.shiftKey) {
              e.preventDefault();
              sendChat(e);
            }
          }}
          rows={1}
        />
        <button 
          type="submit" 
          className="chat-send-btn"
          disabled={!chatInput.trim() || (aiUsage.isLimited && aiUsage.remaining === 0 && !isPro)}
        >
          <ArrowUp size={20} />
        </button>
      </form>
    </div>
  );
};

export default memo(AIChatSidebar);
