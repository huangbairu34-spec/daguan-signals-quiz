import React, { useState } from 'react';
import { 
  Question, 
  QuestionType 
} from '../types';
import { 
  parseMarkdownQuestions, 
  exportQuestionsToJsonFile, 
  resetToDefaultQuestions 
} from '../utils/storage';
import { 
  Upload, 
  Download, 
  PlusCircle, 
  Trash2, 
  RotateCcw, 
  FileText, 
  Check, 
  AlertCircle, 
  Code,
  Search,
  Sparkles
} from 'lucide-react';

interface QuestionManagerViewProps {
  questions: Question[];
  onUpdateQuestions: (newQuestions: Question[]) => void;
}

export const QuestionManagerView: React.FC<QuestionManagerViewProps> = ({
  questions,
  onUpdateQuestions
}) => {
  const [activeTab, setActiveTab] = useState<'text' | 'json' | 'manual' | 'list'>('text');
  
  // Text import state
  const [markdownInput, setMarkdownInput] = useState<string>('');
  const [defaultSubjectInput, setDefaultSubjectInput] = useState<string>('广工837/809-信号与系统');
  const [textParseFeedback, setTextParseFeedback] = useState<{ count: number; error?: string } | null>(null);

  // JSON import state
  const [jsonInput, setJsonInput] = useState<string>('');
  const [jsonError, setJsonError] = useState<string>('');

  // Single Question Form State
  const [manualForm, setManualForm] = useState<Partial<Question>>({
    subject: '广工837/809-信号与系统',
    chapter: '第一章：信号与系统基础',
    type: 'single',
    difficulty: 3,
    tags: ['强化训练', '经典考点'],
    stem: '',
    options: [
      { key: 'A', text: '' },
      { key: 'B', text: '' },
      { key: 'C', text: '' },
      { key: 'D', text: '' },
    ],
    answer: 'A',
    analysis: '',
  });

  // Question list filter
  const [searchKeyword, setSearchKeyword] = useState<string>('');
  const [filterSubject, setFilterSubject] = useState<string>('ALL');

  // Sample Markdown Template
  const sampleMarkdown = `### 题目 1 [单选]
学科: 广工837/809-信号与系统
章节: 第一章：信号与系统基础
难度: 3
标签: 冲激偶函数, 微分性质, 高频考点
题干:
计算广义定积分 $\\int_{-\\infty}^{+\\infty} (1 - x)\\delta'(x) \\, dx$ 的数值为：
A. -1
B. 0
C. 1
D. 2
答案: C
解析:
由冲激偶函数 $\\delta'(t)$ 的导数筛选性质：
$$\\int_{-\\infty}^{+\\infty} f(t)\\delta'(t) \\, dt = -f'(0)$$
在本题中，设 $f(x) = 1 - x$，对 $x$ 求导得到：
$$f'(x) = -1 \\implies f'(0) = -1$$
代入积分公式得：
$$\\int_{-\\infty}^{+\\infty} (1 - x)\\delta'(x) \\, dx = -(-1) = 1$$
故正确答案为 C。

---

### 题目 2 [判断]
学科: 广工837/809-信号与系统
章节: 第五章：Z变换与离散系统
难度: 2
标签: 稳定性, 因果系统, 单位圆
题干:
线性时不变（LTI）因果离散系统稳定的充分必要条件是系统函数 $H(z)$ 的所有极点都严格落在单位圆内（即 $|z_p| < 1$）。
A. 正确（True）
B. 错误（False）
答案: A
解析:
因果离散系统的收敛域 ROC 为外域 $|z| > \\max_i |z_i|$。
而系统稳定的充要条件是收敛域 ROC 包含单位圆 $|z| = 1$。
两者同时满足当且仅当系统所有极点均位于单位圆内部（模长严格小于 1）。故本题陈述正确。
`;

  // Handle Markdown Import
  const handleParseText = () => {
    if (!markdownInput.trim()) {
      setTextParseFeedback({ count: 0, error: '请先粘贴或输入题目文本内容！' });
      return;
    }
    const parsed = parseMarkdownQuestions(markdownInput, defaultSubjectInput);
    if (parsed.length === 0) {
      setTextParseFeedback({ count: 0, error: '未能识别出题目，请检查格式或参考示例模板。' });
    } else {
      setTextParseFeedback({ count: parsed.length });
    }
  };

  const handleApplyTextImport = () => {
    if (!markdownInput.trim()) return;
    const parsed = parseMarkdownQuestions(markdownInput, defaultSubjectInput);
    if (parsed.length > 0) {
      const merged = [...parsed, ...questions];
      onUpdateQuestions(merged);
      setMarkdownInput('');
      setTextParseFeedback(null);
      alert(`🎉 成功导入并入库 ${parsed.length} 道题目！您可以在章节专项或题库列表中立即开始刷题！`);
      setActiveTab('list');
    }
  };

  // Handle JSON Import
  const handleImportJson = () => {
    setJsonError('');
    try {
      const parsed = JSON.parse(jsonInput);
      if (!Array.isArray(parsed)) {
        setJsonError('JSON 必须为题目数组 (Array)');
        return;
      }
      if (parsed.length === 0) {
        setJsonError('题目数组为空');
        return;
      }
      const merged = [...parsed, ...questions];
      onUpdateQuestions(merged);
      setJsonInput('');
      alert(`🎉 成功导入 ${parsed.length} 道 JSON 题目！`);
      setActiveTab('list');
    } catch (err: any) {
      setJsonError(`JSON 语法解析错误: ${err.message}`);
    }
  };

  // Handle Manual Form Submission
  const handleSaveManual = () => {
    if (!manualForm.stem?.trim()) {
      alert('请填写题干内容！');
      return;
    }
    const newQ: Question = {
      id: `manual-${Date.now()}-${Math.random().toString(36).slice(2, 6)}`,
      subject: manualForm.subject || '专业课综合',
      chapter: manualForm.chapter || '未分类考点',
      type: manualForm.type || 'single',
      difficulty: manualForm.difficulty || 3,
      tags: manualForm.tags || ['自编习题'],
      stem: manualForm.stem || '',
      options: manualForm.type !== 'subjective' ? manualForm.options : undefined,
      answer: manualForm.answer || 'A',
      analysis: manualForm.analysis || '暂无解析',
      source: '手动录入'
    };

    onUpdateQuestions([newQ, ...questions]);
    alert('🎉 题目录入成功！');
    setManualForm({
      subject: manualForm.subject,
      chapter: manualForm.chapter,
      type: 'single',
      difficulty: 3,
      tags: ['自编习题'],
      stem: '',
      options: [
        { key: 'A', text: '' },
        { key: 'B', text: '' },
        { key: 'C', text: '' },
        { key: 'D', text: '' },
      ],
      answer: 'A',
      analysis: '',
    });
    setActiveTab('list');
  };

  // Delete single question
  const handleDeleteQuestion = (id: string) => {
    if (confirm('确定要删除这道题目吗？')) {
      onUpdateQuestions(questions.filter(q => q.id !== id));
    }
  };

  // Reset to default
  const handleResetDefaults = () => {
    if (confirm('警告：此操作将清空所有自定义题目，恢复为系统初始的广工837/809信号与系统权威真题题库，是否继续？')) {
      const defs = resetToDefaultQuestions();
      onUpdateQuestions(defs);
      alert('已恢复为官方题库！');
    }
  };

  // Filter list
  const filteredList = questions.filter(q => {
    if (filterSubject !== 'ALL' && q.subject !== filterSubject) return false;
    if (searchKeyword.trim()) {
      const kw = searchKeyword.toLowerCase();
      const matchStem = q.stem.toLowerCase().includes(kw);
      const matchChapter = q.chapter.toLowerCase().includes(kw);
      const matchSubject = q.subject.toLowerCase().includes(kw);
      return matchStem || matchChapter || matchSubject;
    }
    return true;
  });

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 space-y-6">
      
      {/* Header Banner */}
      <div className="p-6 md:p-8 rounded-3xl bg-slate-900/95 border border-slate-800 border-t-2 border-t-blue-500 shadow-elevation-2 relative overflow-hidden backdrop-blur-xl">
        <div className="relative z-10 flex flex-wrap items-center justify-between gap-6">
          <div className="space-y-2">
            <div className="flex items-center gap-2.5">
              <span className="p-2.5 rounded-2xl bg-blue-500/10 text-blue-400 border border-blue-500/20">
                <Sparkles className="w-5 h-5" />
              </span>
              <h1 className="text-xl md:text-2xl font-black text-white tracking-tight">
                专业课题库中心 · 喂题与数据管理
              </h1>
            </div>
            <p className="text-slate-400 text-sm max-w-2xl leading-relaxed">
              支持一键喂养题库！无论是直接粘贴 Markdown 题目文本、导入 JSON 题库文件，还是手动录入，系统均能完美解析 LaTeX 公式、选项与详细解析，并即时持久化到本地存储。
            </p>
          </div>

          {/* Quick Actions */}
          <div className="flex flex-wrap items-center gap-3">
            <button
              onClick={() => exportQuestionsToJsonFile(questions)}
              className="px-4 py-2.5 rounded-xl bg-slate-850 hover:bg-slate-800 text-slate-200 border border-slate-700/80 font-semibold text-xs flex items-center gap-2 transition-all shadow-sm active:translate-y-0.5"
              title="导出当前题库为标准 JSON 备份"
            >
              <Download className="w-4 h-4 text-blue-400" />
              <span>备份当前题库 ({questions.length}题)</span>
            </button>

            <button
              onClick={handleResetDefaults}
              className="px-4 py-2.5 rounded-xl bg-rose-950/40 hover:bg-rose-900/60 text-rose-300 border border-rose-800/60 font-semibold text-xs flex items-center gap-2 transition-all shadow-sm active:translate-y-0.5"
            >
              <RotateCcw className="w-4 h-4 text-rose-400" />
              <span>重置为官方题库</span>
            </button>
          </div>
        </div>
      </div>

      {/* Tabs */}
      <div className="flex flex-wrap items-center gap-2 border-b border-slate-800/80 pb-2">
        <button
          onClick={() => setActiveTab('text')}
          className={`flex items-center gap-2 px-4 py-2.5 rounded-xl text-sm font-semibold transition-all ${
            activeTab === 'text'
              ? 'bg-blue-600 text-white shadow-sm'
              : 'text-slate-400 hover:text-white hover:bg-slate-800/80'
          }`}
        >
          <FileText className="w-4 h-4" />
          <span>智能文本 / Markdown 喂题</span>
        </button>

        <button
          onClick={() => setActiveTab('json')}
          className={`flex items-center gap-2 px-4 py-2.5 rounded-xl text-sm font-semibold transition-all ${
            activeTab === 'json'
              ? 'bg-blue-600 text-white shadow-sm'
              : 'text-slate-400 hover:text-white hover:bg-slate-800/80'
          }`}
        >
          <Code className="w-4 h-4" />
          <span>批量 JSON 导入</span>
        </button>

        <button
          onClick={() => setActiveTab('manual')}
          className={`flex items-center gap-2 px-4 py-2.5 rounded-xl text-sm font-semibold transition-all ${
            activeTab === 'manual'
              ? 'bg-blue-600 text-white shadow-sm'
              : 'text-slate-400 hover:text-white hover:bg-slate-800/80'
          }`}
        >
          <PlusCircle className="w-4 h-4" />
          <span>单题可视化录入</span>
        </button>

        <button
          onClick={() => setActiveTab('list')}
          className={`flex items-center gap-2 px-4 py-2.5 rounded-xl text-sm font-semibold transition-all ${
            activeTab === 'list'
              ? 'bg-blue-600 text-white shadow-sm'
              : 'text-slate-400 hover:text-white hover:bg-slate-800/80'
          }`}
        >
          <Search className="w-4 h-4" />
          <span>全部题目总览 ({questions.length})</span>
        </button>
      </div>

      {/* Tab 1: Text / Markdown Import */}
      {activeTab === 'text' && (
        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 space-y-6">
          <div className="flex flex-wrap items-center justify-between gap-4">
            <div>
              <h2 className="text-lg font-bold text-white flex items-center gap-2">
                <span>粘贴题目文本智能入库</span>
                <span className="text-xs font-normal text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-md border border-emerald-500/20">
                  支持 LaTeX 公式与代码块
                </span>
              </h2>
              <p className="text-xs text-slate-400 mt-1">
                支持以 Markdown 或结构化文本格式输入任意多道题目，每道题之间可用 <code>---</code> 或 <code>### 题目</code> 分隔。
              </p>
            </div>

            <div className="flex items-center gap-3">
              <input
                type="text"
                placeholder="默认学科（如：广工837/809-信号与系统）"
                value={defaultSubjectInput}
                onChange={(e) => setDefaultSubjectInput(e.target.value)}
                className="bg-slate-800 text-xs text-slate-200 px-3 py-2 rounded-xl border border-slate-700 focus:outline-none focus:border-emerald-500"
              />
              <button
                onClick={() => setMarkdownInput(sampleMarkdown)}
                className="px-3 py-2 rounded-xl text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 flex items-center gap-1.5 transition-colors"
              >
                <Sparkles className="w-3.5 h-3.5 text-amber-400" />
                填入测试模板
              </button>
            </div>
          </div>

          <textarea
            value={markdownInput}
            onChange={(e) => {
              setMarkdownInput(e.target.value);
              setTextParseFeedback(null);
            }}
            placeholder="请在此粘贴您的题目文本，例如：
### 题目 1 [单选]
学科: 广工837/809-信号与系统
章节: 第三章：频域分析与傅里叶变换
题干: 某连续时间理想低通滤波器的截止频率为 \omega_c ...
A. 选项内容
B. 选项内容
C. 选项内容
D. 选项内容
答案: C
解析: 因为 ...

---"
            rows={14}
            className="w-full bg-slate-950 font-mono text-sm text-slate-200 p-4 rounded-2xl border border-slate-800 focus:border-emerald-500 focus:outline-none leading-relaxed resize-y"
          />

          {/* Feedback */}
          {textParseFeedback && (
            <div className={`p-4 rounded-xl text-sm flex items-center gap-3 ${
              textParseFeedback.error 
                ? 'bg-rose-950/40 border border-rose-500/40 text-rose-300' 
                : 'bg-emerald-950/40 border border-emerald-500/40 text-emerald-300'
            }`}>
              {textParseFeedback.error ? (
                <>
                  <AlertCircle className="w-5 h-5 text-rose-400 shrink-0" />
                  <span>{textParseFeedback.error}</span>
                </>
              ) : (
                <>
                  <Check className="w-5 h-5 text-emerald-400 shrink-0" />
                  <span>成功解析出 <strong>{textParseFeedback.count}</strong> 道题目！点击下方按钮即可完成入库。</span>
                </>
              )}
            </div>
          )}

          {/* Buttons */}
          <div className="flex items-center gap-3 justify-end pt-2">
            <button
              onClick={handleParseText}
              className="px-5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold text-sm transition-colors"
            >
              预检解析
            </button>
            <button
              onClick={handleApplyTextImport}
              disabled={!markdownInput.trim()}
              className="px-6 py-2.5 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 text-white font-bold text-sm shadow-lg shadow-emerald-600/30 hover:from-emerald-500 hover:to-teal-500 disabled:opacity-40 disabled:cursor-not-allowed transition-all flex items-center gap-2"
            >
              <Upload className="w-4 h-4" />
              <span>立即确认入库</span>
            </button>
          </div>
        </div>
      )}

      {/* Tab 2: JSON Import */}
      {activeTab === 'json' && (
        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 space-y-6">
          <div className="flex items-center justify-between">
            <div>
              <h2 className="text-lg font-bold text-white flex items-center gap-2">
                <span>批量 JSON 导入</span>
                <span className="text-xs text-slate-400 font-mono">标准 Question[] 格式</span>
              </h2>
              <p className="text-xs text-slate-400 mt-1">
                如果您有程序导出的 JSON 题库，可以直接粘贴至下方文本框中导入。
              </p>
            </div>
          </div>

          <textarea
            value={jsonInput}
            onChange={(e) => {
              setJsonInput(e.target.value);
              setJsonError('');
            }}
            placeholder='[
  {
    "id": "ss-demo-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "type": "single",
    "difficulty": 3,
    "tags": ["Z变换", "收敛域ROC", "经典真题"],
    "stem": "因果离散时间系统函数为 $H(z) = \\frac{1}{1 - 0.5z^{-1}}$，则该系统的收敛域 ROC 为：",
    "options": [
      { "key": "A", "text": "$|z| > 0.5$" },
      { "key": "B", "text": "$|z| < 0.5$" },
      { "key": "C", "text": "$|z| > 1$" },
      { "key": "D", "text": "整个复平面" }
    ],
    "answer": "A",
    "analysis": "因果序列的 Z 变换收敛域必为最外层极点之外的圆外区域。此处极点为 $z = 0.5$，故 ROC 为 $|z| > 0.5$。"
  }
]'
            rows={14}
            className="w-full bg-slate-950 font-mono text-sm text-slate-200 p-4 rounded-2xl border border-slate-800 focus:border-emerald-500 focus:outline-none leading-relaxed resize-y"
          />

          {jsonError && (
            <div className="p-4 rounded-xl bg-rose-950/40 border border-rose-500/40 text-rose-300 text-sm flex items-center gap-2">
              <AlertCircle className="w-4 h-4 shrink-0" />
              <span>{jsonError}</span>
            </div>
          )}

          <div className="flex justify-end">
            <button
              onClick={handleImportJson}
              disabled={!jsonInput.trim()}
              className="px-6 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-sm shadow-lg shadow-emerald-600/30 disabled:opacity-40 transition-all flex items-center gap-2"
            >
              <Upload className="w-4 h-4" />
              <span>解析并导入 JSON</span>
            </button>
          </div>
        </div>
      )}

      {/* Tab 3: Manual Entry */}
      {activeTab === 'manual' && (
        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 space-y-6">
          <h2 className="text-lg font-bold text-white flex items-center gap-2">
            <span>手动录入单道题目</span>
          </h2>

          <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
            <div>
              <label className="block text-xs font-semibold text-slate-400 mb-1.5">学科分类</label>
              <input
                type="text"
                value={manualForm.subject}
                onChange={(e) => setManualForm({ ...manualForm, subject: e.target.value })}
                placeholder="如: 广工837/809-信号与系统"
                className="w-full bg-slate-800 text-slate-200 text-sm px-3.5 py-2 rounded-xl border border-slate-700 focus:border-emerald-500 focus:outline-none"
              />
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-400 mb-1.5">章节与考点</label>
              <input
                type="text"
                value={manualForm.chapter}
                onChange={(e) => setManualForm({ ...manualForm, chapter: e.target.value })}
                placeholder="如: 第一章：信号与系统基础"
                className="w-full bg-slate-800 text-slate-200 text-sm px-3.5 py-2 rounded-xl border border-slate-700 focus:border-emerald-500 focus:outline-none"
              />
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-400 mb-1.5">题型</label>
              <select
                value={manualForm.type}
                onChange={(e) => setManualForm({ ...manualForm, type: e.target.value as QuestionType })}
                className="w-full bg-slate-800 text-slate-200 text-sm px-3.5 py-2 rounded-xl border border-slate-700 focus:border-emerald-500 focus:outline-none"
              >
                <option value="single">单选题</option>
                <option value="multiple">多选题</option>
                <option value="judgment">判断题</option>
                <option value="subjective">综合大题 / 简答题</option>
              </select>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-400 mb-1.5">难度星级 (1-5)</label>
              <input
                type="number"
                min={1}
                max={5}
                value={manualForm.difficulty}
                onChange={(e) => setManualForm({ ...manualForm, difficulty: parseInt(e.target.value) || 3 })}
                className="w-full bg-slate-800 text-slate-200 text-sm px-3.5 py-2 rounded-xl border border-slate-700 focus:border-emerald-500 focus:outline-none"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-400 mb-1.5">
              题干内容 (支持 LaTeX 公式 $math$ 与 Markdown 格式)
            </label>
            <textarea
              rows={4}
              value={manualForm.stem}
              onChange={(e) => setManualForm({ ...manualForm, stem: e.target.value })}
              placeholder="请输入题目题干..."
              className="w-full bg-slate-950 text-slate-200 text-sm p-3.5 rounded-xl border border-slate-800 focus:border-emerald-500 focus:outline-none font-mono"
            />
          </div>

          {/* Options if objective */}
          {manualForm.type !== 'subjective' && (
            <div className="space-y-3">
              <label className="block text-xs font-semibold text-slate-400">选项内容</label>
              {manualForm.options?.map((opt, i) => (
                <div key={opt.key} className="flex items-center gap-3">
                  <span className="w-7 h-7 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs flex items-center justify-center shrink-0">
                    {opt.key}
                  </span>
                  <input
                    type="text"
                    value={opt.text}
                    onChange={(e) => {
                      const newOpts = [...(manualForm.options || [])];
                      newOpts[i] = { ...newOpts[i], text: e.target.value };
                      setManualForm({ ...manualForm, options: newOpts });
                    }}
                    placeholder={`选项 ${opt.key} 内容`}
                    className="flex-1 bg-slate-800 text-slate-200 text-sm px-3.5 py-2 rounded-xl border border-slate-700 focus:border-emerald-500 focus:outline-none"
                  />
                </div>
              ))}
            </div>
          )}

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label className="block text-xs font-semibold text-slate-400 mb-1.5">
                正确答案 (如: A 或多选 A,C)
              </label>
              <input
                type="text"
                value={Array.isArray(manualForm.answer) ? manualForm.answer.join('') : manualForm.answer}
                onChange={(e) => setManualForm({ ...manualForm, answer: e.target.value.trim().toUpperCase() })}
                placeholder="A"
                className="w-full bg-slate-800 text-slate-200 text-sm px-3.5 py-2 rounded-xl border border-slate-700 focus:border-emerald-500 focus:outline-none font-mono"
              />
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-400 mb-1.5">标签 (逗号分隔)</label>
              <input
                type="text"
                value={manualForm.tags?.join(', ')}
                onChange={(e) => setManualForm({ ...manualForm, tags: e.target.value.split(/[,，\s]+/).filter(Boolean) })}
                placeholder="2024真题, 高频难点"
                className="w-full bg-slate-800 text-slate-200 text-sm px-3.5 py-2 rounded-xl border border-slate-700 focus:border-emerald-500 focus:outline-none"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-400 mb-1.5">详细解析与解题思路</label>
            <textarea
              rows={4}
              value={manualForm.analysis}
              onChange={(e) => setManualForm({ ...manualForm, analysis: e.target.value })}
              placeholder="请输入解析推导过程..."
              className="w-full bg-slate-950 text-slate-200 text-sm p-3.5 rounded-xl border border-slate-800 focus:border-emerald-500 focus:outline-none font-mono"
            />
          </div>

          <div className="flex justify-end">
            <button
              onClick={handleSaveManual}
              className="px-6 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-sm shadow-lg shadow-emerald-600/30 transition-all flex items-center gap-2"
            >
              <Check className="w-4 h-4" />
              <span>保存并入库本题</span>
            </button>
          </div>
        </div>
      )}

      {/* Tab 4: Questions List & Management */}
      {activeTab === 'list' && (
        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-8 space-y-6">
          
          {/* Search & Subject Filter Bar */}
          <div className="flex flex-wrap items-center justify-between gap-4">
            <div className="flex items-center gap-3 flex-1 max-w-md">
              <div className="relative w-full">
                <Search className="w-4 h-4 text-slate-500 absolute left-3.5 top-3" />
                <input
                  type="text"
                  placeholder="搜索题目关键字、章节或学科..."
                  value={searchKeyword}
                  onChange={(e) => setSearchKeyword(e.target.value)}
                  className="w-full bg-slate-800 text-slate-200 text-sm pl-10 pr-4 py-2 rounded-xl border border-slate-700 focus:outline-none focus:border-emerald-500"
                />
              </div>
            </div>

            <div className="flex items-center gap-3">
              <select
                value={filterSubject}
                onChange={(e) => setFilterSubject(e.target.value)}
                className="bg-slate-800 text-slate-200 text-xs rounded-xl px-3 py-2 border border-slate-700 focus:outline-none"
              >
                <option value="ALL">全部学科</option>
                {Array.from(new Set(questions.map(q => q.subject))).map(s => (
                  <option key={s} value={s}>{s}</option>
                ))}
              </select>
              <span className="text-xs text-slate-400 font-mono">
                已检索到 <strong className="text-emerald-400">{filteredList.length}</strong> 题
              </span>
            </div>
          </div>

          {/* Table List */}
          <div className="border border-slate-800 rounded-2xl overflow-hidden divide-y divide-slate-800">
            {filteredList.slice(0, 50).map((q, idx) => (
              <div key={q.id} className="p-4 hover:bg-slate-850 transition-colors flex items-start justify-between gap-4">
                <div className="space-y-1.5 flex-1 min-w-0">
                  <div className="flex flex-wrap items-center gap-2">
                    <span className="text-xs font-mono font-bold text-slate-500">#{idx + 1}</span>
                    <span className="text-xs px-2 py-0.5 rounded bg-blue-500/10 text-blue-400 border border-blue-500/20 font-semibold">
                      {q.subject}
                    </span>
                    <span className="text-xs text-slate-400">
                      {q.chapter}
                    </span>
                    <span className="text-[11px] px-1.5 py-0.2 rounded bg-slate-800 text-slate-400">
                      {q.type}
                    </span>
                    <span className="text-xs text-amber-400">
                      {'★'.repeat(q.difficulty)}
                    </span>
                  </div>

                  <div className="text-sm text-slate-200 font-medium line-clamp-2">
                    {q.stem}
                  </div>

                  <div className="text-xs text-slate-500">
                    答案: <span className="text-emerald-400 font-mono font-bold">{Array.isArray(q.answer) ? q.answer.join(', ') : q.answer}</span>
                  </div>
                </div>

                <div className="flex items-center gap-2 shrink-0">
                  <button
                    onClick={() => handleDeleteQuestion(q.id)}
                    className="p-2 rounded-xl text-slate-400 hover:text-rose-400 hover:bg-slate-800 transition-colors"
                    title="删除此题"
                  >
                    <Trash2 className="w-4 h-4" />
                  </button>
                </div>
              </div>
            ))}

            {filteredList.length === 0 && (
              <div className="p-12 text-center text-slate-500 text-sm">
                未找到匹配的题目
              </div>
            )}
          </div>

          {filteredList.length > 50 && (
            <div className="text-center text-xs text-slate-500">
              仅展示前 50 道题目，如需全部查看请使用关键词筛选
            </div>
          )}

        </div>
      )}

    </div>
  );
};
