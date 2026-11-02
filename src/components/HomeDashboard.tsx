import React, { useState, useMemo } from 'react';
import { Question, UserQuestionProgress, ExamRecord, StudyMode } from '../types';
import { getQuestionSourceCategory, STANDARD_SOURCES } from '../utils/sourceHelper';
import { 
  Home, 
  Star, 
  AlertCircle, 
  Settings, 
  ChevronDown, 
  ChevronRight, 
  Search, 
  Sun, 
  Moon, 
  Play, 
  Layers, 
  CheckCircle2, 
  Award, 
  Flame, 
  BarChart3, 
  RotateCcw, 
  TrendingUp,
  BookOpen,
  Sparkles,
  ArrowRight,
  Menu,
  X
} from 'lucide-react';

interface HomeDashboardProps {
  questions: Question[];
  progress: Record<string, UserQuestionProgress>;
  examRecords: ExamRecord[];
  isDark: boolean;
  onToggleTheme: () => void;
  onStartPractice: (chapter?: string, subTopic?: string, questionId?: string) => void;
  onSelectMode: (mode: StudyMode) => void;
  wrongCount: number;
  favoriteCount: number;
  todayCount: number;
}

export const HomeDashboard: React.FC<HomeDashboardProps> = ({
  questions,
  progress,
  examRecords,
  isDark,
  onToggleTheme,
  onStartPractice,
  onSelectMode,
  wrongCount,
  favoriteCount,
  todayCount
}) => {
  // Mobile responsive sidebar drawer
  const [isMobileSidebarOpen, setIsMobileSidebarOpen] = useState<boolean>(false);

  // Scope filter pill in sidebar: 'ALL' | '真题' | '960题' | '教材' | '绝杀'
  const [scopeFilter, setScopeFilter] = useState<string>('ALL');
  
  // Chapter accordion expand state in sidebar
  const [expandedChapter, setExpandedChapter] = useState<string>('第一章：信号与系统基础');
  
  // More menu popover in sidebar
  const [showMoreMenu, setShowMoreMenu] = useState<boolean>(false);

  // Search input state
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [isSearchActive, setIsSearchActive] = useState<boolean>(false);

  // 7 Standard chapters
  const chapterList = useMemo(() => [
    '第一章：信号与系统基础',
    '第二章：系统的时域分析',
    '第三章：频域分析与傅里叶变换',
    '第四章：拉普拉斯变换与复频域分析',
    '第五章：Z变换与离散系统',
    '第六章：系统状态变量与信号流图',
    '第七章：时域抽样与恢复'
  ], []);

  // Filtered questions based on sidebar scope pills
  const scopedQuestions = useMemo(() => {
    if (scopeFilter === 'ALL') return questions;
    if (scopeFilter === '真题') {
      return questions.filter(q => getQuestionSourceCategory(q.source).includes('真题'));
    }
    if (scopeFilter === '960题') {
      return questions.filter(q => getQuestionSourceCategory(q.source).includes('960'));
    }
    if (scopeFilter === '教材') {
      return questions.filter(q => {
        const src = getQuestionSourceCategory(q.source);
        return src.includes('郑君里') || src.includes('奥本海姆');
      });
    }
    if (scopeFilter === '绝杀') {
      return questions.filter(q => getQuestionSourceCategory(q.source).includes('绝杀'));
    }
    return questions;
  }, [questions, scopeFilter]);

  // Overall statistics for Big Data Dashboard (Image 2)
  const totalQuestions = questions.length;
  const totalAnswered = useMemo(() => {
    return questions.filter(q => progress[q.id]?.answered).length;
  }, [questions, progress]);

  const correctCount = useMemo(() => {
    return questions.filter(q => progress[q.id]?.answered && progress[q.id]?.isCorrect).length;
  }, [questions, progress]);

  const masteredCount = useMemo(() => {
    return questions.filter(q => progress[q.id]?.isMastered).length;
  }, [questions, progress]);

  const coveragePercent = totalQuestions > 0 ? Math.round((totalAnswered / totalQuestions) * 100) : 0;
  const accuracyPercent = totalAnswered > 0 ? Math.round((correctCount / totalAnswered) * 100) : 0;

  // Chapter statistics calculation for right panel (Image 2)
  const chapterStats = useMemo(() => {
    return chapterList.map(chName => {
      const chQuestions = questions.filter(q => q.chapter === chName);
      const chAnswered = chQuestions.filter(q => progress[q.id]?.answered).length;
      const chCorrect = chQuestions.filter(q => progress[q.id]?.answered && progress[q.id]?.isCorrect).length;
      const chTotal = chQuestions.length;
      const chPercent = chTotal > 0 ? Math.round((chAnswered / chTotal) * 100) : 0;
      const chAcc = chAnswered > 0 ? Math.round((chCorrect / chAnswered) * 100) : 0;

      // Group sub-topics for this chapter
      const subMap: Record<string, Question[]> = {};
      chQuestions.forEach(q => {
        const subName = q.section || (q.tags && q.tags[0]) || (
          q.type === 'single' ? '单选题型' :
          q.type === 'multiple' ? '多选题型' :
          q.type === 'judgment' ? '判断题型' : '综合大题'
        );
        if (!subMap[subName]) subMap[subName] = [];
        subMap[subName].push(q);
      });

      const subTopics = Object.keys(subMap).map(sName => {
        const subQs = subMap[sName];
        const subAnswered = subQs.filter(q => progress[q.id]?.answered).length;
        return {
          name: sName,
          total: subQs.length,
          answered: subAnswered,
          questions: subQs
        };
      });

      return {
        name: chName,
        total: chTotal,
        answered: chAnswered,
        correct: chCorrect,
        percent: chPercent,
        accuracy: chAcc,
        subTopics
      };
    });
  }, [chapterList, questions, progress]);

  // Source statistics calculation for left panel (Image 2)
  const sourceStats = useMemo(() => {
    return STANDARD_SOURCES.map(sourceName => {
      const srcQuestions = questions.filter(q => getQuestionSourceCategory(q.source) === sourceName);
      const srcAnswered = srcQuestions.filter(q => progress[q.id]?.answered).length;
      const srcCorrect = srcQuestions.filter(q => progress[q.id]?.answered && progress[q.id]?.isCorrect).length;
      const srcTotal = srcQuestions.length;
      const srcPercent = srcTotal > 0 ? Math.round((srcAnswered / srcTotal) * 100) : 0;
      const srcAcc = srcAnswered > 0 ? Math.round((srcCorrect / srcAnswered) * 100) : 0;

      return {
        name: sourceName,
        total: srcTotal,
        answered: srcAnswered,
        percent: srcPercent,
        accuracy: srcAcc
      };
    });
  }, [questions, progress]);

  // Identify last practiced question or default to first question
  const lastPracticedInfo = useMemo(() => {
    let lastQ: Question | null = null;
    let maxTime = -1;

    for (const q of questions) {
      const p = progress[q.id];
      if (p && p.lastAnsweredTime && p.lastAnsweredTime > maxTime) {
        maxTime = p.lastAnsweredTime;
        lastQ = q;
      }
    }

    if (!lastQ && questions.length > 0) {
      lastQ = questions[0];
    }

    if (!lastQ) {
      return {
        question: null,
        chapter: '第一章：信号与系统基础',
        subTopic: '离散序列周期判定',
        source: '广工 837/809 历年真题',
        lastIndex: 0,
        totalInTopic: 19
      };
    }

    const topicQuestions = questions.filter(q => q.chapter === lastQ?.chapter);
    const qIndex = topicQuestions.findIndex(q => q.id === lastQ?.id);

    return {
      question: lastQ,
      chapter: lastQ.chapter,
      subTopic: lastQ.section || (lastQ.tags && lastQ.tags[0]) || '离散序列周期判定',
      source: getQuestionSourceCategory(lastQ.source),
      lastIndex: qIndex >= 0 ? qIndex : 0,
      totalInTopic: topicQuestions.length
    };
  }, [questions, progress]);

  // Current formatted date in Chinese: e.g. "10月31日 · 周六"
  const currentDateString = useMemo(() => {
    const now = new Date();
    const month = now.getMonth() + 1;
    const date = now.getDate();
    const weekDays = ['周日', '周一', '周二', '周三', '周四', '周五', '周六'];
    const weekDay = weekDays[now.getDay()];
    return `${month}月${date}日 · ${weekDay}`;
  }, []);

  // Countdown to Graduate Exam (approx. late December)
  const countdownDays = useMemo(() => {
    const examDate = new Date(2026, 11, 26); // Dec 26
    const diff = examDate.getTime() - Date.now();
    const days = Math.max(1, Math.ceil(diff / (1000 * 60 * 60 * 24)));
    return days > 365 ? 49 : days; // default 49 if far
  }, []);

  // Search Results
  const searchResults = useMemo(() => {
    if (!searchQuery.trim()) return [];
    const q = searchQuery.toLowerCase().trim();
    return questions.filter(item => 
      item.stem.toLowerCase().includes(q) ||
      item.chapter.toLowerCase().includes(q) ||
      (item.section && item.section.toLowerCase().includes(q)) ||
      (item.source && item.source.toLowerCase().includes(q))
    ).slice(0, 10);
  }, [searchQuery, questions]);

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-[#0c101c] text-slate-800 dark:text-slate-100 flex transition-colors duration-200">
      
      {/* Mobile Drawer Backdrop */}
      {isMobileSidebarOpen && (
        <div 
          onClick={() => setIsMobileSidebarOpen(false)} 
          className="fixed inset-0 bg-black/60 backdrop-blur-xs z-30 md:hidden animate-fadeIn" 
        />
      )}

      {/* ========================================================= */}
      {/* 1. LEFT SIDEBAR (Exact Layout & Visual Style from Image 3) */}
      {/* ========================================================= */}
      <aside className={`w-64 sm:w-72 bg-white dark:bg-[#0e1322] border-r border-slate-200 dark:border-slate-800/80 flex flex-col shrink-0 select-none z-40 transition-transform duration-200 md:translate-x-0 ${
        isMobileSidebarOpen 
          ? 'fixed inset-y-0 left-0 shadow-2xl translate-x-0' 
          : 'hidden md:flex'
      }`}>
        
        {/* Brand Logo & Subject Pill */}
        <div className="p-4 sm:p-5 border-b border-slate-200/80 dark:border-slate-800/80 flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            {/* Butterfly / Leaf Logo Icon */}
            <div className="w-8 h-8 rounded-xl bg-gradient-to-tr from-blue-600 to-indigo-500 flex items-center justify-center text-white shadow-md shadow-blue-500/20">
              <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" />
              </svg>
            </div>
            <div>
              <span className="font-extrabold text-base tracking-tight text-slate-900 dark:text-white">
                大观园
              </span>
              <span className="ml-1.5 px-2 py-0.5 rounded-full text-[11px] font-bold bg-blue-100 dark:bg-blue-950/80 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800/60">
                837/809
              </span>
            </div>
          </div>

          {/* Close button on mobile */}
          <button
            onClick={() => setIsMobileSidebarOpen(false)}
            className="md:hidden p-1.5 rounded-xl text-slate-400 hover:text-slate-600 dark:hover:text-slate-200"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Primary Navigation Menu */}
        <div className="p-3 space-y-1 border-b border-slate-200/60 dark:border-slate-800/60 text-xs sm:text-sm font-semibold">
          {/* 首页 */}
          <button
            className="w-full flex items-center gap-3 px-3.5 py-2.5 rounded-xl bg-blue-50 dark:bg-blue-950/50 text-blue-600 dark:text-blue-400 font-bold border border-blue-200/80 dark:border-blue-800/50 shadow-xs"
          >
            <Home className="w-4 h-4" />
            <span>首页</span>
          </button>

          {/* 收藏本 */}
          <button
            onClick={() => onSelectMode('favorite')}
            className="w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800/60 transition-colors"
          >
            <div className="flex items-center gap-3">
              <Star className="w-4 h-4 text-amber-500" />
              <span>收藏本</span>
            </div>
            {favoriteCount > 0 && (
              <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-amber-100 dark:bg-amber-950/80 text-amber-700 dark:text-amber-300">
                {favoriteCount}
              </span>
            )}
          </button>

          {/* 错题复测 */}
          <button
            onClick={() => onSelectMode('wrong')}
            className="w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800/60 transition-colors"
          >
            <div className="flex items-center gap-3">
              <AlertCircle className="w-4 h-4 text-rose-500" />
              <span>错题复测</span>
            </div>
            {wrongCount > 0 && (
              <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-rose-100 dark:bg-rose-950/80 text-rose-700 dark:text-rose-300">
                {wrongCount}
              </span>
            )}
          </button>

          {/* 更多功能 Dropdown */}
          <div className="relative">
            <button
              onClick={() => setShowMoreMenu(s => !s)}
              className="w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800/60 transition-colors"
            >
              <div className="flex items-center gap-3">
                <Settings className="w-4 h-4 text-slate-400" />
                <span>更多功能</span>
              </div>
              <ChevronRight className={`w-3.5 h-3.5 text-slate-400 transition-transform ${showMoreMenu ? 'rotate-90' : ''}`} />
            </button>

            {showMoreMenu && (
              <div className="mt-1 ml-4 pl-2 border-l-2 border-slate-200 dark:border-slate-800 space-y-1 animate-fadeIn">
                <button
                  onClick={() => onSelectMode('exam')}
                  className="w-full text-left px-3 py-2 rounded-lg text-xs text-slate-600 dark:text-slate-300 hover:text-blue-600 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800/50 flex items-center gap-2"
                >
                  <Award className="w-3.5 h-3.5 text-indigo-500" />
                  <span>全真模拟机考</span>
                </button>
                <button
                  onClick={() => onSelectMode('manage')}
                  className="w-full text-left px-3 py-2 rounded-lg text-xs text-slate-600 dark:text-slate-300 hover:text-blue-600 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800/50 flex items-center gap-2"
                >
                  <Sparkles className="w-3.5 h-3.5 text-emerald-500" />
                  <span>题库中心与导入</span>
                </button>
              </div>
            )}
          </div>
        </div>

        {/* Scope Filter Pills (Matching Image 3: 题单 完整 严选 真题) */}
        <div className="p-3 border-b border-slate-200/60 dark:border-slate-800/60">
          <div className="flex items-center gap-1.5 p-1 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-200/80 dark:border-slate-800 text-[11px] font-bold">
            {[
              { id: 'ALL', label: '全部' },
              { id: '真题', label: '真题' },
              { id: '960题', label: '960题' },
              { id: '教材', label: '教材' },
              { id: '绝杀', label: '绝杀' }
            ].map(item => (
              <button
                key={item.id}
                onClick={() => setScopeFilter(item.id)}
                className={`flex-1 py-1 rounded-lg transition-all ${
                  scopeFilter === item.id
                    ? 'bg-white dark:bg-slate-800 text-blue-600 dark:text-blue-400 shadow-xs'
                    : 'text-slate-500 hover:text-slate-800 dark:text-slate-400 dark:hover:text-white'
                }`}
              >
                {item.label}
              </button>
            ))}
          </div>
        </div>

        {/* Chapter Accordion List (Matching Image 3) */}
        <div className="flex-1 overflow-y-auto p-3 space-y-1">
          <div className="px-3 py-1.5 text-[11px] font-bold text-slate-400 dark:text-slate-500 flex items-center justify-between">
            <span>七大章节考点</span>
            <span className="font-mono text-[10px]">{scopedQuestions.length} 题</span>
          </div>

          {chapterStats.map((c, idx) => {
            const isExpanded = expandedChapter === c.name;
            const chineseNums = ['(一)', '(二)', '(三)', '(四)', '(五)', '(六)', '(七)'];
            const shortName = c.name.replace(/^第[一二三四五六七]章：/, '');

            return (
              <div key={c.name} className="rounded-xl overflow-hidden">
                {/* Chapter Title Row */}
                <button
                  onClick={() => setExpandedChapter(isExpanded ? '' : c.name)}
                  className={`w-full flex items-center justify-between px-3 py-2 rounded-xl text-xs font-semibold transition-all ${
                    isExpanded 
                      ? 'bg-slate-100 dark:bg-slate-850/90 text-slate-900 dark:text-white'
                      : 'text-slate-600 dark:text-slate-400 hover:bg-slate-100/60 dark:hover:bg-slate-850/50'
                  }`}
                >
                  <div className="flex items-center gap-2 truncate">
                    <span className="font-bold text-blue-600 dark:text-blue-400 shrink-0">
                      {chineseNums[idx] || `(${idx + 1})`}
                    </span>
                    <span className="truncate">{shortName}</span>
                  </div>
                  <ChevronDown className={`w-3.5 h-3.5 text-slate-400 shrink-0 transition-transform ${isExpanded ? 'rotate-180 text-blue-500' : ''}`} />
                </button>

                {/* Sub-topics list inside chapter */}
                {isExpanded && (
                  <div className="mt-1 ml-4 pl-2 border-l border-slate-200 dark:border-slate-800 space-y-1 py-1 animate-fadeIn">
                    {c.subTopics.map(sub => (
                      <button
                        key={sub.name}
                        onClick={() => onStartPractice(c.name, sub.name)}
                        className="w-full text-left px-3 py-1.5 rounded-lg text-[11px] text-slate-600 dark:text-slate-400 hover:text-blue-600 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800/60 flex items-center justify-between group transition-colors"
                      >
                        <span className="truncate pr-2">{sub.name}</span>
                        <span className="font-mono text-[10px] text-slate-400 group-hover:text-blue-500 shrink-0">
                          {sub.answered}/{sub.total}
                        </span>
                      </button>
                    ))}
                    <button
                      onClick={() => onStartPractice(c.name, 'ALL')}
                      className="w-full text-left px-3 py-1 rounded-lg text-[10px] font-bold text-blue-600 dark:text-blue-400 hover:underline flex items-center gap-1 pt-1"
                    >
                      <span>练习本章全部 {c.total} 题</span>
                      <ArrowRight className="w-3 h-3" />
                    </button>
                  </div>
                )}
              </div>
            );
          })}

          {/* Bottom Fast Links (Matching Image 3: 极简版 / 历年真题) */}
          <div className="pt-4 border-t border-slate-200/60 dark:border-slate-800/60 space-y-1">
            <button
              onClick={() => onStartPractice('ALL', 'ALL')}
              className="w-full text-left px-3.5 py-2 rounded-xl text-xs font-semibold text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800/60 flex items-center gap-2"
            >
              <Layers className="w-3.5 h-3.5 text-emerald-500" />
              <span>题库极速刷 (全部题型)</span>
            </button>
            <button
              onClick={() => onStartPractice('ALL', 'ALL')}
              className="w-full text-left px-3.5 py-2 rounded-xl text-xs font-semibold text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800/60 flex items-center gap-2"
            >
              <Award className="w-3.5 h-3.5 text-blue-500" />
              <span>历年真题集 (广工专攻)</span>
            </button>
          </div>
        </div>

      </aside>

      {/* ========================================================= */}
      {/* 2. MAIN WORKSPACE (Exact Layout from Image 3 + Image 2)  */}
      {/* ========================================================= */}
      <main className="flex-1 flex flex-col min-w-0 overflow-y-auto">
        
        {/* Top Header Bar (Matching Image 3) */}
        <header className="sticky top-0 z-10 w-full bg-white/95 dark:bg-[#0c101c]/95 backdrop-blur-md border-b border-slate-200 dark:border-slate-800/80 px-4 sm:px-10 h-16 flex items-center justify-between gap-4 transition-colors">
          
          {/* Mobile Menu Button */}
          <button
            onClick={() => setIsMobileSidebarOpen(true)}
            className="md:hidden p-2 rounded-xl text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
            title="展开章节考点侧边栏"
          >
            <Menu className="w-5 h-5" />
          </button>

          {/* Search Box */}
          <div className="relative flex-1 max-w-md">
            <div className="flex items-center gap-2 px-3.5 py-2 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-xs text-slate-500 focus-within:border-blue-500 focus-within:bg-white dark:focus-within:bg-slate-950 transition-all">
              <Search className="w-4 h-4 text-slate-400 shrink-0" />
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => {
                  setSearchQuery(e.target.value);
                  setIsSearchActive(Boolean(e.target.value.trim()));
                }}
                placeholder="搜索题目、公式、考点或出处..."
                className="w-full bg-transparent border-none outline-none text-slate-800 dark:text-slate-100 placeholder-slate-400 text-xs"
              />
              {searchQuery && (
                <button
                  onClick={() => { setSearchQuery(''); setIsSearchActive(false); }}
                  className="text-slate-400 hover:text-slate-600 text-xs"
                >
                  ✕
                </button>
              )}
            </div>

            {/* Live Search Results Dropdown */}
            {isSearchActive && searchResults.length > 0 && (
              <div className="absolute left-0 right-0 mt-2 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl shadow-2xl p-2 z-50 max-h-80 overflow-y-auto animate-fadeIn">
                <div className="px-3 py-1.5 text-[11px] font-bold text-slate-400">找到 {searchResults.length} 道相关题目</div>
                {searchResults.map(q => (
                  <button
                    key={q.id}
                    onClick={() => {
                      setIsSearchActive(false);
                      onStartPractice(q.chapter, q.section, q.id);
                    }}
                    className="w-full text-left p-2.5 rounded-xl hover:bg-slate-100 dark:hover:bg-slate-800/80 transition-colors space-y-1 block"
                  >
                    <div className="flex items-center gap-2 text-[10px] text-blue-600 dark:text-blue-400 font-semibold">
                      <span>{q.chapter}</span>
                      <span>·</span>
                      <span>{getQuestionSourceCategory(q.source)}</span>
                    </div>
                    <div className="text-xs text-slate-800 dark:text-slate-200 truncate">
                      {q.stem.replace(/[$#`*]/g, '')}
                    </div>
                  </button>
                ))}
              </div>
            )}
          </div>

          {/* Right Status Bar: Date, Countdown, Theme Toggle, Profile */}
          <div className="flex items-center gap-3 sm:gap-5 text-xs text-slate-600 dark:text-slate-300">
            {/* Date Display */}
            <span className="hidden sm:inline font-medium text-slate-500 dark:text-slate-400">
              {currentDateString}
            </span>

            {/* 考研倒计时 Badge (Matching Image 3) */}
            <div className="flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 font-bold text-slate-700 dark:text-slate-200">
              <span className="text-blue-600 dark:text-blue-400">考研倒计时</span>
              <span className="font-mono text-rose-500">{countdownDays}</span>
              <span>天</span>
            </div>

            {/* Dark / Light Theme Toggle */}
            <button
              onClick={onToggleTheme}
              className="p-2 rounded-xl text-slate-500 hover:text-amber-500 dark:text-slate-400 dark:hover:text-amber-400 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
              title={isDark ? "切换为明亮白天模式" : "切换为夜晚黑暗模式"}
            >
              {isDark ? <Sun className="w-4 h-4 text-amber-400" /> : <Moon className="w-4 h-4 text-slate-700" />}
            </button>

            {/* User Avatar */}
            <div className="w-8 h-8 rounded-full bg-blue-600 text-white font-bold text-xs flex items-center justify-center shadow-sm">
              837
            </div>
          </div>

        </header>

        {/* Content Canvas */}
        <div className="p-6 sm:p-10 space-y-8 max-w-7xl mx-auto w-full">
          
          {/* ========================================================= */}
          {/* ROW 1: TWO HERO CARDS (Matching Image 3)                  */}
          {/* Left: 继续做题 Card | Right: 到期复习 / 每日计划 Card      */}
          {/* ========================================================= */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            
            {/* Card 1: 继续做题 (Left Hero Card from Image 3) */}
            <div className="p-6 rounded-3xl bg-white dark:bg-[#131b2e] border border-slate-200 dark:border-slate-800/80 shadow-xs flex flex-col justify-between space-y-6 group hover:border-blue-500/50 transition-all">
              <div className="space-y-3">
                {/* Top context tag and dropdown */}
                <div className="flex items-center justify-between text-xs">
                  <span className="text-slate-500 dark:text-slate-400 font-medium">
                    {lastPracticedInfo.source}
                  </span>
                  <button 
                    onClick={() => onStartPractice(lastPracticedInfo.chapter, 'ALL')}
                    className="flex items-center gap-1 text-slate-400 hover:text-blue-500 transition-colors font-medium"
                  >
                    <span>切换题单</span>
                    <ChevronDown className="w-3.5 h-3.5" />
                  </button>
                </div>

                {/* Main Topic Title (Large, Bold Heading) */}
                <h2 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white tracking-tight">
                  {lastPracticedInfo.subTopic}
                </h2>

                {/* Subtext breadcrumb & progress */}
                <div className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 space-y-1">
                  <div>{lastPracticedInfo.chapter}</div>
                  <div className="font-mono text-slate-600 dark:text-slate-300">
                    上次刷到第 <strong className="text-blue-600 dark:text-blue-400 font-bold">{lastPracticedInfo.lastIndex + 1}</strong> 题 · 共 {lastPracticedInfo.totalInTopic} 题
                  </div>
                </div>
              </div>

              {/* Blue "继续" Button (Solid Blue Button from Image 3) */}
              <div>
                <button
                  onClick={() => onStartPractice(lastPracticedInfo.chapter, lastPracticedInfo.subTopic, lastPracticedInfo.question?.id)}
                  className="px-8 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-bold text-sm shadow-md shadow-blue-600/20 active:scale-95 transition-all flex items-center gap-2 group-hover:shadow-lg group-hover:shadow-blue-600/30"
                >
                  <Play className="w-4 h-4 fill-white" />
                  <span>继续做题</span>
                </button>
              </div>
            </div>

            {/* Card 2: 到期复习 / 每日计划 (Right Hero Card from Image 3) */}
            <div className="p-6 rounded-3xl bg-white dark:bg-[#131b2e] border border-slate-200 dark:border-slate-800/80 shadow-xs flex flex-col justify-between space-y-6">
              <div className="space-y-3">
                <div className="flex items-center justify-between text-xs">
                  <span className="font-bold text-slate-700 dark:text-slate-300 text-sm">到期复习</span>
                  <button 
                    onClick={() => onSelectMode('wrong')}
                    className="text-blue-600 dark:text-blue-400 hover:underline font-semibold"
                  >
                    复习计划
                  </button>
                </div>

                <div className="py-2 text-slate-600 dark:text-slate-300 text-sm leading-relaxed">
                  {wrongCount > 0 ? (
                    <div className="flex items-center gap-2 text-rose-500 font-bold">
                      <AlertCircle className="w-4 h-4 shrink-0" />
                      <span>待巩固复测错题 {wrongCount} 道，建议今日完成彻底消灭！</span>
                    </div>
                  ) : (
                    <span>暂无到期复习题目，状态绝佳！</span>
                  )}
                </div>

                <div className="text-xs text-slate-500 dark:text-slate-400">
                  今日已完成 <strong className="font-mono text-slate-800 dark:text-white font-bold text-sm">{todayCount}</strong> 题
                </div>
              </div>

              <div>
                {wrongCount > 0 ? (
                  <button
                    onClick={() => onSelectMode('wrong')}
                    className="px-6 py-2.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold text-sm shadow-md shadow-rose-600/20 active:scale-95 transition-all flex items-center gap-2"
                  >
                    <RotateCcw className="w-4 h-4" />
                    <span>立即开始错题复测</span>
                  </button>
                ) : (
                  <button
                    onClick={() => onStartPractice('ALL', 'ALL')}
                    className="px-6 py-2.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 font-bold text-sm transition-all"
                  >
                    继续保持每日节奏
                  </button>
                )}
              </div>
            </div>

          </div>

          {/* ========================================================= */}
          {/* ROW 2: 刷题热度图 (Matching Image 3)                       */}
          {/* ========================================================= */}
          <div className="p-6 rounded-3xl bg-white dark:bg-[#131b2e] border border-slate-200 dark:border-slate-800/80 shadow-xs space-y-4">
            
            {/* Heatmap Header */}
            <div className="flex flex-wrap items-center justify-between gap-3 text-xs">
              
              {/* Left Legend: 无 ▪ 轻 ▪ 中 ▪ 高 ▪ 很高 */}
              <div className="flex items-center gap-2 text-slate-600 dark:text-slate-300 font-medium">
                <span className="font-bold text-slate-800 dark:text-white">刷题热度</span>
                <span className="text-slate-300 dark:text-slate-700">|</span>
                <span>无</span>
                <span className="w-2.5 h-2.5 rounded-xs bg-slate-200 dark:bg-slate-800" />
                <span className="w-2.5 h-2.5 rounded-xs bg-blue-300 dark:bg-blue-900" />
                <span>轻</span>
                <span className="w-2.5 h-2.5 rounded-xs bg-blue-400 dark:bg-blue-700" />
                <span>中</span>
                <span className="w-2.5 h-2.5 rounded-xs bg-blue-500 dark:bg-blue-600" />
                <span>高</span>
                <span className="w-2.5 h-2.5 rounded-xs bg-blue-600 dark:bg-blue-400" />
                <span>很高</span>
              </div>

              {/* Right Counter */}
              <div className="text-slate-500 dark:text-slate-400">
                今日已做 <strong className="font-mono text-blue-600 dark:text-blue-400 font-bold">{todayCount}</strong> 题
              </div>
            </div>

            {/* Heatmap Grid (7 rows for Mon-Sun across 36 columns) */}
            <div className="overflow-x-auto pb-1">
              <div className="min-w-[700px] flex gap-1.5 items-start">
                {/* Weekday labels: 一, 三, 五, 七 */}
                <div className="flex flex-col justify-between h-[104px] text-[10px] text-slate-400 dark:text-slate-500 font-mono pr-2 py-0.5">
                  <span>一</span>
                  <span>三</span>
                  <span>五</span>
                  <span>七</span>
                </div>

                {/* 36 Weeks Grid */}
                <div className="flex-1 grid grid-flow-col grid-rows-7 gap-1">
                  {Array.from({ length: 36 * 7 }).map((_, i) => {
                    // Highlight the last few days if user has answered today or recently
                    const isTodaySquare = i === (36 * 7 - 1);
                    const isRecentSquare = i >= (36 * 7 - 5);
                    let colorClass = 'bg-slate-100 dark:bg-slate-800/80 hover:ring-1 hover:ring-blue-400';

                    if (isTodaySquare && todayCount > 0) {
                      colorClass = todayCount > 10 
                        ? 'bg-blue-600 dark:bg-blue-400' 
                        : todayCount > 4 
                        ? 'bg-blue-500 dark:bg-blue-600' 
                        : 'bg-blue-400 dark:bg-blue-700';
                    } else if (isRecentSquare && totalAnswered > 0) {
                      colorClass = 'bg-blue-300 dark:bg-blue-900/80';
                    }

                    return (
                      <div
                        key={i}
                        className={`w-3.5 h-3 rounded-xs transition-colors cursor-pointer ${colorClass}`}
                        title={isTodaySquare ? `今天已做 ${todayCount} 题` : `考研研学轨迹点`}
                      />
                    );
                  })}
                </div>
              </div>

              {/* Month Markers (11月, 12月, 1月... 10月) */}
              <div className="flex justify-between pl-6 text-[10px] text-slate-400 dark:text-slate-500 pt-1 font-mono">
                <span>11月</span>
                <span>12月</span>
                <span>1月</span>
                <span>2月</span>
                <span>3月</span>
                <span>4月</span>
                <span>5月</span>
                <span>6月</span>
                <span>7月</span>
                <span>8月</span>
                <span>9月</span>
                <span>10月</span>
              </div>
            </div>

          </div>

          {/* ========================================================= */}
          {/* ROW 3: 学情大数据 · 掌握度全景看板 (Data from Image 2)     */}
          {/* 4 KPI Cards + 题库来源掌握度分布 + 七大章节考点掌握度分布   */}
          {/* ========================================================= */}
          <div className="p-6 sm:p-8 rounded-3xl bg-white dark:bg-[#131b2e] border border-slate-200 dark:border-slate-800/80 shadow-xs space-y-8">
            
            {/* Header: 学情大数据 · 掌握度全景看板 */}
            <div className="flex items-center gap-3 pb-2 border-b border-slate-200/80 dark:border-slate-800/80">
              <div className="w-10 h-10 rounded-2xl bg-blue-100 dark:bg-blue-950/80 text-blue-600 dark:text-blue-400 flex items-center justify-center shadow-xs">
                <BarChart3 className="w-5 h-5" />
              </div>
              <div>
                <h3 className="text-lg font-bold text-slate-900 dark:text-white">
                  学情大数据 · 掌握度全景看板
                </h3>
                <p className="text-xs text-slate-500 dark:text-slate-400">
                  实时统计做题进度、正确率与考点掌握分布
                </p>
              </div>
            </div>

            {/* 4 KPI Cards (Exact Metric Cards from Image 2) */}
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
              
              {/* Card 1: 题库覆盖率 */}
              <div className="p-4 sm:p-5 rounded-2xl bg-slate-50 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800 space-y-2">
                <div className="flex items-center gap-2 text-xs font-semibold text-slate-500 dark:text-slate-400">
                  <Layers className="w-4 h-4 text-blue-500" />
                  <span>题库覆盖率</span>
                </div>
                <div className="text-2xl sm:text-3xl font-extrabold font-mono text-slate-900 dark:text-white">
                  {coveragePercent}%
                </div>
                <div className="text-[11px] text-slate-400 font-mono">
                  已做 {totalAnswered} / {totalQuestions}
                </div>
              </div>

              {/* Card 2: 综合正确率 */}
              <div className="p-4 sm:p-5 rounded-2xl bg-slate-50 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800 space-y-2">
                <div className="flex items-center gap-2 text-xs font-semibold text-slate-500 dark:text-slate-400">
                  <TrendingUp className="w-4 h-4 text-amber-500" />
                  <span>综合正确率</span>
                </div>
                <div className="text-2xl sm:text-3xl font-extrabold font-mono text-emerald-600 dark:text-emerald-400">
                  {accuracyPercent}%
                </div>
                <div className="text-[11px] text-slate-400 font-mono">
                  首对 {correctCount} 题
                </div>
              </div>

              {/* Card 3: 彻底攻克掌握 */}
              <div className="p-4 sm:p-5 rounded-2xl bg-slate-50 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800 space-y-2">
                <div className="flex items-center gap-2 text-xs font-semibold text-slate-500 dark:text-slate-400">
                  <CheckCircle2 className="w-4 h-4 text-emerald-500" />
                  <span>彻底攻克掌握</span>
                </div>
                <div className="text-2xl sm:text-3xl font-extrabold font-mono text-blue-600 dark:text-blue-400">
                  {masteredCount}
                </div>
                <div className="text-[11px] text-slate-400">
                  考点已完全内化
                </div>
              </div>

              {/* Card 4: 模考机考场次 */}
              <div className="p-4 sm:p-5 rounded-2xl bg-slate-50 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800 space-y-2">
                <div className="flex items-center gap-2 text-xs font-semibold text-slate-500 dark:text-slate-400">
                  <Flame className="w-4 h-4 text-rose-500" />
                  <span>模考机考场次</span>
                </div>
                <div className="text-2xl sm:text-3xl font-extrabold font-mono text-indigo-600 dark:text-indigo-400">
                  {examRecords.length}
                </div>
                <div className="text-[11px] text-slate-400">
                  高分真题实战
                </div>
              </div>

            </div>

            {/* Split Distribution Columns: Sources (Left) & Chapters (Right) */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 pt-2">
              
              {/* Column A: 题库来源掌握度分布 (Exact List from Image 2) */}
              <div className="space-y-4">
                <div className="flex items-center gap-2 text-sm font-bold text-slate-900 dark:text-white">
                  <BookOpen className="w-4 h-4 text-blue-500" />
                  <span>题库来源掌握度分布</span>
                </div>

                <div className="space-y-3.5">
                  {sourceStats.map(src => (
                    <div key={src.name} className="p-3.5 rounded-2xl bg-slate-50 dark:bg-slate-900/50 border border-slate-200/80 dark:border-slate-800/80 space-y-2">
                      <div className="flex items-center justify-between text-xs">
                        <span className="font-bold text-slate-800 dark:text-slate-200 truncate pr-2">
                          {src.name}
                        </span>
                        <div className="flex items-center gap-2 font-mono text-[11px] text-slate-500 dark:text-slate-400 shrink-0">
                          <span>进度: {src.answered}/{src.total}</span>
                          <span>正确率: <strong className={src.accuracy > 70 ? 'text-emerald-500' : 'text-blue-500'}>{src.accuracy}%</strong></span>
                        </div>
                      </div>

                      {/* Progress Bar with Image 2 style */}
                      <div className="w-full h-2 rounded-full bg-slate-200 dark:bg-slate-800 overflow-hidden flex">
                        <div 
                          className="h-full bg-blue-500 transition-all duration-500"
                          style={{ width: `${src.percent}%` }}
                        />
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              {/* Column B: 七大章节考点掌握度 (Exact List from Image 2) */}
              <div className="space-y-4">
                <div className="flex items-center gap-2 text-sm font-bold text-slate-900 dark:text-white">
                  <Layers className="w-4 h-4 text-emerald-500" />
                  <span>七大章节考点掌握度</span>
                </div>

                <div className="space-y-3.5">
                  {chapterStats.map(ch => (
                    <div 
                      key={ch.name} 
                      onClick={() => onStartPractice(ch.name, 'ALL')}
                      className="p-3.5 rounded-2xl bg-slate-50 dark:bg-slate-900/50 border border-slate-200/80 dark:border-slate-800/80 space-y-2 cursor-pointer hover:border-blue-400 transition-all group"
                      title="点击直接刷本章题目"
                    >
                      <div className="flex items-center justify-between text-xs">
                        <span className="font-bold text-slate-800 dark:text-slate-200 group-hover:text-blue-600 dark:group-hover:text-blue-400 truncate pr-2">
                          {ch.name}
                        </span>
                        <div className="flex items-center gap-2 font-mono text-[11px] text-slate-500 dark:text-slate-400 shrink-0">
                          <span>进度: {ch.answered}/{ch.total}</span>
                          <span>正确率: <strong className={ch.accuracy > 70 ? 'text-emerald-500' : 'text-blue-500'}>{ch.accuracy}%</strong></span>
                        </div>
                      </div>

                      {/* Progress Bar with Image 2 style */}
                      <div className="w-full h-2 rounded-full bg-slate-200 dark:bg-slate-800 overflow-hidden flex">
                        <div 
                          className="h-full bg-gradient-to-r from-blue-500 to-emerald-400 transition-all duration-500"
                          style={{ width: `${ch.percent}%` }}
                        />
                      </div>
                    </div>
                  ))}
                </div>
              </div>

            </div>

          </div>

        </div>

      </main>

    </div>
  );
};
