import React from 'react';
import { X, Keyboard, Zap } from 'lucide-react';

interface KeyboardHelpModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export const KeyboardHelpModal: React.FC<KeyboardHelpModalProps> = ({ isOpen, onClose }) => {
  if (!isOpen) return null;

  const shortcuts = [
    { key: '1 / 2 / 3 / 4 或 A / B / C / D', desc: '极速选择对应选项作答' },
    { key: 'J 或 ← (左箭头)', desc: '切换至上一题' },
    { key: 'K 或 → (右箭头)', desc: '切换至下一题' },
    { key: 'Space (空格键)', desc: '展开 / 收起原位题目解析' },
    { key: 'S', desc: '重点收藏本题 / 取消收藏' },
    { key: 'M', desc: '标记考点已攻克掌握 / 取消标记' },
    { key: 'C', desc: '原位复制 LaTeX 题面与完整解析至剪贴板' },
    { key: 'Enter (回车)', desc: '多选题提交答案' },
  ];

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md animate-fadeIn">
      <div className="bg-slate-900 border border-slate-800 border-t-2 border-t-blue-500 w-full max-w-lg rounded-3xl p-6 md:p-8 shadow-elevation-4 space-y-6">
        
        <div className="flex items-center justify-between pb-4 border-b border-slate-800">
          <div className="flex items-center gap-2.5">
            <div className="p-2.5 rounded-2xl bg-blue-500/10 text-blue-400 border border-blue-500/20">
              <Keyboard className="w-5 h-5" />
            </div>
            <div>
              <h2 className="text-lg font-black text-white tracking-tight">大观园 · 键盘盲操快捷键</h2>
              <p className="text-xs text-slate-400">专为沉浸式高强度刷题打造的高效热键体系</p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-2 rounded-xl text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="space-y-2">
          {shortcuts.map((sc, i) => (
            <div key={i} className="flex items-center justify-between p-3 rounded-xl bg-slate-850/80 border border-slate-800 shadow-sm">
              <div className="text-xs text-slate-200 font-medium">{sc.desc}</div>
              <kbd className="px-2.5 py-1 rounded-lg bg-slate-900 border border-slate-700/80 text-blue-400 font-mono text-xs font-bold shadow-sm">
                {sc.key}
              </kbd>
            </div>
          ))}
        </div>

        <div className="p-3.5 rounded-2xl bg-blue-950/40 border border-blue-500/20 text-xs text-blue-200 flex items-center gap-2.5 shadow-sm">
          <Zap className="w-4 h-4 text-blue-400 shrink-0" />
          <span>在输入框或便签编辑时，全局快捷键会自动禁用以防干扰文本输入。</span>
        </div>

      </div>
    </div>
  );
};
