import React, { useState, useEffect, useMemo, useCallback } from 'react';
import { 
  Question, 
  UserQuestionProgress,
  StudyMode 
} from '../types';
import { getQuestionSourceCategory } from '../utils/sourceHelper';
import { MathRenderer } from './MathRenderer';
import { TopicDrawer } from './TopicDrawer';
import { ScratchpadModal } from './ScratchpadModal';
import { GuidanceModal } from './GuidanceModal';
import { 
  ArrowLeft,
  ChevronDown,
  ChevronLeft,
  ChevronRight,
  Clock,
  Edit3,
  MessageSquare,
  Sun,
  Moon,
  Settings,
  Star,
  Copy,
  MoreHorizontal,
  Play,
  Tag,
  Eye,
  BookOpen,
  FileText,
  CheckCircle2,
  XCircle,
  RotateCcw,
  Sparkles,
  HelpCircle,
  Award,
  AlertCircle,
  Home
} from 'lucide-react';
import confetti from 'canvas-confetti';

interface QuestionWorkbenchProps {
  questions: Question[];
  progress: Record<string, UserQuestionProgress>;
  onAnswerQuestion: (questionId: string, answer: string | string[], isCorrect: boolean) => void;
  onToggleFavorite: (questionId: string) => void;
  onToggleMastered: (questionId: string) => void;
  onSaveNote: (questionId: string, note: string) => void;
  initialQuestionId?: string;
  initialChapter?: string;
  initialSubTopic?: string;
  forcedSource?: string;
  isDark?: boolean;
  onToggleTheme?: () => void;
  onSelectMode?: (mode: StudyMode) => void;
  onBackToHome?: () => void;
}

