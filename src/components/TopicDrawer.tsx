import React, { useState, useMemo } from 'react';
import { Question, UserQuestionProgress } from '../types';
import { getQuestionSourceCategory, STANDARD_SOURCES } from '../utils/sourceHelper';
import { 
  X, 
  ChevronRight, 
  ChevronDown, 
  Check, 
  BookMarked, 
  Layers,
  Search
} from 'lucide-react';

interface TopicDrawerProps {
  isOpen: boolean;
  onClose: () => void;
  questions: Question[];
  progress: Record<string, UserQuestionProgress>;
  selectedChapter: string;
  selectedSubTopic: string;
  selectedSource: string;
  onSelectTopic: (chapter: string, subTopic: string, source: string) => void;
  isDark: boolean;
}

export const TopicDrawer: React.FC<TopicDrawerProps> = ({
  isOpen,
  onClose,
  questions,
  progress,
  selectedChapter,
  selectedSubTopic,
  selectedSource,
  onSelectTopic
}) => {
  if (!isOpen) return null;

  // View mode inside drawer: 'chapter' (按章节考点) | 'source' (按题库来源)
  const [drawerMode, setDrawerMode] = useState<'chapter' | 'source'>('chapter');
  const [expandedChapters, setExpandedChapters] = useState<Record<string, boolean>>({
    [selectedChapter === 'ALL' ? '第一章：信号与系统基础' : selectedChapter]: true
  });
  const [searchKeyword, setSearchKeyword] = useState<string>('');

  // Chapter Order
  const chapterList = [
    '第一章：信号与系统基础',
    '第二章：系统的时域分析',
    '第三章：频域分析与傅里叶变换',
    '第四章：拉普拉斯变换与复频域分析',
    '第五章：Z变换与离散系统',
    '第六章：系统状态变量与信号流图',
    '第七章：时域抽样与恢复'
  ];

  // Total completed / mastered stats
  const totalQuestionsCount = questions.length;
  const totalMasteredCount = useMemo(() => {
    return questions.filter(q => progress[q.id]?.isMastered || progress[q.id]?.answered).length;
  }, [questions, progress]);

  // Compute Chapter Data Structure (Level 1 + Level 2)
  const chapterData = useMemo(() => {
    return chapterList.map(chName => {
      const chQuestions = questions.filter(q => q.chapter === chName);
      const chAnswered = chQuestions.filter(q => progress[q.id]?.answered || progress[q.id]?.isMastered).length;
      const chTotal = chQuestions.length;

      // Group sub-topics inside this chapter
      const subMap: Record<string, Question[]> = {};
      chQuestions.forEach(q => {
        // Priority for sub-topic label: q.section -> primary tag -> question type
        const subName = q.section || (q.tags && q.tags[0]) || (
          q.type === 'single' ? '单选题型' :
          q.type === 'multiple' ? '多选题型' :
          q.type === 'judgment' ? '判断题型' : '综合大题'
        );
        if (!subMap[subName]) subMap[subName] = [];
        subMap[subName].push(q);
      });

      const subTopics = Object.keys(subMap).map(subName => {
        const subQs = subMap[subName];
        const subAnswered = subQs.filter(q => progress[q.id]?.answered || progress[q.id]?.isMastered).length;
        return {
          name: subName,
          total: subQs.length,
          answered: subAnswered,
          questions: subQs
        };
      });

      return {
        chapter: chName,
        total: chTotal,
        answered: chAnswered,
        percent: chTotal > 0 ? Math.round((chAnswered / chTotal) * 100) : 0,
        subTopics
      };
    }).filter(c => c.total > 0);
  }, [questions, progress]);

  // Compute Source Data Structure
  const sourceData = useMemo(() => {
    return STANDARD_SOURCES.map(sourceName => {
      const srcQuestions = questions.filter(q => getQuestionSourceCategory(q.source) === sourceName);
      const srcAnswered = srcQuestions.filter(q => progress[q.id]?.answered || progress[q.id]?.isMastered).length;
      const srcTotal = srcQuestions.length;

      // Group chapters under this source
      const chMap: Record<string, Question[]> = {};
      srcQuestions.forEach(q => {
        if (!chMap[q.chapter]) chMap[q.chapter] = [];
        chMap[q.chapter].push(q);
      });

      const subTopics = Object.keys(chMap).map(ch => {
        const subQs = chMap[ch];
        const subAnswered = subQs.filter(q => progress[q.id]?.answered || progress[q.id]?.isMastered).length;
        return {
          name: ch,
          total: subQs.length,
          answered: subAnswered
        };
      });

      return {
        source: sourceName,
        total: srcTotal,
        answered: srcAnswered,
        percent: srcTotal > 0 ? Math.round((srcAnswered / srcTotal) * 100) : 0,
        subTopics
      };
    }).filter(s => s.total > 0);
  }, [questions, progress]);

  // Toggle chapter collapse
  const toggleChapter = (name: string) => {
    setExpandedChapters(prev => ({
      ...prev,
      [name]: !prev[name]
    }));
  };

  return (
    <div className="fixed inset-0 z-50 flex animate-fadeIn">
      {/* Backdrop */}
      <div 
        onClick={onClose}
        className="fixed inset-0 bg-black/60 backdrop-blur-sm transition-opacity" 
      />

      {/* Slide-over Drawer Panel */}
      <div className="relative w-full max-w-sm sm:max-w-md bg-white dark:bg-[#131826] text-slate-900 dark:text-slate-100 h-full shadow-2xl flex flex-col z-10 border-r border-slate-200 dark:border-slate-800 transform transition-transform duration-300 ease-in-out">
        
        {/* Drawer Header (Exact match to Image 2) */}
        <div className="px-5 pt-5 pb-3 border-b border-slate-200 dark:border-slate-800/90">
          <div className="flex items-center justify-between pb-3">
            <div className="flex items-center gap-2">
              <span className="font-bold text-base tracking-tight text-slate-800 dark:text-slate-100">
                信号与系统 · 全部题目
              </span>
            </div>

            <div className="flex items-center gap-3">
              <span className="text-xs font-mono font-medium text-slate-500 dark:text-slate-400">
                已标记 <strong className="text-blue-600 dark:text-blue-400 font-bold">{totalMasteredCount}</strong> / {totalQuestionsCount}
              </span>
              <button
                onClick={onClose}
                className="p-1.5 rounded-lg text-slate-400 hover:text-slate-700 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
                title="关闭菜单 (Esc)"
              >
                <X className="w-4 h-4" />
              </button>
            </div>
          </div>

          {/* Mode Switcher Tabs */}
          <div className="flex items-center gap-1 bg-slate-100 dark:bg-slate-900 p-1 rounded-xl text-xs font-medium border border-slate-200/80 dark:border-slate-800/80">
            <button
              onClick={() => setDrawerMode('chapter')}
              className={`flex-1 py-1.5 rounded-lg text-center transition-all flex items-center justify-center gap-1.5 ${
                drawerMode === 'chapter'
                  ? 'bg-white dark:bg-blue-600 text-blue-600 dark:text-white shadow-sm font-bold'
                  : 'text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
              }`}
            >
              <Layers className="w-3.5 h-3.5" />
              <span>按章节考点</span>
            </button>
            <button
              onClick={() => setDrawerMode('source')}
              className={`flex-1 py-1.5 rounded-lg text-center transition-all flex items-center justify-center gap-1.5 ${
                drawerMode === 'source'
                  ? 'bg-white dark:bg-blue-600 text-blue-600 dark:text-white shadow-sm font-bold'
                  : 'text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
              }`}
            >
              <BookMarked className="w-3.5 h-3.5" />
              <span>按题库来源</span>
            </button>
          </div>

          {/* Quick Search in Topics */}
          <div className="mt-3 relative">
            <Search className="w-3.5 h-3.5 text-slate-400 absolute left-3 top-2.5" />
            <input
              type="text"
              placeholder="搜索章节、考点、题型或公式..."
              value={searchKeyword}
              onChange={(e) => setSearchKeyword(e.target.value)}
              className="w-full bg-slate-50 dark:bg-slate-900 text-xs text-slate-800 dark:text-slate-200 pl-8 pr-3 py-2 rounded-xl border border-slate-200 dark:border-slate-800 focus:outline-none focus:border-blue-500"
            />
          </div>
        </div>

        {/* Accordion Tree List (Image 2 Two-Level Menu) */}
        <div className="flex-1 overflow-y-auto px-3 py-3 space-y-1.5">
          
          {/* Quick: All Questions option */}
          <div 
            onClick={() => {
              onSelectTopic('ALL', 'ALL', 'ALL');
              onClose();
            }}
            className={`px-3 py-2.5 rounded-xl cursor-pointer text-xs font-semibold flex items-center justify-between transition-all ${
              selectedChapter === 'ALL' && selectedSubTopic === 'ALL' && selectedSource === 'ALL'
                ? 'bg-blue-50 dark:bg-blue-950/60 text-blue-600 dark:text-blue-400 border border-blue-200 dark:border-blue-500/40'
                : 'text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800/60'
            }`}
          >
            <span className="flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-blue-500" />
              全部题目通刷 (全书 192 题)
            </span>
            <span className="font-mono text-[11px]">
              {totalMasteredCount}/{totalQuestionsCount}
            </span>
          </div>

          {/* 1. Mode: By Chapter (按章节二级菜单) */}
          {drawerMode === 'chapter' && chapterData.map((item) => {
            const isExpanded = Boolean(expandedChapters[item.chapter]);
            const isCurrentChapter = selectedChapter === item.chapter;

            // Check if filtered by search keyword
            const matchingSub = searchKeyword.trim()
              ? item.subTopics.filter(s => s.name.toLowerCase().includes(searchKeyword.toLowerCase()) || item.chapter.toLowerCase().includes(searchKeyword.toLowerCase()))
              : item.subTopics;

            if (searchKeyword.trim() && matchingSub.length === 0 && !item.chapter.toLowerCase().includes(searchKeyword.toLowerCase())) {
              return null;
            }

            return (
              <div 
                key={item.chapter}
                className="rounded-xl overflow-hidden transition-colors"
              >
                {/* Level 1 Item (Chapter Header) */}
                <div
                  onClick={() => toggleChapter(item.chapter)}
                  className={`px-3 py-2.5 flex items-center justify-between cursor-pointer rounded-xl transition-all select-none ${
                    isCurrentChapter 
                      ? 'bg-slate-100 dark:bg-slate-850 text-slate-900 dark:text-slate-100 font-bold' 
                      : 'text-slate-700 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-850/60'
                  }`}
                >
                  <div className="flex items-center gap-2 min-w-0 pr-2">
                    <span className="text-slate-400 shrink-0">
                      {isExpanded ? <ChevronDown className="w-4 h-4" /> : <ChevronRight className="w-4 h-4" />}
                    </span>
                    <span className="text-xs font-semibold truncate tracking-tight">
                      {item.chapter}
                    </span>
                  </div>

                  <div className="flex items-center gap-2 shrink-0 font-mono text-[11px] text-slate-500 dark:text-slate-400">
                    <span>已标记 {item.answered}/{item.total}</span>
                    {item.percent === 100 && (
                      <Check className="w-3.5 h-3.5 text-emerald-500 font-bold" />
                    )}
                  </div>
                </div>

                {/* Progress bar under Level 1 Chapter */}
                <div className="px-3 pb-1">
                  <div className="w-full h-1 bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                    <div 
                      className={`h-full rounded-full transition-all duration-300 ${
                        item.percent === 100 
                          ? 'bg-emerald-500' 
                          : item.percent > 0 
                          ? 'bg-amber-500' 
                          : 'bg-transparent'
                      }`}
                      style={{ width: `${item.percent}%` }}
                    />
                  </div>
                </div>

                {/* Level 2 Sub-Topics (Indented child list, matching Image 2) */}
                {isExpanded && (
                  <div className="pl-6 pr-2 py-1 space-y-1">
                    {/* Chapter all item */}
                    <div
                      onClick={() => {
                        onSelectTopic(item.chapter, 'ALL', 'ALL');
                        onClose();
                      }}
                      className={`px-3 py-1.5 rounded-lg text-xs cursor-pointer flex items-center justify-between transition-all ${
                        isCurrentChapter && selectedSubTopic === 'ALL'
                          ? 'bg-blue-600 text-white font-bold shadow-sm'
                          : 'text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-slate-900 dark:hover:text-white'
                      }`}
                    >
                      <span>本章全部题目</span>
                      <span className="font-mono text-[10px]">
                        {item.answered}/{item.total}
                      </span>
                    </div>

                    {/* Sub topics */}
                    {matchingSub.map(sub => {
                      const isSubSelected = isCurrentChapter && selectedSubTopic === sub.name;
                      return (
                        <div
                          key={sub.name}
                          onClick={() => {
                            onSelectTopic(item.chapter, sub.name, 'ALL');
                            onClose();
                          }}
                          className={`px-3 py-2 rounded-lg text-xs cursor-pointer flex items-center justify-between transition-all ${
                            isSubSelected
                              ? 'bg-blue-600 text-white font-bold shadow-sm'
                              : 'text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-slate-900 dark:hover:text-white'
                          }`}
                        >
                          <span className="truncate pr-2">{sub.name}</span>
                          <span className="font-mono text-[10px] shrink-0">
                            已标记 {sub.answered}/{sub.total}
                          </span>
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>
            );
          })}

          {/* 2. Mode: By Source (按题库来源二级菜单) */}
          {drawerMode === 'source' && sourceData.map((item) => {
            const isExpanded = Boolean(expandedChapters[item.source]);
            const isCurrentSource = selectedSource === item.source;

            return (
              <div 
                key={item.source}
                className="rounded-xl overflow-hidden transition-colors"
              >
                {/* Level 1 Item (Source Header) */}
                <div
                  onClick={() => toggleChapter(item.source)}
                  className={`px-3 py-2.5 flex items-center justify-between cursor-pointer rounded-xl transition-all select-none ${
                    isCurrentSource 
                      ? 'bg-slate-100 dark:bg-slate-850 text-slate-900 dark:text-slate-100 font-bold' 
                      : 'text-slate-700 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-850/60'
                  }`}
                >
                  <div className="flex items-center gap-2 min-w-0 pr-2">
                    <span className="text-slate-400 shrink-0">
                      {isExpanded ? <ChevronDown className="w-4 h-4" /> : <ChevronRight className="w-4 h-4" />}
                    </span>
                    <span className="text-xs font-semibold truncate tracking-tight">
                      {item.source}
                    </span>
                  </div>

                  <div className="flex items-center gap-2 shrink-0 font-mono text-[11px] text-slate-500 dark:text-slate-400">
                    <span>已标记 {item.answered}/{item.total}</span>
                  </div>
                </div>

                {/* Progress bar */}
                <div className="px-3 pb-1">
                  <div className="w-full h-1 bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                    <div 
                      className={`h-full rounded-full transition-all duration-300 ${
                        item.percent === 100 
                          ? 'bg-emerald-500' 
                          : item.percent > 0 
                          ? 'bg-blue-500' 
                          : 'bg-transparent'
                      }`}
                      style={{ width: `${item.percent}%` }}
                    />
                  </div>
                </div>

                {/* Level 2 Chapters under this Source */}
                {isExpanded && (
                  <div className="pl-6 pr-2 py-1 space-y-1">
                    {/* Source All */}
                    <div
                      onClick={() => {
                        onSelectTopic('ALL', 'ALL', item.source);
                        onClose();
                      }}
                      className={`px-3 py-1.5 rounded-lg text-xs cursor-pointer flex items-center justify-between transition-all ${
                        isCurrentSource && selectedChapter === 'ALL'
                          ? 'bg-blue-600 text-white font-bold shadow-sm'
                          : 'text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-slate-900 dark:hover:text-white'
                      }`}
                    >
                      <span>全本综合题目</span>
                      <span className="font-mono text-[10px]">
                        {item.answered}/{item.total}
                      </span>
                    </div>

                    {item.subTopics.map(sub => {
                      const isSubSelected = isCurrentSource && selectedChapter === sub.name;
                      return (
                        <div
                          key={sub.name}
                          onClick={() => {
                            onSelectTopic(sub.name, 'ALL', item.source);
                            onClose();
                          }}
                          className={`px-3 py-2 rounded-lg text-xs cursor-pointer flex items-center justify-between transition-all ${
                            isSubSelected
                              ? 'bg-blue-600 text-white font-bold shadow-sm'
                              : 'text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-slate-900 dark:hover:text-white'
                          }`}
                        >
                          <span className="truncate pr-2">{sub.name}</span>
                          <span className="font-mono text-[10px] shrink-0">
                            已标记 {sub.answered}/{sub.total}
                          </span>
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>
            );
          })}

        </div>

      </div>
    </div>
  );
};
