export const STANDARD_SOURCES = [
  '广工 837/809 历年真题',
  '小马哥《信号与系统960题》',
  '郑君里《信号与系统》(第3版)',
  '奥本海姆《信号与系统》(第2版)',
  '32 绝杀专题'
] as const;

export type StandardSource = typeof STANDARD_SOURCES[number];

/**
 * Maps any question source string into a clean, unified standard source category.
 */
export const getQuestionSourceCategory = (source?: string): StandardSource | string => {
  if (!source) return '广工 837/809 历年真题';
  
  if (source.includes('960')) {
    return '小马哥《信号与系统960题》';
  }
  if (source.includes('郑君里')) {
    return '郑君里《信号与系统》(第3版)';
  }
  if (source.includes('奥本海姆')) {
    return '奥本海姆《信号与系统》(第2版)';
  }
  if (source.includes('绝杀') || source.includes('32专题') || source.includes('32')) {
    return '32 绝杀专题';
  }
  if (
    source.includes('广工') || 
    source.includes('广东工业大学') || 
    source.includes('837') || 
    source.includes('809')
  ) {
    return '广工 837/809 历年真题';
  }
  
  return '广工 837/809 历年真题';
};
