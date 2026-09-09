import React, { memo } from 'react';
import { Bot, ArrowUp } from 'lucide-react';
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
}) => {
  return (
    <div className={`ws-chat ${mobileTab === 'chat' ? 'mobile-active' : ''}`}>
      <div className="chat-header-bar">
        <div className="ai-avatar" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}><Bot size={24} /></div>
        <div className="ai-info">
          <div className="ai-name">Mabel Tutor</div>
          <div className="ai-status"><div className="status-dot"></div> Online</div>
        </div>
      </div>
      <div className="chat-messages">
        {messages.map((msg, i) => (
          <div key={i} className={`chat-msg ${msg.sender}`}>
            <div className="msg-bubble" dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(marked(msg.text)) }}></div>
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
