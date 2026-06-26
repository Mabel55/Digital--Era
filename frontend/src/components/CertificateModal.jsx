import React, { useEffect, useRef } from 'react';

const CertificateModal = ({ courseName, studentName, onClose }) => {
  const canvasRef = useRef(null);

  useEffect(() => {
    if (!canvasRef.current) return;
    drawCertificate(courseName, studentName || 'Student', canvasRef.current);
  }, [courseName, studentName]);

  const drawCertificate = (course, student, canvas) => {
    const ctx = canvas.getContext('2d');
    const W = 620, H = 440;
    ctx.clearRect(0, 0, W, H);

    // Background
    const bgGrad = ctx.createLinearGradient(0, 0, W, H);
    bgGrad.addColorStop(0, '#0a0d15'); 
    bgGrad.addColorStop(1, '#111827');
    ctx.fillStyle = bgGrad; 
    ctx.fillRect(0, 0, W, H);

    // Border
    ctx.strokeStyle = '#00e5a0'; ctx.lineWidth = 2;
    ctx.strokeRect(16, 16, W - 32, H - 32);
    ctx.strokeStyle = 'rgba(0,229,160,0.2)'; ctx.lineWidth = 1;
    ctx.strokeRect(22, 22, W - 44, H - 44);

    // Corner decorations
    const corners = [[22,22],[W-22,22],[22,H-22],[W-22,H-22]];
    corners.forEach(([x, y]) => {
      ctx.fillStyle = '#00e5a0';
      ctx.beginPath(); ctx.arc(x, y, 5, 0, Math.PI*2); ctx.fill();
    });

    // Top accent line
    const lineGrad = ctx.createLinearGradient(50, 0, W-50, 0);
    lineGrad.addColorStop(0, 'transparent'); lineGrad.addColorStop(0.5, '#00e5a0'); lineGrad.addColorStop(1, 'transparent');
    ctx.fillStyle = lineGrad; ctx.fillRect(50, 55, W - 100, 1);

    // Academy name
    ctx.fillStyle = '#00e5a0';
    ctx.font = 'bold 13px sans-serif';
    ctx.textAlign = 'center'; 
    ctx.letterSpacing = '4px';
    ctx.fillText('DIGITAL ERA', W/2, 88);

    // Certificate of Completion
    ctx.fillStyle = 'rgba(255,255,255,0.15)';
    ctx.font = '11px sans-serif';
    ctx.fillText('CERTIFICATE OF COMPLETION', W/2, 112);

    // Decorative line
    ctx.fillStyle = lineGrad; ctx.fillRect(80, 124, W - 160, 1);

    // "This certifies that"
    ctx.fillStyle = '#6b7a99'; ctx.font = '14px sans-serif';
    ctx.fillText('This certifies that', W/2, 165);

    // Student name
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 36px sans-serif';
    ctx.fillText(student, W/2, 218);

    // Underline
    const nameWidth = ctx.measureText(student).width;
    const lineGrad2 = ctx.createLinearGradient(W/2 - nameWidth/2, 0, W/2 + nameWidth/2, 0);
    lineGrad2.addColorStop(0, 'transparent'); lineGrad2.addColorStop(0.5, '#00e5a0'); lineGrad2.addColorStop(1, 'transparent');
    ctx.fillStyle = lineGrad2; ctx.fillRect(W/2 - nameWidth/2, 226, nameWidth, 1);

    // "has successfully completed"
    ctx.fillStyle = '#6b7a99'; ctx.font = '14px sans-serif';
    ctx.fillText('has successfully completed', W/2, 258);

    // Course name
    ctx.fillStyle = '#00e5a0'; ctx.font = 'bold 22px sans-serif';
    ctx.fillText(course, W/2, 296);

    // Date
    const dateStr = new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' });
    ctx.fillStyle = '#4a5268'; ctx.font = '12px sans-serif';
    ctx.fillText(`Issued on ${dateStr}`, W/2, 328);

    // Bottom strip
    const botGrad = ctx.createLinearGradient(0, H-50, 0, H-30);
    botGrad.addColorStop(0, 'transparent'); botGrad.addColorStop(1, 'rgba(0,229,160,0.06)');
    ctx.fillStyle = botGrad; ctx.fillRect(0, H-50, W, 50);

    // XP badge
    ctx.fillStyle = 'rgba(0,229,160,0.1)'; ctx.strokeStyle = 'rgba(0,229,160,0.3)'; ctx.lineWidth = 1;
    roundRect(ctx, W/2 - 60, H - 55, 120, 28, 14);
    ctx.fill(); ctx.stroke();
    ctx.fillStyle = '#00e5a0'; ctx.font = 'bold 12px sans-serif';
    ctx.fillText(`⚡ +500 XP Awarded`, W/2, H - 36);

    // --- INSTRUCTOR SIGNATURE BLOCK ---
    ctx.textAlign = 'right';

    ctx.fillStyle = '#ffffff'; 
    ctx.font = 'italic 20px serif';
    ctx.fillText('Arua Mabel Chinasa', W - 50, H - 85);

    ctx.strokeStyle = 'rgba(0, 229, 160, 0.5)';
    ctx.lineWidth = 1;
    ctx.beginPath(); 
    ctx.moveTo(W - 240, H - 75);
    ctx.lineTo(W - 50, H - 75);
    ctx.stroke();

    ctx.fillStyle = '#6b7a99'; 
    ctx.font = '12px sans-serif';
    ctx.fillText('Lead AI & Backend Engineer', W - 50, H - 60);

    ctx.textAlign = 'center';
  };

  const roundRect = (ctx, x, y, w, h, r) => {
    ctx.beginPath(); ctx.moveTo(x+r, y);
    ctx.lineTo(x+w-r, y); ctx.quadraticCurveTo(x+w, y, x+w, y+r);
    ctx.lineTo(x+w, y+h-r); ctx.quadraticCurveTo(x+w, y+h, x+w-r, y+h);
    ctx.lineTo(x+r, y+h); ctx.quadraticCurveTo(x, y+h, x, y+h-r);
    ctx.lineTo(x, y+r); ctx.quadraticCurveTo(x, y, x+r, y);
    ctx.closePath();
  };

  const downloadCertificate = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const link = document.createElement('a');
    link.download = `Digital_Era_Certificate_${(studentName||'Student').replace(/ /g, '_')}.png`;
    link.href = canvas.toDataURL('image/png');
    link.click();
  };

  return (
    <div style={{
      position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, 
      backgroundColor: 'rgba(0,0,0,0.85)', display: 'flex', 
      justifyContent: 'center', alignItems: 'center', zIndex: 9999,
      backdropFilter: 'blur(10px)'
    }}>
      <div style={{
        background: '#0a0d15', padding: '30px', borderRadius: '16px',
        border: '1px solid #1e293b', display: 'flex', flexDirection: 'column', alignItems: 'center',
        boxShadow: '0 20px 50px rgba(0,0,0,0.5)'
      }}>
        <h2 style={{ color: '#00e5a0', marginTop: 0, marginBottom: '10px' }}>🏆 Certificate Earned!</h2>
        <p style={{ color: '#94a3b8', marginBottom: '20px' }}>You've successfully completed {courseName}. Download your certificate below.</p>
        
        <canvas 
          ref={canvasRef} 
          width={620} 
          height={440} 
          style={{ width: '100%', maxWidth: '620px', height: 'auto', borderRadius: '8px', boxShadow: '0 0 20px rgba(0,229,160,0.1)' }} 
        />
        
        <div style={{ display: 'flex', gap: '15px', marginTop: '25px', width: '100%', justifyContent: 'center' }}>
          <button 
            onClick={onClose}
            style={{ padding: '12px 24px', background: 'transparent', color: '#e2e8f0', border: '1px solid #334155', borderRadius: '8px', cursor: 'pointer', fontWeight: 'bold' }}
          >
            Close
          </button>
          <button 
            onClick={downloadCertificate}
            style={{ padding: '12px 24px', background: '#00e5a0', color: '#000', border: 'none', borderRadius: '8px', cursor: 'pointer', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '8px' }}
          >
            ⬇ Download Certificate
          </button>
        </div>
      </div>
    </div>
  );
};

export default CertificateModal;
