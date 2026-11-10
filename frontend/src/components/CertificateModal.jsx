import React, { useEffect, useRef, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';
import { Trophy, Download, Share2, X, Crown, CheckCircle2 } from 'lucide-react';

const CertificateModal = ({ courseName, studentName, onClose }) => {
  const canvasRef = useRef(null);
  const navigate = useNavigate();
  const { user, subscription } = useAuth();
  const isPro = subscription?.is_pro;
  const [imageLoaded, setImageLoaded] = useState(false);
  const [copiedLink, setCopiedLink] = useState(false);

  // Clean and format course name automatically
  const formatCourseName = (raw) => {
    if (!raw) return 'Technology Certification';
    let str = raw;
    try {
      str = decodeURIComponent(raw);
    } catch (e) {}
    if (str.includes('_') || (str.includes('-') && !str.includes(' - '))) {
      return str.replace(/[-_]/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
    }
    return str.trim();
  };

  // Derive the student's full name from sign-up data
  const displayName = (studentName || user?.full_name || user?.email?.split('@')?.[0] || 'Digital Era Student').trim();
  const displayCourse = formatCourseName(courseName);

  // Deterministic certificate number based on student and course
  const getCertNumber = (name, course) => {
    let hash = 0;
    const str = `${name}-${course}-digital-era-cac-9882413`;
    for (let i = 0; i < str.length; i++) {
      hash = ((hash << 5) - hash) + str.charCodeAt(i);
      hash |= 0;
    }
    const positiveHash = Math.abs(hash).toString().padStart(5, '0').slice(0, 5);
    const year = new Date().getFullYear();
    return `DE-${year}-9882413-${positiveHash}`;
  };

  const certNumber = getCertNumber(displayName, displayCourse);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const W = 2246;
    const H = 1588;

    canvas.width = W;
    canvas.height = H;

    // Load the official Digital Era certificate template
    const img = new Image();
    img.crossOrigin = 'anonymous';
    img.src = '/certificate-template.png';

    const renderTextOnTemplate = () => {
      // 1. Draw student name (Center X: 1122, line Y: 720, text baseline centered around Y: 650)
      ctx.fillStyle = '#0f2b5c'; // Official Digital Era Deep Navy
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';

      let nameFontSize = 74;
      ctx.font = `bold ${nameFontSize}px "Cinzel", "Times New Roman", "Playfair Display", Georgia, serif`;
      while (ctx.measureText(displayName).width > 1050 && nameFontSize > 34) {
        nameFontSize -= 3;
        ctx.font = `bold ${nameFontSize}px "Cinzel", "Times New Roman", "Playfair Display", Georgia, serif`;
      }
      ctx.fillText(displayName, 1122, 650);

      // 2. Draw course name (Center X: 1122, line Y: 886, text baseline centered around Y: 830)
      ctx.fillStyle = '#1c3d94'; // Deep Royal Blue
      let courseFontSize = 52;
      ctx.font = `bold ${courseFontSize}px "Segoe UI", Arial, sans-serif`;
      while (ctx.measureText(displayCourse).width > 1050 && courseFontSize > 28) {
        courseFontSize -= 3;
        ctx.font = `bold ${courseFontSize}px "Segoe UI", Arial, sans-serif`;
      }
      ctx.fillText(displayCourse, 1122, 830);

      // 3. Draw Date (Center X: 480, line Y: 1414, text baseline centered around Y: 1375)
      const dateStr = new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
      ctx.fillStyle = '#1e293b'; // Charcoal
      ctx.font = '600 36px "Segoe UI", Arial, sans-serif';
      ctx.fillText(dateStr, 480, 1375);

      // 4. Draw Footer: Cert Number + CAC Reg No + Website (Center X: 1060, Y: 1495)
      ctx.fillStyle = '#475569'; // Slate
      ctx.font = '500 28px "Segoe UI", Arial, sans-serif';
      const footerText = `Certificate No. ${certNumber}   ·   CAC Reg. No. 9882413   ·   digital-era.live`;
      ctx.fillText(footerText, 1060, 1495);

      setImageLoaded(true);
    };

    img.onload = () => {
      ctx.drawImage(img, 0, 0, W, H);
      renderTextOnTemplate();
    };

    img.onerror = () => {
      // Fallback in case template image takes time to load: draw clean canvas
      ctx.fillStyle = '#F7FAFF';
      ctx.fillRect(0, 0, W, H);

      ctx.strokeStyle = '#0f2b5c';
      ctx.lineWidth = 8;
      ctx.strokeRect(60, 60, W - 120, H - 120);

      ctx.fillStyle = '#0f2b5c';
      ctx.font = 'bold 50px "Segoe UI", sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('DIGITAL ERA TECH TRAINING & HUB', W / 2, 200);

      ctx.font = 'bold 80px "Times New Roman", serif';
      ctx.fillText('CERTIFICATE OF COMPLETION', W / 2, 340);

      renderTextOnTemplate();
    };
  }, [displayName, displayCourse, certNumber]);

  const downloadCertificate = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const link = document.createElement('a');
    const safeStudent = displayName.replace(/[^a-zA-Z0-9]/g, '_');
    const safeCourse = displayCourse.replace(/[^a-zA-Z0-9]/g, '_');
    link.download = `Digital_Era_Certificate_${safeStudent}_${safeCourse}.png`;
    link.href = canvas.toDataURL('image/png', 1.0);
    link.click();
  };

  const copyVerifyLink = () => {
    const url = `https://digital-era.live/verify?cert=${encodeURIComponent(certNumber)}`;
    navigator.clipboard.writeText(url);
    setCopiedLink(true);
    setTimeout(() => setCopiedLink(false), 3000);
  };

  const shareToLinkedIn = () => {
    const url = encodeURIComponent('https://digital-era.live');
    window.open(`https://www.linkedin.com/sharing/share-offsite/?url=${url}`, '_blank');
  };

  const shareToTwitter = () => {
    const url = encodeURIComponent('https://digital-era.live');
    const text = encodeURIComponent(`I just completed ${displayCourse} at Digital Era Tech Training & Hub! Check out my accredited certificate:`);
    window.open(`https://twitter.com/intent/tweet?url=${url}&text=${text}`, '_blank');
  };

  const shareToWhatsApp = () => {
    const url = encodeURIComponent('https://digital-era.live');
    const text = encodeURIComponent(`I just completed ${displayCourse} at Digital Era Tech Training & Hub (CAC Reg. No. 9882413)! Check it out: ${url}`);
    window.open(`https://api.whatsapp.com/send?text=${text}`, '_blank');
  };

  return (
    <div style={{
      position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, 
      backgroundColor: 'rgba(5, 10, 20, 0.88)', display: 'flex', 
      justifyContent: 'center', alignItems: 'center', zIndex: 9999,
      backdropFilter: 'blur(12px)', padding: '20px', overflowY: 'auto'
    }}>
      <div style={{
        background: '#0d131f', padding: '32px', borderRadius: '20px',
        border: '1px solid #1e293b', display: 'flex', flexDirection: 'column', alignItems: 'center',
        boxShadow: '0 25px 70px rgba(0,0,0,0.7)', maxWidth: '920px', width: '100%', maxHeight: '95vh', overflowY: 'auto'
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', width: '100%', marginBottom: '16px' }}>
          <h2 style={{ color: 'var(--accent, #00e5a0)', margin: 0, display: 'flex', alignItems: 'center', gap: '10px', fontSize: '22px' }}>
            <Trophy size={26} color="var(--accent, #00e5a0)" /> Official Certificate of Completion
          </h2>
          <button 
            onClick={onClose} 
            style={{ background: 'transparent', border: 'none', color: '#94a3b8', cursor: 'pointer', padding: '4px' }}
            aria-label="Close"
          >
            <X size={24} />
          </button>
        </div>

        <p style={{ color: '#94a3b8', margin: '0 0 20px 0', fontSize: '14px', textAlign: 'center', width: '100%' }}>
          Accredited by <strong>Digital Era Tech Training & Hub</strong> (CAC Reg. No. 9882413). Issued to <strong>{displayName}</strong>.
        </p>
        
        {/* Certificate Canvas Preview */}
        <div style={{ width: '100%', display: 'flex', justifyContent: 'center', position: 'relative', background: '#070b14', borderRadius: '12px', padding: '12px', border: '1px solid #1f2937' }}>
          <canvas 
            ref={canvasRef} 
            width={2246} 
            height={1588} 
            style={{ width: '100%', maxWidth: '820px', height: 'auto', borderRadius: '8px', boxShadow: '0 10px 30px rgba(0,0,0,0.6)', display: 'block' }} 
          />
        </div>
        
        {/* Actions bar */}
        <div style={{ display: 'flex', gap: '12px', marginTop: '24px', width: '100%', justifyContent: 'center', flexWrap: 'wrap' }}>
          <button 
            onClick={downloadCertificate}
            style={{ 
              padding: '12px 28px', background: 'linear-gradient(135deg, #00e5a0, #00bcd4)', 
              color: '#0d0f14', border: 'none', borderRadius: '10px', cursor: 'pointer', 
              fontWeight: 'bold', fontSize: '15px', display: 'flex', alignItems: 'center', gap: '8px',
              boxShadow: '0 4px 15px rgba(0, 229, 160, 0.3)'
            }}
          >
            <Download size={18} /> Download HD Certificate
          </button>

          <button 
            onClick={copyVerifyLink}
            style={{ padding: '12px 20px', background: 'var(--surface2, #1f2937)', color: '#e2e8f0', border: '1px solid #374151', borderRadius: '10px', cursor: 'pointer', fontWeight: '600', fontSize: '14px', display: 'flex', alignItems: 'center', gap: '6px' }}
          >
            {copiedLink ? <CheckCircle2 size={16} color="var(--accent)" /> : <Share2 size={16} />}
            {copiedLink ? 'Link Copied!' : 'Copy Verification Link'}
          </button>

          <button 
            onClick={shareToLinkedIn}
            style={{ padding: '12px 20px', background: '#0a66c2', color: '#fff', border: 'none', borderRadius: '10px', cursor: 'pointer', fontWeight: 'bold', fontSize: '14px', display: 'flex', alignItems: 'center', gap: '6px' }}
          >
            LinkedIn
          </button>

          <button 
            onClick={shareToWhatsApp}
            style={{ padding: '12px 20px', background: '#25D366', color: '#fff', border: 'none', borderRadius: '10px', cursor: 'pointer', fontWeight: 'bold', fontSize: '14px', display: 'flex', alignItems: 'center', gap: '6px' }}
          >
            WhatsApp
          </button>

          <button 
            onClick={shareToTwitter}
            style={{ padding: '12px 20px', background: '#1e293b', color: '#cbd5e1', border: '1px solid #334155', borderRadius: '10px', cursor: 'pointer', fontWeight: '600', fontSize: '14px', display: 'flex', alignItems: 'center', gap: '6px' }}
          >
            X / Twitter
          </button>

          <button 
            onClick={onClose}
            style={{ padding: '12px 24px', background: 'transparent', color: '#94a3b8', border: '1px solid #334155', borderRadius: '10px', cursor: 'pointer', fontWeight: '600', fontSize: '14px' }}
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
};

export default CertificateModal;
