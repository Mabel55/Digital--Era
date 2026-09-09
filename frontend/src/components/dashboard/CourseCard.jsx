import React, { memo } from 'react';
import { Terminal, Lock } from 'lucide-react';
import { hasAccess } from '../../utils/access';
import { useNavigate } from 'react-router-dom';

const CourseCard = ({
  courseName,
  activeTab,
  currentTrack,
  subscription,
  openOverview,
  delayClass,
  totalLessons,
  completed,
}) => {
  const navigate = useNavigate();
  const progressPct = totalLessons > 0 ? (completed / totalLessons) * 100 : 0;
  const isLocked = !hasAccess(activeTab, currentTrack, courseName, subscription);

  return (
    <div 
      className={`track-card ${delayClass}`}
      onClick={() => isLocked ? navigate('/pricing') : openOverview(courseName)}
      role="button"
      tabIndex={0}
      onKeyDown={(e) => e.key === 'Enter' && (isLocked ? navigate('/pricing') : openOverview(courseName))}
      aria-label={`Course: ${courseName}`}
      style={{ opacity: isLocked ? 0.7 : 1 }}
    >
      <div className="track-card-icon">
        {isLocked ? <Lock size={32} strokeWidth={1.5} color="#ef4444" /> : <Terminal size={32} strokeWidth={1.5} />}
      </div>
      <div className="track-card-name">{courseName}</div>
      <div className="track-card-desc">
        {totalLessons} lessons • {completed} completed
      </div>
      <div className="track-card-meta">
        <span className={`track-tag tag-${activeTab.toLowerCase()}`}>{activeTab}</span>
      </div>
      <div className="track-progress-bar">
        <div className="bar-bg">
          <div className="bar-fill" style={{ width: `${progressPct}%` }}></div>
        </div>
        <div className="bar-label">{Math.round(progressPct)}% Complete</div>
      </div>
    </div>
  );
};

export default memo(CourseCard);
