import React, { memo } from 'react';
import { Lightbulb } from 'lucide-react';
import DOMPurify from 'dompurify';
import { marked } from 'marked';
import LessonDiscussion from '../LessonDiscussion';

const LessonViewer = ({
  lesson,
  mobileTab,
  activeTab,
  setActiveTab,
  isTranslating,
  translatedTheory,
  translatedInstructions,
  determineLanguage,
  showHint,
  sendChat,
  setMobileTab,
}) => {
  return (
    <div className={`ws-exercise ${mobileTab === 'exercise' ? 'mobile-active' : ''}`}>
      <div className="exercise-tabs">
        <div className={`ex-tab ${activeTab === 'theory' ? 'active' : ''}`} onClick={() => setActiveTab('theory')}>Theory</div>
        <div className={`ex-tab ${activeTab === 'instructions' ? 'active' : ''}`} onClick={() => setActiveTab('instructions')}>Instructions</div>
        <div className={`ex-tab ${activeTab === 'solution' ? 'active' : ''}`} onClick={() => setActiveTab('solution')}>Solution</div>
      </div>
      <div className="ex-tab-content">
        <div className="exercise-title">{lesson.title}</div>
        <div className="exercise-body" dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(marked(
          activeTab === 'theory' ? (isTranslating ? "*(Translating into your preferred language...)*" : (translatedTheory || "No theory provided.")) : 
          activeTab === 'instructions' ? (isTranslating ? "*(Translating into your preferred language...)*" : (translatedInstructions || "No instructions provided.")) : 
          `### Solution Code\n\n\`\`\`${determineLanguage()}\n` + (lesson.solution || 'No solution provided.') + '\n```'
        )) }}></div>
        
        {showHint && lesson.hint && activeTab !== 'solution' && (
          <div style={{ marginTop: '20px', padding: '16px', background: 'rgba(245, 158, 11, 0.1)', borderLeft: '4px solid #f59e0b', borderRadius: '4px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: '#f59e0b', fontWeight: 'bold', marginBottom: '8px' }}>
              <Lightbulb size={18} /> Hint
            </div>
            <div style={{ color: 'var(--text)' }}>{lesson.hint}</div>
          </div>
        )}
        
        {(activeTab === 'theory' || activeTab === 'solution') && (
          <button 
            onClick={() => {
              sendChat(null, `Please give me a detailed technical explanation of this lesson: "${lesson.title}". Explain the concepts and how the code works step-by-step.`);
              if(window.innerWidth <= 768) setMobileTab('chat');
            }}
            style={{ 
              marginTop: '20px', padding: '10px 16px', background: 'var(--surface)', 
              color: 'var(--accent)', border: '1px solid var(--border)', 
              borderRadius: '8px', cursor: 'pointer', fontWeight: 'bold',
              display: 'flex', alignItems: 'center', gap: '8px'
            }}
          >
            Get Detail Explanation
          </button>
        )}
        
        <LessonDiscussion lessonName={lesson.title} />
      </div>
    </div>
  );
};

export default memo(LessonViewer);
