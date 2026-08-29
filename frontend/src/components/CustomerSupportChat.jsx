import React, { useState, useRef, useEffect } from 'react';
import { MessageSquare, X, Send, Bot, User } from 'lucide-react';

const CustomerSupportChat = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    { sender: 'ai', text: 'Hi! I am the Digital Era support bot. How can I help you today?' }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = input;
    setMessages(prev => [...prev, { sender: 'user', text: userMessage }]);
    setInput('');
    setIsLoading(true);

    try {
      const res = await fetch('/api/support/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userMessage })
      });
      const data = await res.json();
      setMessages(prev => [...prev, { sender: 'ai', text: data.answer }]);
    } catch (error) {
      setMessages(prev => [...prev, { sender: 'ai', text: 'Sorry, I am having trouble connecting to the server. Please call us at +234 703 719 7261.' }]);
    } finally {
      setIsLoading(false);
    }
  };

  if (!isOpen) {
    return (
      <button 
        onClick={() => setIsOpen(true)}
        style={{
          position: 'fixed',
          bottom: '24px',
          right: '24px',
          width: '60px',
          height: '60px',
          borderRadius: '50%',
          background: 'linear-gradient(135deg, var(--accent), #00b37d)',
          color: '#fff',
          border: 'none',
          boxShadow: '0 8px 30px rgba(0, 229, 160, 0.4)',
          cursor: 'pointer',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          zIndex: 9999,
          transition: 'transform 0.2s',
        }}
        onMouseEnter={e => e.currentTarget.style.transform = 'scale(1.1)'}
        onMouseLeave={e => e.currentTarget.style.transform = 'scale(1)'}
      >
        <MessageSquare size={28} />
      </button>
    );
  }

  return (
    <div style={{
      position: 'fixed',
      bottom: '24px',
      right: '24px',
      width: '350px',
      height: '500px',
      background: 'var(--surface)',
      borderRadius: '20px',
      boxShadow: '0 20px 50px rgba(0,0,0,0.5), 0 0 0 1px var(--border)',
      display: 'flex',
      flexDirection: 'column',
      zIndex: 9999,
      overflow: 'hidden',
      backdropFilter: 'blur(20px)'
    }}>
      {/* Header */}
      <div style={{
        padding: '16px',
        background: 'rgba(0, 229, 160, 0.1)',
        borderBottom: '1px solid var(--border)',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <div style={{ width: '36px', height: '36px', borderRadius: '50%', background: 'var(--accent)', display: 'flex', justifyContent: 'center', alignItems: 'center', color: '#000' }}>
            <Bot size={20} />
          </div>
          <div>
            <h4 style={{ margin: 0, fontSize: '15px', fontWeight: 600, color: 'var(--text)' }}>Support AI</h4>
            <span style={{ fontSize: '12px', color: 'var(--accent)' }}>Online</span>
          </div>
        </div>
        <button 
          onClick={() => setIsOpen(false)}
          style={{ background: 'transparent', border: 'none', color: 'var(--text2)', cursor: 'pointer' }}
        >
          <X size={20} />
        </button>
      </div>

      {/* Messages */}
      <div style={{
        flex: 1,
        padding: '16px',
        overflowY: 'auto',
        display: 'flex',
        flexDirection: 'column',
        gap: '12px'
      }}>
        {messages.map((msg, idx) => (
          <div key={idx} style={{
            display: 'flex',
            justifyContent: msg.sender === 'user' ? 'flex-end' : 'flex-start',
            gap: '8px'
          }}>
            {msg.sender === 'ai' && (
              <div style={{ width: '28px', height: '28px', borderRadius: '50%', background: 'var(--surface2)', display: 'flex', justifyContent: 'center', alignItems: 'center', flexShrink: 0 }}>
                <Bot size={14} color="var(--accent)" />
              </div>
            )}
            <div style={{
              background: msg.sender === 'user' ? 'var(--accent)' : 'var(--surface2)',
              color: msg.sender === 'user' ? '#000' : 'var(--text)',
              padding: '10px 14px',
              borderRadius: '16px',
              borderBottomRightRadius: msg.sender === 'user' ? '4px' : '16px',
              borderBottomLeftRadius: msg.sender === 'ai' ? '4px' : '16px',
              fontSize: '14px',
              lineHeight: 1.5,
              maxWidth: '80%'
            }}>
              {msg.text}
            </div>
          </div>
        ))}
        {isLoading && (
          <div style={{ display: 'flex', gap: '8px' }}>
            <div style={{ width: '28px', height: '28px', borderRadius: '50%', background: 'var(--surface2)', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
              <Bot size={14} color="var(--accent)" />
            </div>
            <div style={{ background: 'var(--surface2)', padding: '10px 14px', borderRadius: '16px', borderBottomLeftRadius: '4px', fontSize: '14px', color: 'var(--text2)' }}>
              Typing...
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input Form */}
      <form onSubmit={handleSend} style={{
        padding: '12px',
        borderTop: '1px solid var(--border)',
        display: 'flex',
        gap: '8px',
        background: 'var(--surface)'
      }}>
        <input 
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask a question..."
          disabled={isLoading}
          style={{
            flex: 1,
            background: 'var(--surface2)',
            border: '1px solid var(--border)',
            padding: '10px 14px',
            borderRadius: '24px',
            color: 'var(--text)',
            outline: 'none',
            fontSize: '14px'
          }}
        />
        <button 
          type="submit"
          disabled={!input.trim() || isLoading}
          style={{
            width: '40px',
            height: '40px',
            borderRadius: '50%',
            background: input.trim() && !isLoading ? 'var(--accent)' : 'var(--surface2)',
            color: input.trim() && !isLoading ? '#000' : 'var(--text2)',
            border: 'none',
            cursor: input.trim() && !isLoading ? 'pointer' : 'default',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            transition: 'all 0.2s'
          }}
        >
          <Send size={18} style={{ marginLeft: '2px' }} />
        </button>
      </form>
    </div>
  );
};

export default CustomerSupportChat;
