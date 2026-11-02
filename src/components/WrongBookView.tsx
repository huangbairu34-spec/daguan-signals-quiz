import React, { useState, useMemo } from 'react';
import { Question, UserQuestionProgress } from '../types';
import { exportQuestionsToAnkiTsv } from '../utils/storage';
import { getQuestionSourceCategory, STANDARD_SOURCES } from '../utils/sourceHelper';
import { MathRenderer } from './MathRenderer';
import { 
  AlertCircle, 
  CheckCircle2, 
  Filter, 
  RotateCcw, 
  Check, 
  Trash2,
  FileSpreadsheet
} from 'lucide-react';

interface WrongBookViewProps {
  questions: Question[];
  progress: Record<string, UserQuestionProgress>;
  onToggleMastered: (questionId: string) => void;
  onJumpToPractice: (questionId: string) => void;
  onClearWrongStatus: (questionId: string) => void;
}

export const WrongBookView: React.FC<WrongBookViewProps> = ({
  questions,
  progress,
  onToggleMastered,
  onJumpToPractice,
  onClearWrongStatus
}) => {
  const [selectedSource, setSelectedSource] = useState<string>('ALL');
  const [onlyUnmastered, setOnlyUnmastered] = useState<boolean>(true);
  const [expandedId, setExpandedId] = useState<string | null>(null);

  // All wrong questions
  const wrongQuestions = useMemo(() => {
    return questions.filter(q => {
      const p = progress[q.id];
      if (!p || p.isCorrect !== false) return false;
      if (selectedSource !== 'ALL' && getQuestionSourceCategory(q.source) !== selectedSource) return false;
      if (onlyUnmastered && p.isMastered) return false;
      return true;
    });
  }, [questions, progress, selectedSource, onlyUnmastered]);

  const masteredCount = useMemo(() => {
    return questions.filter(q => {
      const p = progress[q.id];
      return p && p.wrongCount > 0 && p.isMastered;
    }).length;
  }, [questions, progress]);

  const totalWrongEver = useMemo(() => {
    return questions.filter(q => {
      const p = progress[q.id];
      return p && p.wrongCount > 0;
    }).length;
  }, [questions, progress]);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 space-y-6">
      
      {/* Header Banner */}
      <div className="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-slate-800 border-t-2 border-t-rose-500 shadow-elevation-2 relative overflow-hidden backdrop-blur-xl space-y-6">
        <div className="flex flex-wrap items-center justify-between gap-6">
          <div className="space-y-2">
            <div className="flex items-center gap-2.5">
              <span className="p-2.5 rounded-2xl bg-rose-500/10 text-rose-400 border border-rose-500/20">
                <AlertCircle className="w-5 h-5" />
              </span>
              <h1 className="text-xl md:text-2xl font-black text-white tracking-tight">
                错题攻坚本 · 专项突破
              </h1>
            </div>
            <p className="text-slate-400 text-sm max-w-2xl leading-relaxed">
              集中攻克做题薄弱盲区。系统根据您的做题历史自动汇聚错题，支持标记“已彻底掌握”归档，并可一键导出为 Anki 记忆闪卡，随时随地利用碎片时间复习背诵。
            </p>
          </div>

          {/* Quick Anki Export Button */}
          <div className="flex flex-wrap items-center gap-3">
            <button
              onClick={() => exportQuestionsToAnkiTsv(wrongQuestions)}
              disabled={wrongQuestions.length === 0}
              className="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-750 text-slate-200 border border-slate-700/80 font-semibold text-xs flex items-center gap-2 transition-all shadow-sm active:translate-y-0.5 disabled:opacity-40 disabled:cursor-not-allowed"
              title="导出当前筛选出的错题为 Anki 格式"
            >
              <FileSpreadsheet className="w-4 h-4 text-rose-400" />
              <span>导出为 Anki 闪卡卡片</span>
            </button>
          </div>
        </div>

        {/* Mini Stats Bar */}
        <div className="pt-5 border-t border-slate-800/80 grid grid-cols-1 sm:grid-cols-3 gap-4 max-w-xl">
          <div className="p-3.5 rounded-2xl bg-slate-850/70 border border-slate-800/80">
            <div className="text-[11px] text-slate-400 font-medium">当前待攻克</div>
            <div className="text-2xl font-black text-rose-400 font-mono mt-0.5">{wrongQuestions.length}</div>
          </div>
          <div className="p-3.5 rounded-2xl bg-slate-850/70 border border-slate-800/80">
            <div className="text-[11px] text-slate-400 font-medium">已攻破掌握</div>
            <div className="text-2xl font-black text-emerald-400 font-mono mt-0.5">{masteredCount}</div>
          </div>
          <div className="p-3.5 rounded-2xl bg-slate-850/70 border border-slate-800/80">
            <div className="text-[11px] text-slate-400 font-medium">累计错题库</div>
            <div className="text-2xl font-black text-slate-200 font-mono mt-0.5">{totalWrongEver}</div>
          </div>
        </div>
      </div>

      {/* Filter Bar */}
      <div className="flex flex-wrap items-center justify-between gap-4 p-4 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-sm">
        <div className="flex items-center gap-3">
          <Filter className="w-4 h-4 text-rose-400" />
          <select
            value={selectedSource}
            onChange={(e) => setSelectedSource(e.target.value)}
            className="bg-slate-850 text-slate-200 text-xs rounded-xl px-3.5 py-2 border border-slate-700/80 focus:outline-none focus:border-rose-500 font-medium"
          >
            <option value="ALL">全部错题来源</option>
            {STANDARD_SOURCES.map(s => (
              <option key={s} value={s}>{s}</option>
            ))}
          </select>

          <label className="flex items-center gap-2 text-xs text-slate-300 cursor-pointer ml-2">
            <input
              type="checkbox"
              checked={onlyUnmastered}
              onChange={(e) => setOnlyUnmastered(e.target.checked)}
              className="rounded bg-slate-800 border-slate-700 text-rose-500 focus:ring-0"
            />
            <span>仅显示未掌握题目</span>
          </label>
        </div>

        <div className="text-xs text-slate-400 font-mono">
          共收录 <strong className="text-rose-400 font-bold">{wrongQuestions.length}</strong> 道错题
        </div>
      </div>

      {/* Wrong Questions List */}
      <div className="space-y-4">
        {wrongQuestions.map((q, idx) => {
          const p = progress[q.id];
          const isExpanded = expandedId === q.id;

          return (
            <div
              key={q.id}
              className="bg-slate-900/95 border border-slate-800 rounded-2xl p-6 transition-all hover:border-slate-700/80 space-y-4 shadow-sm"
            >
              {/* Question Header */}
              <div className="flex flex-wrap items-center justify-between gap-3">
                <div className="flex items-center gap-2.5">
                  <span className="font-mono font-bold text-xs text-slate-500">#{idx + 1}</span>
                  <span className="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-rose-500/10 text-rose-300 border border-rose-500/25">
                    {getQuestionSourceCategory(q.source)}
                  </span>
                  <span className="text-xs text-slate-400">{q.chapter}</span>
                  {p?.wrongCount && p.wrongCount > 1 && (
                    <span className="px-2 py-0.5 rounded-md bg-rose-950/90 text-rose-300 border border-rose-800/80 text-[11px] font-bold">
                      曾错 {p.wrongCount} 次
                    </span>
                  )}
                </div>

                <div className="flex items-center gap-2">
                  <button
                    onClick={() => onToggleMastered(q.id)}
                    className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold transition-all ${
                      p?.isMastered
                        ? 'bg-emerald-600/20 text-emerald-400 border border-emerald-500/40'
                        : 'bg-slate-850 hover:bg-slate-800 text-slate-300 border border-slate-700/70'
                    }`}
                  >
                    <Check className="w-3.5 h-3.5" />
                    <span>{p?.isMastered ? '已标记掌握' : '标记已掌握'}</span>
                  </button>

                  <button
                    onClick={() => onJumpToPractice(q.id)}
                    className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl text-xs font-bold bg-blue-600 hover:bg-blue-500 text-white transition-all shadow-sm active:translate-y-0.5"
                    title="跳转到做题台进行重做练习"
                  >
                    <RotateCcw className="w-3.5 h-3.5" />
                    <span>进入重测</span>
                  </button>

                  <button
                    onClick={() => onClearWrongStatus(q.id)}
                    className="p-1.5 rounded-xl text-slate-500 hover:text-rose-400 hover:bg-slate-800/80 transition-colors"
                    title="从错题本中移除"
                  >
                    <Trash2 className="w-4 h-4" />
                  </button>
                </div>
              </div>

              {/* Stem */}
              <div className="text-sm md:text-base leading-relaxed text-slate-100 font-normal">
                <MathRenderer content={q.stem} />
              </div>

              {/* Options */}
              {q.options && (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-2.5 text-xs">
                  {q.options.map(opt => (
                    <div key={opt.key} className="p-3 rounded-xl bg-slate-850/80 border border-slate-800 text-slate-200 flex items-start gap-2.5">
                      <span className="font-bold text-slate-400 font-mono">{opt.key}.</span>
                      <MathRenderer content={opt.text} inline />
                    </div>
                  ))}
                </div>
              )}

              {/* Footer info & Toggle Analysis */}
              <div className="pt-2 flex flex-wrap items-center justify-between gap-3 text-xs border-t border-slate-800/80">
                <div className="flex items-center gap-4 text-slate-400">
                  <span>正确答案: <strong className="text-emerald-400 font-mono text-sm tracking-wide">{Array.isArray(q.answer) ? q.answer.join(', ') : q.answer}</strong></span>
                  {p?.selectedAnswer && (
                    <span>您的曾选: <strong className="text-rose-400 font-mono">{Array.isArray(p.selectedAnswer) ? p.selectedAnswer.join(', ') : p.selectedAnswer}</strong></span>
                  )}
                </div>

                <button
                  onClick={() => setExpandedId(isExpanded ? null : q.id)}
                  className="text-xs text-blue-400 hover:text-blue-300 font-semibold"
                >
                  {isExpanded ? '收起解析 ▲' : '查看完整解析 ▼'}
                </button>
              </div>

              {/* Expanded Analysis */}
              {isExpanded && (
                <div className="p-4 rounded-xl bg-slate-925 border border-slate-800 text-xs md:text-sm text-slate-200 leading-relaxed animate-fadeIn shadow-inner space-y-2">
                  <div className="font-bold text-slate-100 flex items-center gap-2">
                    <span className="w-2 h-2 rounded-full bg-blue-500"></span>
                    <span>大观园权威解题步骤：</span>
                  </div>
                  <MathRenderer content={q.analysis} />
                </div>
              )}
            </div>
          );
        })}

        {wrongQuestions.length === 0 && (
          <div className="bg-slate-900 border border-slate-800 rounded-3xl p-16 text-center space-y-5 shadow-elevation-1">
            <div className="w-16 h-16 rounded-2xl bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 flex items-center justify-center mx-auto shadow-sm">
              <CheckCircle2 className="w-8 h-8" />
            </div>
            <div className="space-y-1">
              <h3 className="text-lg font-bold text-slate-100">暂无待攻克的错题！</h3>
              <p className="text-sm text-slate-400 max-w-md mx-auto">
                太棒了！您当前没有未攻克的错题记录，或者所有错题均已被标记掌握。继续在「章节专项」或「模拟机考」中刷题挑战吧！
              </p>
            </div>
          </div>
        )}
      </div>

    </div>
  );
};
