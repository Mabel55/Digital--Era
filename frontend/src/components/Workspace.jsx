import React, { useState, useEffect, useRef, useCallback } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';
import { useDataSaver } from '../DataSaverContext';
import { useTranslation } from 'react-i18next';
import Editor from '@monaco-editor/react';
import { marked } from 'marked';
import DOMPurify from 'dompurify';
import { useCurriculum } from '../hooks/useCurriculum';
import LessonDiscussion from './LessonDiscussion';
import { queueProgressUpdate, saveCode as saveCodeToDB, loadCode as loadCodeFromDB, saveCachedProgress, getCachedProgress } from '../lib/offlineDB';
import { useOfflineSync } from '../hooks/useOfflineSync';
import { hasAccess, hasLessonAccess } from '../utils/access';
import { ArrowLeft, Play, Terminal, CheckCircle2, XCircle, Bug, Bot, ArrowUp, PartyPopper, Home, RotateCcw, Menu, Lightbulb, RotateCcw as ResetIcon, Clock, ChevronRight, WifiOff, CloudOff, RefreshCw, Code, Sparkles, Lock, Crown, Trophy } from 'lucide-react';
import GitHubExportModal from './GitHubExportModal';
import CertificateModal from './CertificateModal';
import AIChatSidebar from './workspace/AIChatSidebar';
import CodeEditorArea from './workspace/CodeEditorArea';
import LessonViewer from './workspace/LessonViewer';

