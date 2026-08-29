import React from 'react';
import { useDataSaver } from '../DataSaverContext';
import { Zap, ZapOff, Wifi, TrendingDown, Info } from 'lucide-react';

/**
 * DataSaverToggle — Settings toggle for data-saving mode
 * 
 * Can be placed in Dashboard nav, Profile page, or settings area.
 * Shows what's affected so users make an informed choice.
 */
const DataSaverToggle = ({ compact = false }) => {
  const { dataSaver, setDataSaver } = useDataSaver();

  if (compact) {
    // Compact version for nav bar — just an icon toggle
    return (
      <button
        onClick={() => setDataSaver(!dataSaver)}
        title={dataSaver ? 'Data Saver ON — tap to disable' : 'Enable Data Saver to reduce data usage'}
        style={{
          padding: '8px 12px',
          background: dataSaver 
            ? 'linear-gradient(135deg, rgba(34, 197, 94, 0.15), rgba(34, 197, 94, 0.05))' 
            : 'var(--surface)',
          color: dataSaver ? '#22c55e' : 'var(--text)',
          border: dataSaver ? '1px solid rgba(34, 197, 94, 0.4)' : '1px solid var(--border)',
          borderRadius: '20px',
          cursor: 'pointer',
          display: 'flex',
          alignItems: 'center',
          gap: '6px',
          fontWeight: 'bold',
          fontSize: '13px',
          transition: 'all 0.3s ease',
        }}
      >
        {dataSaver ? <ZapOff size={16} /> : <Zap size={16} />}
        {dataSaver ? 'Saver ON' : 'Data Saver'}
      </button>
    );
  }

  // Full version with explanation — for Profile/Settings page
  return (
    <div style={{
      background: 'var(--surface)',
      border: '1px solid var(--border)',
      borderRadius: '12px',
      padding: '20px',
      marginBottom: '16px',
    }}>
      {/* Header row with toggle */}
      <div style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        marginBottom: '12px',
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <div style={{
            width: '40px', height: '40px', borderRadius: '10px',
            background: dataSaver 
              ? 'linear-gradient(135deg, #22c55e, #16a34a)' 
              : 'var(--surface2)',
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            transition: 'all 0.3s ease',
          }}>
            {dataSaver ? <ZapOff size={20} color="#fff" /> : <Zap size={20} color="var(--text2)" />}
          </div>
          <div>
            <h3 style={{ margin: 0, fontSize: '1rem', color: 'var(--text)' }}>Data Saver Mode</h3>
            <p style={{ margin: 0, fontSize: '0.8rem', color: 'var(--text2)' }}>
              Reduce data usage by up to 80%
            </p>
          </div>
        </div>

        {/* Toggle switch */}
        <button
          onClick={() => setDataSaver(!dataSaver)}
          role="switch"
          aria-checked={dataSaver}
          style={{
            width: '52px', height: '28px',
            borderRadius: '14px',
            border: 'none',
            cursor: 'pointer',
            position: 'relative',
            background: dataSaver 
              ? 'linear-gradient(135deg, #22c55e, #16a34a)' 
              : 'var(--surface2)',
            transition: 'background 0.3s ease',
            padding: 0,
          }}
        >
          <div style={{
            width: '22px', height: '22px',
            borderRadius: '50%',
            background: '#fff',
            position: 'absolute',
            top: '3px',
            left: dataSaver ? '27px' : '3px',
            transition: 'left 0.3s ease',
            boxShadow: '0 2px 4px rgba(0,0,0,0.2)',
          }} />
        </button>
      </div>

      {/* What changes */}
      {dataSaver && (
        <div style={{
          background: 'rgba(34, 197, 94, 0.05)',
          border: '1px solid rgba(34, 197, 94, 0.2)',
          borderRadius: '8px',
          padding: '12px 16px',
          fontSize: '0.8rem',
          color: 'var(--text2)',
          lineHeight: 1.6,
        }}>
          <div style={{ fontWeight: 600, color: '#22c55e', marginBottom: '6px', display: 'flex', alignItems: 'center', gap: '6px' }}>
            <TrendingDown size={14} /> Active — saving your data:
          </div>
          <ul style={{ margin: 0, paddingLeft: '18px' }}>
            <li>Python engine loads only when you click "Run"</li>
            <li>Animations and visual effects reduced</li>
            <li>Uses system fonts instead of downloading web fonts</li>
            <li>Auto-translation disabled (English only)</li>
          </ul>
          <div style={{ marginTop: '8px', display: 'flex', alignItems: 'center', gap: '4px', color: 'var(--text2)', fontSize: '0.75rem' }}>
            <Info size={12} /> Toggle off anytime to restore full experience
          </div>
        </div>
      )}
    </div>
  );
};

export default DataSaverToggle;
