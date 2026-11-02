import { Question, UserQuestionProgress, ExamRecord } from '../types';
import { initialQuestions } from '../data/initialQuestions';

const STORAGE_KEYS = {
  QUESTIONS: 'daguan_major_questions_v6',
  PROGRESS: 'daguan_user_progress_v5',
  EXAM_RECORDS: 'daguan_exam_records_v1',
  THEME: 'daguan_theme_v1'
};

export const getStoredQuestions = (): Question[] => {
  try {
    const raw = localStorage.getItem(STORAGE_KEYS.QUESTIONS);
    if (!raw) {
      localStorage.setItem(STORAGE_KEYS.QUESTIONS, JSON.stringify(initialQuestions));
      return initialQuestions;
    }
    const parsed = JSON.parse(raw);
    if (Array.isArray(parsed) && parsed.length >= initialQuestions.length) {
      return parsed;
    }
    // If newer initialQuestions are present (e.g. 960题 added), update cache
    localStorage.setItem(STORAGE_KEYS.QUESTIONS, JSON.stringify(initialQuestions));
    return initialQuestions;
  } catch (err) {
    console.error('Failed to read questions from localStorage:', err);
    return initialQuestions;
  }
};

export const saveStoredQuestions = (questions: Question[]): void => {
  try {
    localStorage.setItem(STORAGE_KEYS.QUESTIONS, JSON.stringify(questions));
  } catch (err) {
    console.error('Failed to save questions:', err);
  }
};

export const resetToDefaultQuestions = (): Question[] => {
  localStorage.setItem(STORAGE_KEYS.QUESTIONS, JSON.stringify(initialQuestions));
  return initialQuestions;
};

export const getStoredProgress = (): Record<string, UserQuestionProgress> => {
  try {
    const raw = localStorage.getItem(STORAGE_KEYS.PROGRESS);
    if (raw) return JSON.parse(raw);
    const legacy = localStorage.getItem('daguan_user_progress_v4') || localStorage.getItem('daguan_user_progress_v3');
    if (legacy) {
      localStorage.setItem(STORAGE_KEYS.PROGRESS, legacy);
      return JSON.parse(legacy);
    }
    return {};
  } catch (err) {
    console.error('Failed to load progress:', err);
    return {};
  }
};

export const saveStoredProgress = (progress: Record<string, UserQuestionProgress>): void => {
  try {
    localStorage.setItem(STORAGE_KEYS.PROGRESS, JSON.stringify(progress));
  } catch (err) {
    console.error('Failed to save progress:', err);
  }
};

export const getStoredExamRecords = (): ExamRecord[] => {
  try {
    const raw = localStorage.getItem(STORAGE_KEYS.EXAM_RECORDS);
    return raw ? JSON.parse(raw) : [];
  } catch (err) {
    return [];
  }
};

export const saveStoredExamRecord = (record: ExamRecord): void => {
  try {
    const records = getStoredExamRecords();
    records.unshift(record);
    localStorage.setItem(STORAGE_KEYS.EXAM_RECORDS, JSON.stringify(records));
  } catch (err) {
    console.error('Failed to save exam record:', err);
  }
};

/**
 * Smart Markdown / Text Question Parser
 * Supports questions separated by `---` or `### 题目` or numbered headers.
 */