const Workspace = () => {
  const { courseId } = useParams();
  const navigate = useNavigate();
  const { token, user, subscription, refreshUser } = useAuth();
  const { dataSaver } = useDataSaver();
  const { i18n } = useTranslation();
  const courseName = decodeURIComponent(courseId);
  const { data: curriculumData, isLoading: curriculumLoading } = useCurriculum();
  const manifest = curriculumData?.courseManifest?.[courseName];

  const [currentLessonIdx, setCurrentLessonIdx] = useState(0);
  const [translatedTheory, setTranslatedTheory] = useState('');
  const [translatedInstructions, setTranslatedInstructions] = useState('');
  const [isTranslating, setIsTranslating] = useState(false);
  const [activeTab, setActiveTab] = useState('theory');
  const [code, setCode] = useState('');
  const [showGithubModal, setShowGithubModal] = useState(false);
  const [terminalOutput, setTerminalOutput] = useState('');
  const [terminalClass, setTerminalClass] = useState('');
  const [isRunning, setIsRunning] = useState(false);
  const [messages, setMessages] = useState([]);
  const [chatInput, setChatInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const [hasError, setHasError] = useState(false);
  const [lastFailedMsg, setLastFailedMsg] = useState(null);
  const [selectedOption, setSelectedOption] = useState(null);
  const [quizResult, setQuizResult] = useState(null);
  const [showCelebration, setShowCelebration] = useState(false);
  const [showCertModal, setShowCertModal] = useState(false);
  const [showStory, setShowStory] = useState(true); // Story Mode State
  const [showHint, setShowHint] = useState(false);
  const [pyodide, setPyodide] = useState(null);
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const [persona, setPersona] = useState('study_buddy');
  const [mobileTab, setMobileTab] = useState('exercise'); // 'exercise', 'editor', 'chat' for mobile
  const [executionTime, setExecutionTime] = useState(0);
  const [outputTab, setOutputTab] = useState('terminal'); // 'terminal' | 'preview'
  
  // AI Limits State
  const [aiUsage, setAiUsage] = useState({ remaining: -1, limit: -1, isLimited: false });
  const isPro = subscription?.is_pro;
  
  const chatEndRef = useRef(null);
  const editorRef = useRef(null);

  // Derive level and track from manifest if available
  const courseLevel = manifest ? manifest.level || 'Beginner' : 'Beginner';
  const courseTrack = manifest ? manifest.track || 'General' : 'General';
  const hasCourseAccess = hasAccess(courseLevel, courseTrack, courseName, subscription);

  useEffect(() => {
    const fetchTranslations = async () => {
      const lesson = manifest?.lessons?.[currentLessonIdx];
      if (!lesson) return;
      
      const lang = i18n.language || 'en';
      // ★ Data Saver: skip translation API calls to save data
      if (lang === 'en' || lang.startsWith('en') || dataSaver) {
        setTranslatedTheory(lesson.theory);
        setTranslatedInstructions(lesson.instructions);
        return;
      }

      setIsTranslating(true);
      try {
        const token = localStorage.getItem('token');
        const headers = { 'Content-Type': 'application/json' };
        if (token) headers['Authorization'] = `Bearer ${token}`;
        
        // Translate Theory
        const theoryRes = await fetch('/translate', {
          method: 'POST',
          headers,
          body: JSON.stringify({ text: lesson.theory || '', target_language: lang })
        });
        const theoryData = await theoryRes.json();
        setTranslatedTheory(theoryData.translated_text || lesson.theory);

        // Translate Instructions
        const instRes = await fetch('/translate', {
          method: 'POST',
          headers,
          body: JSON.stringify({ text: lesson.instructions || '', target_language: lang })
        });
        const instData = await instRes.json();
        setTranslatedInstructions(instData.translated_text || lesson.instructions);
        
      } catch (err) {
        console.error("Translation error", err);
        setTranslatedTheory(lesson.theory);
        setTranslatedInstructions(lesson.instructions);
      } finally {
        setIsTranslating(false);
      }
    };

    fetchTranslations();
  }, [currentLessonIdx, i18n.language, manifest, dataSaver]);

  // ★ Pyodide loader — extracted so it can be called on-demand in data saver mode
  const loadPyodideRuntime = useCallback(async () => {
    if (pyodide) return pyodide; // Already loaded
    
    return new Promise((resolve, reject) => {
      if (document.getElementById('pyodide-script') && window.loadPyodide) {
        // Script already added, just initialize
        window.loadPyodide({
          indexURL: "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/"
        }).then(instance => {
          instance.runPython(`import sys\nimport io\nsys.stdout = io.StringIO()`);
          setPyodide(instance);
          resolve(instance);
        }).catch(reject);
        return;
      }

      const script = document.createElement('script');
      script.src = 'https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js';
      script.id = 'pyodide-script';
      script.async = true;
      document.body.appendChild(script);
      
      script.onload = async () => {
        try {
          const pyodideInstance = await window.loadPyodide({
            indexURL: "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/"
          });
          pyodideInstance.runPython(`
            import sys
            import io
            sys.stdout = io.StringIO()
          `);
          setPyodide(pyodideInstance);
          console.log("Pyodide loaded successfully.");
          resolve(pyodideInstance);
        } catch (e) {
          console.error("Pyodide load failed", e);
          reject(e);
        }
      };
      script.onerror = reject;
    });
  }, [pyodide]);

  const determineLanguage = useCallback(() => {
    const c = courseName.toLowerCase();

    // 1. Explicit HTML courses & keywords
    if (c.includes('html') || c.includes('markup') || c.includes('web accessibility')) return 'html';

    // 2. CSS courses & keywords
    if (c.includes('css') || c.includes('tailwind') || c.includes('flexbox') || c.includes('grid &') || c.includes('styling')) return 'css';

    // 3. SQL & Database courses
    if (c.includes('sql') || c.includes('database') || c.includes('selects') || c.includes('filtering data') || 
        c.includes('basic joins') || c.includes('aggregations') || c.includes('subqueries') || 
        c.includes('indexing') || c.includes('transactions')) return 'sql';

    // 4. JavaScript & Frontend frameworks
    if (c.includes('javascript') || c.includes('react') || c.includes('vue') || c.includes('next.js') || 
        c.includes('typescript') || c.includes('node') || c.includes('express') || c.includes('frontend') || 
        c.startsWith('js ') || c.includes('js basics') || c.includes('web animations') || 
        c.includes('frontend testing') || c.includes('state management') || c.includes('hooks masterclass')) return 'javascript';

    // 5. C programming
    if (c.includes('c syntax') || c.includes('pointers') || c.includes('strings in c') || 
        c.includes('structs & unions') || c.includes('dynamic memory') || c.includes('c programming')) return 'c';

    // 6. Go programming
    if (c.startsWith('go ') || c.includes('goroutines') || c.includes('golang')) return 'go';

    // 7. Rust
    if (c.includes('rust')) return 'rust';

    // 8. Track-level fallback from curriculum manifest
    if (curriculumData?.curriculum) {
      for (const [track, tiers] of Object.entries(curriculumData.curriculum)) {
        for (const courses of Object.values(tiers)) {
          if (Array.isArray(courses) && courses.includes(courseName)) {
            if (track === 'Frontend') {
              if (c.includes('html')) return 'html';
              if (c.includes('css')) return 'css';
              return 'javascript';
            }
            if (track === 'SQL & Databases') return 'sql';
            if (track === 'C Programming') return 'c';
            if (track === 'Cloud Native & Go') return 'go';
            if (track === 'Systems Programming') return 'rust';
          }
        }
      }
    }

    // 9. Inspect lesson code heuristic
    const currentLesson = manifest?.lessons?.[currentLessonIdx];
    const sample = (currentLesson?.solution || currentLesson?.starterCode || code || '').trim().toLowerCase();
    if (sample.startsWith('<!doctype') || sample.startsWith('<html') || (sample.startsWith('<') && sample.includes('</'))) {
      return 'html';
    }
    if (sample.includes('{') && (sample.includes('color:') || sample.includes('padding:') || sample.includes('margin:') || sample.includes('border:'))) {
      return 'css';
    }
    if (sample.includes('select ') || sample.includes('create table') || sample.includes('insert into')) {
      return 'sql';
    }

    return 'python'; // Default
  }, [courseName, curriculumData, manifest, currentLessonIdx, code]);

  useEffect(() => {
    // ★ Data Saver: defer Pyodide loading until user clicks "Run Code"
    // Normal mode: only preload if this course actually uses Python
    if (!dataSaver && determineLanguage() === 'python') {
      loadPyodideRuntime();
    }
  }, [dataSaver, loadPyodideRuntime, determineLanguage]);

  const hasLoadedLessonRef = useRef(false);

  useEffect(() => {
    hasLoadedLessonRef.current = false;
  }, [courseName]);

  useEffect(() => {
    if (!manifest || manifest.lessons.length === 0) return;

    // Check localStorage first for instant synchronous resume
    const localSaved = localStorage.getItem(`de_last_lesson_${courseName}`);
    const localIdx = localSaved !== null ? parseInt(localSaved, 10) : 0;
    
    // Server progress from user profile
    const serverProgress = user?.progress?.[courseName]?.completed_lessons;
    
    // Determine the highest known completed/saved lesson
    let targetIdx = localIdx;
    if (typeof serverProgress === 'number' && serverProgress > targetIdx) {
      targetIdx = serverProgress;
    }
    
    targetIdx = Math.min(Math.max(0, targetIdx), manifest.lessons.length - 1);

    if (!hasLoadedLessonRef.current) {
      hasLoadedLessonRef.current = true;
      loadLesson(targetIdx);

      // Also check IndexedDB cache asynchronously as fallback
      getCachedProgress(courseName).then(cached => {
        if (cached && typeof cached.completedLessons === 'number' && cached.completedLessons > targetIdx) {
          const cachedIdx = Math.min(cached.completedLessons, manifest.lessons.length - 1);
          loadLesson(cachedIdx);
        }
      }).catch(() => {});
    } else if (typeof serverProgress === 'number' && serverProgress > currentLessonIdx) {
      // If user profile finishes loading with higher progress than current lesson, jump forward
      loadLesson(Math.min(serverProgress, manifest.lessons.length - 1));
    }
    
    setMessages([
      { sender: 'ai', text: `Hi ${user?.full_name?.split(' ')?.[0] || 'there'}! I'm your AI Tutor for **${courseName}**. Ask me anything!` }
    ]);
  }, [courseName, manifest, user?.progress]);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isTyping]);

  useEffect(() => {
    // Fetch initial AI usage limits for free users
    if (token && !isPro) {
      fetch('/ai-usage', { headers: { 'Authorization': `Bearer ${token}` } })
        .then(res => res.json())
        .then(data => {
          if (data.is_limited) {
            setAiUsage({
              remaining: Math.max(0, data.daily_limit - data.messages_used),
              limit: data.daily_limit,
              isLimited: true
            });
          }
        })
        .catch(e => console.error("Failed to fetch AI usage:", e));
    }
  }, [token, isPro]);

  const getStorageKey = (idx) => `workspace_${courseName}_${idx}`;

  const loadLesson = (idx) => {
    setCurrentLessonIdx(idx);
    try {
      localStorage.setItem(`de_last_lesson_${courseName}`, idx.toString());
    } catch (e) {}
    const lesson = manifest.lessons[idx];
    
    // Load from localStorage if exists, otherwise starter code
    const savedCode = localStorage.getItem(getStorageKey(idx));
    setCode(savedCode || lesson.starterCode || '');
    
    setTerminalOutput('');
    setActiveTab('theory');
    setSelectedOption(null);
    setQuizResult(null);
    setShowHint(false);
    setShowStory(true); // Always start in story mode for a new lesson
    setIsSidebarOpen(false); // Close sidebar on navigate
    setOutputTab('terminal');
  };

  const handleCodeChange = (value) => {
    setCode(value);
    localStorage.setItem(getStorageKey(currentLessonIdx), value);
  };

  const handleResetCode = () => {
    if (window.confirm("Are you sure you want to reset your code to the starting state?")) {
      const lesson = manifest.lessons[currentLessonIdx];
      setCode(lesson.starterCode || '');
      localStorage.removeItem(getStorageKey(currentLessonIdx));
    }
  };

  const handleGetHint = () => {
    const lesson = manifest.lessons[currentLessonIdx];
    if (lesson.hint && !showHint) {
      setShowHint(true);
      if (activeTab === 'theory') setActiveTab('instructions');
    } else {
      sendChat(null, "I need more help with this lesson. Can you give me another hint?");
      if(window.innerWidth <= 768) setMobileTab('chat');
    }
  };

  const triggerProgressUpdate = async () => {
    // ★ OFFLINE-FIRST: Always save progress locally first, then try server
    try {
      localStorage.setItem(`de_last_lesson_${courseName}`, (currentLessonIdx + 1).toString());
      await queueProgressUpdate(courseName, currentLessonIdx, 10);
      await saveCachedProgress(courseName, currentLessonIdx + 1);
    } catch (dbErr) {
      console.warn('[Offline] IndexedDB save failed:', dbErr);
    }

    const token = localStorage.getItem('token');
    if (token && navigator.onLine) {
        try {
            const isLastLesson = manifest?.lessons && currentLessonIdx >= manifest.lessons.length - 1;
            const progressRes = await fetch('/users/me/progress', {
                method: 'POST',
                headers: { 
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}` 
                },
                body: JSON.stringify({ 
                course_name: courseName, 
                lesson_index: currentLessonIdx,
                total_lessons: manifest?.lessons?.length || 1,
                is_completed: isLastLesson
                })
            });
            
            if (progressRes.ok) {
                const userData = await progressRes.json();
                if (userData && userData.level) {
                    setTerminalOutput(prev => prev + `\n\nLesson Passed! +10 XP Awarded! You are now level: ${userData.level}`);
                }
                if (isLastLesson && refreshUser) refreshUser();
            }
        } catch (e) {
            // Server unreachable — progress is safely queued in IndexedDB
            console.log('[Offline] Server unreachable, progress saved locally.');
            setTerminalOutput(prev => prev + `\n\nLesson Passed! Progress saved locally — will sync when you're back online.`);
        }
    } else if (!navigator.onLine) {
        // Fully offline — inform user their progress is safe
        setTerminalOutput(prev => prev + `\n\nLesson Passed! You're offline — progress saved locally and will sync automatically.`);
    }
  };

  const handleRunCode = async () => {
    setIsRunning(true);
    setTerminalOutput('Executing...');
    setTerminalClass('');
    setHasError(false);
    
    const lang = determineLanguage();
    const lesson = manifest.lessons[currentLessonIdx];
    let fullCode = code;
    if (lesson.testCode) {
      if (lang === 'sql') {
        fullCode = code + "\n" + lesson.testCode;
      } else {
        fullCode = code + "\n\n" + lesson.testCode;
      }
    }
    
    const startTime = performance.now();

    try {
      // 1. HTML CLIENT-SIDE
      if (lang === 'html') {
        if (code.includes('___')) {
          setTerminalOutput('⚠️ Please replace all blanks (___) with the correct HTML tags and content before running.');
          setTerminalClass('error');
          setHasError(true);
          setOutputTab('terminal');
          setIsRunning(false);
          setExecutionTime(Math.round(performance.now() - startTime));
          return;
        }

        if (!code.trim()) {
          setTerminalOutput('⚠️ Code is empty. Write your HTML code to continue.');
          setTerminalClass('error');
          setHasError(true);
          setOutputTab('terminal');
          setIsRunning(false);
          setExecutionTime(Math.round(performance.now() - startTime));
          return;
        }

        const parser = new DOMParser();
        const doc = parser.parseFromString(fullCode, 'text/html');
        const elements = Array.from(doc.body.querySelectorAll('*'));

        // Check if key expected elements from the solution/instructions are present
        const sol = (lesson.solution || '').toLowerCase();
        let missingTag = null;
        if (sol.includes('<h1') && !doc.querySelector('h1')) missingTag = '<h1>';
        else if (sol.includes('<h2') && !doc.querySelector('h2')) missingTag = '<h2>';
        else if (sol.includes('<p') && !doc.querySelector('p')) missingTag = '<p>';
        else if (sol.includes('<ul') && !doc.querySelector('ul')) missingTag = '<ul>';
        else if (sol.includes('<ol') && !doc.querySelector('ol')) missingTag = '<ol>';
        else if (sol.includes('<li') && !doc.querySelector('li')) missingTag = '<li>';
        else if (sol.includes('<a ') && !doc.querySelector('a')) missingTag = '<a>';
        else if (sol.includes('<img') && !doc.querySelector('img')) missingTag = '<img>';
        else if (sol.includes('<form') && !doc.querySelector('form')) missingTag = '<form>';
        else if (sol.includes('<input') && !doc.querySelector('input')) missingTag = '<input>';

        if (missingTag) {
          setTerminalOutput(`⚠️ Almost there! Your code is missing the ${missingTag} tag required by this lesson. Check the instructions and try again.`);
          setTerminalClass('error');
          setHasError(true);
          setOutputTab('terminal');
          setIsRunning(false);
          setExecutionTime(Math.round(performance.now() - startTime));
          return;
        }

        const tagList = Array.from(new Set(elements.map(el => `<${el.tagName.toLowerCase()}>`))).join(', ');
        setTerminalOutput(`✓ HTML rendered successfully!\n\nElements detected: ${tagList || 'Text content'}\nPage preview loaded in Browser Preview tab.\nAutomatic Tests Passed! +10 XP Awarded!`);
        setTerminalClass('success');
        setHasError(false);
        setOutputTab('preview');
        triggerProgressUpdate();
        setIsRunning(false);
        setExecutionTime(Math.round(performance.now() - startTime));
        return;
      }

      // 2. CSS CLIENT-SIDE
      if (lang === 'css') {
        if (code.includes('___')) {
          setTerminalOutput('⚠️ Please replace all blanks (___) with the correct CSS selectors or properties before running.');
          setTerminalClass('error');
          setHasError(true);
          setOutputTab('terminal');
          setIsRunning(false);
          setExecutionTime(Math.round(performance.now() - startTime));
          return;
        }

        if (!code.trim()) {
          setTerminalOutput('⚠️ Code is empty. Write your CSS rules to continue.');
          setTerminalClass('error');
          setHasError(true);
          setOutputTab('terminal');
          setIsRunning(false);
          setExecutionTime(Math.round(performance.now() - startTime));
          return;
        }

        const openBraces = (fullCode.match(/\{/g) || []).length;
        const closeBraces = (fullCode.match(/\}/g) || []).length;
        if (openBraces !== closeBraces || openBraces === 0) {
          setTerminalOutput('⚠️ CSS Syntax Error: Mismatched curly braces { }. Make sure every rule opens with { and closes with }.');
          setTerminalClass('error');
          setHasError(true);
          setOutputTab('terminal');
          setIsRunning(false);
          setExecutionTime(Math.round(performance.now() - startTime));
          return;
        }

        setTerminalOutput(`✓ CSS compiled successfully!\nStyles applied to preview elements.\nAutomatic Tests Passed! +10 XP Awarded!`);
        setTerminalClass('success');
        setHasError(false);
        setOutputTab('preview');
        triggerProgressUpdate();
        setIsRunning(false);
        setExecutionTime(Math.round(performance.now() - startTime));
        return;
      }

      // 3. PYTHON CLIENT-SIDE (PYODIDE)
      if (lang === 'python') {
        // ★ Data Saver: load Pyodide on first run if not yet loaded
        let pyodideInstance = pyodide;
        if (!pyodideInstance) {
          setTerminalOutput('⚡ Loading Python engine (first run)...');
          try {
            pyodideInstance = await loadPyodideRuntime();
          } catch (loadErr) {
            // Fall through to server-side execution
            console.warn('Pyodide load failed, falling back to server:', loadErr);
          }
        }

        if (pyodideInstance) {
          try {
            pyodideInstance.runPython("sys.stdout = io.StringIO()");
            pyodideInstance.runPython(fullCode);
            const stdout = pyodideInstance.runPython("sys.stdout.getvalue()");
            setTerminalOutput(stdout || "No output.");
            setTerminalClass('success');
            triggerProgressUpdate();
          } catch (err) {
            setTerminalOutput(err.toString());
            setTerminalClass('error');
            setHasError(true);
          }
          setIsRunning(false);
          return;
        }
      }
      
      // 2. JAVASCRIPT CLIENT-SIDE
      if (lang === 'javascript') {
        try {
            // Run JS in a sandboxed iframe to prevent access to parent page
            const result = await new Promise((resolve, reject) => {
              const iframe = document.createElement('iframe');
              iframe.sandbox = 'allow-scripts';
              iframe.style.display = 'none';
              document.body.appendChild(iframe);

              const timeout = setTimeout(() => {
                document.body.removeChild(iframe);
                reject(new Error('Execution timed out (5s limit)'));
              }, 5000);

              window.addEventListener('message', function handler(e) {
                if (e.source === iframe.contentWindow) {
                  clearTimeout(timeout);
                  window.removeEventListener('message', handler);
                  document.body.removeChild(iframe);
                  if (e.data.error) reject(new Error(e.data.error));
                  else resolve(e.data.logs || 'No output.');
                }
              });

              const sandboxedCode = `
                <script>
                  try {
                    const __logs = [];
                    const console = { log: (...a) => __logs.push(a.join(' ')), error: (...a) => __logs.push('Error: ' + a.join(' ')), warn: (...a) => __logs.push('Warning: ' + a.join(' ')) };
                    ${fullCode}
                    parent.postMessage({ logs: __logs.join('\\n') }, '*');
                  } catch(e) {
                    parent.postMessage({ error: e.toString() }, '*');
                  }
                <\/script>
              `;
              iframe.srcdoc = sandboxedCode;
            });
            setTerminalOutput(result || "No output.");
            setTerminalClass('success');
            triggerProgressUpdate();
        } catch (err) {
            setTerminalOutput(err.toString());
            setTerminalClass('error');
            setHasError(true);
        }
        setIsRunning(false);
        return;
      }

      // 3. FALLBACK TO BACKEND DOCKER (C, SQL, Go, etc.)
      const res = await fetch('/run-code/', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code: fullCode, language: lang })
      });
      const data = await res.json();
      
      if (!res.ok) {
        setTerminalOutput(`Error: ${data.detail}`);
        setTerminalClass('error');
        setHasError(true);
      } else {
        setTerminalOutput(data.output || "No output.");
        const codeHasError = data.output.toLowerCase().includes('error') || data.exit_code !== 0 || data.output.toLowerCase().includes('traceback');
        setTerminalClass(codeHasError ? 'error' : 'success');
        setHasError(codeHasError);
        
        if (!codeHasError) {
          triggerProgressUpdate();
        }
      }
    } catch (err) {
      setTerminalOutput("Execution failed. Ensure backend/Docker is running.");
      setTerminalClass('error');
      setHasError(true);
    } finally {
      setIsRunning(false);
      setExecutionTime(Math.round(performance.now() - startTime));
    }
  };

  const handleFixMyCode = () => {
    const prompt = `I am getting an error. Can you find the bug in my code **without giving me the full solution**? Tell me what line it is on, and give me a hint.\n\nHere is my code:\n\`\`\`${determineLanguage()}\n${code}\n\`\`\`\n\nError output:\n\`\`\`\n${terminalOutput}\n\`\`\``;
    sendChat(null, prompt);
  };

  const handleAIReview = () => {
    const prompt = `Please review my code and give me feedback on best practices, optimizations, and any potential issues:\n\n\`\`\`${determineLanguage()}\n${code}\n\`\`\``;
    sendChat(null, prompt);
    if(window.innerWidth <= 768) setMobileTab('chat');
  };

  const handleQuizSubmit = async () => {
    const lesson = manifest.lessons[currentLessonIdx];
    if (selectedOption === lesson.correctAnswer) {
      setQuizResult('correct');
      const token = localStorage.getItem('token');
      if (token) {
        try {
          const isLastLesson = manifest?.lessons && currentLessonIdx >= manifest.lessons.length - 1;
          const progressRes = await fetch('/users/me/progress', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
            body: JSON.stringify({ 
              course_name: courseName, 
              lesson_index: currentLessonIdx,
              total_lessons: manifest?.lessons?.length || 1,
              is_completed: isLastLesson
            })
          });
          if (progressRes.ok) {
            const userData = await progressRes.json();
            setQuizResult(`correct_xp_${userData.level}`);
            if (isLastLesson && refreshUser) refreshUser();
          }
        } catch (e) { console.error(e); }
      }
    } else {
      setQuizResult('incorrect');
    }
  };

  const handleFinishCourse = async () => {
    const activeToken = token || localStorage.getItem('token');
    if (activeToken) {
      try {
        await fetch('/users/me/complete-course', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${activeToken}`
          },
          body: JSON.stringify({
            course_name: courseName,
            total_lessons: manifest?.lessons?.length || (currentLessonIdx + 1)
          })
        });
        if (refreshUser) refreshUser();
      } catch (e) {
        console.error("Failed to record course completion:", e);
      }
    }
    setShowCelebration(true);
  };

  const sendChat = async (e, directMessage = null) => {
    e?.preventDefault();
    const userMsg = directMessage || chatInput;
    if (!userMsg.trim()) return;

    const authToken = token || localStorage.getItem('token');
    if (!authToken) {
      setMessages(prev => [...prev, { sender: 'ai', text: "Please log in to use the AI tutor. Create a free account to get started!" }]);
      setIsTyping(false);
      return;
    }

    if (aiUsage.isLimited && aiUsage.remaining <= 0 && !isPro) {
      setMessages(prev => [...prev, { sender: 'ai', text: "You've used all your free AI tutor messages for today. Upgrade to Pro for unlimited access!" }]);
      return;
    }

    setMessages(prev => [...prev, { sender: 'user', text: userMsg }]);
    if (!directMessage) setChatInput('');
    setIsTyping(true);

    if (!navigator.onLine) {
      try {
        // ★ OFFLINE AI TUTOR: Fetch pre-cached FAQs
        const faqRes = await fetch('/ai-faqs.json');
        if (faqRes.ok) {
          const faqData = await faqRes.json();
          const lowerMsg = userMsg.toLowerCase();
          
          let matchedAnswer = null;
          for (const faq of faqData.faqs) {
            if (faq.keywords.some(kw => lowerMsg.includes(kw))) {
              matchedAnswer = faq.answer;
              break;
            }
          }
          
          setTimeout(() => {
            setMessages(prev => [...prev, { 
              sender: 'ai', 
              text: matchedAnswer || faqData.fallback 
            }]);
            setIsTyping(false);
          }, 600); // Fake delay for realism
          return;
        }
      } catch (e) {
        console.warn('Offline FAQ failed', e);
      }
      
      // Fallback if ai-faqs.json fails for some reason
      setTimeout(() => {
        setMessages(prev => [...prev, { 
          sender: 'ai', 
          text: "📴 You're offline right now. The AI tutor needs an internet connection for complex questions, but you can still read lessons, write code, and run Python locally!" 
        }]);
        setIsTyping(false);
      }, 500);
      return;
    }

    try {
      const currentLesson = manifest?.lessons?.[currentLessonIdx];
      let res;
      let data;
      try {
        res = await fetch(`/api/v2/ai/chat`, {
          method: 'POST',
          headers: { 
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token || localStorage.getItem('token')}` 
          },
          body: JSON.stringify({ 
            message: userMsg, 
            course: courseName, 
            persona: persona,
            lesson_id: currentLesson?.id || null
          })
        });
        
        if (res.status === 429) {
          setMessages(prev => [...prev, { sender: 'ai', text: "You've reached your daily AI limit. Please upgrade to Pro." }]);
          setAiUsage(prev => ({ ...prev, remaining: 0 }));
          return;
        }

        if (res.ok) {
          data = await res.json().catch(() => null);
        }
      } catch (v2Err) {
        console.warn("AI v2 endpoint fetch failed, falling back to legacy chat:", v2Err);
      }

      // If /api/v2/ai/chat wasn't ok or failed, try fallback to /chat
      if (!data) {
        try {
          const fallbackRes = await fetch(`/chat`, {
            method: 'POST',
            headers: { 
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${token || localStorage.getItem('token')}` 
            },
            body: JSON.stringify({ 
              message: userMsg, 
              course: courseName, 
              persona: persona,
              lesson_id: currentLesson?.id || null
            })
          });

          if (fallbackRes.status === 429) {
            setMessages(prev => [...prev, { sender: 'ai', text: "You've reached your daily AI limit. Please upgrade to Pro." }]);
            setAiUsage(prev => ({ ...prev, remaining: 0 }));
            return;
          }

          if (fallbackRes.ok) {
            data = await fallbackRes.json().catch(() => null);
          }
        } catch (fbErr) {
          console.warn("Fallback chat also failed:", fbErr);
        }
      }

      if (!data) {
        setMessages(prev => [...prev, { 
          sender: 'ai', 
          text: "Sorry, I'm having trouble connecting to my brain right now. Please try again in a moment.", 
          isError: true 
        }]);
        setLastFailedMsg(userMsg);
        return;
      }
      
      setLastFailedMsg(null);
      setMessages(prev => [...prev, { 
        sender: 'ai', 
        text: data.answer || data.response || "No response",
        thought_process: data.metadata?.thought_process
      }]);
      
      // Update remaining messages if provided
      if (data.remaining_messages !== undefined && data.daily_limit !== undefined) {
        setAiUsage({
          remaining: Math.max(0, data.remaining_messages),
          limit: data.daily_limit,
          isLimited: data.daily_limit > 0
        });
      }
    } catch (err) {
      setMessages(prev => [...prev, { sender: 'ai', text: "Sorry, I'm having trouble connecting to my brain right now. Please try again in a moment.", isError: true }]);
      setLastFailedMsg(userMsg);
    } finally {
      setIsTyping(false);
    }
  };

  if (curriculumLoading) {
    return <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', color: 'white', background: 'var(--bg)' }}>Loading Course Data...</div>;
  }

  if (!manifest) {
    return <div style={{color:'white', padding: '20px'}}>Course not found</div>;
  }

  if (!hasCourseAccess) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', height: '100vh', color: 'white', background: 'var(--bg)' }}>
        <Lock size={64} color="#ef4444" style={{ marginBottom: '20px' }} />
        <h2 style={{ marginBottom: '10px' }}>Course Locked</h2>
        <p style={{ color: 'var(--text-dim)', marginBottom: '30px' }}>You need a Pro subscription or a specific access grant to view this course.</p>
        <button onClick={() => navigate('/pricing')} style={{ padding: '12px 24px', background: 'var(--accent)', color: 'black', borderRadius: '8px', border: 'none', fontWeight: 'bold', cursor: 'pointer' }}>
          View Pricing
        </button>
      </div>
    );
  }

  const lesson = manifest.lessons[currentLessonIdx];
  const progressPct = ((currentLessonIdx + 1) / manifest.lessons.length) * 100;
  const hasCurrentLessonAccess = hasLessonAccess(currentLessonIdx, courseLevel, courseTrack, courseName, subscription);

  return (
    <div id="workspace" className="screen active" style={{ height: '100vh', display: 'flex', flexDirection: 'column' }}>
      <div className="ws-topbar">
        <div className="ws-topbar-left">
          <button 
            className="ws-back-btn" 
            onClick={() => navigate('/dashboard')} 
            style={{ display: 'flex', alignItems: 'center', gap: '6px' }}
            aria-label="Go back to Dashboard"
          >
            <ArrowLeft size={16} /> Dashboard
          </button>
          {user && ((user.role || '').toLowerCase() === 'admin' || (user.role || '').toLowerCase() === 'teacher' || (user.email || '').toLowerCase() === 'nasaadanna@gmail.com') && (
            <button 
              onClick={() => navigate('/teacher')}
              style={{ background: 'rgba(56, 189, 248, 0.15)', color: 'var(--accent)', border: '1px solid var(--accent)', padding: '6px 12px', borderRadius: '6px', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '6px', fontWeight: 'bold', fontSize: '13px' }}
              title="Open Admin Portal"
              aria-label="Open Admin Portal"
            >
              <Crown size={14} /> Admin
            </button>
          )}
          <button 
            onClick={() => setIsSidebarOpen(!isSidebarOpen)}
            style={{ background: 'transparent', border: '1px solid var(--border)', color: 'var(--text)', padding: '6px', borderRadius: '6px', cursor: 'pointer', display: 'flex', alignItems: 'center' }}
            aria-label="Toggle Lesson List"
          >
            <Menu size={16} />
          </button>
          <div className="ws-course-title">{courseName}</div>
          <div className="ws-lesson-nav" style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            Lesson {currentLessonIdx + 1} of {manifest.lessons.length}
          </div>
        </div>
        <div className="ws-topbar-right">
          {!showStory && lesson.type !== 'quiz' && hasCurrentLessonAccess && (
            <>
              <button 
                onClick={handleGetHint}
                style={{ background: 'rgba(245, 158, 11, 0.1)', color: '#f59e0b', border: '1px solid rgba(245, 158, 11, 0.3)', padding: '8px 12px', borderRadius: '8px', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '6px', fontWeight: 'bold' }}
                aria-label="Get Hint"
              >
                <Lightbulb size={16} /> Hint
              </button>
              <button 
                onClick={handleResetCode}
                style={{ background: 'transparent', color: 'var(--text-dim)', border: '1px solid var(--border)', padding: '8px 12px', borderRadius: '8px', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '6px' }}
                aria-label="Reset Code"
              >
                <ResetIcon size={16} /> Reset
              </button>
              <button 
                onClick={handleAIReview}
                style={{ background: 'rgba(0, 229, 160, 0.1)', color: 'var(--accent)', border: '1px solid var(--accent)', padding: '8px 12px', borderRadius: '8px', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '6px', fontWeight: 'bold' }}
                aria-label="AI Code Review"
              >
                <Sparkles size={16} /> AI Review
              </button>
              <button 
                className="btn-run" 
                onClick={handleRunCode} 
                disabled={isRunning} 
                style={{ display: 'flex', alignItems: 'center', gap: '6px' }}
                aria-label="Run Code"
              >
                <Play size={16} /> {isRunning ? 'Running...' : 'Run Code'}
              </button>
            </>
          )}
          {hasCurrentLessonAccess ? (
            <button className="btn-submit" onClick={() => {
              if (currentLessonIdx < manifest.lessons.length - 1) {
                loadLesson(currentLessonIdx + 1);
              } else {
                handleFinishCourse();
              }
            }}>
              {currentLessonIdx < manifest.lessons.length - 1 ? 'Next Lesson' : 'Finish Course'}
            </button>
          ) : (
            <button 
              className="btn-submit" 
              onClick={() => navigate('/pricing')}
              style={{ background: 'linear-gradient(135deg, #00e5a0, #00bcd4)', color: '#0d0f14', display: 'flex', alignItems: 'center', gap: '6px' }}
            >
              <Crown size={16} /> Unlock with Pro
            </button>
          )}
        </div>
      </div>
      
      {/* Mobile Tab Navigation */}
      {!showStory && (
        <div className="mobile-tabs" style={{ display: 'none', background: 'var(--surface)', borderBottom: '1px solid var(--border)' }}>
          {['exercise', 'editor', 'chat'].map(tab => (
            <div 
              key={tab} 
              onClick={() => setMobileTab(tab)}
              style={{ flex: 1, padding: '12px', textAlign: 'center', fontWeight: 'bold', color: mobileTab === tab ? 'var(--accent)' : 'var(--text-dim)', borderBottom: mobileTab === tab ? '2px solid var(--accent)' : 'none' }}
            >
              {tab.charAt(0).toUpperCase() + tab.slice(1)}
            </div>
          ))}
        </div>
      )}

      <div className="progress-strip">
        <div className="progress-strip-fill" style={{ width: `${progressPct}%` }}></div>
      </div>

      {/* Lesson Sidebar Overlay */}
      {isSidebarOpen && (
        <div style={{ position: 'absolute', top: '60px', bottom: 0, left: 0, width: '300px', background: 'var(--surface2)', borderRight: '1px solid var(--border)', zIndex: 100, display: 'flex', flexDirection: 'column' }}>
          <div style={{ padding: '20px', borderBottom: '1px solid var(--border)', fontWeight: 'bold', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            Course Curriculum
            <button onClick={() => setIsSidebarOpen(false)} style={{ background: 'none', border: 'none', color: 'var(--text)', cursor: 'pointer' }}><XCircle size={20}/></button>
          </div>
          <div style={{ overflowY: 'auto', flex: 1 }}>
            {manifest.lessons.map((lsn, idx) => (
              <div 
                key={idx}
                onClick={() => loadLesson(idx)}
                style={{ 
                  padding: '16px 20px', borderBottom: '1px solid var(--border)', 
                  cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '12px',
                  background: currentLessonIdx === idx ? 'rgba(0, 229, 160, 0.1)' : 'transparent',
                  borderLeft: currentLessonIdx === idx ? '3px solid var(--accent)' : '3px solid transparent'
                }}
              >
                <div style={{ background: currentLessonIdx > idx ? 'var(--accent)' : 'var(--surface)', width: '24px', height: '24px', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', color: currentLessonIdx > idx ? 'black' : 'var(--text-dim)', fontSize: '12px', fontWeight: 'bold' }}>
                  {currentLessonIdx > idx ? <CheckCircle2 size={14} /> : !hasLessonAccess(idx, courseLevel, courseTrack, courseName, subscription) ? <Lock size={12} color="#ef4444" /> : idx + 1}
                </div>
                <div style={{ flex: 1, color: currentLessonIdx === idx ? 'var(--accent)' : 'var(--text)' }}>
                  {lsn.title}
                  {!hasLessonAccess(idx, courseLevel, courseTrack, courseName, subscription) && <span style={{ fontSize: '10px', color: '#ef4444', marginLeft: '6px' }}>PRO</span>}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {!hasCurrentLessonAccess ? (
        <div className="story-mode-container" style={{ flex: 1, display: 'flex', justifyContent: 'center', alignItems: 'center', background: 'var(--bg)', padding: '40px', overflowY: 'auto' }}>
          <div className="story-card" style={{ maxWidth: '600px', width: '100%', background: 'var(--surface)', padding: '60px', borderRadius: '16px', border: '1px solid #ef4444', boxShadow: '0 20px 60px rgba(0,0,0,0.5)', textAlign: 'center' }}>
            <Lock size={64} color="#ef4444" style={{ marginBottom: '24px' }} />
            <h2 style={{ color: 'white', marginBottom: '12px' }}>Lesson {currentLessonIdx + 1} is Locked</h2>
            <p style={{ color: 'var(--text-dim)', marginBottom: '8px' }}>The first 3 lessons of every beginner course are free.</p>
            <p style={{ color: 'var(--text-dim)', marginBottom: '32px' }}>Upgrade to Pro to unlock all lessons, intermediate & advanced courses, and unlimited AI tutor access.</p>
            <button onClick={() => navigate('/pricing')} style={{ padding: '14px 28px', background: 'linear-gradient(135deg, #00e5a0, #00bcd4)', color: '#0d0f14', borderRadius: '8px', border: 'none', fontWeight: 'bold', cursor: 'pointer', fontSize: '16px', marginBottom: '16px', width: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px' }}>
              <Crown size={18} /> Upgrade to Pro
            </button>
            <button onClick={() => { if (currentLessonIdx > 0) loadLesson(currentLessonIdx - 1); }} style={{ padding: '10px 20px', background: 'transparent', color: 'var(--text-dim)', border: '1px solid var(--border)', borderRadius: '8px', cursor: 'pointer', width: '100%' }}>
              Go Back to Previous Lesson
            </button>
          </div>
        </div>
      ) : showStory ? (
        <div className="story-mode-container" style={{ flex: 1, display: 'flex', justifyContent: 'center', alignItems: 'center', background: 'var(--bg)', padding: '40px', overflowY: 'auto' }}>
          <div className="story-card" style={{ maxWidth: '800px', width: '100%', background: 'var(--surface)', padding: '60px', borderRadius: '16px', border: '1px solid var(--border)', boxShadow: '0 20px 60px rgba(0,0,0,0.5)', animation: 'slideUp 0.5s ease' }}>
            <h1 style={{ fontFamily: 'var(--font-display)', fontSize: '32px', color: 'var(--accent)', marginBottom: '24px' }}>{lesson.title}</h1>
            <div className="exercise-body story-body" dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(marked(isTranslating ? "*(Translating into your preferred language...)*" : (translatedTheory || "No theory provided."))) }} style={{ fontSize: '16px', lineHeight: '1.8', color: 'var(--text)', marginBottom: '40px' }}></div>
            <button 
              onClick={() => { setShowStory(false); if(lesson.starterCode) setCode(lesson.starterCode); }}
              className="btn-submit"
              style={{ width: '100%', padding: '16px', fontSize: '18px', display: 'flex', justifyContent: 'center', gap: '10px' }}
              aria-label="Start Practice"
            >
              <Terminal size={20} /> I'm Ready to Practice
            </button>
          </div>
        </div>
      ) : (
        <div className="ws-layout">
          {/* Left Panel - Exercise */}
          <LessonViewer 
            lesson={lesson}
            mobileTab={mobileTab}
            activeTab={activeTab}
            setActiveTab={setActiveTab}
            isTranslating={isTranslating}
            translatedTheory={translatedTheory}
            translatedInstructions={translatedInstructions}
            determineLanguage={determineLanguage}
            showHint={showHint}
            sendChat={sendChat}
            setMobileTab={setMobileTab}
          />

          {/* Middle Panel - Editor & Terminal OR Quiz */}
          <CodeEditorArea 
            lesson={lesson}
            mobileTab={mobileTab}
            determineLanguage={determineLanguage}
            editorRef={editorRef}
            code={code}
            handleCodeChange={handleCodeChange}
            hasError={hasError}
            handleFixMyCode={handleFixMyCode}
            terminalClass={terminalClass}
            terminalOutput={terminalOutput}
            executionTime={executionTime}
            selectedOption={selectedOption}
            setSelectedOption={setSelectedOption}
            handleQuizSubmit={handleQuizSubmit}
            quizResult={quizResult}
            outputTab={outputTab}
            setOutputTab={setOutputTab}
          />

          {/* Right Panel - AI Chat */}
          <AIChatSidebar 
            mobileTab={mobileTab}
            messages={messages}
            isTyping={isTyping}
            chatEndRef={chatEndRef}
            aiUsage={aiUsage}
            isPro={isPro}
            navigate={navigate}
            chatInput={chatInput}
            setChatInput={setChatInput}
            sendChat={sendChat}
            persona={persona}
            setPersona={setPersona}
            lastFailedMsg={lastFailedMsg}
          />
        </div>
      )}

      {/* Course Completion Celebration */}
      {showCelebration && (
        <div 
          className="celebration-overlay" 
          onClick={() => { setShowCelebration(false); navigate('/dashboard'); }}
          role="dialog"
          aria-modal="true"
          aria-label="Course Completed Celebration"
        >
          <div className="celebration-card" onClick={e => e.stopPropagation()}>
            <div className="celebration-emoji"><PartyPopper size={64} color="var(--accent)" /></div>
            <div className="celebration-title">Course Complete!</div>
            <div className="celebration-subtitle">
              Congratulations! You've finished <strong>{courseName}</strong>. Keep the momentum going!
            </div>
            <div className="celebration-actions">
              <button 
                className="btn-primary" 
                style={{ padding: '12px 28px', borderRadius: '100px', width: 'auto', background: 'linear-gradient(135deg, #00e5a0, #00bcd4)', color: '#0d0f14', fontWeight: 'bold' }}
                onClick={() => { setShowCelebration(false); setShowCertModal(true); }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}><Trophy size={18} /> View Certificate</div>
              </button>
              <button 
                className="btn-primary" 
                style={{ padding: '12px 28px', borderRadius: '100px', width: 'auto' }}
                onClick={() => { setShowCelebration(false); navigate('/dashboard'); }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}><Home size={18} /> Back to Dashboard</div>
              </button>
              <button 
                className="returning-btn" 
                style={{ padding: '12px 28px', borderRadius: '100px', width: 'auto' }}
                onClick={() => { setShowCelebration(false); loadLesson(0); }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}><RotateCcw size={18} /> Review Course</div>
              </button>
              <button 
                className="btn-primary" 
                style={{ padding: '12px 28px', borderRadius: '100px', width: 'auto', background: 'var(--surface2)', color: 'var(--text)', border: '1px solid var(--border)' }}
                onClick={() => { setShowCelebration(false); setShowGithubModal(true); }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}><Code size={18} /> Push to GitHub</div>
              </button>
            </div>
          </div>
        </div>
      )}

      {showCertModal && (
        <CertificateModal
          courseName={courseName}
          studentName={user?.full_name}
          onClose={() => setShowCertModal(false)}
        />
      )}

      <GitHubExportModal 
        isOpen={showGithubModal} 
        onClose={() => setShowGithubModal(false)}
        code={code}
        language={determineLanguage()}
        courseName={courseName}
      />
    </div>
  );
};

export default Workspace;
