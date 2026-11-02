import React, { useRef, useState, useEffect } from 'react';
import { X, Eraser, Pen, Trash2, Download } from 'lucide-react';

interface ScratchpadModalProps {
  isOpen: boolean;
  onClose: () => void;
  isDark: boolean;
}

export const ScratchpadModal: React.FC<ScratchpadModalProps> = ({
  isOpen,
  onClose,
  isDark
}) => {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const [tool, setTool] = useState<'pen' | 'eraser'>('pen');
  const [color, setColor] = useState<string>(isDark ? '#60a5fa' : '#2563eb');
  const [lineWidth, setLineWidth] = useState<number>(3);
  const [isDrawing, setIsDrawing] = useState<boolean>(false);
  const [activeTab, setActiveTab] = useState<'canvas' | 'text'>('canvas');
  const [textNotes, setTextNotes] = useState<string>(() => {
    return localStorage.getItem('daguan_scratch_text') || '';
  });

  // Sync default color when theme changes
  useEffect(() => {
    if (tool === 'pen') {
      setColor(isDark ? '#60a5fa' : '#2563eb');
    }
  }, [isDark, tool]);

  // Save text notes
  useEffect(() => {
    localStorage.setItem('daguan_scratch_text', textNotes);
  }, [textNotes]);

  // Initialize canvas
  useEffect(() => {
    if (!isOpen || activeTab !== 'canvas') return;
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    // Set canvas dimensions based on client rect
    const rect = canvas.getBoundingClientRect();
    if (canvas.width !== rect.width || canvas.height !== rect.height) {
      canvas.width = rect.width;
      canvas.height = rect.height;
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
    }
  }, [isOpen, activeTab]);

  if (!isOpen) return null;

  // Drawing event handlers
  const startDrawing = (e: React.MouseEvent<HTMLCanvasElement> | React.TouchEvent<HTMLCanvasElement>) => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    setIsDrawing(true);
    const rect = canvas.getBoundingClientRect();
    const x = 'touches' in e ? e.touches[0].clientX - rect.left : e.clientX - rect.left;
    const y = 'touches' in e ? e.touches[0].clientY - rect.top : e.clientY - rect.top;

    ctx.beginPath();
    ctx.moveTo(x, y);
  };

  const draw = (e: React.MouseEvent<HTMLCanvasElement> | React.TouchEvent<HTMLCanvasElement>) => {
    if (!isDrawing) return;
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const rect = canvas.getBoundingClientRect();
    const x = 'touches' in e ? e.touches[0].clientX - rect.left : e.clientX - rect.left;
    const y = 'touches' in e ? e.touches[0].clientY - rect.top : e.clientY - rect.top;

    ctx.lineWidth = tool === 'eraser' ? lineWidth * 4 : lineWidth;
    ctx.strokeStyle = tool === 'eraser' ? (isDark ? '#0f172a' : '#ffffff') : color;
    ctx.lineTo(x, y);
    ctx.stroke();
  };

  const stopDrawing = () => {
    setIsDrawing(false);
  };

  const clearCanvas = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  };

  const downloadCanvas = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const url = canvas.toDataURL('image/png');
    const a = document.createElement('a');
    a.href = url;
    a.download = `大观园草稿纸_${Date.now()}.png`;
    a.click();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm animate-fadeIn">
      <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 w-full max-w-4xl h-[80vh] rounded-3xl shadow-2xl flex flex-col overflow-hidden">
        
        {/* Header */}
        <div className="px-6 py-4 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="p-2 rounded-xl bg-blue-50 dark:bg-blue-950/60 text-blue-600 dark:text-blue-400">
              <Pen className="w-5 h-5" />
            </div>
            <div>
              <h3 className="font-bold text-base text-slate-800 dark:text-slate-100">
                随题草稿纸 · 实时推演
              </h3>
              <p className="text-xs text-slate-400">
                支持手绘波形、极零点图与草算公式推导
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            {/* Mode switch */}
            <div className="flex items-center gap-1 bg-slate-100 dark:bg-slate-800 p-1 rounded-xl text-xs font-semibold mr-2">
              <button
                onClick={() => setActiveTab('canvas')}
                className={`px-3 py-1 rounded-lg transition-all ${
                  activeTab === 'canvas'
                    ? 'bg-white dark:bg-slate-700 text-blue-600 dark:text-white shadow-sm'
                    : 'text-slate-500 hover:text-slate-900 dark:hover:text-white'
                }`}
              >
                手绘板
              </button>
              <button
                onClick={() => setActiveTab('text')}
                className={`px-3 py-1 rounded-lg transition-all ${
                  activeTab === 'text'
                    ? 'bg-white dark:bg-slate-700 text-blue-600 dark:text-white shadow-sm'
                    : 'text-slate-500 hover:text-slate-900 dark:hover:text-white'
                }`}
              >
                打字稿纸
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

        {/* Toolbar (when Canvas is active) */}
        {activeTab === 'canvas' && (
          <div className="px-6 py-2.5 bg-slate-50 dark:bg-slate-850/80 border-b border-slate-200 dark:border-slate-800 flex flex-wrap items-center justify-between gap-3 text-xs">
            <div className="flex items-center gap-2">
              {/* Tool choice */}
              <button
                onClick={() => setTool('pen')}
                className={`p-2 rounded-xl flex items-center gap-1.5 font-medium transition-all ${
                  tool === 'pen'
                    ? 'bg-blue-600 text-white shadow-sm'
                    : 'bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 border border-slate-200 dark:border-slate-700'
                }`}
              >
                <Pen className="w-3.5 h-3.5" />
                <span>画笔</span>
              </button>

              <button
                onClick={() => setTool('eraser')}
                className={`p-2 rounded-xl flex items-center gap-1.5 font-medium transition-all ${
                  tool === 'eraser'
                    ? 'bg-blue-600 text-white shadow-sm'
                    : 'bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 border border-slate-200 dark:border-slate-700'
                }`}
              >
                <Eraser className="w-3.5 h-3.5" />
                <span>橡皮擦</span>
              </button>

              {/* Color dots */}
              {tool === 'pen' && (
                <div className="flex items-center gap-1.5 ml-2 pl-2 border-l border-slate-300 dark:border-slate-700">
                  {['#60a5fa', '#34d399', '#f43f5e', '#fbbf24', '#ffffff', '#0f172a'].map(c => (
                    <button
                      key={c}
                      onClick={() => setColor(c)}
                      className={`w-6 h-6 rounded-full border-2 transition-transform ${
                        color === c ? 'scale-110 border-blue-500 ring-2 ring-blue-400/40' : 'border-transparent'
                      }`}
                      style={{ backgroundColor: c }}
                    />
                  ))}
                </div>
              )}

              {/* Brush size */}
              <div className="flex items-center gap-1.5 ml-3">
                <span className="text-slate-400">粗细:</span>
                {[2, 4, 8].map(size => (
                  <button
                    key={size}
                    onClick={() => setLineWidth(size)}
                    className={`px-2 py-1 rounded-md text-[11px] font-mono ${
                      lineWidth === size
                        ? 'bg-slate-200 dark:bg-slate-700 font-bold text-slate-900 dark:text-white'
                        : 'text-slate-400 hover:text-slate-700'
                    }`}
                  >
                    {size}px
                  </button>
                ))}
              </div>
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={clearCanvas}
                className="px-3 py-1.5 rounded-xl bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 border border-slate-200 dark:border-slate-700 hover:text-rose-500 dark:hover:text-rose-400 flex items-center gap-1 transition-colors"
                title="清空画板"
              >
                <Trash2 className="w-3.5 h-3.5" />
                <span>清空</span>
              </button>

              <button
                onClick={downloadCanvas}
                className="px-3 py-1.5 rounded-xl bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 border border-slate-200 dark:border-slate-700 hover:text-blue-500 flex items-center gap-1 transition-colors"
                title="保存为图片"
              >
                <Download className="w-3.5 h-3.5" />
                <span>保存草稿</span>
              </button>
            </div>
          </div>
        )}

        {/* Content Area */}
        <div className="flex-1 relative overflow-hidden bg-white dark:bg-slate-950">
          {activeTab === 'canvas' ? (
            <canvas
              ref={canvasRef}
              onMouseDown={startDrawing}
              onMouseMove={draw}
              onMouseUp={stopDrawing}
              onMouseLeave={stopDrawing}
              onTouchStart={startDrawing}
              onTouchMove={draw}
              onTouchEnd={stopDrawing}
              className="w-full h-full cursor-crosshair touch-none"
            />
          ) : (
            <textarea
              value={textNotes}
              onChange={(e) => setTextNotes(e.target.value)}
              placeholder="在此快速敲写演算步骤、推导方程、临时公式等草稿内容（内容自动保存）..."
              className="w-full h-full p-6 bg-transparent text-slate-800 dark:text-slate-100 font-mono text-sm leading-relaxed outline-none resize-none"
            />
          )}
        </div>

      </div>
    </div>
  );
};
