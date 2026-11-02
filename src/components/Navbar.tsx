import React from 'react';
import { 
  Home,
  BookOpen, 
  Award, 
  AlertCircle, 
  Star, 
  Database, 
  BarChart3, 
  Keyboard, 
  Moon, 
  Sun,
  Sparkles
} from 'lucide-react';
import { StudyMode } from '../types';

interface NavbarProps {
  currentMode: StudyMode;
  onSelectMode: (mode: StudyMode) => void;
  wrongCount: number;
  favoriteCount: number;
  onOpenStats: () => void;
  onOpenShortcuts: () => void;
  isDark: boolean;
  onToggleTheme: () => void;
  totalAnswered: number;
  todayCount: number;
}

export const Navbar: React.FC<NavbarProps> = ({
  currentMode,
  onSelectMode,
  wrongCount,
  favoriteCount,
  onOpenStats,
  onOpenShortcuts,
  isDark,
  onToggleTheme,
  todayCount
}) => {
  return (
    <header className="sticky top-0 z-40 w-full border-b border-slate-200 dark:border-slate-800 bg-white/95 dark:bg-slate-900/90 backdrop-blur-md transition-colors duration-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          
          {/* Logo & Platform Name */}
          <div className="flex items-center gap-3">
            <div 
              onClick={() => onSelectMode('home')}
              className="flex items-center gap-2.5 cursor-pointer group"
              title="返回大观园首页"
            >
              <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-blue-600 to-indigo-600 flex items-center justify-center shadow-md shadow-blue-500/20 group-hover:scale-105 transition-transform">
                <Sparkles className="w-4 h-4 text-white" />
              </div>
              <div>
                <div className="flex items-center gap-2">
                  <span className="font-bold text-base tracking-tight text-slate-900 dark:text-white group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">
                    大观园 · 信号与系统
                  </span>
                  <span className="text-[10px] font-semibold px-2 py-0.5 rounded-full bg-blue-500/10 text-blue-600 dark:text-blue-300 border border-blue-500/20">
                    广工837/809
                  </span>
                </div>
                <div className="text-[11px] text-slate-500 dark:text-slate-400 hidden sm:block">
                  考研真题与经典题库 · 智能刷题与错题攻坚系统
                </div>
              </div>
            </div>
          </div>

          {/* Navigation Modes - Consistent active state per Refactoring UI §2.8 */}
          <nav className="hidden md:flex items-center gap-1 bg-slate-100 dark:bg-slate-950/60 p-1 rounded-xl border border-slate-200 dark:border-slate-800">
            <button
              onClick={() => onSelectMode('home')}
              className={`flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                currentMode === 'home'
                  ? 'bg-blue-600 text-white shadow-sm shadow-blue-600/30'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 hover:bg-slate-200/60 dark:hover:bg-slate-800/60'
              }`}
            >
              <Home className="w-3.5 h-3.5" />
              <span>首页看板</span>
            </button>
            <button
              onClick={() => onSelectMode('chapter')}
              className={`flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                currentMode === 'chapter'
                  ? 'bg-blue-600 text-white shadow-sm shadow-blue-600/30'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 hover:bg-slate-200/60 dark:hover:bg-slate-800/60'
              }`}
            >
              <BookOpen className="w-3.5 h-3.5" />
              <span>章节专项</span>
            </button>

            <button
              onClick={() => onSelectMode('exam')}
              className={`flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                currentMode === 'exam'
                  ? 'bg-blue-600 text-white shadow-sm shadow-blue-600/30'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 hover:bg-slate-200/60 dark:hover:bg-slate-800/60'
              }`}
            >
              <Award className="w-3.5 h-3.5" />
              <span>模拟机考</span>
            </button>

            <button
              onClick={() => onSelectMode('wrong')}
              className={`relative flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                currentMode === 'wrong'
                  ? 'bg-blue-600 text-white shadow-sm shadow-blue-600/30'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 hover:bg-slate-200/60 dark:hover:bg-slate-800/60'
              }`}
            >
              <AlertCircle className="w-3.5 h-3.5" />
              <span>错题攻坚</span>
              {wrongCount > 0 && (
                <span className="px-1.5 py-0.2 text-[10px] rounded-full bg-rose-500/25 text-rose-500 dark:text-rose-300 border border-rose-500/30 font-bold">
                  {wrongCount}
                </span>
              )}
            </button>

            <button
              onClick={() => onSelectMode('favorite')}
              className={`relative flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                currentMode === 'favorite'
                  ? 'bg-blue-600 text-white shadow-sm shadow-blue-600/30'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 hover:bg-slate-200/60 dark:hover:bg-slate-800/60'
              }`}
            >
              <Star className="w-3.5 h-3.5" />
              <span>收藏标记</span>
              {favoriteCount > 0 && (
                <span className="px-1.5 py-0.2 text-[10px] rounded-full bg-amber-500/25 text-amber-500 dark:text-amber-300 border border-amber-500/30 font-bold">
                  {favoriteCount}
                </span>
              )}
            </button>

            <button
              onClick={() => onSelectMode('manage')}
              className={`flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                currentMode === 'manage'
                  ? 'bg-blue-600 text-white shadow-sm shadow-blue-600/30'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 hover:bg-slate-200/60 dark:hover:bg-slate-800/60'
              }`}
              title="用户喂题、导入题库与备份中心"
            >
              <Database className="w-3.5 h-3.5 text-emerald-500" />
              <span>题库中心</span>
            </button>
          </nav>

          {/* Right Action Tools */}
          <div className="flex items-center gap-2">
            {/* Today's count pill */}
            <div className="hidden lg:flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-100 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700/60 text-xs text-slate-700 dark:text-slate-300">
              <span className="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
              <span>今日刷题:</span>
              <strong className="text-emerald-600 dark:text-emerald-400 font-bold">{todayCount}</strong>
            </div>

            {/* Stats Button */}
            <button
              onClick={onOpenStats}
              title="学情统计与掌握度全景"
              className="p-2 rounded-lg text-slate-500 hover:text-slate-900 dark:text-slate-400 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
            >
              <BarChart3 className="w-5 h-5" />
            </button>

            {/* Shortcuts Guide Button */}
            <button
              onClick={onOpenShortcuts}
              title="键盘快捷键指引 (1/2/3/4, Space, J/K)"
              className="p-2 rounded-lg text-slate-500 hover:text-slate-900 dark:text-slate-400 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors hidden sm:block"
            >
              <Keyboard className="w-5 h-5" />
            </button>

            {/* Theme Toggle Button */}
            <button
              onClick={onToggleTheme}
              title={isDark ? "切换为白天光明模式" : "切换为夜晚黑暗模式"}
              className="p-2 rounded-lg text-slate-500 hover:text-slate-900 dark:text-slate-400 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
            >
              {isDark ? <Sun className="w-5 h-5 text-amber-400" /> : <Moon className="w-5 h-5 text-slate-700" />}
            </button>
          </div>

        </div>

        {/* Mobile secondary navigation */}
        <div className="flex md:hidden overflow-x-auto py-2.5 gap-2 border-t border-slate-200 dark:border-slate-800/80 no-scrollbar">
          <button
            onClick={() => onSelectMode('chapter')}
            className={`px-3 py-1.5 rounded-xl text-xs font-semibold whitespace-nowrap flex items-center gap-1.5 transition-all ${
              currentMode === 'chapter' ? 'bg-blue-600 text-white shadow-sm' : 'bg-slate-100 dark:bg-slate-850 border border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400'
            }`}
          >
            <BookOpen className="w-3.5 h-3.5" /> 章节专项
          </button>
          <button
            onClick={() => onSelectMode('exam')}
            className={`px-3 py-1.5 rounded-xl text-xs font-semibold whitespace-nowrap flex items-center gap-1.5 transition-all ${
              currentMode === 'exam' ? 'bg-blue-600 text-white shadow-sm' : 'bg-slate-100 dark:bg-slate-850 border border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400'
            }`}
          >
            <Award className="w-3.5 h-3.5" /> 模拟机考
          </button>
          <button
            onClick={() => onSelectMode('wrong')}
            className={`px-3 py-1.5 rounded-xl text-xs font-semibold whitespace-nowrap flex items-center gap-1.5 transition-all ${
              currentMode === 'wrong' ? 'bg-blue-600 text-white shadow-sm' : 'bg-slate-100 dark:bg-slate-850 border border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400'
            }`}
          >
            <AlertCircle className="w-3.5 h-3.5 text-rose-500" /> 错题 {wrongCount > 0 && `(${wrongCount})`}
          </button>
          <button
            onClick={() => onSelectMode('favorite')}
            className={`px-3 py-1.5 rounded-xl text-xs font-semibold whitespace-nowrap flex items-center gap-1.5 transition-all ${
              currentMode === 'favorite' ? 'bg-blue-600 text-white shadow-sm' : 'bg-slate-100 dark:bg-slate-850 border border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400'
            }`}
          >
            <Star className="w-3.5 h-3.5 text-amber-500" /> 收藏 {favoriteCount > 0 && `(${favoriteCount})`}
          </button>
          <button
            onClick={() => onSelectMode('manage')}
            className={`px-3 py-1.5 rounded-xl text-xs font-semibold whitespace-nowrap flex items-center gap-1.5 transition-all ${
              currentMode === 'manage' ? 'bg-blue-600 text-white shadow-sm' : 'bg-slate-100 dark:bg-slate-850 border border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400'
            }`}
          >
            <Database className="w-3.5 h-3.5 text-emerald-500" /> 题库管理
          </button>
        </div>
      </div>
    </header>
  );
};
