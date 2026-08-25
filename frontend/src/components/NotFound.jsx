import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Helmet } from 'react-helmet-async';
import { Search, Home, ArrowLeft } from 'lucide-react';
import PublicNavbar from './PublicNavbar';

const NotFound = () => {
  const navigate = useNavigate();

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      <Helmet>
        <title>Page Not Found | Digital Era Academy</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>
      <PublicNavbar />
      
      <main style={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '40px 24px' }}>
        <div style={{ textAlign: 'center', maxWidth: '500px' }}>
          <div style={{
            width: '80px', height: '80px', borderRadius: '50%',
            background: 'rgba(239, 68, 68, 0.1)', color: 'var(--danger)',
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            margin: '0 auto 24px'
          }}>
            <Search size={40} />
          </div>
          
          <h1 style={{ fontFamily: 'var(--font-display)', fontSize: '48px', fontWeight: 800, margin: '0 0 16px 0', color: 'var(--text)' }}>
            404
          </h1>
          <h2 style={{ fontSize: '24px', fontWeight: 600, margin: '0 0 16px 0', color: 'var(--text)' }}>
            Page Not Found
          </h2>
          <p style={{ color: 'var(--text2)', fontSize: '16px', lineHeight: 1.6, marginBottom: '32px' }}>
            Oops! The page you are looking for doesn't exist, has been moved, or is temporarily unavailable.
          </p>
          
          <div style={{ display: 'flex', gap: '16px', justifyContent: 'center', flexWrap: 'wrap' }}>
            <button
              onClick={() => navigate(-1)}
              style={{
                padding: '12px 24px', background: 'transparent', color: 'var(--text)',
                border: '1px solid var(--border)', borderRadius: '12px',
                fontWeight: 600, fontSize: '15px', cursor: 'pointer',
                display: 'flex', alignItems: 'center', gap: '8px', minHeight: '44px'
              }}
            >
              <ArrowLeft size={18} /> Go Back
            </button>
            <button
              onClick={() => navigate('/')}
              style={{
                padding: '12px 24px', background: 'var(--accent)', color: '#000',
                border: 'none', borderRadius: '12px',
                fontWeight: 600, fontSize: '15px', cursor: 'pointer',
                display: 'flex', alignItems: 'center', gap: '8px', minHeight: '44px'
              }}
            >
              <Home size={18} /> Back to Home
            </button>
          </div>
        </div>
      </main>
    </div>
  );
};

export default NotFound;
