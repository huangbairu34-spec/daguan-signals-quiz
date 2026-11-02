import React from 'react';
import { Question, UserQuestionProgress, ExamRecord } from '../types';
import { getQuestionSourceCategory, STANDARD_SOURCES } from '../utils/sourceHelper';
import { 
  X, 
  BarChart2, 
  Trophy, 
  CheckCircle2, 
  Target, 
  History, 
  Flame,
  BookMarked,
  Layers
} from 'lucide-react';

interface StatsModalProps {
  isOpen: boolean;
  onClose: () => void;
  questions: Question[];
  progress: Record<string, UserQuestionProgress>;
  examRecords: ExamRecord[];
}

export const StatsModal: React.FC<StatsModalProps> = ({
  isOpen,
  onClose,
  questions,
  progress,
  examRecords
}) => {
  if (!isOpen) return null;

  const totalQuestions = questions.length;
  const answeredList = Object.values(progress).filter(p => p.answered);
  const totalAnswered = answeredList.length;
  const correctCount = answeredList.filter(p => p.isCorrect).length;
  const overallAccuracy = totalAnswered > 0 ? Math.round((correctCount / totalAnswered) * 100) : 0;
  const masteredCount = Object.values(progress).filter(p => p.isMastered).length;

  // Breakdown by Question Source
  const sourceStats = STANDARD_SOURCES.map(sourceName => {
    const srcQuestions = questions.filter(q => getQuestionSourceCategory(q.source) === sourceName);
    const srcAnswered = srcQuestions.filter(q => progress[q.id]?.answered);
    const srcCorrect = srcAnswered.filter(q => progress[q.id]?.isCorrect).length;
    const accuracy = srcAnswered.length > 0 ? Math.round((srcCorrect / srcAnswered.length) * 100) : 0;
    return {
      name: sourceName,
      total: srcQuestions.length,
      answered: srcAnswered.length,
      accuracy
    };
  }).filter(s => s.total > 0);

  // Breakdown by Chapter
  const chapterOrder = [
    '第一章：信号与系统基础',
    '第二章：系统的时域分析',
    '第三章：频域分析与傅里叶变换',
    '第四章：拉普拉斯变换与复频域分析',
    '第五章：Z变换与离散系统',
    '第六章：系统状态变量与信号流图',
    '第七章：时域抽样与恢复'
  ];
  const chapterStats = chapterOrder.map(chName => {
    const chQuestions = questions.filter(q => q.chapter === chName);
    const chAnswered = chQuestions.filter(q => progress[q.id]?.answered);
    const chCorrect = chAnswered.filter(q => progress[q.id]?.isCorrect).length;
    const accuracy = chAnswered.length > 0 ? Math.round((chCorrect / chAnswered.length) * 100) : 0;
    return {
      name: chName,
      total: chQuestions.length,
      answered: chAnswered.length,
      accuracy
    };
  }).filter(c => c.total > 0);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md animate-fadeIn">
      <div className="bg-slate-900 border border-slate-800 border-t-2 border-t-blue-500 w-full max-w-3xl rounded-3xl p-6 md:p-8 shadow-elevation-4 space-y-6 max-h-[90vh] overflow-y-auto">
        
        {/* Header */}
        <div className="flex items-center justify-between pb-4 border-b border-slate-800">
          <div className="flex items-center gap-2.5">
            <div className="p-2.5 rounded-2xl bg-blue-500/10 text-blue-400 border border-blue-500/20">
              <BarChart2 className="w-5 h-5" />
            </div>
            <div>
              <h2 className="text-xl font-black text-white tracking-tight">学情大数据 · 掌握度全景看板</h2>
              <p className="text-xs text-slate-400">实时统计做题进度、正确率与考点掌握分布</p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-2 rounded-xl text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Top 4 Stat Cards */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="p-4 rounded-2xl bg-slate-850/80 border border-slate-800 shadow-sm">
            <div className="text-xs text-slate-400 flex items-center gap-1.5 mb-1 font-medium">
              <Target className="w-3.5 h-3.5 text-blue-400" />
              <span>题库覆盖率</span>
            </div>
            <div className="text-2xl font-black text-white font-mono">
              {totalQuestions > 0 ? Math.round((totalAnswered / totalQuestions) * 100) : 0}%
            </div>
            <div className="text-[11px] text-slate-500 mt-1 font-mono">
              已做 {totalAnswered} / {totalQuestions}
            </div>
          </div>

          <div className="p-4 rounded-2xl bg-slate-850/80 border border-slate-800 shadow-sm">
            <div className="text-xs text-slate-400 flex items-center gap-1.5 mb-1 font-medium">
              <Trophy className="w-3.5 h-3.5 text-amber-400" />
              <span>综合正确率</span>
            </div>
            <div className="text-2xl font-black text-emerald-400 font-mono">
              {overallAccuracy}%
            </div>
            <div className="text-[11px] text-slate-500 mt-1 font-mono">
              答对 {correctCount} 题
            </div>
          </div>

          <div className="p-4 rounded-2xl bg-slate-850/80 border border-slate-800 shadow-sm">
            <div className="text-xs text-slate-400 flex items-center gap-1.5 mb-1 font-medium">
              <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
              <span>彻底攻破掌握</span>
            </div>
            <div className="text-2xl font-black text-blue-400 font-mono">
              {masteredCount}
            </div>
            <div className="text-[11px] text-slate-500 mt-1">
              考点已完全内化
            </div>
          </div>

          <div className="p-4 rounded-2xl bg-slate-850/80 border border-slate-800 shadow-sm">
            <div className="text-xs text-slate-400 flex items-center gap-1.5 mb-1 font-medium">
              <Flame className="w-3.5 h-3.5 text-rose-400" />
              <span>模考机考场次</span>
            </div>
            <div className="text-2xl font-black text-rose-400 font-mono">
              {examRecords.length}
            </div>
            <div className="text-[11px] text-slate-500 mt-1">
              套卷模拟实战
            </div>
          </div>
        </div>

        {/* Source Breakdown Progress Bars */}
        <div className="space-y-3.5">
          <h3 className="text-sm font-bold text-slate-200 flex items-center gap-2">
            <BookMarked className="w-4 h-4 text-indigo-400" />
            <span>题库来源掌握度分布</span>
          </h3>
          <div className="space-y-2.5">
            {sourceStats.map(stat => (
              <div key={stat.name} className="p-3.5 rounded-xl bg-slate-850/80 border border-slate-800 space-y-2 shadow-sm">
                <div className="flex items-center justify-between text-xs">
                  <span className="font-bold text-slate-200">{stat.name}</span>
                  <div className="space-x-3 font-mono text-slate-400">
                    <span>进度: {stat.answered}/{stat.total}</span>
                    <span>正确率: <strong className="text-blue-400">{stat.accuracy}%</strong></span>
                  </div>
                </div>

                <div className="w-full h-2 rounded-full bg-slate-800 overflow-hidden">
                  <div 
                    className="h-full bg-gradient-to-r from-blue-600 to-indigo-600 rounded-full transition-all duration-500"
                    style={{ width: `${stat.total > 0 ? (stat.answered / stat.total) * 100 : 0}%` }}
                  />
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Chapter Breakdown Progress Bars */}
        <div className="space-y-3.5">
          <h3 className="text-sm font-bold text-slate-200 flex items-center gap-2">
            <Layers className="w-4 h-4 text-cyan-400" />
            <span>七大章节考点掌握度</span>
          </h3>
          <div className="space-y-2.5">
            {chapterStats.map(stat => (
              <div key={stat.name} className="p-3.5 rounded-xl bg-slate-850/80 border border-slate-800 space-y-2 shadow-sm">
                <div className="flex items-center justify-between text-xs">
                  <span className="font-bold text-slate-200">{stat.name}</span>
                  <div className="space-x-3 font-mono text-slate-400">
                    <span>进度: {stat.answered}/{stat.total}</span>
                    <span>正确率: <strong className="text-emerald-400">{stat.accuracy}%</strong></span>
                  </div>
                </div>

                <div className="w-full h-2 rounded-full bg-slate-800 overflow-hidden">
                  <div 
                    className="h-full bg-gradient-to-r from-blue-500 to-teal-500 rounded-full transition-all duration-500"
                    style={{ width: `${stat.total > 0 ? (stat.answered / stat.total) * 100 : 0}%` }}
                  />
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Recent Exam History */}
        {examRecords.length > 0 && (
          <div className="space-y-3 pt-2">
            <h3 className="text-sm font-bold text-slate-200 flex items-center gap-2">
              <History className="w-4 h-4 text-blue-400" />
              <span>近期机考成绩记录</span>
            </h3>

            <div className="space-y-2 max-h-48 overflow-y-auto pr-1">
              {examRecords.slice(0, 5).map(record => (
                <div key={record.id} className="p-3 rounded-xl bg-slate-850/80 border border-slate-800 flex items-center justify-between text-xs shadow-sm">
                  <div>
                    <div className="font-bold text-slate-200">{record.title}</div>
                    <div className="text-slate-500 text-[11px] font-mono mt-0.5">{new Date(record.date).toLocaleString('zh-CN')}</div>
                  </div>
                  <div className="text-right">
                    <span className="font-mono font-black text-sm text-blue-400">{record.score}分</span>
                    <span className="text-slate-500 ml-2 font-mono">({record.correctCount}/{record.totalQuestions})</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

      </div>
    </div>
  );
};
