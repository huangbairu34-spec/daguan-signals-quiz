import React, { useState, useEffect, useMemo, useCallback } from 'react';
import { 
  Question, 
  UserQuestionProgress, 
  StudyMode, 
  ExamRecord 
} from './types';
import { 
  getStoredQuestions, 
  saveStoredQuestions, 
  getStoredProgress, 
  saveStoredProgress, 
  getStoredExamRecords, 
  saveStoredExamRecord 
} from './utils/storage';
import { Navbar } from './components/Navbar';
import { HomeDashboard } from './components/HomeDashboard';
import { QuestionWorkbench } from './components/QuestionWorkbench';
import { ExamView } from './components/ExamView';
import { WrongBookView } from './components/WrongBookView';
import { QuestionManagerView } from './components/QuestionManagerView';
import { StatsModal } from './components/StatsModal';
import { KeyboardHelpModal } from './components/KeyboardHelpModal';

export const App: React.FC = () => {
  // Application Data States
  const [questions, setQuestions] = useState<Question[]>(() => getStoredQuestions());
  const [progress, setProgress] = useState<Record<string, UserQuestionProgress>>(() => getStoredProgress());
  const [examRecords, setExamRecords] = useState<ExamRecord[]>(() => getStoredExamRecords());

  // Navigation State
  const [currentMode, setCurrentMode] = useState<StudyMode>('home');
  const [activeQuestionId, setActiveQuestionId] = useState<string | undefined>(undefined);
  const [activeChapter, setActiveChapter] = useState<string | undefined>(undefined);
  const [activeSubTopic, setActiveSubTopic] = useState<string | undefined>(undefined);

  // Modals
  const [isStatsOpen, setIsStatsOpen] = useState<boolean>(false);
  const [isKeyboardHelpOpen, setIsKeyboardHelpOpen] = useState<boolean>(false);

  // Dark / Light Theme
  const [isDark, setIsDark] = useState<boolean>(() => {
    const saved = localStorage.getItem('daguan_theme_v1');
    return saved !== 'light';
  });

  // Apply theme class to <html>
  useEffect(() => {
    const root = document.documentElement;
    if (isDark) {
      root.classList.add('dark');
      localStorage.setItem('daguan_theme_v1', 'dark');
    } else {
      root.classList.remove('dark');
      localStorage.setItem('daguan_theme_v1', 'light');
    }
  }, [isDark]);

  // Today answered counter
  const todayCount = useMemo(() => {
    const todayStart = new Date().setHours(0, 0, 0, 0);
    return Object.values(progress).filter(p => p.lastAnsweredTime && p.lastAnsweredTime >= todayStart).length;
  }, [progress]);

  // Derived counts for Navbar badges
  const wrongCount = useMemo(() => {
    return questions.filter(q => {
      const p = progress[q.id];
      return p && p.isCorrect === false && !p.isMastered;
    }).length;
  }, [questions, progress]);

  const favoriteCount = useMemo(() => {
    return Object.values(progress).filter(p => p.isFavorite).length;
  }, [progress]);

  const totalAnswered = useMemo(() => {
    return Object.values(progress).filter(p => p.answered).length;
  }, [progress]);

  // Progress update helper
  const updateProgress = useCallback((newProgress: Record<string, UserQuestionProgress>) => {
    setProgress(newProgress);
    saveStoredProgress(newProgress);
  }, []);

  // Answer a question
  const handleAnswerQuestion = useCallback((questionId: string, answer: string | string[], isCorrect: boolean) => {
    const prev = progress[questionId] || {
      answered: false,
      answerCount: 0,
      wrongCount: 0
    };

    const updated: Record<string, UserQuestionProgress> = {
      ...progress,
      [questionId]: {
        ...prev,
        answered: true,
        selectedAnswer: answer,
        isCorrect,
        lastAnsweredTime: Date.now(),
        answerCount: prev.answerCount + 1,
        wrongCount: isCorrect ? prev.wrongCount : prev.wrongCount + 1,
        isMastered: isCorrect ? prev.isMastered : false
      }
    };

    updateProgress(updated);
  }, [progress, updateProgress]);

  // Toggle favorite
  const handleToggleFavorite = useCallback((questionId: string) => {
    const prev = progress[questionId] || {
      answered: false,
      answerCount: 0,
      wrongCount: 0
    };

    const updated: Record<string, UserQuestionProgress> = {
      ...progress,
      [questionId]: {
        ...prev,
        isFavorite: !prev.isFavorite
      }
    };

    updateProgress(updated);
  }, [progress, updateProgress]);

  // Toggle mastered
  const handleToggleMastered = useCallback((questionId: string) => {
    const prev = progress[questionId] || {
      answered: false,
      answerCount: 0,
      wrongCount: 0
    };

    const updated: Record<string, UserQuestionProgress> = {
      ...progress,
      [questionId]: {
        ...prev,
        isMastered: !prev.isMastered
      }
    };

    updateProgress(updated);
  }, [progress, updateProgress]);

  // Save note
  const handleSaveNote = useCallback((questionId: string, note: string) => {
    const prev = progress[questionId] || {
      answered: false,
      answerCount: 0,
      wrongCount: 0
    };

    const updated: Record<string, UserQuestionProgress> = {
      ...progress,
      [questionId]: {
        ...prev,
        note
      }
    };

    updateProgress(updated);
  }, [progress, updateProgress]);

  // Clear wrong status
  const handleClearWrongStatus = useCallback((questionId: string) => {
    if (!progress[questionId]) return;
    const updated = { ...progress };
    updated[questionId] = {
      ...updated[questionId],
      isCorrect: true
    };
    updateProgress(updated);
  }, [progress, updateProgress]);

  // Save Exam Record
  const handleSaveExamRecord = useCallback((record: ExamRecord) => {
    saveStoredExamRecord(record);
    setExamRecords(getStoredExamRecords());
  }, []);

  // Update Questions list (from manager import)
  const handleUpdateQuestions = useCallback((newQuestions: Question[]) => {
    setQuestions(newQuestions);
    saveStoredQuestions(newQuestions);
  }, []);

  // Start practice from Home Dashboard or Tree
  const handleStartPractice = useCallback((chapter?: string, subTopic?: string, questionId?: string) => {
    setActiveChapter(chapter);
    setActiveSubTopic(subTopic);
    setActiveQuestionId(questionId);
    setCurrentMode('chapter');
  }, []);

  // Jump from wrong book or elsewhere to practice
  const handleJumpToPractice = (questionId: string) => {
    setActiveChapter(undefined);
    setActiveSubTopic(undefined);
    setActiveQuestionId(questionId);
    setCurrentMode('chapter');
  };

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-[#0c101c] text-slate-900 dark:text-slate-100 flex flex-col selection:bg-blue-600 selection:text-white font-sans antialiased transition-colors duration-200">
      
      {/* Top Navigation - displayed when in secondary tool views (not in home or zen workbench) */}
      {currentMode !== 'chapter' && currentMode !== 'home' && (
        <Navbar
          currentMode={currentMode}
          onSelectMode={(mode) => {
            setActiveQuestionId(undefined);
            setCurrentMode(mode);
          }}
          wrongCount={wrongCount}
          favoriteCount={favoriteCount}
          onOpenStats={() => setIsStatsOpen(true)}
          onOpenShortcuts={() => setIsKeyboardHelpOpen(true)}
          isDark={isDark}
          onToggleTheme={() => setIsDark(d => !d)}
          totalAnswered={totalAnswered}
          todayCount={todayCount}
        />
      )}

      {/* Main Content Area */}
      <main className="flex-1">
        
        {/* Home Dashboard (Matching Image 3 + Image 2 Big Data) */}
        {currentMode === 'home' && (
          <HomeDashboard
            questions={questions}
            progress={progress}
            examRecords={examRecords}
            isDark={isDark}
            onToggleTheme={() => setIsDark(d => !d)}
            onStartPractice={handleStartPractice}
            onSelectMode={(mode) => {
              setActiveQuestionId(undefined);
              setCurrentMode(mode);
            }}
            wrongCount={wrongCount}
            favoriteCount={favoriteCount}
            todayCount={todayCount}
          />
        )}

        {/* Chapter Practice Mode (Zen mode matching Image 1 & Image 2) */}
        {currentMode === 'chapter' && (
          <QuestionWorkbench
            questions={questions}
            progress={progress}
            onAnswerQuestion={handleAnswerQuestion}
            onToggleFavorite={handleToggleFavorite}
            onToggleMastered={handleToggleMastered}
            onSaveNote={handleSaveNote}
            initialQuestionId={activeQuestionId}
            initialChapter={activeChapter}
            initialSubTopic={activeSubTopic}
            isDark={isDark}
            onToggleTheme={() => setIsDark(d => !d)}
            onSelectMode={(mode) => {
              setActiveQuestionId(undefined);
              setCurrentMode(mode);
            }}
            onBackToHome={() => setCurrentMode('home')}
          />
        )}

        {/* Favorite / Starred Mode */}
        {currentMode === 'favorite' && (
          <QuestionWorkbench
            questions={questions.filter(q => progress[q.id]?.isFavorite)}
            progress={progress}
            onAnswerQuestion={handleAnswerQuestion}
            onToggleFavorite={handleToggleFavorite}
            onToggleMastered={handleToggleMastered}
            onSaveNote={handleSaveNote}
            isDark={isDark}
            onToggleTheme={() => setIsDark(d => !d)}
            onSelectMode={(mode) => {
              setActiveQuestionId(undefined);
              setCurrentMode(mode);
            }}
            onBackToHome={() => setCurrentMode('home')}
          />
        )}

        {/* Mock Exam Mode */}
        {currentMode === 'exam' && (
          <ExamView
            questions={questions}
            onSaveExamRecord={handleSaveExamRecord}
            onRecordWrong={(qId, ans) => handleAnswerQuestion(qId, ans, false)}
          />
        )}

        {/* Dedicated Wrong Book Mode */}
        {currentMode === 'wrong' && (
          <WrongBookView
            questions={questions}
            progress={progress}
            onToggleMastered={handleToggleMastered}
            onJumpToPractice={handleJumpToPractice}
            onClearWrongStatus={handleClearWrongStatus}
          />
        )}

        {/* Question Bank Manager & Feeding Center */}
        {currentMode === 'manage' && (
          <QuestionManagerView
            questions={questions}
            onUpdateQuestions={handleUpdateQuestions}
          />
        )}

      </main>

      {/* Footer - displayed only in secondary utility pages */}
      {currentMode !== 'chapter' && currentMode !== 'home' && (
        <footer className="border-t border-slate-200 dark:border-slate-900 bg-white dark:bg-slate-950/80 py-6 text-center text-xs text-slate-500">
          <div className="max-w-7xl mx-auto px-4 flex flex-wrap items-center justify-between gap-4">
            <div className="flex items-center gap-2">
              <span className="font-bold text-slate-700 dark:text-slate-400">大观园 · 信号与系统智能研学知识库</span>
              <span>·</span>
              <span>广东工业大学 837/809 专业课专属题库与真题解析系统</span>
            </div>

            <div className="flex items-center gap-4 text-slate-400 dark:text-slate-500">
              <span>支持 LaTeX 公式 / KaTeX</span>
              <span>·</span>
              <span>支持纯键盘盲操</span>
              <span>·</span>
              <span>随时在「题库中心」喂入新题</span>
            </div>
          </div>
        </footer>
      )}

      {/* Analytics Modal */}
      <StatsModal
        isOpen={isStatsOpen}
        onClose={() => setIsStatsOpen(false)}
        questions={questions}
        progress={progress}
        examRecords={examRecords}
      />

      {/* Keyboard Shortcuts Cheatsheet Modal */}
      <KeyboardHelpModal
        isOpen={isKeyboardHelpOpen}
        onClose={() => setIsKeyboardHelpOpen(false)}
      />

    </div>
  );
};
