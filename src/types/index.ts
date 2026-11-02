export type QuestionType = 'single' | 'multiple' | 'judgment' | 'subjective';

export interface OptionItem {
  key: string;   // 'A', 'B', 'C', 'D'
  text: string;  // LaTeX and Markdown supported
}

export interface Question {
  id: string;
  subject: string;         // e.g. "数据结构", "计算机组成原理", "操作系统", "计算机网络"
  chapter: string;         // e.g. "树与二叉树", "存储系统与Cache"
  section?: string;        // e.g. "哈夫曼树与二叉排序树"
  type: QuestionType;
  stem: string;            // 题干，支持 Markdown / LaTeX / 代码块
  options?: OptionItem[];  // 客观题选项
  answer: string | string[]; // 正确答案，单选为 'A'，多选为 ['A', 'C']，判断题为 'T'|'F'，主观题为标准答题点
  analysis: string;        // 解析内容
  difficulty: number;      // 1 - 5 星
  tags: string[];          // ['2024真题', '高频易错', '综合大题']
  source?: string;         // 题目出处
}

export interface UserQuestionProgress {
  answered: boolean;
  selectedAnswer?: string | string[];
  isCorrect?: boolean;
  lastAnsweredTime?: number;
  answerCount: number;
  wrongCount: number;
  isMastered?: boolean;
  isFavorite?: boolean;
  note?: string;
}

export interface SubjectStats {
  subject: string;
  totalQuestions: number;
  completedCount: number;
  correctCount: number;
  wrongCount: number;
  masteredCount: number;
}

export type StudyMode = 
  | 'home'        // 大观园主页看板 (Matching Image 3)
  | 'chapter'     // 章节专项刷题 / 沉浸工作台 (Matching Image 1)
  | 'wrong'       // 错题攻坚本
  | 'favorite'    // 收藏集 / 标记本
  | 'exam'        // 模拟全真机考 / 智能组卷
  | 'manage';     // 题库中心 / 导入管理

export interface ExamRecord {
  id: string;
  date: number;
  title: string;
  totalQuestions: number;
  correctCount: number;
  score: number;
  durationSeconds: number;
  questionIds: string[];
}
