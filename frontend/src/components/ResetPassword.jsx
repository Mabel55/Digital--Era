import React, { useState } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import { GraduationCap, ArrowRight, CheckCircle2 } from 'lucide-react';

export default function ResetPassword() {
  const [searchParams] = useSearchParams();
  const token = searchParams.get('token');
  const navigate = useNavigate();
  
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    
    if (!token) {
      setError('Invalid or missing reset token. Please request a new link.');
      return;
    }
    
    if (password !== confirmPassword) {
      setError('Passwords do not match.');
      return;
    }
    
    if (password.length < 6) {
      setError('Password must be at least 6 characters long.');
      return;
    }
    
    setLoading(true);
    try {
      const res = await fetch('/users/reset-password-with-token', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ token, new_password: password })
      });
      
      const data = await res.json();
      
      if (res.ok) {
        setSuccess(true);
        setTimeout(() => {
          navigate('/onboarding');
        }, 3000);
      } else {
        setError(data.detail || 'Failed to reset password. The link may have expired.');
      }
    } catch (err) {
      setError('An error occurred. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div id="onboarding" className="screen active">
      <div className="onboard-card" style={{ width: '400px', padding: '40px' }}>
        <div className="logo-row" style={{ justifyContent: 'center', marginBottom: '24px' }}>
          <div className="logo-icon"><GraduationCap size={24} /></div>
          <div className="logo-text">Digital <span>Era</span></div>
        </div>

        {success ? (
          <div style={{ textAlign: 'center' }}>
            <CheckCircle2 size={48} color="var(--accent)" style={{ margin: '0 auto 16px' }} />
            <h2 className="onboard-title" style={{ fontSize: '22px' }}>Password Reset!</h2>
            <p className="onboard-sub">Your password has been successfully updated. Redirecting you to login...</p>
            <button 
              onClick={() => navigate('/onboarding')} 
              className="btn-primary"
              style={{ marginTop: '16px' }}
            >
              Go to Login <ArrowRight size={16} style={{ marginLeft: '8px' }} />
            </button>
          </div>
        ) : (
          <>
            <h2 className="onboard-title" style={{ textAlign: 'center', fontSize: '22px' }}>Reset Password</h2>
            <p className="onboard-sub" style={{ textAlign: 'center' }}>Enter your new password below.</p>
            
            <form onSubmit={handleSubmit}>
              <div className="field-row">
                <label className="field-label">New Password</label>
                <input 
                  type="password" 
                  value={password} 
                  onChange={(e) => setPassword(e.target.value)} 
                  required 
                  placeholder="At least 6 characters"
                />
              </div>
              <div className="field-row">
                <label className="field-label">Confirm Password</label>
                <input 
                  type="password" 
                  value={confirmPassword} 
                  onChange={(e) => setConfirmPassword(e.target.value)} 
                  required 
                  placeholder="Re-enter your new password"
                />
              </div>
              
              {error && <div style={{ color: 'var(--danger)', fontSize: '13px', marginBottom: '16px', textAlign: 'center' }}>{error}</div>}
              
              <button type="submit" className="btn-primary" disabled={loading}>
                {loading ? 'Updating...' : 'Set New Password'}
              </button>
            </form>
          </>
        )}
      </div>
    </div>
  );
}
