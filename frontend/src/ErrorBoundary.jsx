import React from 'react';
import { AlertTriangle, RefreshCcw } from 'lucide-react';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error("ErrorBoundary caught an error", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100vh', background: 'var(--bg)', color: 'var(--text-bright)', padding: '20px', textAlign: 'center' }}>
          <div style={{ background: 'var(--surface)', padding: '40px', borderRadius: '16px', border: '1px solid var(--border)', maxWidth: '500px', width: '100%' }}>
            <div style={{ display: 'flex', justifyContent: 'center', marginBottom: '20px', color: 'var(--accent3)' }}>
              <AlertTriangle size={64} />
            </div>
            <h1 style={{ fontFamily: 'var(--font-display)', marginBottom: '16px', fontSize: '28px' }}>Oops, something went wrong</h1>
            <p style={{ color: 'var(--text2)', marginBottom: '32px', lineHeight: '1.6' }}>
              We've encountered an unexpected error. This has been logged and we're looking into it. Please try refreshing the page or going back to the dashboard.
            </p>
            <div style={{ display: 'flex', gap: '16px', justifyContent: 'center' }}>
              <button 
                onClick={() => window.location.href = '/'}
                style={{ padding: '12px 24px', background: 'var(--surface2)', color: 'var(--text-bright)', border: '1px solid var(--border)', borderRadius: '8px', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '8px', fontWeight: 'bold', transition: 'all 0.2s' }}
              >
                Go Home
              </button>
              <button 
                onClick={() => window.location.reload()}
                style={{ padding: '12px 24px', background: 'linear-gradient(135deg, var(--accent), var(--accent2))', color: 'white', border: 'none', borderRadius: '8px', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '8px', fontWeight: 'bold', transition: 'all 0.2s', boxShadow: '0 4px 15px rgba(0,229,160,0.3)' }}
              >
                <RefreshCcw size={16} /> Reload Page
              </button>
            </div>
          </div>
        </div>
      );
    }

    return this.props.children; 
  }
}

export default ErrorBoundary;
