import React, { useState } from 'react';
import { Bell, Check, Trash2, BellOff } from 'lucide-react';

const NotificationCenter = ({ notifications = [], markAsRead, clearAll }) => {
  const [isOpen, setIsOpen] = useState(false);
  const unreadCount = notifications.filter(n => !n.is_read).length;

  const formatTimeAgo = (dateStr) => {
    const diff = (new Date() - new Date(dateStr)) / 1000;
    if (diff < 60) return 'Just now';
    if (diff < 3600) return `${Math.floor(diff / 60)}m ago`;
    if (diff < 86400) return `${Math.floor(diff / 3600)}h ago`;
    return `${Math.floor(diff / 86400)}d ago`;
  };

  return (
    <div style={{ position: 'relative' }}>
      <button 
        onClick={() => setIsOpen(!isOpen)}
        style={{ position: 'relative', padding: '8px', background: 'transparent', color: 'var(--text)', border: 'none', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center' }}
        aria-label="Notifications"
      >
        <Bell size={20} />
        {unreadCount > 0 && (
          <span style={{ position: 'absolute', top: '4px', right: '4px', background: 'var(--accent3)', color: 'black', fontSize: '10px', fontWeight: 'bold', borderRadius: '50%', width: '16px', height: '16px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            {unreadCount}
          </span>
        )}
      </button>

      {isOpen && (
        <>
          <div style={{ position: 'fixed', inset: 0, zIndex: 90 }} onClick={() => setIsOpen(false)}></div>
          <div style={{ position: 'absolute', top: 'calc(100% + 8px)', right: 0, width: '320px', background: 'var(--surface)', border: '1px solid var(--border)', borderRadius: '16px', boxShadow: '0 10px 40px rgba(0,0,0,0.5)', zIndex: 100, overflow: 'hidden', animation: 'slideDownFade 0.2s ease-out' }}>
            <div style={{ padding: '16px', borderBottom: '1px solid var(--border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--surface2)' }}>
              <h3 style={{ margin: 0, fontSize: '16px', color: 'var(--text)', fontWeight: 800 }}>Notifications</h3>
              <div style={{ display: 'flex', gap: '8px' }}>
                <button onClick={markAsRead} style={{ background: 'none', border: 'none', color: 'var(--accent)', cursor: 'pointer', fontSize: '12px', display: 'flex', alignItems: 'center', gap: '4px', fontWeight: 'bold' }}>
                  <Check size={14} /> Mark Read
                </button>
              </div>
            </div>
            
            <div style={{ maxHeight: '350px', overflowY: 'auto' }}>
              {notifications.length === 0 ? (
                <div style={{ padding: '40px 16px', textAlign: 'center', color: 'var(--text-dim)', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '12px' }}>
                  <BellOff size={32} opacity={0.5} />
                  <span>No new notifications</span>
                </div>
              ) : (
                notifications.map((notif) => (
                  <div key={notif.id} style={{ padding: '16px', borderBottom: '1px solid var(--border)', background: notif.is_read ? 'var(--bg)' : 'rgba(0, 229, 160, 0.05)', display: 'flex', gap: '12px', alignItems: 'flex-start' }}>
                    <div style={{ width: '8px', height: '8px', borderRadius: '50%', background: notif.is_read ? 'transparent' : 'var(--accent)', marginTop: '6px', flexShrink: 0 }}></div>
                    <div style={{ flex: 1 }}>
                      <p style={{ margin: '0 0 6px', fontSize: '14px', color: 'var(--text)', lineHeight: 1.4 }}>{notif.message}</p>
                      <span style={{ fontSize: '11px', color: 'var(--text-dim)' }}>
                        {formatTimeAgo(notif.created_at)}
                      </span>
                    </div>
                  </div>
                ))
              )}
            </div>
            
            {notifications.length > 0 && (
              <div style={{ padding: '12px', borderTop: '1px solid var(--border)', textAlign: 'center', background: 'var(--surface2)' }}>
                <button onClick={clearAll} style={{ background: 'none', border: 'none', color: '#ef4444', cursor: 'pointer', fontSize: '13px', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '6px', width: '100%', fontWeight: 'bold' }}>
                  <Trash2 size={14} /> Clear All
                </button>
              </div>
            )}
          </div>
        </>
      )}
    </div>
  );
};

export default NotificationCenter;