export const QuestionWorkbench: React.FC<QuestionWorkbenchProps> = ({
  questions,
  progress,
  onAnswerQuestion,
  onToggleFavorite,
  onToggleMastered,
  onSaveNote,
  initialQuestionId,
  initialChapter,
  initialSubTopic,
  forcedSource,
  isDark = true,
  onToggleTheme,
  onSelectMode,
  onBackToHome
}) => {
  // Drawer state for Two-Level Menu (Image 2)
  const [isDrawerOpen, setIsDrawerOpen] = useState<boolean>(false);

  // Topic filters
  const [selectedChapter, setSelectedChapter] = useState<string>(initialChapter || 'ALL');
  const [selectedSubTopic, setSelectedSubTopic] = useState<string>(initialSubTopic || 'ALL');
  const [selectedSource, setSelectedSource] = useState<string>(forcedSource || 'ALL');

  // Update topic filter if props change
  useEffect(() => {
    if (initialChapter) setSelectedChapter(initialChapter);
    if (initialSubTopic) setSelectedSubTopic(initialSubTopic);
  }, [initialChapter, initialSubTopic]);

  // Modals state
  const [isScratchpadOpen, setIsScratchpadOpen] = useState<boolean>(false);
  const [isGuidanceOpen, setIsGuidanceOpen] = useState<boolean>(false);
  const [isSettingsOpen, setIsSettingsOpen] = useState<boolean>(false);
  const [isQuestionPickerOpen, setIsQuestionPickerOpen] = useState<boolean>(false);

  // Question interaction displays
  const [showAnswer, setShowAnswer] = useState<boolean>(false);
  const [showAnalysis, setShowAnalysis] = useState<boolean>(false);
  const [showNote, setShowNote] = useState<boolean>(false);
  const [showKnowledgePoints, setShowKnowledgePoints] = useState<boolean>(false);
  const [copyToast, setCopyToast] = useState<boolean>(false);

  // Stopwatch timer
  const [timerSeconds, setTimerSeconds] = useState<number>(0);
  const [timerActive, setTimerActive] = useState<boolean>(true);

  // Stopwatch tick
  useEffect(() => {
    let t: any = null;
    if (timerActive) {
      t = setInterval(() => {
        setTimerSeconds(s => s + 1);
      }, 1000);
    }
    return () => clearInterval(t);
  }, [timerActive]);

  const formatTimer = (sec: number) => {
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  // Filtered Questions Pool
  const filteredQuestions = useMemo(() => {
    return questions.filter(q => {
      // 1. Source filter
      if (selectedSource !== 'ALL' && getQuestionSourceCategory(q.source) !== selectedSource) {
        return false;
      }
      // 2. Chapter filter
      if (selectedChapter !== 'ALL' && q.chapter !== selectedChapter) {
        return false;
      }
      // 3. Sub-Topic / Section filter
      if (selectedSubTopic !== 'ALL') {
        const subName = q.section || (q.tags && q.tags[0]) || (
          q.type === 'single' ? '单选题型' :
          q.type === 'multiple' ? '多选题型' :
          q.type === 'judgment' ? '判断题型' : '综合大题'
        );
        if (subName !== selectedSubTopic) return false;
      }
      return true;
    });
  }, [questions, selectedSource, selectedChapter, selectedSubTopic]);

  // Current Question Index
  const [currentIndex, setCurrentIndex] = useState<number>(0);

  // Sync initial question
  useEffect(() => {
    if (initialQuestionId) {
      const idx = filteredQuestions.findIndex(q => q.id === initialQuestionId);
      if (idx !== -1) setCurrentIndex(idx);
    }
  }, [initialQuestionId, filteredQuestions]);

  // Bound index safely
  useEffect(() => {
    if (currentIndex >= filteredQuestions.length) {
      setCurrentIndex(Math.max(0, filteredQuestions.length - 1));
    }
  }, [filteredQuestions.length, currentIndex]);

  const currentQ = filteredQuestions[currentIndex] || null;
  const currentProgress = currentQ ? progress[currentQ.id] : undefined;

  // Local selection state for option answering
  const [selectedOptions, setSelectedOptions] = useState<string[]>([]);
  const [noteText, setNoteText] = useState<string>('');

  // Sync state when question changes
  useEffect(() => {
    if (currentQ) {
      setNoteText(currentProgress?.note || '');
      // If already answered, show analysis/answer automatically
      if (currentProgress?.answered) {
        setShowAnswer(true);
      } else {
        setShowAnswer(false);
        setShowAnalysis(false);
      }
      if (currentProgress?.selectedAnswer) {
        setSelectedOptions(
          Array.isArray(currentProgress.selectedAnswer)
            ? currentProgress.selectedAnswer
            : [currentProgress.selectedAnswer]
        );
      } else {
        setSelectedOptions([]);
      }
    }
  }, [currentQ?.id, currentProgress]);

  // Handle select option
  const handleSelectOption = (key: string) => {
    if (!currentQ) return;
    if (currentQ.type === 'multiple') {
      const updated = selectedOptions.includes(key)
        ? selectedOptions.filter(k => k !== key)
        : [...selectedOptions, key].sort();
      setSelectedOptions(updated);
    } else {
      setSelectedOptions([key]);
      // For single or judgment, verify immediately
      const correctAnswers = Array.isArray(currentQ.answer) 
        ? currentQ.answer.map(a => a.toUpperCase())
        : [String(currentQ.answer).toUpperCase()];
      const isCorrect = correctAnswers.includes(key.toUpperCase());
      onAnswerQuestion(currentQ.id, key, isCorrect);
      setShowAnswer(true);
      if (isCorrect) {
        confetti({ particleCount: 40, spread: 60, origin: { y: 0.8 } });
      }
    }
  };

  // Submit multiple choice
  const handleSubmitMultiple = () => {
    if (!currentQ || selectedOptions.length === 0) return;
    const correctAnswers = Array.isArray(currentQ.answer) 
      ? currentQ.answer.map(a => a.toUpperCase()).sort()
      : [String(currentQ.answer).toUpperCase()];
    const userSorted = [...selectedOptions].map(a => a.toUpperCase()).sort();
    const isCorrect = JSON.stringify(userSorted) === JSON.stringify(correctAnswers);
    onAnswerQuestion(currentQ.id, userSorted, isCorrect);
    setShowAnswer(true);
    if (isCorrect) {
      confetti({ particleCount: 50, spread: 70, origin: { y: 0.8 } });
    }
  };

  // Navigation handlers
  const handlePrev = useCallback(() => {
    if (currentIndex > 0) {
      setCurrentIndex(i => i - 1);
    }
  }, [currentIndex]);

  const handleNext = useCallback(() => {
    if (currentIndex < filteredQuestions.length - 1) {
      setCurrentIndex(i => i + 1);
    }
  }, [currentIndex, filteredQuestions.length]);

  // Bottom action: 掌握
  const handleMarkMastered = () => {
    if (!currentQ) return;
    onToggleMastered(currentQ.id);
    onAnswerQuestion(currentQ.id, selectedOptions.length > 0 ? selectedOptions[0] : (Array.isArray(currentQ.answer) ? currentQ.answer[0] : currentQ.answer), true);
    setShowAnswer(true);
    confetti({ particleCount: 50, spread: 80, origin: { y: 0.7 } });
  };

  // Bottom action: 不会 (加入错题本)
  const handleMarkWrong = () => {
    if (!currentQ) return;
    onAnswerQuestion(currentQ.id, selectedOptions.length > 0 ? selectedOptions[0] : '', false);
    setShowAnswer(true);
    setShowAnalysis(true);
  };

  // Bottom action: 不熟练 (标记收藏)
  const handleMarkUnskilled = () => {
    if (!currentQ) return;
    onToggleFavorite(currentQ.id);
  };

  // Copy LaTeX
  const handleCopyLatex = () => {
    if (!currentQ) return;
    const optText = currentQ.options 
      ? currentQ.options.map(o => `${o.key}. ${o.text}`).join('\n') 
      : '';
    const fullText = `### [${getQuestionSourceCategory(currentQ.source)} · ${currentQ.chapter}]\n${currentQ.stem}\n\n${optText}\n\n【答案】：${Array.isArray(currentQ.answer) ? currentQ.answer.join('') : currentQ.answer}\n\n【解析】：\n${currentQ.analysis}`;
    
    navigator.clipboard.writeText(fullText).then(() => {
      setCopyToast(true);
      setTimeout(() => setCopyToast(false), 2000);
    });
  };

  // Reset current question
  const handleResetCurrent = () => {
    if (!currentQ) return;
    setSelectedOptions([]);
    setShowAnswer(false);
    setShowAnalysis(false);
  };

  // Title for top left dropdown pill
  const activeTopicTitle = useMemo(() => {
    if (selectedSubTopic !== 'ALL') return selectedSubTopic;
    if (selectedChapter !== 'ALL') return selectedChapter;
    if (selectedSource !== 'ALL') return selectedSource;
    return '信号与系统 · 全部题型';
  }, [selectedSubTopic, selectedChapter, selectedSource]);

  // Keyboard Shortcuts Listener
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      const target = e.target as HTMLElement;
      if (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA') return;

      const key = e.key.toUpperCase();

      if (['1', 'A'].includes(key)) {
        e.preventDefault();
        handleSelectOption(currentQ?.type === 'judgment' ? 'T' : 'A');
      } else if (['2', 'B'].includes(key)) {
        e.preventDefault();
        handleSelectOption(currentQ?.type === 'judgment' ? 'F' : 'B');
      } else if (['3', 'C'].includes(key) && currentQ?.options && currentQ.options.length >= 3) {
        e.preventDefault();
        handleSelectOption('C');
      } else if (['4', 'D'].includes(key) && currentQ?.options && currentQ.options.length >= 4) {
        e.preventDefault();
        handleSelectOption('D');
      } else if (e.key === 'j' || e.key === 'J' || e.key === 'ArrowLeft') {
        e.preventDefault();
        handlePrev();
      } else if (e.key === 'k' || e.key === 'K' || e.key === 'ArrowRight') {
        e.preventDefault();
        handleNext();
      } else if (e.code === 'Space') {
        e.preventDefault();
        setShowAnalysis(s => !s);
      } else if (e.key === 's' || e.key === 'S') {
        e.preventDefault();
        if (currentQ) onToggleFavorite(currentQ.id);
      } else if (e.key === 'm' || e.key === 'M') {
        e.preventDefault();
        handleMarkMastered();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [currentQ, handlePrev, handleNext, onToggleFavorite]);

  return (
    <div className="relative min-h-[calc(100vh-4rem)] flex flex-col justify-between bg-white dark:bg-[#0e131f] text-slate-800 dark:text-slate-100 transition-colors duration-200 select-text">
      
      {/* 1. TOP HEADER (Exact Layout from Image 1) */}
      <header className="sticky top-0 z-30 w-full bg-white/95 dark:bg-[#0e131f]/95 backdrop-blur-md border-b border-slate-200 dark:border-slate-800/80 px-4 sm:px-8 h-14 flex items-center justify-between transition-colors">
        
        {/* Left: Back button (Returns to Home Dashboard) + Current Topic Dropdown Button (Triggers Image 2 Drawer) */}
        <div className="flex items-center gap-2 sm:gap-3">
          <button
            onClick={() => {
              if (onBackToHome) {
                onBackToHome();
              } else if (onSelectMode) {
                onSelectMode('home');
              }
            }}
            className="p-2 rounded-xl text-slate-500 hover:text-slate-900 dark:text-slate-400 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800/80 transition-colors"
            title="返回主页大厅"
          >
            <ArrowLeft className="w-4 h-4" />
          </button>

          {/* Current Category Pill (Click to open Level 2 menu) */}
          <button
            onClick={() => setIsDrawerOpen(true)}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs sm:text-sm font-bold text-slate-800 dark:text-slate-100 bg-slate-100/80 dark:bg-slate-850/90 border border-slate-200 dark:border-slate-700/80 hover:border-blue-500 dark:hover:border-blue-500 transition-all max-w-[220px] sm:max-w-md truncate shadow-sm group"
            title="点击切换题型考点二级菜单"
          >
            <span className="truncate">{activeTopicTitle}</span>
            <ChevronDown className="w-3.5 h-3.5 text-slate-400 group-hover:text-blue-500 shrink-0 transition-transform group-hover:translate-y-0.5" />
          </button>
        </div>

        {/* Right: Timer, Scratchpad, Tutoring, Theme Toggle & Settings */}
        <div className="flex items-center gap-2 sm:gap-3 text-xs">
          
          {/* Stopwatch Timer */}
          <button
            onClick={() => setTimerActive(a => !a)}
            className="flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800/80 transition-colors font-mono font-medium"
            title="点击暂停 / 继续计时"
          >
            <Clock className={`w-3.5 h-3.5 ${timerActive ? 'text-blue-500 animate-spin' : 'text-slate-400'}`} style={{ animationDuration: '6s' }} />
            <span>{formatTimer(timerSeconds)}</span>
          </button>

          {/* 草稿 (Draft Paper) */}
          <button
            onClick={() => setIsScratchpadOpen(true)}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-slate-600 dark:text-slate-300 hover:text-blue-600 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800/80 transition-colors font-medium"
            title="打开草稿纸进行手绘演算"
          >
            <Edit3 className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">草稿</span>
          </button>

          {/* 辅导 (Tutoring & Guidance) */}
          <button
            onClick={() => setIsGuidanceOpen(true)}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-slate-600 dark:text-slate-300 hover:text-purple-600 dark:hover:text-purple-400 hover:bg-slate-100 dark:hover:bg-slate-800/80 transition-colors font-medium"
            title="考点提示、公式速查与解题辅导"
          >
            <MessageSquare className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">辅导</span>
          </button>

          {/* 黑暗 / 光明两种模式切换 (Requested Light & Dark Theme Toggle) */}
          {onToggleTheme && (
            <button
              onClick={onToggleTheme}
              className="p-2 rounded-xl text-slate-500 hover:text-amber-500 dark:text-slate-400 dark:hover:text-amber-400 hover:bg-slate-100 dark:hover:bg-slate-800/80 transition-colors"
              title={isDark ? "切换为白天光明模式" : "切换为夜晚黑暗模式"}
            >
              {isDark ? <Sun className="w-4 h-4 text-amber-400" /> : <Moon className="w-4 h-4 text-slate-700" />}
            </button>
          )}

          {/* Settings / Mode Switch Popover */}
          <div className="relative">
            <button
              onClick={() => setIsSettingsOpen(s => !s)}
              className="p-2 rounded-xl text-slate-500 hover:text-slate-900 dark:text-slate-400 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800/80 transition-colors"
              title="设置与导航模式"
            >
              <Settings className="w-4 h-4" />
            </button>

            {isSettingsOpen && (
              <div className="absolute right-0 mt-2 w-48 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl shadow-xl py-2 z-50 text-xs animate-fadeIn">
                <div className="px-3 py-1.5 text-[11px] font-bold text-slate-400 uppercase tracking-wider">
                  功能导航
                </div>
                <button
                  onClick={() => { 
                    setIsSettingsOpen(false);
                    if (onBackToHome) onBackToHome();
                    else if (onSelectMode) onSelectMode('home');
                  }}
                  className="w-full text-left px-4 py-2 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-800 dark:text-slate-200 flex items-center gap-2 font-medium"
                >
                  <Home className="w-3.5 h-3.5 text-blue-500" />
                  <span>返回主页大厅</span>
                </button>
                {onSelectMode && (
                  <>
                    <button
                      onClick={() => { onSelectMode('exam'); setIsSettingsOpen(false); }}
                      className="w-full text-left px-4 py-2 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-300 flex items-center gap-2"
                    >
                      <Award className="w-3.5 h-3.5 text-indigo-500" />
                      <span>模拟机考</span>
                    </button>
                    <button
                      onClick={() => { onSelectMode('wrong'); setIsSettingsOpen(false); }}
                      className="w-full text-left px-4 py-2 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-300 flex items-center gap-2"
                    >
                      <AlertCircle className="w-3.5 h-3.5 text-rose-500" />
                      <span>错题攻坚本</span>
                    </button>
                    <button
                      onClick={() => { onSelectMode('manage'); setIsSettingsOpen(false); }}
                      className="w-full text-left px-4 py-2 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-300 flex items-center gap-2"
                    >
                      <Sparkles className="w-3.5 h-3.5 text-emerald-500" />
                      <span>题库管理中心</span>
                    </button>
                  </>
                )}
                <div className="border-t border-slate-100 dark:border-slate-800 my-1" />
                <button
                  onClick={() => { handleResetCurrent(); setIsSettingsOpen(false); }}
                  className="w-full text-left px-4 py-2 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-300 flex items-center gap-2"
                >
                  <RotateCcw className="w-3.5 h-3.5 text-slate-400" />
                  <span>重做当前题目</span>
                </button>
              </div>
            )}
          </div>

        </div>

      </header>

      {/* 2. FLOATING EDGE NAVIGATION ARROWS (Left & Right margins as in Image 1) */}
      <button
        onClick={handlePrev}
        disabled={currentIndex === 0}
        className="fixed left-3 sm:left-6 top-1/2 -translate-y-1/2 z-20 w-10 h-10 rounded-full bg-white/90 dark:bg-slate-850/90 border border-slate-200 dark:border-slate-700/80 shadow-md flex items-center justify-center text-slate-600 dark:text-slate-300 hover:text-blue-600 dark:hover:text-white hover:scale-110 active:scale-95 disabled:opacity-20 disabled:cursor-not-allowed transition-all"
        title="上一题 (J 或 ←)"
      >
        <ChevronLeft className="w-5 h-5" />
      </button>

      <button
        onClick={handleNext}
        disabled={currentIndex === filteredQuestions.length - 1}
        className="fixed right-3 sm:right-6 top-1/2 -translate-y-1/2 z-20 w-10 h-10 rounded-full bg-white/90 dark:bg-slate-850/90 border border-slate-200 dark:border-slate-700/80 shadow-md flex items-center justify-center text-slate-600 dark:text-slate-300 hover:text-blue-600 dark:hover:text-white hover:scale-110 active:scale-95 disabled:opacity-20 disabled:cursor-not-allowed transition-all"
        title="下一题 (K 或 →)"
      >
        <ChevronRight className="w-5 h-5" />
      </button>

      {/* 3. MAIN WORKBENCH CANVAS (Exact Minimalist Layout from Image 1) */}
      <main className="flex-1 w-full max-w-4xl mx-auto px-6 sm:px-12 py-8 space-y-6">
        
        {currentQ ? (
          <div className="space-y-6 animate-fadeIn">
            
            {/* Context Line 1: Question Number Jumper Dropdown (e.g. "2 ∨") + Header Tools */}
            <div className="flex items-center justify-between pb-2">
              
              {/* Question Number Picker Dropdown ("2 ∨") */}
              <div className="relative">
                <button
                  onClick={() => setIsQuestionPickerOpen(p => !p)}
                  className="flex items-center gap-1.5 text-xl font-bold font-mono text-slate-800 dark:text-slate-100 hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
                  title="点击展开题号列表直接跳转"
                >
                  <span>{currentIndex + 1}</span>
                  <ChevronDown className="w-4 h-4 text-slate-400" />
                </button>

                {/* Question Numbers Quick Grid Popover */}
                {isQuestionPickerOpen && (
                  <div className="absolute left-0 mt-2 w-72 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl shadow-2xl p-4 z-40 max-h-72 overflow-y-auto animate-fadeIn">
                    <div className="text-xs font-bold text-slate-500 mb-2.5 flex items-center justify-between">
                      <span>跳转指定题号</span>
                      <span className="font-mono">共 {filteredQuestions.length} 题</span>
                    </div>
                    <div className="grid grid-cols-5 gap-2">
                      {filteredQuestions.map((q, idx) => {
                        const p = progress[q.id];
                        const isCur = idx === currentIndex;
                        return (
                          <button
                            key={q.id}
                            onClick={() => {
                              setCurrentIndex(idx);
                              setIsQuestionPickerOpen(false);
                            }}
                            className={`h-9 rounded-xl text-xs font-mono font-bold transition-all ${
                              isCur
                                ? 'bg-blue-600 text-white shadow-sm'
                                : p?.answered
                                ? p.isCorrect
                                  ? 'bg-emerald-50 dark:bg-emerald-950/40 text-emerald-600 dark:text-emerald-400 border border-emerald-300 dark:border-emerald-800/60'
                                  : 'bg-rose-50 dark:bg-rose-950/40 text-rose-600 dark:text-rose-400 border border-rose-300 dark:border-rose-800/60'
                                : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700'
                            }`}
                          >
                            {idx + 1}
                          </button>
                        );
                      })}
                    </div>
                  </div>
                )}
              </div>

              {/* Right Tools: Star, Copy LaTeX, Note, More */}
              <div className="flex items-center gap-1 sm:gap-2 text-slate-400">
                
                {/* Star / Favorite toggle */}
                <button
                  onClick={() => onToggleFavorite(currentQ.id)}
                  className={`p-2 rounded-xl transition-all ${
                    currentProgress?.isFavorite
                      ? 'text-amber-500 bg-amber-50 dark:bg-amber-950/40'
                      : 'hover:text-amber-500 hover:bg-slate-100 dark:hover:bg-slate-800/80'
                  }`}
                  title="收藏本题 (S)"
                >
                  <Star className={`w-4 h-4 ${currentProgress?.isFavorite ? 'fill-amber-400 text-amber-400' : ''}`} />
                </button>

                {/* Copy LaTeX */}
                <button
                  onClick={handleCopyLatex}
                  className="p-2 rounded-xl hover:text-blue-500 hover:bg-slate-100 dark:hover:bg-slate-800/80 transition-colors"
                  title="复制本题 LaTeX 题面 (C)"
                >
                  <Copy className="w-4 h-4" />
                </button>

                {/* Note Toggle */}
                <button
                  onClick={() => setShowNote(n => !n)}
                  className={`p-2 rounded-xl transition-all ${
                    showNote || currentProgress?.note
                      ? 'text-cyan-600 dark:text-cyan-400 bg-cyan-50 dark:bg-cyan-950/40'
                      : 'hover:text-cyan-500 hover:bg-slate-100 dark:hover:bg-slate-800/80'
                  }`}
                  title="写专属做题笔记"
                >
                  <FileText className="w-4 h-4" />
                </button>

                {/* More */}
                <button
                  onClick={() => setShowAnalysis(a => !a)}
                  className="p-2 rounded-xl hover:text-slate-800 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800/80 transition-colors"
                  title="查看解析 (Space)"
                >
                  <MoreHorizontal className="w-4 h-4" />
                </button>
              </div>

            </div>

            {/* Copy Notification Toast */}
            {copyToast && (
              <div className="bg-emerald-600 text-white text-xs px-3 py-1.5 rounded-xl shadow-lg flex items-center gap-1.5 w-fit">
                <CheckCircle2 className="w-3.5 h-3.5" />
                <span>已复制题目 LaTeX 题面与解析至剪贴板！</span>
              </div>
            )}

            {/* Context Line 2: Tags ("▷ 1997年数三", "🏷 相关知识点") */}
            <div className="flex flex-wrap items-center gap-2.5 text-xs text-slate-500 dark:text-slate-400">
              {/* Source Tag with Play icon */}
              <span className="flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-100 dark:bg-slate-850 border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 font-medium">
                <Play className="w-3 h-3 text-blue-500 fill-blue-500" />
                <span>{getQuestionSourceCategory(currentQ.source)}</span>
              </span>

              {/* Section / Knowledge point Tag */}
              <span className="flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-100 dark:bg-slate-850 border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 font-medium">
                <Tag className="w-3 h-3 text-indigo-500" />
                <span>{currentQ.section || currentQ.chapter}</span>
              </span>

              {/* Difficulty */}
              <div className="flex items-center text-amber-400 text-xs gap-0.5 ml-1">
                {Array.from({ length: 5 }).map((_, i) => (
                  <span key={i} className={i < currentQ.difficulty ? 'text-amber-400' : 'text-slate-300 dark:text-slate-700'}>★</span>
                ))}
              </div>
            </div>

            {/* Question Stem (Large, airy, centered LaTeX typography) */}
            <div className="py-4 text-base sm:text-lg leading-relaxed text-slate-900 dark:text-slate-100 font-normal">
              <MathRenderer content={currentQ.stem} />
            </div>

            {/* Options List (for Objective Questions) */}
            {currentQ.options && currentQ.options.length > 0 && (
              <div className="space-y-3 pt-2">
                {currentQ.options.map((opt) => {
                  const isSelected = selectedOptions.includes(opt.key);
                  const isAnswered = Boolean(currentProgress?.answered);

                  const correctAnswers = Array.isArray(currentQ.answer) 
                    ? currentQ.answer.map(a => a.toUpperCase())
                    : [String(currentQ.answer).toUpperCase()];
                  const isThisCorrect = correctAnswers.includes(opt.key.toUpperCase());

                  let cardStyle = "bg-white dark:bg-slate-850/60 border-slate-200 dark:border-slate-800 hover:border-blue-500 hover:bg-slate-50 dark:hover:bg-slate-800/80 text-slate-900 dark:text-slate-100";

                  if (isAnswered) {
                    if (isThisCorrect) {
                      cardStyle = "bg-emerald-50/90 dark:bg-emerald-950/40 border-emerald-500 text-emerald-950 dark:text-emerald-100 shadow-sm";
                    } else if (isSelected && !isThisCorrect) {
                      cardStyle = "bg-rose-50/90 dark:bg-rose-950/40 border-rose-500 text-rose-950 dark:text-rose-100 shadow-sm";
                    } else {
                      cardStyle = "bg-slate-50/50 dark:bg-slate-900/40 border-slate-200 dark:border-slate-800/60 text-slate-500 dark:text-slate-400 opacity-60";
                    }
                  } else if (isSelected) {
                    cardStyle = "bg-blue-50/90 dark:bg-blue-950/40 border-blue-500 text-blue-950 dark:text-blue-100 shadow-sm";
                  }

                  return (
                    <div
                      key={opt.key}
                      onClick={() => handleSelectOption(opt.key)}
                      className={`group p-4 rounded-2xl border transition-all cursor-pointer flex items-start gap-3.5 ${cardStyle}`}
                    >
                      {/* Option Key Badge */}
                      <div className={`w-8 h-8 rounded-xl flex items-center justify-center font-bold text-sm shrink-0 transition-colors ${
                        isAnswered && isThisCorrect 
                          ? 'bg-emerald-500 text-white' 
                          : isAnswered && isSelected && !isThisCorrect 
                          ? 'bg-rose-500 text-white' 
                          : isSelected 
                          ? 'bg-blue-600 text-white' 
                          : 'bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 group-hover:bg-blue-600 group-hover:text-white'
                      }`}>
                        {opt.key}
                      </div>

                      {/* Option Text */}
                      <div className="flex-1 text-sm sm:text-base pt-0.5 leading-relaxed text-slate-900 dark:text-slate-100 font-medium">
                        <MathRenderer content={opt.text} inline />
                      </div>

                      {/* Status Icon */}
                      {isAnswered && isThisCorrect && (
                        <CheckCircle2 className="w-5 h-5 text-emerald-500 shrink-0 mt-0.5" />
                      )}
                      {isAnswered && isSelected && !isThisCorrect && (
                        <XCircle className="w-5 h-5 text-rose-500 shrink-0 mt-0.5" />
                      )}
                    </div>
                  );
                })}

                {/* Multiple choice submit */}
                {currentQ.type === 'multiple' && (
                  <div className="pt-2 flex justify-end">
                    <button
                      onClick={handleSubmitMultiple}
                      disabled={selectedOptions.length === 0}
                      className="px-6 py-2.5 rounded-xl font-bold text-xs bg-blue-600 hover:bg-blue-500 text-white disabled:opacity-40 shadow-sm"
                    >
                      提交多选答案
                    </button>
                  </div>
                )}
              </div>
            )}

            {/* Collapsible "◇ 相关知识点 1 ∨" (Matching Image 1) */}
            <div className="pt-2">
              <button
                onClick={() => setShowKnowledgePoints(k => !k)}
                className="flex items-center gap-2 text-xs font-semibold text-slate-600 dark:text-slate-400 hover:text-blue-600 dark:hover:text-blue-400 transition-colors py-2"
              >
                <span>◇ 相关知识点 ({currentQ.tags.length || 1})</span>
                <ChevronDown className={`w-3.5 h-3.5 transition-transform ${showKnowledgePoints ? 'rotate-180' : ''}`} />
              </button>

              {showKnowledgePoints && (
                <div className="mt-2 p-4 rounded-2xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-xs space-y-2 animate-fadeIn">
                  <div className="font-bold text-slate-800 dark:text-slate-200">
                    本题核心定理与考点剖析：
                  </div>
                  <div className="text-slate-600 dark:text-slate-400 leading-relaxed">
                    本题主要考察 <strong>{currentQ.chapter}</strong> 中的核心考点「{currentQ.section || currentQ.tags.join(' / ')}」。解题时注意因果性、稳定性的极点位置要求，以及时域与频域/复频域之间的转换对应定理。
                  </div>
                </div>
              )}
            </div>

            {/* Note Area (Expanded when 📝 笔记 is clicked) */}
            {showNote && (
              <div className="p-4 rounded-2xl bg-cyan-50/50 dark:bg-slate-900 border border-cyan-200 dark:border-cyan-500/30 space-y-2 animate-fadeIn">
                <div className="flex items-center justify-between text-xs font-bold text-cyan-700 dark:text-cyan-400">
                  <span className="flex items-center gap-1.5">
                    <FileText className="w-3.5 h-3.5" />
                    专属备考笔记 · 自动保存
                  </span>
                  <span className="text-[11px] text-slate-400 font-normal">随题永久云端同步</span>
                </div>
                <textarea
                  value={noteText}
                  onChange={(e) => {
                    setNoteText(e.target.value);
                    onSaveNote(currentQ.id, e.target.value);
                  }}
                  placeholder="在此记录本题解题易错点、公式推导心得或解法反思..."
                  rows={3}
                  className="w-full bg-white dark:bg-slate-950 text-slate-800 dark:text-slate-200 text-xs sm:text-sm p-3 rounded-xl border border-slate-200 dark:border-slate-800 focus:outline-none focus:border-cyan-500 resize-none leading-relaxed"
                />
              </div>
            )}

            {/* Detailed Analysis & Standard Answer Card (Expanded when 📖 解析 or 👁 答案 is clicked) */}
            {(showAnalysis || showAnswer) && (
              <div className="p-6 rounded-3xl bg-slate-50 dark:bg-slate-900/90 border border-slate-200 dark:border-slate-800 shadow-inner space-y-4 animate-fadeIn">
                <div className="flex items-center justify-between pb-3 border-b border-slate-200 dark:border-slate-800">
                  <div className="flex items-center gap-2">
                    <span className="w-2.5 h-2.5 rounded-full bg-blue-500" />
                    <span className="font-bold text-sm text-slate-800 dark:text-slate-100">
                      大观园权威详解与步骤推演
                    </span>
                  </div>
                  <div className="text-xs text-slate-500 dark:text-slate-400">
                    标准参考答案: <span className="font-mono font-bold text-emerald-600 dark:text-emerald-400 text-sm tracking-wide">{Array.isArray(currentQ.answer) ? currentQ.answer.join(', ') : currentQ.answer}</span>
                  </div>
                </div>

                <div className="text-slate-900 dark:text-slate-100 text-sm sm:text-base leading-relaxed">
                  <MathRenderer content={currentQ.analysis} />
                </div>
              </div>
            )}

          </div>
        ) : (
          <div className="py-24 text-center space-y-4">
            <div className="w-16 h-16 rounded-2xl bg-slate-100 dark:bg-slate-850 flex items-center justify-center mx-auto text-slate-400">
              <HelpCircle className="w-8 h-8" />
            </div>
            <h3 className="text-base font-bold text-slate-700 dark:text-slate-300">当前分类暂无题目</h3>
            <p className="text-xs text-slate-400 max-w-sm mx-auto">
              请点击左上角分类菜单选择其他章节考点，或重置题库筛选条件。
            </p>
            <button
              onClick={() => {
                setSelectedChapter('ALL');
                setSelectedSubTopic('ALL');
                setSelectedSource('ALL');
              }}
              className="px-4 py-2 rounded-xl text-xs font-bold bg-blue-600 text-white hover:bg-blue-500 shadow-sm transition-all"
            >
              浏览全部题目
            </button>
          </div>
        )}

      </main>

      {/* 4. BOTTOM ACTION BAR (Exact Layout from Image 1) */}
      <footer className="sticky bottom-0 z-30 w-full bg-white/95 dark:bg-[#0e131f]/95 backdrop-blur-md border-t border-slate-200 dark:border-slate-800/80 px-4 sm:px-8 py-3 flex items-center justify-between gap-4 transition-colors">
        
        {/* Left Actions: 👁 答案, 📖 解析, 📝 笔记 */}
        <div className="flex items-center gap-2 sm:gap-3 text-xs">
          <button
            onClick={() => setShowAnswer(a => !a)}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl transition-all font-semibold ${
              showAnswer
                ? 'bg-blue-50 dark:bg-blue-950/60 text-blue-600 dark:text-blue-400 border border-blue-200 dark:border-blue-500/40'
                : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800'
            }`}
          >
            <Eye className="w-3.5 h-3.5" />
            <span>答案</span>
          </button>

          <button
            onClick={() => setShowAnalysis(s => !s)}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl transition-all font-semibold ${
              showAnalysis
                ? 'bg-blue-600 text-white shadow-sm'
                : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800'
            }`}
          >
            <BookOpen className="w-3.5 h-3.5" />
            <span>解析</span>
          </button>

          <button
            onClick={() => setShowNote(n => !n)}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl transition-all font-semibold ${
              showNote
                ? 'bg-cyan-50 dark:bg-cyan-950/60 text-cyan-600 dark:text-cyan-400 border border-cyan-200 dark:border-cyan-500/40'
                : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800'
            }`}
          >
            <FileText className="w-3.5 h-3.5" />
            <span>笔记</span>
          </button>
        </div>

        {/* Right Status Actions: ⊙ 不熟练, ⊗ 不会, ✓ 掌握 */}
        <div className="flex items-center gap-2 sm:gap-3 text-xs">
          
          {/* ⊙ 不熟练 */}
          <button
            onClick={handleMarkUnskilled}
            className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl transition-all font-semibold ${
              currentProgress?.isFavorite
                ? 'bg-amber-500 text-white shadow-sm font-bold'
                : 'text-slate-600 dark:text-slate-400 hover:text-amber-500 hover:bg-amber-50 dark:hover:bg-amber-950/30 border border-slate-200 dark:border-slate-800'
            }`}
            title="标记为不熟练，后续重点重练"
          >
            <span>⊙</span>
            <span>不熟练</span>
          </button>

          {/* ⊗ 不会 */}
          <button
            onClick={handleMarkWrong}
            className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl transition-all font-semibold ${
              currentProgress && currentProgress.isCorrect === false
                ? 'bg-rose-500 text-white shadow-sm font-bold'
                : 'text-slate-600 dark:text-slate-400 hover:text-rose-500 hover:bg-rose-50 dark:hover:bg-rose-950/30 border border-slate-200 dark:border-slate-800'
            }`}
            title="完全不会，自动收录至错题攻坚本"
          >
            <span>⊗</span>
            <span>不会</span>
          </button>

          {/* ✓ 掌握 */}
          <button
            onClick={handleMarkMastered}
            className={`flex items-center gap-1.5 px-4 py-1.5 rounded-xl transition-all font-bold ${
              currentProgress?.isMastered
                ? 'bg-emerald-600 text-white shadow-sm'
                : 'bg-emerald-600/10 dark:bg-emerald-500/20 text-emerald-600 dark:text-emerald-400 hover:bg-emerald-600 hover:text-white border border-emerald-500/30'
            }`}
            title="本考点已攻破掌握 (快捷键 M)"
          >
            <span>✓</span>
            <span>掌握</span>
          </button>

        </div>

      </footer>

      {/* 5. TOPIC DRAWER (Image 2: Slide-over Two-Level Menu) */}
      <TopicDrawer
        isOpen={isDrawerOpen}
        onClose={() => setIsDrawerOpen(false)}
        questions={questions}
        progress={progress}
        selectedChapter={selectedChapter}
        selectedSubTopic={selectedSubTopic}
        selectedSource={selectedSource}
        onSelectTopic={(ch, sub, src) => {
          setSelectedChapter(ch);
          setSelectedSubTopic(sub);
          setSelectedSource(src);
          setCurrentIndex(0);
        }}
        isDark={isDark}
      />

      {/* 6. SCRATCHPAD MODAL (✏ 草稿) */}
      <ScratchpadModal
        isOpen={isScratchpadOpen}
        onClose={() => setIsScratchpadOpen(false)}
        isDark={isDark}
      />

      {/* 7. GUIDANCE MODAL (💭 辅导) */}
      <GuidanceModal
        isOpen={isGuidanceOpen}
        onClose={() => setIsGuidanceOpen(false)}
        currentQuestion={currentQ}
        isDark={isDark}
      />

    </div>
  );
};
