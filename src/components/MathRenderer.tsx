import React, { useMemo } from 'react';
import katex from 'katex';

interface MathRendererProps {
  content: string;
  className?: string;
  inline?: boolean;
}

export const MathRenderer: React.FC<MathRendererProps> = ({ content, className = '', inline = false }) => {
  const renderedHtml = useMemo(() => {
    if (!content) return '';

    // First handle code blocks ```lang ... ```
    const codeBlocks: string[] = [];
    let text = content.replace(/```([\w-]*)\n([\s\S]*?)```/g, (_, lang, code) => {
      const idx = codeBlocks.length;
      const escapedCode = code
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');
      codeBlocks.push(
        `<div class="my-3 rounded-xl overflow-hidden border border-slate-200 dark:border-slate-800 bg-slate-100 dark:bg-slate-950 font-mono text-xs md:text-sm shadow-sm">
          ${lang ? `<div class="bg-slate-200/80 dark:bg-slate-800/80 px-3 py-1 text-slate-600 dark:text-slate-400 text-xs font-semibold border-b border-slate-200 dark:border-slate-700/50 uppercase tracking-wider">${lang}</div>` : ''}
          <pre class="p-3.5 overflow-x-auto text-emerald-700 dark:text-emerald-400 leading-relaxed font-medium"><code>${escapedCode}</code></pre>
        </div>`
      );
      return `__CODE_BLOCK_${idx}__`;
    });

    // Handle block math $$ ... $$
    const blockMaths: string[] = [];
    text = text.replace(/\$\$([\s\S]*?)\$\$/g, (_, math) => {
      const idx = blockMaths.length;
      try {
        const rendered = katex.renderToString(math.trim(), {
          displayMode: true,
          throwOnError: false,
        });
        blockMaths.push(`<div class="my-2.5 overflow-x-auto py-1">${rendered}</div>`);
      } catch (err) {
        blockMaths.push(`<div class="text-rose-600 dark:text-rose-400 font-mono text-sm py-1">$$${math}$$</div>`);
      }
      return `__BLOCK_MATH_${idx}__`;
    });

    // Handle inline math $ ... $
    const inlineMaths: string[] = [];
    text = text.replace(/\$([^\$\n]+?)\$/g, (_, math) => {
      const idx = inlineMaths.length;
      try {
        const rendered = katex.renderToString(math.trim(), {
          displayMode: false,
          throwOnError: false,
        });
        inlineMaths.push(rendered);
      } catch (err) {
        inlineMaths.push(`<span class="text-rose-600 dark:text-rose-400 font-mono text-xs">$${math}$</span>`);
      }
      return `__INLINE_MATH_${idx}__`;
    });

    // Escape basic html characters in the remaining text
    text = text
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');

    // Handle bold **text** with dynamic contrast
    text = text.replace(/\*\*(.*?)\*\*/g, '<strong class="font-bold text-slate-950 dark:text-white">$1</strong>');
    
    // Handle inline code `code`
    text = text.replace(/`([^`]+)`/g, '<code class="px-1.5 py-0.5 mx-0.5 rounded bg-slate-100 dark:bg-slate-800 text-blue-700 dark:text-amber-300 font-mono text-xs md:text-sm border border-slate-200 dark:border-slate-700/50">$1</code>');

    // Handle lists with - or 1.
    text = text.replace(/^\s*-\s+(.*)$/gm, '<li class="ml-4 list-disc text-slate-800 dark:text-slate-200">$1</li>');

    // Handle line breaks (unless inline)
    if (!inline) {
      text = text.replace(/\n\n/g, '<div class="h-2"></div>');
      text = text.replace(/\n/g, '<br/>');
    }

    // Restore inline math
    text = text.replace(/__INLINE_MATH_(\d+)__/g, (_, idx) => inlineMaths[Number(idx)] || '');

    // Restore block math
    text = text.replace(/__BLOCK_MATH_(\d+)__/g, (_, idx) => blockMaths[Number(idx)] || '');

    // Restore code blocks
    text = text.replace(/__CODE_BLOCK_(\d+)__/g, (_, idx) => codeBlocks[Number(idx)] || '');

    return text;
  }, [content, inline]);

  if (inline) {
    return <span className={`text-slate-900 dark:text-slate-100 font-normal ${className}`} dangerouslySetInnerHTML={{ __html: renderedHtml }} />;
  }

  return (
    <div 
      className={`max-w-none leading-relaxed text-slate-900 dark:text-slate-100 font-normal ${className}`} 
      dangerouslySetInnerHTML={{ __html: renderedHtml }} 
    />
  );
};
