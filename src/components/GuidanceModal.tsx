import React, { useState } from 'react';
import { X, Sparkles, BookOpen, Lightbulb } from 'lucide-react';
import { Question } from '../types';
import { MathRenderer } from './MathRenderer';

interface GuidanceModalProps {
  isOpen: boolean;
  onClose: () => void;
  currentQuestion: Question | null;
  isDark: boolean;
}

export const GuidanceModal: React.FC<GuidanceModalProps> = ({
  isOpen,
  onClose,
  currentQuestion
}) => {
  if (!isOpen) return null;

  const [activeTab, setActiveTab] = useState<'current' | 'cheatsheet' | 'shortcuts'>('current');

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm animate-fadeIn">
      <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 w-full max-w-3xl max-h-[85vh] rounded-3xl shadow-2xl flex flex-col overflow-hidden">
        
        {/* Header */}
        <div className="px-6 py-4 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="p-2 rounded-xl bg-purple-50 dark:bg-purple-950/60 text-purple-600 dark:text-purple-400">
              <Sparkles className="w-5 h-5" />
            </div>
            <div>
              <h3 className="font-bold text-base text-slate-800 dark:text-slate-100">
                大观园 · 考点辅导与公式速查
              </h3>
              <p className="text-xs text-slate-400">
                针对当前考点的解题提示、公式推演要点与系统图谱
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            {/* Tabs */}
            <div className="flex items-center gap-1 bg-slate-100 dark:bg-slate-800 p-1 rounded-xl text-xs font-semibold mr-2">
              <button
                onClick={() => setActiveTab('current')}
                className={`px-3 py-1 rounded-lg transition-all ${
                  activeTab === 'current'
                    ? 'bg-white dark:bg-slate-700 text-purple-600 dark:text-white shadow-sm'
                    : 'text-slate-500 hover:text-slate-900 dark:hover:text-white'
                }`}
              >
                本题解题思路
              </button>
              <button
                onClick={() => setActiveTab('cheatsheet')}
                className={`px-3 py-1 rounded-lg transition-all ${
                  activeTab === 'cheatsheet'
                    ? 'bg-white dark:bg-slate-700 text-purple-600 dark:text-white shadow-sm'
                    : 'text-slate-500 hover:text-slate-900 dark:hover:text-white'
                }`}
              >
                核心公式宝典
              </button>
              <button
                onClick={() => setActiveTab('shortcuts')}
                className={`px-3 py-1 rounded-lg transition-all ${
                  activeTab === 'shortcuts'
                    ? 'bg-white dark:bg-slate-700 text-purple-600 dark:text-white shadow-sm'
                    : 'text-slate-500 hover:text-slate-900 dark:hover:text-white'
                }`}
              >
                极速快捷键
              </button>
            </div>

            <button
              onClick={onClose}
              className="p-2 rounded-xl text-slate-400 hover:text-slate-700 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Body */}
        <div className="flex-1 overflow-y-auto p-6 space-y-6 text-sm text-slate-700 dark:text-slate-200">
          
          {/* Tab 1: Current Question Guidance */}
          {activeTab === 'current' && (
            <div className="space-y-4">
              {currentQuestion ? (
                <>
                  <div className="p-4 rounded-2xl bg-purple-50 dark:bg-purple-950/30 border border-purple-200 dark:border-purple-800/40 space-y-2">
                    <div className="flex items-center gap-2 font-bold text-purple-700 dark:text-purple-300 text-sm">
                      <Lightbulb className="w-4 h-4" />
                      <span>所属章节考点：{currentQuestion.chapter}</span>
                    </div>
                    <div className="text-xs text-purple-800 dark:text-purple-200/90 leading-relaxed">
                      {currentQuestion.section && <div><strong>核心模块：</strong>{currentQuestion.section}</div>}
                      <div><strong>出题来源：</strong>{currentQuestion.source}</div>
                      <div><strong>知识点标签：</strong>{currentQuestion.tags.join(' · ')}</div>
                    </div>
                  </div>

                  {/* Hints */}
                  <div className="space-y-3">
                    <h4 className="font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2">
                      <BookOpen className="w-4 h-4 text-blue-500" />
                      <span>广工高频命题突破要诀：</span>
                    </h4>
                    <div className="p-4 rounded-2xl bg-slate-50 dark:bg-slate-850/80 border border-slate-200 dark:border-slate-800 space-y-2 text-xs leading-relaxed">
                      <div>
                        1. <strong>时域分析破题点</strong>：求解零输入响应看特征根，求解零状态响应看卷积积分 <MathRenderer content="$y_{zs}(t) = f(t) * h(t)$" inline />。
                      </div>
                      <div>
                        2. <strong>频域与傅里叶变换</strong>：时域相乘等于频域卷积除以 <MathRenderer content="$2\pi$" inline />；时移对应相位线性变化 <MathRenderer content="$e^{-j\omega t_0}$" inline />，幅频响应不变。
                      </div>
                      <div>
                        3. <strong>复频域与因果稳定性</strong>：连续系统因果稳定的充要条件是系统函数 <MathRenderer content="$H(s)$" inline /> 的所有极点均位于 <MathRenderer content="$s$" inline /> 平面左半开平面（<MathRenderer content="$\text{Re}(s_p) < 0$" inline />）。
                      </div>
                      <div>
                        4. <strong>离散与Z变换</strong>：因果稳定系统所有极点必须严格落在单位圆内（<MathRenderer content="$|z_p| < 1$" inline />）。
                      </div>
                    </div>
                  </div>
                </>
              ) : (
                <div className="text-center py-12 text-slate-400">
                  当前暂未选定题目
                </div>
              )}
            </div>
          )}

          {/* Tab 2: Signals & Systems Cheatsheet */}
          {activeTab === 'cheatsheet' && (
            <div className="space-y-4">
              <div className="p-4 rounded-2xl bg-slate-50 dark:bg-slate-850/80 border border-slate-200 dark:border-slate-800 space-y-3">
                <h4 className="font-bold text-sm text-blue-600 dark:text-blue-400">1. 常用连续傅里叶变换对</h4>
                <div className="space-y-1 text-xs">
                  <div>• <MathRenderer content="$\delta(t) \leftrightarrow 1$" inline /></div>
                  <div>• <MathRenderer content="$1 \leftrightarrow 2\pi\delta(\omega)$" inline /></div>
                  <div>• <MathRenderer content="$u(t) \leftrightarrow \pi\delta(\omega) + \frac{1}{j\omega}$" inline /></div>
                  <div>• <MathRenderer content="$e^{-at}u(t) \leftrightarrow \frac{1}{a + j\omega} \quad (a > 0)$" inline /></div>
                  <div>• <MathRenderer content="$\text{rect}(\frac{t}{\tau}) \leftrightarrow \tau \text{Sa}(\frac{\omega\tau}{2})$" inline /></div>
                </div>
              </div>

              <div className="p-4 rounded-2xl bg-slate-50 dark:bg-slate-850/80 border border-slate-200 dark:border-slate-800 space-y-3">
                <h4 className="font-bold text-sm text-emerald-600 dark:text-emerald-400">2. 常用单边拉普拉斯变换对</h4>
                <div className="space-y-1 text-xs">
                  <div>• <MathRenderer content="$\delta(t) \leftrightarrow 1, \quad \text{ROC: 全平面}$" inline /></div>
                  <div>• <MathRenderer content="$u(t) \leftrightarrow \frac{1}{s}, \quad \text{ROC: } \text{Re}(s) > 0$" inline /></div>
                  <div>• <MathRenderer content="$e^{-at}u(t) \leftrightarrow \frac{1}{s + a}, \quad \text{ROC: } \text{Re}(s) > -a$" inline /></div>
                  <div>• <MathRenderer content="$t u(t) \leftrightarrow \frac{1}{s^2}$" inline /></div>
                  <div>• <MathRenderer content="$\cos(\omega_0 t)u(t) \leftrightarrow \frac{s}{s^2 + \omega_0^2}$" inline /></div>
                </div>
              </div>

              <div className="p-4 rounded-2xl bg-slate-50 dark:bg-slate-850/80 border border-slate-200 dark:border-slate-800 space-y-3">
                <h4 className="font-bold text-sm text-amber-600 dark:text-amber-400">3. 时域抽样定理</h4>
                <div className="text-xs leading-relaxed">
                  <MathRenderer content="对于最高截止角频率为 $\omega_m$ 的带限连续信号 $f(t)$，抽样角频率 $\omega_s \ge 2\omega_m$（即抽样频率 $f_s \ge 2f_m$）时，信号可以通过理想低通滤波器无失真恢复，奈奎斯特抽样间隔为 $T_s \le \frac{\pi}{\omega_m}$。" />
                </div>
              </div>
            </div>
          )}

          {/* Tab 3: Shortcuts */}
          {activeTab === 'shortcuts' && (
            <div className="space-y-2">
              {[
                { k: '1 / 2 / 3 / 4 或 A / B / C / D', d: '选择对应选项作答' },
                { k: 'J 或 ← (左箭头)', d: '切换至上一题' },
                { k: 'K 或 → (右箭头)', d: '切换至下一题' },
                { k: 'Space (空格键)', d: '一键展开 / 收起题目解析' },
                { k: 'S', d: '收藏本题 / 取消收藏' },
                { k: 'M', d: '标记考点攻克掌握' },
                { k: 'C', d: '复制题目 LaTeX 题面至剪贴板' },
              ].map((s, idx) => (
                <div key={idx} className="flex items-center justify-between p-3 rounded-xl bg-slate-50 dark:bg-slate-850/70 border border-slate-200 dark:border-slate-800 text-xs">
                  <span className="text-slate-700 dark:text-slate-300">{s.d}</span>
                  <kbd className="px-2 py-0.5 rounded-md bg-white dark:bg-slate-800 border border-slate-300 dark:border-slate-700 text-blue-600 dark:text-blue-400 font-mono font-bold">
                    {s.k}
                  </kbd>
                </div>
              ))}
            </div>
          )}

        </div>

      </div>
    </div>
  );
};