export const parseMarkdownQuestions = (rawText: string, defaultSubject = '专业课综合'): Question[] => {
  const blocks = rawText.split(/\n(?=(?:###|\d+[\.、]|【题号】|---))/g).filter(b => b.trim().length > 10);
  const result: Question[] = [];

  for (let i = 0; i < blocks.length; i++) {
    const block = blocks[i].replace(/^---+\s*/, '').trim();
    if (!block) continue;

    // Detect subject
    let subject = defaultSubject;
    const subMatch = block.match(/(?:学科|科目|【科目】)[:：]\s*([^\n\r]+)/);
    if (subMatch) subject = subMatch[1].trim();

    // Detect chapter
    let chapter = '精选考点';
    const chMatch = block.match(/(?:章节|考点|【章节】)[:：]\s*([^\n\r]+)/);
    if (chMatch) chapter = chMatch[1].trim();

    // Detect difficulty
    let difficulty = 3;
    const diffMatch = block.match(/(?:难度|【难度】)[:：]\s*([1-5])/);
    if (diffMatch) difficulty = parseInt(diffMatch[1], 10);

    // Detect tags
    let tags = ['用户导入'];
    const tagMatch = block.match(/(?:标签|【标签】)[:：]\s*([^\n\r]+)/);
    if (tagMatch) {
      tags = tagMatch[1].split(/[,，、\s]+/).filter(Boolean);
    }

    // Detect answer
    let answer: string | string[] = 'A';
    const ansMatch = block.match(/(?:【?答案】?|参考答案)[:：]\s*([A-Za-z0-9,，、TF]+)/i);
    if (ansMatch) {
      const rawAns = ansMatch[1].trim().toUpperCase();
      if (rawAns.includes(',') || rawAns.includes('，') || rawAns.length > 1 && !['TF', 'TRUE', 'FALSE'].includes(rawAns)) {
        answer = rawAns.replace(/[,，]/g, '').split('').filter(c => /[A-D]/.test(c));
      } else {
        answer = rawAns.charAt(0);
      }
    }

    // Detect analysis
    let analysis = '暂无详细解析';
    const anaMatch = block.match(/(?:【?解析】?|解题思路)[:：]([\s\S]*?)(?=$|\n(?:###|---|\d+[\.、]))/i);
    if (anaMatch) {
      analysis = anaMatch[1].trim();
    }

    // Parse options A, B, C, D
    const options: { key: string; text: string }[] = [];
    const optionMatches = [...block.matchAll(/(?:^|\n)\s*([A-D])[、\.．\s]\s*([^\n\r]+)/g)];
    if (optionMatches.length > 0) {
      for (const m of optionMatches) {
        options.push({ key: m[1].toUpperCase(), text: m[2].trim() });
      }
    }

    // Extract stem (before options or answer)
    let stem = block;
    // remove header lines like "### 题目 1", "科目: xxx"
    stem = stem.replace(/^###[^\n]+\n?/, '');
    stem = stem.replace(/^(?:\d+[\.、])[^\n]+\n?/, (match) => match.replace(/^\d+[\.、]\s*/, ''));
    stem = stem.replace(/(?:学科|科目|章节|考点|难度|标签|【科目】|【章节】|【难度】|【标签】)[:：][^\n\r]+\n?/g, '');
    
    // cut before options
    const firstOptIndex = stem.search(/(?:^|\n)\s*[A-D][、\.．\s]/);
    if (firstOptIndex !== -1) {
      stem = stem.slice(0, firstOptIndex).trim();
    } else {
      // cut before answer
      const ansIndex = stem.search(/(?:【?答案】?|参考答案)[:：]/);
      if (ansIndex !== -1) {
        stem = stem.slice(0, ansIndex).trim();
      }
    }

    // Determine type
    let type: Question['type'] = 'single';
    if (Array.isArray(answer) && answer.length > 1) {
      type = 'multiple';
    } else if (['T', 'F'].includes(String(answer)) || /判断/i.test(block)) {
      type = 'judgment';
    } else if (options.length === 0) {
      type = 'subjective';
    }

    if (stem.trim().length > 3) {
      result.push({
        id: `custom-${Date.now()}-${i}-${Math.random().toString(36).substring(2, 6)}`,
        subject,
        chapter,
        type,
        stem: stem.trim(),
        options: options.length > 0 ? options : undefined,
        answer,
        analysis,
        difficulty,
        tags,
        source: '自定义题库'
      });
    }
  }

  return result;
};

/**
 * Export questions to downloadable JSON
 */
export const exportQuestionsToJsonFile = (questions: Question[]) => {
  const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(questions, null, 2));
  const downloadAnchor = document.createElement('a');
  downloadAnchor.setAttribute("href", dataStr);
  downloadAnchor.setAttribute("download", `daguan_major_quiz_bank_${new Date().toISOString().slice(0, 10)}.json`);
  document.body.appendChild(downloadAnchor);
  downloadAnchor.click();
  downloadAnchor.remove();
};

/**
 * Export wrong/starred questions to Anki TSV format
 */
export const exportQuestionsToAnkiTsv = (questions: Question[]) => {
  const rows = questions.map(q => {
    const front = `<b>[${q.subject} · ${q.chapter}]</b><br/>${q.stem}<br/><br/>` + 
      (q.options ? q.options.map(o => `${o.key}. ${o.text}`).join('<br/>') : '');
    const back = `<b>【正确答案】</b>: ${Array.isArray(q.answer) ? q.answer.join(', ') : q.answer}<br/><br/><b>【详细解析】</b>:<br/>${q.analysis.replace(/\n/g, '<br/>')}`;
    return `${front.replace(/\t/g, ' ')}\t${back.replace(/\t/g, ' ')}\t${q.tags.join(' ')}`;
  });
  
  const content = rows.join('\n');
  const blob = new Blob([content], { type: 'text/tab-separated-values;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `Anki_大观园专业课错题卡片_${new Date().toISOString().slice(0, 10)}.txt`;
  document.body.appendChild(a);
  a.click();
  a.remove();
  URL.revokeObjectURL(url);
};
