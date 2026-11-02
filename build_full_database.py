# -*- coding: utf-8 -*-
"""
Full Question Bank Generator for 广工 837/809 信号与系统
Incorporating 2005-2025 genuine exams, 32 专题, and classic drill collections.
Organized strictly into 7 chapters, fully deduplicated, with 100% complete answers and derivations.
"""

import json
import os

all_questions = []

# ==========================================
# 第一章：信号与系统基础 (22 题)
# ==========================================
chapter1_questions = [
  {
    "id": "ss-c1-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "离散序列周期判定",
    "type": "single",
    "difficulty": 3,
    "tags": ["2024年837真题", "离散周期", "高频必考"],
    "source": "广东工业大学2024年837全国统考真题第1题",
    "stem": "已知离散序列 $f(k) = \\sin\\left(\\frac{3}{4}\\pi k + \\frac{\\pi}{3}\\right) + 2\\cos\\left(\\frac{5}{6}\\pi k + \\frac{\\pi}{4}\\right)$，则该序列的周期 $N$ 为：",
    "options": [
      { "key": "A", "text": "12" },
      { "key": "B", "text": "24" },
      { "key": "C", "text": "48" },
      { "key": "D", "text": "该序列不是周期序列" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：离散正弦序列的周期性判定及最小公倍数法。

1. **第一分量分析**：
   对于 $f_1(k) = \\sin\\left(\\frac{3}{4}\\pi k + \\frac{\\pi}{3}\\right)$，数字角频率为 $\\Omega_1 = \\frac{3}{4}\\pi$。
   由离散周期公式 $\\frac{2\\pi}{\\Omega_1} = \\frac{2\\pi}{\\frac{3}{4}\\pi} = \\frac{8}{3}$。
   因为 $\\frac{8}{3}$ 是既约有理数，取正整数倍 $m_1 = 3$，其基本周期为：
   $$N_1 = \\frac{2\\pi}{\\Omega_1} \\times 3 = 8$$

2. **第二分量分析**：
   对于 $f_2(k) = 2\\cos\\left(\\frac{5}{6}\\pi k + \\frac{\\pi}{4}\\right)$，数字角频率 $\\Omega_2 = \\frac{5}{6}\\pi$。
   同理有 $\\frac{2\\pi}{\\Omega_2} = \\frac{2\\pi}{\\frac{5}{6}\\pi} = \\frac{12}{5}$。
   取正整数倍 $m_2 = 5$，其基本周期为：
   $$N_2 = \\frac{2\\pi}{\\Omega_2} \\times 5 = 12$$

3. **求复合信号总周期**：
   两分量周期的最小公倍数：
   $$N = \\text{lcm}(N_1, N_2) = \\text{lcm}(8, 12) = 24$$
故该序列的周期为 **24**。选 **B**。"""
  },
  {
    "id": "ss-c1-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "连续信号周期判定",
    "type": "single",
    "difficulty": 2,
    "tags": ["2022年837真题", "连续周期", "经典题型"],
    "source": "广东工业大学2022年837全国统考真题第1题",
    "stem": "连续时间信号 $f(t) = \\cos(10t + 0.5\\pi) + \\sin(20t + \\frac{\\pi}{3})$ 的基波周期 $T$ 为：",
    "options": [
      { "key": "A", "text": "$\\frac{\\pi}{10}$" },
      { "key": "B", "text": "$\\frac{\\pi}{5}$" },
      { "key": "C", "text": "$\\frac{\\pi}{20}$" },
      { "key": "D", "text": "非周期信号" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：连续信号的周期性条件及基波周期计算。

1. 第一个分量角频率 $\\omega_1 = 10\\text{ rad/s}$，周期 $T_1 = \\frac{2\\pi}{\\omega_1} = \\frac{2\\pi}{10} = \\frac{\\pi}{5}$；
2. 第二个分量角频率 $\\omega_2 = 20\\text{ rad/s}$，周期 $T_2 = \\frac{2\\pi}{\\omega_2} = \\frac{2\\pi}{20} = \\frac{\\pi}{10}$；
3. 两周期比值 $\\frac{T_1}{T_2} = \\frac{\\pi / 5}{\\pi / 10} = 2$ 为有理数，因此复合信号是周期信号；
4. 基波周期为两分量周期的最小公倍数：$T = \\frac{\\pi}{5}$。
选 **B**。"""
  },
  {
    "id": "ss-c1-03",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "离散无周期判定",
    "type": "judgment",
    "difficulty": 2,
    "tags": ["经典概念", "离散周期", "陷阱题"],
    "source": "广东工业大学837核心考点与绝杀32专题",
    "stem": "离散时间序列 $f(k) = \\cos(3k)$ 是周期的，其周期为 $\\frac{2\\pi}{3}$。",
    "options": [
      { "key": "A", "text": "正确（True）" },
      { "key": "B", "text": "错误（False）" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：离散正弦序列具有周期的充分必要条件。

1. 离散正弦信号具有周期性的充要条件是其数字角频率 $\\Omega$ 与 $2\\pi$ 的比值为**有理数**：
   $$\\frac{2\\pi}{\\Omega} = \\frac{2\\pi}{3}$$
2. 因为 $\\pi$ 是无理数，故 $\\frac{2\\pi}{3}$ 是无理数，不存在任何正整数对 $(N, m)$ 使得 $3N = 2\\pi m$。
3. 因此该序列虽然包络为余弦，但在离散采样点上**永远不重复**，是严格的非周期序列！
故陈述错误，选 **B**。"""
  },
  {
    "id": "ss-c1-04",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "广义导数与冲激筛选",
    "type": "single",
    "difficulty": 3,
    "tags": ["2021年837真题", "广义导数", "阶跃求导"],
    "source": "广东工业大学2021年837全国统考真题第1题",
    "stem": "计算广义导数 $\\frac{d}{dt} \\left\\{ [\\cos(2t) + \\sin(t)] \\varepsilon(t) \\right\\}$ 的化简结果为：",
    "options": [
      { "key": "A", "text": "$[-2\\sin(2t) + \\cos(t)]\\varepsilon(t)$" },
      { "key": "B", "text": "$[-2\\sin(2t) + \\cos(t)]\\varepsilon(t) + \\delta(t)$" },
      { "key": "C", "text": "$[-2\\sin(2t) + \\cos(t)]\\varepsilon(t) + 2\\delta(t)$" },
      { "key": "D", "text": "$\\delta(t)$" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：含阶跃跃变信号的广义微积分法则。

1. 根据乘积微分法则：
   $$\\frac{d}{dt}[f(t)\\varepsilon(t)] = f'(t)\\varepsilon(t) + f(t)\\frac{d\\varepsilon(t)}{dt} = f'(t)\\varepsilon(t) + f(t)\\delta(t)$$
2. 代入冲激乘积性质 $f(t)\\delta(t) = f(0)\\delta(t)$：
   - 设 $f(t) = \\cos(2t) + \\sin(t)$；
   - 导数 $f'(t) = -2\\sin(2t) + \\cos(t)$；
   - 在原点处取值：$f(0) = \\cos(0) + \\sin(0) = 1 + 0 = 1$；
3. 合并得：
   $$\\frac{d}{dt}\\{f(t)\\varepsilon(t)\\} = [-2\\sin(2t) + \\cos(t)]\\varepsilon(t) + 1 \\cdot \\delta(t)$$
故正确答案选 **B**。"""
  },
  {
    "id": "ss-c1-05",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "冲激偶导数筛选",
    "type": "single",
    "difficulty": 3,
    "tags": ["2024年837真题", "冲激偶", "导数筛选"],
    "source": "广东工业大学2024年837全国统考真题第2题",
    "stem": "计算广义定积分 $\\int_{-\\infty}^\\infty (1 - x)\\delta'(x) \\, dx$ 的数值为：",
    "options": [
      { "key": "A", "text": "-1" },
      { "key": "B", "text": "0" },
      { "key": "C", "text": "1" },
      { "key": "D", "text": "2" }
    ],
    "answer": "C",
    "analysis": """【核心考点】：冲激偶函数 $\\delta'(t)$ 的导数筛选性质。

1. 冲激偶基本积分公式：
   $$\\int_{-\\infty}^{+\\infty} f(x)\\delta'(x) \\, dx = -f'(0)$$
   （注意公式前自带负号，来自分布分部积分法）。
2. 本题中待积函数为 $f(x) = 1 - x$；
3. 求导得：$f'(x) = -1$，因此 $f'(0) = -1$；
4. 代入公式计算：
   $$\\int_{-\\infty}^{+\\infty} (1 - x)\\delta'(x) \\, dx = -(-1) = 1$$
故正确答案为 **C**。"""
  },
  {
    "id": "ss-c1-06",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "尺度变换与极限化简",
    "type": "single",
    "difficulty": 3,
    "tags": ["2022年837真题", "尺度变换", "洛必达/等价无穷小"],
    "source": "广东工业大学2022年837全国统考真题第2题",
    "stem": "广义定积分 $\\int_{-\\infty}^\\infty \\frac{\\sin(\\pi t)}{t}\\delta(2t) \\, dt$ 的计算结果为：",
    "options": [
      { "key": "A", "text": "$\\pi$" },
      { "key": "B", "text": "$\\frac{\\pi}{2}$" },
      { "key": "C", "text": "$2\\pi$" },
      { "key": "D", "text": "0" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：冲激函数的尺度变换性质及 $t \\to 0$ 极限筛选。

1. 由冲激函数尺度变换公式：$\\delta(at) = \\frac{1}{|a|}\\delta(t)$，此处 $a = 2$：
   $$\\delta(2t) = \\frac{1}{2}\\delta(t)$$
2. 原积分转化为：
   $$I = \\int_{-\\infty}^\\infty \\frac{\\sin(\\pi t)}{t} \\cdot \\left[\\frac{1}{2}\\delta(t)\\right] dt = \\frac{1}{2} \\int_{-\\infty}^\\infty \\left[\\frac{\\sin(\\pi t)}{t}\\right] \\delta(t) \\, dt$$
3. 由冲激筛选性质，被积函数在 $t = 0$ 处的取值为极限值：
   $$\\lim_{t \\to 0} \\frac{\\sin(\\pi t)}{t} = \\pi$$
4. 因此：
   $$I = \\frac{1}{2} \\times \\pi = \\frac{\\pi}{2}$$
故选 **B**。"""
  },
  {
    "id": "ss-c1-07",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "时移冲激二次多项式筛选",
    "type": "single",
    "difficulty": 2,
    "tags": ["2023年837真题", "冲激筛选", "基础送分"],
    "source": "广东工业大学2023年837全国统考真题第1题",
    "stem": "计算广义定积分 $\\int_{-\\infty}^\\infty (t^2 - 3t + 2)\\delta(t - 2) \\, dt$ 的数值为：",
    "options": [
      { "key": "A", "text": "0" },
      { "key": "B", "text": "2" },
      { "key": "C", "text": "-2" },
      { "key": "D", "text": "4" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：时移冲激函数 $\\delta(t - t_0)$ 的积分筛选性质。

1. 冲激函数脉冲中心在 $t = 2$ 处；
2. 由筛选性质公式：
   $$\\int_{-\\infty}^\\infty f(t)\\delta(t - t_0)dt = f(t_0)$$
3. 将 $t = 2$ 代入 $f(t) = t^2 - 3t + 2$：
   $$f(2) = 2^2 - 3(2) + 2 = 4 - 6 + 2 = 0$$
故原积分值为 **0**。选 **A**。"""
  },
  {
    "id": "ss-c1-08",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "时变性差分判定",
    "type": "single",
    "difficulty": 2,
    "tags": ["2021年837真题", "时变性", "线性性"],
    "source": "广东工业大学2021年837全国统考真题第3题",
    "stem": "已知某离散系统由差分方程 $y(k) - k y(k - 1) + y(k - 2) = f(k)$ 描述，则该系统属于：",
    "options": [
      { "key": "A", "text": "线性、时不变系统" },
      { "key": "B", "text": "线性、时变系统" },
      { "key": "C", "text": "非线性、时不变系统" },
      { "key": "D", "text": "非线性、时变系统" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：差分方程系统的线性与时不变性判断。

1. **线性判断**：方程中所有的 $y$ 和 $f$ 项均为一次项，不存在乘方、交叉相乘或非线性函数操作，满足齐次性与可加性，因此系统为**线性系统**；
2. **时变性判断**：在项 $k y(k-1)$ 中，系数包含了时间自变量 $k$。当输入延时 $k_0$ 时，方程中的系数 $k$ 不发生同步平移，导致系统响应不满足时移不变性，因此为**时变系统**（变系数差分方程必时变）。
综上，该系统为**线性时变系统**。选 **B**。"""
  },
  {
    "id": "ss-c1-09",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "非线性时不变判定",
    "type": "single",
    "difficulty": 2,
    "tags": ["2022年837真题", "系统五大特性", "余弦非线性"],
    "source": "广东工业大学2022年837全国统考真题第4题",
    "stem": "某连续系统的输入激励为 $e(t)$，输出响应为 $r(t) = \\cos[e(t)]\\, (t > 0)$，则该系统是：",
    "options": [
      { "key": "A", "text": "线性、时不变系统" },
      { "key": "B", "text": "非线性、时不变系统" },
      { "key": "C", "text": "线性、时变系统" },
      { "key": "D", "text": "非线性、时变系统" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：输入输出代数关系的线性与时变性检验。

1. **线性检验**：
   若输入 $e_1(t) \\to r_1(t) = \\cos[e_1(t)]$；
   输入 $e_2(t) \\to r_2(t) = \\cos[e_2(t)]$；
   当输入复合激励 $e_1(t) + e_2(t)$ 时，输出为 $\\cos[e_1(t) + e_2(t)] \\ne \\cos[e_1(t)] + \\cos[e_2(t)]$，违背可加性。且 $e=0$ 时输出为 $\\cos(0)=1 \\ne 0$。因此必为**非线性系统**。
2. **时变性检验**：
   若输入延时 $t_0$：$e(t - t_0)$，系统的直接输出为 $\\cos[e(t - t_0)]$，恰好等于原响应延时 $r(t - t_0)$。因此满足时不变性，为**时不变系统**。
综上，该系统为**非线性、时不变系统**。选 **B**。"""
  },
  {
    "id": "ss-c1-10",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "指数衰减信号能量计算",
    "type": "single",
    "difficulty": 2,
    "tags": ["2023年837真题", "能量信号", "积分计算"],
    "source": "广东工业大学2023年837全国统考真题第3题",
    "stem": "计算单边实指数衰减信号 $f_1(t) = e^{-2t}\\varepsilon(t)$ 的总能量 $E$ 与平均功率 $P$ 分别为：",
    "options": [
      { "key": "A", "text": "$E = \\frac{1}{4}\\text{ J}, \\, P = 0\\text{ W}$" },
      { "key": "B", "text": "$E = \\frac{1}{2}\\text{ J}, \\, P = 0\\text{ W}$" },
      { "key": "C", "text": "$E = \\infty, \\, P = \\frac{1}{4}\\text{ W}$" },
      { "key": "D", "text": "$E = 1\\text{ J}, \\, P = 0\\text{ W}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：连续信号能量 $E$ 与平均功率 $P$ 的定义公式。

1. **信号总能量定义**：
   $$E = \\int_{-\\infty}^\\infty |f(t)|^2 dt = \\int_0^\\infty (e^{-2t})^2 dt = \\int_0^\\infty e^{-4t} dt$$
2. 计算定积分：
   $$E = \\left[ -\\frac{1}{4}e^{-4t} \\right]_0^\\infty = 0 - \\left(-\\frac{1}{4}\\right) = \\frac{1}{4}$$
3. 由于总能量 $0 < E < \\infty$ 为有限值，该信号为典型**能量信号**，其在无限区间的平均功率恒为 **0**：
   $$P = \\lim_{T \\to \\infty} \\frac{1}{T} \\int_{-T/2}^{T/2} |f(t)|^2 dt = 0$$
选 **A**。"""
  },
  {
    "id": "ss-c1-11",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "虚指数信号功率计算",
    "type": "single",
    "difficulty": 2,
    "tags": ["绝杀32专题", "功率信号", "复指数模长"],
    "source": "通信考研绝杀32专题系列之专题4",
    "stem": "计算连续复指数信号 $f_2(t) = e^{j(2t + \\frac{\\pi}{4})}$ 的能量与平均功率：",
    "options": [
      { "key": "A", "text": "$E = \\infty, \\, P = 1\\text{ W}$" },
      { "key": "B", "text": "$E = 1\\text{ J}, \\, P = 0\\text{ W}$" },
      { "key": "C", "text": "$E = \\infty, \\, P = \\frac{1}{2}\\text{ W}$" },
      { "key": "D", "text": "$E = \\infty, \\, P = 2\\text{ W}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：复指数信号的模长性质与功率计算。

1. 复指数信号的瞬时模长恒定：
   $$|f_2(t)| = \\left| e^{j(2t + \\frac{\\pi}{4})} \\right| = 1$$
2. 在有限区间积分的瞬时功率为 1，在全时域总能量为：
   $$E = \\int_{-\\infty}^\\infty 1^2 dt = \\infty$$
3. 平均功率计算：
   $$P = \\lim_{T \\to \\infty} \\frac{1}{T} \\int_{-T/2}^{T/2} 1 \\, dt = 1\\text{ W}$$
因此该信号属于标准的**功率信号**。选 **A**。"""
  },
  {
    "id": "ss-c1-12",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "初始状态微分系统线性判断",
    "type": "judgment",
    "difficulty": 3,
    "tags": ["2025年809真题", "微分方程", "零输入线性"],
    "source": "广东工业大学2025年809全国统考真题第2题",
    "stem": "判断系统 $\\frac{df(t)}{dt} + 3f(t) + 5y(0_-) = 0$ 满足线性系统的定义（具有线性性质）。",
    "options": [
      { "key": "A", "text": "正确（True）" },
      { "key": "B", "text": "错误（False）" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：动态系统的零输入线性与零状态线性。

1. 线性系统的充要条件是同时满足：
   - **可加性**：$T[f_1 + f_2, x_1(0) + x_2(0)] = T[f_1, x_1(0)] + T[f_2, x_2(0)]$
   - **齐次性**：$T[a f, a x(0)] = a T[f, x(0)]$
2. 该常微分方程中，$f(t)$、其导数项 $\\frac{df(t)}{dt}$ 以及初始状态项 $y(0_-)$ 均严格为一次线性组合，不存在乘方或非线性运算。
3. 因此分别满足零输入响应线性和零状态响应线性，叠加后仍满足整体线性。
故陈述正确，选 **A**。"""
  },
  {
    "id": "ss-c1-13",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "因果系统判定",
    "type": "single",
    "difficulty": 2,
    "tags": ["经典真题", "因果性", "反折非因果"],
    "source": "广东工业大学837/809真题高频题",
    "stem": "在以下输入输出对应关系中，属于因果系统（Causal System）的是：",
    "options": [
      { "key": "A", "text": "$y(t) = f(2t)$" },
      { "key": "B", "text": "$y(t) = f(t - 2) + f(t)$" },
      { "key": "C", "text": "$y(t) = f(t + 1)$" },
      { "key": "D", "text": "$y(t) = f(-t)$" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：因果系统的物理定义。

1. 因果系统的本质特征是：系统在任意时刻 $t_0$ 的输出响应，只取决于**当前时刻 $t_0$ 和过去时刻 $t < t_0$** 的输入激励，绝不能取决于**未来时刻 $t > t_0$** 的输入。
2. 逐项检验：
   - A: $y(t) = f(2t)$，当 $t = 1$ 时，$y(1) = f(2)$ 取决于未来值，非因果；
   - B: $y(t) = f(t - 2) + f(t)$，输出仅取决于过去时刻 $t - 2$ 和当前时刻 $t$，完全不依赖未来值，是**因果系统**！
   - C: $y(t) = f(t + 1)$，明显超前 1 个时间单位，非因果；
   - D: $y(t) = f(-t)$，当 $t = -2$ 时，$y(-2) = f(2)$ 取决于未来时刻的值，非因果。
故选 **B**。"""
  },
  {
    "id": "ss-c1-14",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "积分器系统BIBO稳定性",
    "type": "judgment",
    "difficulty": 3,
    "tags": ["2019年837真题", "BIBO稳定", "积分器不稳定"],
    "source": "广东工业大学2019年837统考真题",
    "stem": "理想积分器系统 $y(t) = \\int_{-\\infty}^t f(\\tau) \\, d\\tau$ 是 BIBO（有界输入有界输出）稳定系统。",
    "options": [
      { "key": "A", "text": "正确（True）" },
      { "key": "B", "text": "错误（False）" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：连续 LTI 系统的 BIBO 稳定性判据。

1. 连续 LTI 系统 BIBO 稳定的充要条件是其冲激响应 $h(t)$ 必须在全时域**绝对可积**：
   $$\\int_{-\\infty}^{+\\infty} |h(t)| \\, dt < \\infty$$
2. 对于理想积分器，令输入为 $f(t) = \\delta(t)$，其冲激响应为单位阶跃函数：
   $$h(t) = \\int_{-\\infty}^t \\delta(\\tau) d\\tau = \\varepsilon(t)$$
3. 对其冲激响应积分：
   $$\\int_{-\\infty}^{+\\infty} |h(t)| dt = \\int_0^{+\\infty} 1 \\, dt = \\infty$$
   不满足绝对可积条件。
4. 反例举证：输入有界信号 $f(t) = \\varepsilon(t)$（$|f(t)| \\le 1$ 有界），输出为斜坡信号 $y(t) = t \\varepsilon(t)$，当 $t \\to \\infty$ 时 $y(t) \\to \\infty$ 发散无界！
因此理想积分器**不是**稳定系统。本题陈述错误，选 **B**。"""
  },
  {
    "id": "ss-c1-15",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "有限区间冲激筛选积分",
    "type": "single",
    "difficulty": 2,
    "tags": ["2020年837真题", "冲激筛选", "经典易错"],
    "source": "广东工业大学2020年837全国统考真题第1题",
    "stem": "计算广义定积分 $\\int_{-1}^2 (2t^2 - 2t)\\delta(t - 1) \\, dt$ 的值为：",
    "options": [
      { "key": "A", "text": "0" },
      { "key": "B", "text": "2" },
      { "key": "C", "text": "-2" },
      { "key": "D", "text": "4" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：冲激函数的有限区间筛选性质。

1. 冲激函数脉冲中心在 $t = 1$ 处；
2. 积分区间为 $[-1, 2]$，由于 $1 \\in (-1, 2)$，冲激点落在积分区间内部；
3. 代入筛选性质公式：
   $$\\int_{-1}^2 f(t)\\delta(t - 1)dt = f(1)$$
4. 计算函数值：
   $$f(1) = 2(1)^2 - 2(1) = 2 - 2 = 0$$
故原积分值为 **0**。选 **A**。"""
  },
  {
    "id": "ss-c1-16",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "冲激乘积与零信号",
    "type": "single",
    "difficulty": 2,
    "tags": ["2020年837真题", "冲激乘积", "零信号"],
    "source": "广东工业大学2020年837全国统考真题第2题",
    "stem": "计算时域表达式 $t\\delta(t) * [\\delta(t) - \\delta(t - 3)]$ 的化简结果为：",
    "options": [
      { "key": "A", "text": "0" },
      { "key": "B", "text": "$\\delta(t)$" },
      { "key": "C", "text": "$t\\delta(t)$" },
      { "key": "D", "text": "$-3\\delta(t - 3)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：自变量与冲激函数的乘积性质。

1. 根据冲激函数的基本乘积性质：
   $$f(t)\\delta(t) = f(0)\\delta(t)$$
2. 当 $f(t) = t$ 时，在 $t = 0$ 处 $f(0) = 0$：
   $$t\\delta(t) = 0 \\cdot \\delta(t) = 0$$
3. 任何信号与恒等于零的零信号做卷积，结果仍为零信号：
   $$0 * [\\delta(t) - \\delta(t - 3)] = 0$$
故化简结果恒为 **0**。选 **A**。"""
  },
  {
    "id": "ss-c1-17",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "负无穷到正无穷冲激筛选",
    "type": "single",
    "difficulty": 2,
    "tags": ["2018年837真题", "冲激积分", "原点筛选"],
    "source": "广东工业大学2018年837全国统考真题第1题",
    "stem": "计算广义积分 $\\int_{-\\infty}^\\infty (t^2 - 2)\\delta(t) \\, dt$ 的值为：",
    "options": [
      { "key": "A", "text": "-2" },
      { "key": "B", "text": "0" },
      { "key": "C", "text": "2" },
      { "key": "D", "text": "-4" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：原点冲激函数 $\\delta(t)$ 的标准筛选性质。

1. 冲激函数筛选公式：
   $$\\int_{-\\infty}^\\infty f(t)\\delta(t)dt = f(0)$$
2. 代入 $f(t) = t^2 - 2$：
   $$f(0) = 0^2 - 2 = -2$$
故正确答案为 **A**。"""
  },
  {
    "id": "ss-c1-18",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "区间外冲激积分等于零",
    "type": "single",
    "difficulty": 2,
    "tags": ["2025年809真题", "冲激区间", "易错防坑"],
    "source": "广东工业大学2025年809全国统考真题第1题",
    "stem": "计算广义积分 $\\int_{-2}^2 \\delta\\left(\\frac{t}{4} - 1\\right) \\, dt$ 的值为：",
    "options": [
      { "key": "A", "text": "0" },
      { "key": "B", "text": "4" },
      { "key": "C", "text": "1" },
      { "key": "D", "text": "$\\frac{1}{4}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：冲激函数作用点与积分区间的从属关系。

1. 令冲激函数内部自变量为零：
   $$\\frac{t}{4} - 1 = 0 \\implies t = 4$$
2. 本题的定积分区间为 $[-2, 2]$；
3. 由于冲激作用点 $t = 4 \\notin [-2, 2]$，在积分区间内部被积函数处处严格为零；
4. 因此该广义定积分的值恒等于 **0**。
选 **A**。"""
  },
  {
    "id": "ss-c1-19",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "尺度变换冲激积分",
    "type": "single",
    "difficulty": 2,
    "tags": ["2019年837真题", "尺度变换", "冲激积分"],
    "source": "广东工业大学2019年837全国统考真题第1题",
    "stem": "计算广义定积分 $\\int_{-\\infty}^\\infty \\delta\\left(\\frac{t}{2} - 1\\right)(t^2 + 2) \\, dt$ 的数值为：",
    "options": [
      { "key": "A", "text": "6" },
      { "key": "B", "text": "12" },
      { "key": "C", "text": "3" },
      { "key": "D", "text": "24" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：冲激函数内部含平移与尺度的化简公式 $\\delta(at - b) = \\frac{1}{|a|}\\delta(t - \\frac{b}{a})$。

1. 化简复合冲激项：
   $$\\delta\\left(\\frac{t}{2} - 1\\right) = \\delta\\left(\\frac{1}{2}(t - 2)\\right) = \\frac{1}{\\frac{1}{2}}\\delta(t - 2) = 2\\delta(t - 2)$$
2. 代入积分表达式：
   $$I = \\int_{-\\infty}^\\infty 2\\delta(t - 2)(t^2 + 2) \\, dt = 2 \\times (2^2 + 2) = 2 \\times 6 = 12$$
故正确答案为 **B**。"""
  },
  {
    "id": "ss-c1-20",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "时域尺度加移位综合",
    "type": "single",
    "difficulty": 3,
    "tags": ["2024年809真题", "尺度变换", "时移计算"],
    "source": "广东工业大学2024年809全国统考真题第9题",
    "stem": "计算定积分 $\\int_{-\\infty}^\\infty (t^2 + 1)\\delta(3t - 2) \\, dt$ 的数值为：",
    "options": [
      { "key": "A", "text": "$\\frac{13}{27}$" },
      { "key": "B", "text": "$\\frac{13}{9}$" },
      { "key": "C", "text": "$\\frac{4}{9}$" },
      { "key": "D", "text": "$\\frac{5}{3}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：冲激函数的尺度变换性质 $\\delta(at - b) = \\frac{1}{|a|}\\delta(t - \\frac{b}{a})$。

1. 提取自变量系数：
   $$\\delta(3t - 2) = \\frac{1}{3}\\delta\\left(t - \\frac{2}{3}\\right)$$
2. 代入积分公式筛选：
   $$\\int_{-\\infty}^\\infty (t^2 + 1) \\cdot \\left[\\frac{1}{3}\\delta\\left(t - \\frac{2}{3}\\right)\\right] dt = \\frac{1}{3} \\left[ \\left(\\frac{2}{3}\\right)^2 + 1 \\right]$$
3. 计算数值：
   $$\\frac{1}{3} \\left( \\frac{4}{9} + 1 \\right) = \\frac{1}{3} \\times \\frac{13}{9} = \\frac{13}{27}$$
故正确答案为 **A**。"""
  },
  {
    "id": "ss-c1-21",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "非线性因果性判定",
    "type": "single",
    "difficulty": 2,
    "tags": ["2024年809真题", "时变性", "因果性"],
    "source": "广东工业大学2024年809全国统考真题第2、3题",
    "stem": "连续时间系统输入输出关系为 $r(t) = e(-2t)$，则该系统属于：",
    "options": [
      { "key": "A", "text": "时不变、因果系统" },
      { "key": "B", "text": "时变、非因果系统" },
      { "key": "C", "text": "时变、因果系统" },
      { "key": "D", "text": "时不变、非因果系统" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：反折与尺度系统的时变性与因果性判定。

1. **时变性分析**：
   - 若激励延时 $t_0$：$e_1(t) = e(t - t_0)$；
   - 系统的响应为 $r_1(t) = e_1(-2t) = e(-2t - t_0)$；
   - 而原响应延时为 $r(t - t_0) = e(-2(t - t_0)) = e(-2t + 2t_0)$；
   - 显然 $r_1(t) \\ne r(t - t_0)$，故该系统为**时变系统**。
2. **因果性分析**：
   - 考察时刻 $t = -1$ 时的输出响应：$r(-1) = e(-2(-1)) = e(2)$；
   - 在当前时刻 $t = -1$，输出值却取决于未来时刻 $t = 2$ 的输入值，违背因果律。
   - 故该系统为**非因果系统**。
综上，选 **B**。"""
  },
  {
    "id": "ss-c1-22",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "能量信号与功率信号判定",
    "type": "single",
    "difficulty": 3,
    "tags": ["2025年809真题", "能量计算", "反比例函数"],
    "source": "广东工业大学2025年809全国统考真题第13题",
    "stem": "连续信号 $f(t) = \\frac{1}{1 + t}\\varepsilon(t)$ 的总能量 $E$ 与平均功率 $P$ 分别为：",
    "options": [
      { "key": "A", "text": "$E = 1\\text{ J}, \\, P = 0\\text{ W}$" },
      { "key": "B", "text": "$E = \\infty, \\, P = 0\\text{ W}$" },
      { "key": "C", "text": "$E = 1\\text{ J}, \\, P = 1\\text{ W}$" },
      { "key": "D", "text": "$E = \\infty, \\, P = 1\\text{ W}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：连续信号的能量积分与能量/功率信号判定。

1. 根据连续信号总能量定义：
   $$E = \\int_{-\\infty}^{+\\infty} |f(t)|^2 dt = \\int_0^\\infty \\left(\\frac{1}{1 + t}\\right)^2 dt$$
2. 计算反常积分：
   $$E = \\left[ -\\frac{1}{1 + t} \\right]_0^\\infty = 0 - (-1) = 1\\text{ J}$$
3. 由于总能量为非零有限正数（$0 < E < \\infty$），故该信号是标准的**能量信号**。
4. 任何能量信号在无限时域上的平均功率必恒为零：$P = 0\\text{ W}$。
故选 **A**。"""
  }
]

all_questions.extend(chapter1_questions)
print(f"Added Chapter 1: {len(chapter1_questions)} questions")

# ==========================================
# 第二章：系统的时域分析 (15 题)
# ==========================================
chapter2_questions = [
  {
    "id": "ss-c2-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "离散卷积和图解法",
    "type": "single",
    "difficulty": 3,
    "tags": ["2024年837真题", "离散卷积", "序列计算"],
    "source": "广东工业大学2024年837全国统考真题第3题",
    "stem": "已知序列 $f_1(k) = \{\mathbf{3}_{k=0}, 2, 1\}$，$f_2(k) = \{\mathbf{2}_{k=0}, 1, 2\}$（带下划线处为 $k = 0$ 点），则卷积和 $f(k) = f_1(k) * f_2(k)$ 在 $k = 3$ 处的值 $f(3)$ 为：",
    "options": [
      { "key": "A", "text": "2" },
      { "key": "B", "text": "5" },
      { "key": "C", "text": "4" },
      { "key": "D", "text": "0" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：离散有限长序列卷积和的公式计算。

1. **序列非零区间分析**：
   - $f_1(k)$ 的非零点为 $k = 0, 1, 2$，对应数值 $f_1(0)=3, f_1(1)=2, f_1(2)=1$；
   - $f_2(k)$ 的非零点为 $k = 0, 1, 2$，对应数值 $f_2(0)=2, f_2(1)=1, f_2(2)=2$；
2. **计算 $k = 3$ 处的卷积值**：
   由离散卷积定义公式 $f(3) = \sum_{m=-\infty}^\infty f_1(m)f_2(3 - m)$：
   - 当 $m = 1$ 时：$f_1(1) f_2(2) = 2 \times 2 = 4$；
   - 当 $m = 2$ 时：$f_1(2) f_2(1) = 1 \times 1 = 1$；
   - 其余各项乘积均为 0；
3. **求和结果**：
   $$f(3) = 4 + 1 = 5$$
故正确答案为 **B**。"""
  },
  {
    "id": "ss-c2-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "全响应分解定理",
    "type": "single",
    "difficulty": 3,
    "tags": ["2023年837真题", "零输入响应", "零状态响应"],
    "source": "广东工业大学2023年837全国统考真题第2题",
    "stem": "某 LTI 连续系统，当初始状态不变、输入为 $f_1(t)$ 时，全响应 $y_1(t) = 2e^{-t} + e^{-2t}$；当输入变为 $2f_1(t)$ 时，全响应为 $y_2(t) = 2e^{-t} + 2e^{-2t}$。若输入为零（仅有原初始状态），则系统的零输入响应 $y_{zi}(t)$ 为：",
    "options": [
      { "key": "A", "text": "$2e^{-t}$" },
      { "key": "B", "text": "$e^{-2t}$" },
      { "key": "C", "text": "$2e^{-t} - e^{-2t}$" },
      { "key": "D", "text": "$e^{-t} + e^{-2t}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：线性时不变系统的全响应线性分解特性。

1. 根据 LTI 系统的全响应分解原理：
   $$y(t) = y_{zi}(t) + y_{zs}(t)$$
   其中零输入响应 $y_{zi}(t)$ 仅由初始状态产生，输入改变时不发生改变；
   零状态响应 $y_{zs}(t)$ 与输入激励成严格的正比例线性关系。
2. 建立线性方程组：
   - 第一次激励 $f_1(t)$：$y_{zi}(t) + y_{zs1}(t) = 2e^{-t} + e^{-2t}$    (式 1)
   - 第二次激励 $2f_1(t)$：$y_{zi}(t) + 2y_{zs1}(t) = 2e^{-t} + 2e^{-2t}$   (式 2)
3. 求解线性方程：
   - 用 (式 2) 减去 (式 1)：$y_{zs1}(t) = e^{-2t}$；
   - 代入 (式 1) 解得：
     $$y_{zi}(t) = (2e^{-t} + e^{-2t}) - e^{-2t} = 2e^{-t}$$
故零输入响应为 **A**。"""
  },
  {
    "id": "ss-c2-03",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "离散指数卷积和",
    "type": "single",
    "difficulty": 3,
    "tags": ["2021年837真题", "离散卷积公式", "等比求和"],
    "source": "广东工业大学2021年837全国统考真题第4题",
    "stem": "计算离散序列卷积和 $[(0.2)^k \varepsilon(k)] * [(0.4)^k \varepsilon(k)]$ 的化简解析式为：",
    "options": [
      { "key": "A", "text": "$[2(0.4)^k - (0.2)^k]\varepsilon(k)$" },
      { "key": "B", "text": "$[(0.4)^k - (0.2)^k]\varepsilon(k)$" },
      { "key": "C", "text": "$[2(0.4)^k - 2(0.2)^k]\varepsilon(k)$" },
      { "key": "D", "text": "$5[(0.4)^{k+1} - (0.2)^{k+1}]\varepsilon(k)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：单边指数阶跃序列的卷积公式。

1. 经典离散卷积公式（$a \ne b$ 时）：
   $$(a^k \varepsilon[k]) * (b^k \varepsilon[k]) = \frac{a^{k+1} - b^{k+1}}{a - b}\varepsilon[k]$$
2. 代入 $a = 0.4, \, b = 0.2$：
   $$y(k) = \frac{(0.4)^{k+1} - (0.2)^{k+1}}{0.4 - 0.2}\varepsilon[k] = \frac{0.4(0.4)^k - 0.2(0.2)^k}{0.2}\varepsilon[k]$$
3. 提取分母约分：
   $$y(k) = \left[ \frac{0.4}{0.2}(0.4)^k - \frac{0.2}{0.2}(0.2)^k \right] \varepsilon[k] = [2(0.4)^k - (0.2)^k]\varepsilon[k]$$
故正确答案为 **A**。"""
  },
  {
    "id": "ss-c2-04",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "单位样值响应求解",
    "type": "single",
    "difficulty": 2,
    "tags": ["2025年809真题", "离散冲激响应", "样值计算"],
    "source": "广东工业大学2025年809全国统考真题第15题",
    "stem": "已知离散系统单位样值响应 $h(n) = \delta(n) + 2\delta(n - 1) - \delta(n - 3)$，输入激励为 $x(n) = 2\delta(n - 1)$，则系统在 $n = 0$ 和 $n = 2$ 处的响应值 $y(0)$ 与 $y(2)$ 分别为：",
    "options": [
      { "key": "A", "text": "$y(0) = 0, \, y(2) = 4$" },
      { "key": "B", "text": "$y(0) = 2, \, y(2) = 2$" },
      { "key": "C", "text": "$y(0) = 0, \, y(2) = 2$" },
      { "key": "D", "text": "$y(0) = 1, \, y(2) = 4$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散时不变系统的卷积性质。

1. 根据卷积的时移和数乘性质：
   $$y(n) = x(n) * h(n) = 2\delta(n - 1) * [\delta(n) + 2\delta(n - 1) - \delta(n - 3)]$$
2. 逐项展开：
   $$y(n) = 2\delta(n - 1) + 4\delta(n - 2) - 2\delta(n - 4)$$
3. 计算指定点数值：
   - 当 $n = 0$ 时，由于各项冲激位置分别为 $1, 2, 4$，故 $y(0) = 0$；
   - 当 $n = 2$ 时，只有中间项 $4\delta(n - 2)$ 在 $n = 2$ 处激发出脉冲，故 $y(2) = 4$；
选 **A**。"""
  },
  {
    "id": "ss-c2-05",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "斜坡与阶跃连续卷积",
    "type": "single",
    "difficulty": 2,
    "tags": ["2018年837真题", "连续卷积", "积分性质"],
    "source": "广东工业大学2018年837全国统考真题第3题",
    "stem": "计算连续时间卷积积分 $t\varepsilon(t) * \varepsilon(t)$ 的化简结果为：",
    "options": [
      { "key": "A", "text": "$\frac{1}{2}t^2 \varepsilon(t)$" },
      { "key": "B", "text": "$t^2 \varepsilon(t)$" },
      { "key": "C", "text": "$t \varepsilon(t)$" },
      { "key": "D", "text": "$\frac{1}{6}t^3 \varepsilon(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：任意因果信号与单位阶跃信号的卷积积分等价于时域积分。

1. 任何信号 $f(t)$ 与单位阶跃函数 $\varepsilon(t)$ 卷积，其物理实质为其积分运算：
   $$f(t) * \varepsilon(t) = \int_{-\infty}^t f(\tau) \, d\tau$$
2. 本题中 $f(t) = t\varepsilon(t)$ 是因果信号，因此当 $t > 0$ 时：
   $$y(t) = \int_0^t \tau \, d\tau = \left[ \frac{1}{2}\tau^2 \right]_0^t = \frac{1}{2}t^2$$
   当 $t < 0$ 时，$y(t) = 0$。
3. 写作统一因果表达式：
   $$y(t) = \frac{1}{2}t^2 \varepsilon(t)$$
故选 **A**。"""
  },
  {
    "id": "ss-c2-06",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "时域积分性求零状态响应",
    "type": "single",
    "difficulty": 3,
    "tags": ["2018年837真题", "冲激响应", "斜坡响应"],
    "source": "广东工业大学2018年837全国统考真题第2题",
    "stem": "已知某 LTI 系统的冲激响应为 $h(t) = e^{-2t}\varepsilon(t)$，当输入激励为斜坡信号 $f(t) = t\varepsilon(t)$ 时，系统的零状态响应 $y_{zs}(t)$ 为：",
    "options": [
      { "key": "A", "text": "$\frac{1}{4}[2t - 1 + e^{-2t}]\varepsilon(t)$" },
      { "key": "B", "text": "$\frac{1}{2}[t - e^{-2t}]\varepsilon(t)$" },
      { "key": "C", "text": "$\frac{1}{2}[1 - e^{-2t}]\varepsilon(t)$" },
      { "key": "D", "text": "$[t e^{-2t}]\varepsilon(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：阶跃响应与斜坡响应的时域积分关联。

1. 当输入为单位阶跃 $\varepsilon(t)$ 时，系统的阶跃响应为：
   $$g(t) = \int_0^t h(\tau)d\tau = \int_0^t e^{-2\tau}d\tau = \frac{1}{2}(1 - e^{-2t})\varepsilon(t)$$
2. 斜坡信号 $t\varepsilon(t)$ 是阶跃信号的时域积分：$t\varepsilon(t) = \int_0^t \varepsilon(\tau)d\tau$。
3. 由 LTI 系统的积分性质，零状态响应等于阶跃响应的二次积分：
   $$y_{zs}(t) = \int_0^t g(\tau)d\tau = \int_0^t \frac{1}{2}(1 - e^{-2\tau})d\tau = \frac{1}{2}\left[ \tau + \frac{1}{2}e^{-2\tau} \right]_0^t$$
4. 代入限值化简：
   $$y_{zs}(t) = \frac{1}{2}\left[ t + \frac{1}{2}e^{-2t} - \frac{1}{2} \right] = \frac{1}{4}(2t - 1 + e^{-2t})\varepsilon(t)$$
故正确答案为 **A**。"""
  },
  {
    "id": "ss-c2-07",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "有限长离散序列全卷积",
    "type": "single",
    "difficulty": 2,
    "tags": ["2024年809真题", "离散卷积", "多项式乘法"],
    "source": "广东工业大学2024年809全国统考真题第1题",
    "stem": "已知离散序列 $f_1(n) = [3, 1, 7, 2]$（从 $n = 0$ 开始），$f_2(n) = [2, 3]$（从 $n = 0$ 开始），则卷积和 $f(n) = f_1(n) * f_2(n)$ 的完整序列为：",
    "options": [
      { "key": "A", "text": "$[6, 11, 17, 25, 6]$" },
      { "key": "B", "text": "$[6, 9, 21, 6, 0]$" },
      { "key": "C", "text": "$[6, 11, 14, 23, 6]$" },
      { "key": "D", "text": "$[5, 4, 10, 5, 0]$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散有限长序列卷积（对角线多项式乘法）。

1. 序列长度：$N_1 = 4, N_2 = 2$，卷积后序列长度为 $L = N_1 + N_2 - 1 = 5$；
2. 采用列竖式多项式乘法：
   - 乘以 2：$2 \times [3, 1, 7, 2] = [6, 2, 14, 4]$
   - 乘以 3（错开 1 位）：$3 \times [3, 1, 7, 2] = [0, 9, 3, 21, 6]$
3. 同位相加：
   - $n = 0$: $6$
   - $n = 1$: $2 + 9 = 11$
   - $n = 2$: $14 + 3 = 17$
   - $n = 3$: $4 + 21 = 25$
   - $n = 4$: $6$
故卷积结果为 $[6, 11, 17, 25, 6]$。选 **A**。"""
  },
  {
    "id": "ss-c2-08",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "卷积微分与平移性质",
    "type": "single",
    "difficulty": 3,
    "tags": ["2024年809真题", "微分性质", "冲激平移"],
    "source": "广东工业大学2024年809全国统考真题第5题",
    "stem": "已知连续信号满足 $f(t) * \delta(t + 1) * g(t) = s(t)$，则二阶导数 $s''(t)$ 等于：",
    "options": [
      { "key": "A", "text": "$g''(t) * f(t + 1)$" },
      { "key": "B", "text": "$g''(t) * f(t - 1)$" },
      { "key": "C", "text": "$g'(t) * f'(t + 1)$" },
      { "key": "D", "text": "$g(t) * f''(t - 1)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：时域卷积的微分性质与冲激平移性质。

1. 冲激函数的卷积平移性质：
   $$f(t) * \delta(t + 1) = f(t + 1)$$
   因此原式化简为：
   $$s(t) = f(t + 1) * g(t)$$
2. 根据卷积的微分性质：
   $$\frac{d^2}{dt^2}[x(t) * y(t)] = x''(t) * y(t) = x(t) * y''(t) = x'(t) * y'(t)$$
3. 将二阶微分作用于 $g(t)$ 上：
   $$s''(t) = f(t + 1) * g''(t) = g''(t) * f(t + 1)$$
选 **A**。"""
  },
  {
    "id": "ss-c2-09",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "离散序列抽样卷积和",
    "type": "single",
    "difficulty": 2,
    "tags": ["2018年837真题", "离散卷积", "序列值"],
    "source": "广东工业大学2018年837全国统考真题第4题",
    "stem": "已知序列 $f_1(k) = \{\mathbf{1}_{k=0}, 2, 3\}$，$f_2(k) = \{\mathbf{1}_{k=0}, 1, 1, 1\}$，令 $f(k) = f_1(k) * f_2(k)$，则 $f(2)$ 的数值为：",
    "options": [
      { "key": "A", "text": "3" },
      { "key": "B", "text": "6" },
      { "key": "C", "text": "5" },
      { "key": "D", "text": "1" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：离散卷积单点数值的定义求法。

1. 根据卷积和公式：
   $$f(2) = \sum_{m=0}^2 f_1(m) f_2(2 - m)$$
2. 展开各项相加：
   - $m = 0$: $f_1(0)f_2(2) = 1 \times 1 = 1$
   - $m = 1$: $f_1(1)f_2(1) = 2 \times 1 = 2$
   - $m = 2$: $f_1(2)f_2(0) = 3 \times 1 = 3$
3. 累加得：
   $$f(2) = 1 + 2 + 3 = 6$$
故正确答案为 **B**。"""
  },
  {
    "id": "ss-c2-10",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "时移连续卷积积分",
    "type": "single",
    "difficulty": 2,
    "tags": ["2019年837真题", "时移卷积", "解析推导"],
    "source": "广东工业大学2019年837全国统考真题第2题",
    "stem": "计算连续卷积表达式 $t\varepsilon(t) * \varepsilon(t - 1)$ 的化简结果为：",
    "options": [
      { "key": "A", "text": "$\frac{1}{2}(t - 1)^2 \varepsilon(t - 1)$" },
      { "key": "B", "text": "$\frac{1}{2}t^2 \varepsilon(t - 1)$" },
      { "key": "C", "text": "$(t - 1)\varepsilon(t - 1)$" },
      { "key": "D", "text": "$\frac{1}{2}(t^2 - 1)\varepsilon(t - 1)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：连续卷积的时移性质 $x(t) * y(t - t_0) = [x * y](t - t_0)$。

1. 已知基础卷积：
   $$t\varepsilon(t) * \varepsilon(t) = \frac{1}{2}t^2 \varepsilon(t)$$
2. 由于第二个信号为时移信号 $\varepsilon(t - 1)$，时延 $t_0 = 1$；
3. 根据时不变系统的时移性质，总输出结果只需在基础卷积结果上整体右移 1：
   $$t\varepsilon(t) * \varepsilon(t - 1) = \left[ \frac{1}{2}t^2 \varepsilon(t) \right]_{t \to t-1} = \frac{1}{2}(t - 1)^2 \varepsilon(t - 1)$$
故正确答案选 **A**。"""
  },
  {
    "id": "ss-c2-11",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "门函数自卷积三角波",
    "type": "single",
    "difficulty": 3,
    "tags": ["经典真题", "门函数", "三角脉冲"],
    "source": "广东工业大学837历年真题核心考点",
    "stem": "宽度为 $\tau$、高度为 1 的对称门函数 $f(t) = \text{rect}(t/\tau)$（即 $-\frac{\tau}{2} \le t \le \frac{\tau}{2}$ 时为 1），其自身卷积 $f(t) * f(t)$ 的波形是：",
    "options": [
      { "key": "A", "text": "底宽为 $2\tau$、峰值为 $\tau$ 的对称三角脉冲" },
      { "key": "B", "text": "底宽为 $\tau$、峰值为 1 的对称三角脉冲" },
      { "key": "C", "text": "宽度为 $2\tau$、高度为 1 的矩形脉冲" },
      { "key": "D", "text": "宽度为 $2\tau$、高度为 $\tau$ 的梯形脉冲" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：矩形脉冲时域自卷积的几何特性。

1. 时长叠加法则：两个时长均为 $\tau$ 的时间有限信号做卷积，卷积结果的时长严格为 $\tau + \tau = 2\tau$，非零区间为 $[-\tau, \tau]$；
2. 几何图解：两个高度为 1、宽度为 $\tau$ 的矩形在相对滑动时，重叠面积随移动距离 $|t|$ 呈线性增减：
   $$[f * f](t) = (\tau - |t|), \quad |t| \le \tau$$
3. 在 $t = 0$ 处重叠面积达到最大值，即峰值为 $\tau$；
4. 因此卷积波形为底宽 $2\tau$、高度为 $\tau$ 的等腰三角脉冲。
选 **A**。"""
  },
  {
    "id": "ss-c2-12",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "差分方程全响应求解",
    "type": "single",
    "difficulty": 3,
    "tags": ["2023年837真题", "差分方程", "齐次特解"],
    "source": "广东工业大学2023年837全国统考真题第4题",
    "stem": "已知离散系统满足差分方程 $y(k) - 0.5y(k - 1) = \varepsilon(k)$，初始状态 $y(-1) = 2$，则系统的全响应 $y(k)\,(k \ge 0)$ 为：",
    "options": [
      { "key": "A", "text": "$[2 - (0.5)^k]\varepsilon(k)$" },
      { "key": "B", "text": "$2\varepsilon(k)$" },
      { "key": "C", "text": "$[1 + (0.5)^k]\varepsilon(k)$" },
      { "key": "D", "text": "$[(0.5)^k]\varepsilon(k)$" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：一阶差分方程时域古典法求解（零输入 + 零状态响应）。

1. **求特征根与齐次解形式**：
   特征方程 $\alpha - 0.5 = 0 \implies \alpha = 0.5$；
   齐次解形式为 $C (0.5)^k$；
2. **零输入响应 $y_{zi}(k)$**：
   由无激励方程 $y(k) - 0.5y(k-1) = 0$：
   当 $k = 0$ 时，$y_{zi}(0) = 0.5 y(-1) = 0.5 \times 2 = 1$；
   由于 $y_{zi}(k) = C_{zi}(0.5)^k$，故 $C_{zi} = 1 \implies y_{zi}(k) = (0.5)^k \varepsilon(k)$；
3. **零状态响应 $y_{zs}(k)$**：
   特解设为常数 $K$：$K - 0.5K = 1 \implies K = 2$；
   全零状态解 $y_{zs}(k) = 2 + C_{zs}(0.5)^k$；
   因零状态条件 $y_{zs}(-1) = 0 \implies y_{zs}(0) = 0.5(0) + 1 = 1$；
   代入 $k = 0$：$2 + C_{zs} = 1 \implies C_{zs} = -1$；
   $$y_{zs}(k) = [2 - (0.5)^k]\varepsilon(k)$$
4. **全响应叠加**：
   $$y(k) = y_{zi}(k) + y_{zs}(k) = (0.5)^k + 2 - (0.5)^k = 2\varepsilon(k)$$
故正确答案为 **B**。"""
  },
  {
    "id": "ss-c2-13",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "矩形窗与阶跃卷积和",
    "type": "single",
    "difficulty": 2,
    "tags": ["2025年809真题", "离散卷积", "矩形序列"],
    "source": "广东工业大学2025年809全国统考真题第5题",
    "stem": "已知离散单位样值响应 $h(n) = u(n) - u(n - 3)$，输入序列为 $x(n) = u(n)$，则卷积输出 $y(n) = h(n) * x(n)$ 在 $n \ge 2$ 时的稳态数值恒为：",
    "options": [
      { "key": "A", "text": "3" },
      { "key": "B", "text": "2" },
      { "key": "C", "text": "1" },
      { "key": "D", "text": "$n + 1$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：有限长矩形窗序列与单位阶跃序列的时域卷积。

1. 单位样值响应 $h(n) = u(n) - u(n - 3) = \delta(n) + \delta(n - 1) + \delta(n - 2)$，非零样值点只有 3 个，且幅度均为 1；
2. 由卷积分配律：
   $$y(n) = x(n) * h(n) = u(n) * [\delta(n) + \delta(n - 1) + \delta(n - 2)] = u(n) + u(n - 1) + u(n - 2)$$
3. 当 $n \ge 2$ 时：
   三个阶跃项 $u(n), u(n-1), u(n-2)$ 均已触发并保持为 1；
   $$y(n) = 1 + 1 + 1 = 3$$
故在 $n \ge 2$ 时其数值恒为 **3**。选 **A**。"""
  },
  {
    "id": "ss-c2-14",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "串联系统总冲激响应",
    "type": "single",
    "difficulty": 1,
    "tags": ["2024年809真题", "串联连接", "时域卷积"],
    "source": "广东工业大学2024年809全国统考真题第8题",
    "stem": "由若干个线性时不变子系统串联组成的复合系统，其总冲激响应是各子系统冲激响应的：",
    "options": [
      { "key": "A", "text": "卷积（Convolution）" },
      { "key": "B", "text": "代数相乘（Multiplication）" },
      { "key": "C", "text": "代数相加（Addition）" },
      { "key": "D", "text": "复频域相加" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：LTI 系统的基本级联连接性质。

1. 若系统 1 冲激响应为 $h_1(t)$，中间输出为 $w(t) = f(t) * h_1(t)$；
2. 系统 2 冲激响应为 $h_2(t)$，最终输出为 $y(t) = w(t) * h_2(t) = [f(t) * h_1(t)] * h_2(t)$；
3. 由时域卷积的结合律：
   $$y(t) = f(t) * [h_1(t) * h_2(t)]$$
4. 因此串联系统的等效总冲激响应等于各子系统冲激响应的**时域卷积** $h(t) = h_1(t) * h_2(t)$。
选 **A**。"""
  },
  {
    "id": "ss-c2-15",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "零状态与强迫响应概念辨析",
    "type": "judgment",
    "difficulty": 2,
    "tags": ["2024年809真题", "自然响应", "强迫响应"],
    "source": "广东工业大学2024年809全国统考真题第11题",
    "stem": "若一个系统的初始状态为零，则该系统的零状态响应必定只包含强迫响应（受迫响应），不包含任何自然响应（固有响应）。",
    "options": [
      { "key": "A", "text": "正确（True）" },
      { "key": "B", "text": "错误（False）" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：全响应两种不同分解方式的交织辨析。

1. **按激励源分解**：全响应 = 零输入响应 $y_{zi}(t)$ + 零状态响应 $y_{zs}(t)$；
2. **按函数形式分解**：全响应 = 自然响应（具有系统特征根函数形式） + 强迫响应（具有外加激励函数形式）；
3. **关键关系**：
   - 零输入响应 $y_{zi}(t)$ 完全由特征根组成，全属于自然响应；
   - 但**零状态响应 $y_{zs}(t)$ 同样同时包含自然响应分量与强迫响应分量**！只有在初始状态为零且外加特征根激励的极端特殊情况下才会全部合并。
   - 正常情况下，$y_{zs}(t) = y_{zs, \text{nat}} + y_{zs, \text{forced}}$。
故题中陈述“零状态响应必定只包含强迫响应”是错误的。选 **B**。"""
  }
]

all_questions.extend(chapter2_questions)
print(f"Added Chapter 2: {len(chapter2_questions)} questions")


# ==========================================
# 第三章：频域分析与傅里叶变换 (18 题)
# ==========================================
chapter3_questions = [
  {
    "id": "ss-c3-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "实信号基波频率与傅里叶级数",
    "type": "single",
    "difficulty": 3,
    "tags": ["2024年837真题", "傅氏级数", "基波角频率"],
    "source": "广东工业大学2024年837全国统考真题第4题",
    "stem": "已知实信号 $f(t) = 5 - 6\cos\left(t - \frac{\pi}{6}\right) + 4\sin\left(\frac{3}{2}t + \frac{\pi}{4}\right)$，则该信号的基波角频率 $\omega_0$ 为：",
    "options": [
      { "key": "A", "text": "$0.5\text{ rad/s}$" },
      { "key": "B", "text": "$1.0\text{ rad/s}$" },
      { "key": "C", "text": "$1.5\text{ rad/s}$" },
      { "key": "D", "text": "$2.0\text{ rad/s}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：复合周期信号的基波角频率求解（最大公约数法）。

1. 信号中包含两个非直流正弦分量：
   - 第一个交流分量角频率：$\omega_1 = 1\text{ rad/s}$；
   - 第二个交流分量角频率：$\omega_2 = \frac{3}{2} = 1.5\text{ rad/s}$；
2. 连续复合周期信号的基波角频率 $\omega_0$ 是各分量角频率的最大公约数：
   $$\omega_0 = \gcd\left(1, \frac{3}{2}\right) = \gcd\left(\frac{2}{2}, \frac{3}{2}\right) = \frac{\gcd(2, 3)}{2} = \frac{1}{2} = 0.5\text{ rad/s}$$
3. 验证谐波次数：
   - $\omega_1 = 2\omega_0$（2次谐波）；
   - $\omega_2 = 3\omega_0$（3次谐波）；
故基波角频率为 **0.5 rad/s**。选 **A**。"""
  },
  {
    "id": "ss-c3-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "LTI系统稳态响应映射",
    "type": "single",
    "difficulty": 3,
    "tags": ["2024年837真题", "频率响应", "稳态正弦"],
    "source": "广东工业大学2024年837全国统考真题第6题",
    "stem": "已知某稳定连续 LTI 系统，当输入 $f(t) = e^{j 5t}$ 时，稳态响应为 $y(t) = e^{j 3t}$；当输入 $f(t) = e^{-j 5t}$ 时，稳态响应为 $y(t) = e^{-j 3t}$。若输入信号为 $f(t) = \cos(5t - 2)$，则系统的稳态输出 $y(t)$ 为：",
    "options": [
      { "key": "A", "text": "$\cos(3t - 2)$" },
      { "key": "B", "text": "$\cos(5t - 2)$" },
      { "key": "C", "text": "$\sin(3t - 2)$" },
      { "key": "D", "text": "$e^{j(3t - 2)}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：连续线性系统的频域特征映射与欧拉公式分解。

1. 由欧拉公式展开实余弦激励信号：
   $$f(t) = \cos(5t - 2) = \frac{1}{2}e^{j(5t - 2)} + \frac{1}{2}e^{-j(5t - 2)} = \frac{1}{2}e^{-j 2} \cdot e^{j 5t} + \frac{1}{2}e^{j 2} \cdot e^{-j 5t}$$
2. 由题意，系统对基底虚指数信号的频域映射关系为：
   - $e^{j 5t} \to e^{j 3t}$
   - $e^{-j 5t} \to e^{-j 3t}$
3. 由线性系统的齐次性与可加性，稳态响应为：
   $$y(t) = \frac{1}{2}e^{-j 2} \cdot e^{j 3t} + \frac{1}{2}e^{j 2} \cdot e^{-j 3t} = \frac{1}{2}e^{j(3t - 2)} + \frac{1}{2}e^{-j(3t - 2)} = \cos(3t - 2)$$
故正确答案为 **A**。"""
  },
  {
    "id": "ss-c3-03",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "傅里叶对偶性变换",
    "type": "single",
    "difficulty": 3,
    "tags": ["2024年837真题", "对偶性质", "双边指数"],
    "source": "广东工业大学2024年837全国统考真题第5题",
    "stem": "信号 $f(t) = \frac{1}{t^2 + 1}$ 的傅里叶变换 $F(j\omega)$ 为：",
    "options": [
      { "key": "A", "text": "$\pi e^{-|\omega|}$" },
      { "key": "B", "text": "$2\pi e^{-|\omega|}$" },
      { "key": "C", "text": "$\frac{1}{2}\pi e^{-|\omega|}$" },
      { "key": "D", "text": "$e^{-|\omega|}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：傅里叶变换的对称性质（对偶性 Duality Property）。

1. 熟知基本双边实指数信号的傅里叶变换对：
   $$e^{-a |t|} \stackrel{\mathcal{F}}{\longleftrightarrow} \frac{2a}{\omega^2 + a^2}$$
   当 $a = 1$ 时：
   $$e^{-|t|} \stackrel{\mathcal{F}}{\longleftrightarrow} \frac{2}{\omega^2 + 1}$$
2. 根据傅里叶变换的对偶性原理：若 $f(t) \leftrightarrow F(\omega)$，则 $F(t) \leftrightarrow 2\pi f(-\omega)$：
   $$\frac{2}{t^2 + 1} \stackrel{\mathcal{F}}{\longleftrightarrow} 2\pi e^{-|-\omega|} = 2\pi e^{-|\omega|}$$
3. 两边同除以 2 得到：
   $$\frac{1}{t^2 + 1} \stackrel{\mathcal{F}}{\longleftrightarrow} \pi e^{-|\omega|}$$
故正确答案为 **A**。"""
  },
  {
    "id": "ss-c3-04",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "稳态正弦响应幅频相频",
    "type": "single",
    "difficulty": 2,
    "tags": ["2024年837真题", "频率响应", "幅相特性"],
    "source": "广东工业大学2024年837全国统考真题第7题",
    "stem": "已知某稳定连续 LTI 系统的频率响应为 $H(j\omega) = \frac{1}{1 + j\omega}$，当输入激励为 $f(t) = \cos(t)$ 时，系统的稳态响应 $y_{ss}(t)$ 为：",
    "options": [
      { "key": "A", "text": "$\frac{1}{\sqrt{2}}\cos\left(t - \frac{\pi}{4}\right)$" },
      { "key": "B", "text": "$\frac{1}{\sqrt{2}}\cos\left(t + \frac{\pi}{4}\right)$" },
      { "key": "C", "text": "$\cos\left(t - \frac{\pi}{4}\right)$" },
      { "key": "D", "text": "$\frac{1}{2}\cos(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：稳定 LTI 系统的稳态正弦响应计算。

1. 输入信号频率为 $\omega_0 = 1\text{ rad/s}$；
2. 计算系统在 $\omega_0 = 1$ 处的频率响应复数值：
   $$H(j 1) = \frac{1}{1 + j 1} = \frac{1}{\sqrt{2}}e^{-j \frac{\pi}{4}}$$
   - 幅度增益：$|H(j 1)| = \frac{1}{\sqrt{1^2 + 1^2}} = \frac{1}{\sqrt{2}}$；
   - 相位滞后：$\theta(1) = -\arctan(1) = -\frac{\pi}{4}$；
3. 稳态输出响应为：
   $$y_{ss}(t) = |H(j 1)| \cos(t + \theta(1)) = \frac{1}{\sqrt{2}}\cos\left(t - \frac{\pi}{4}\right)$$
故选 **A**。"""
  },
  {
    "id": "ss-c3-05",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "无失真传输充要条件",
    "type": "single",
    "difficulty": 2,
    "tags": ["2024年837真题", "无失真传输", "群延时"],
    "source": "广东工业大学2024年837全国统考真题第8题",
    "stem": "一个连续 LTI 系统若要实现信号的无失真传输（Distortionless Transmission），其系统频率响应 $H(j\omega)$ 必须满足的条件是：",
    "options": [
      { "key": "A", "text": "$|H(j\omega)| = K$（常数），且 $\theta(\omega) = -\omega t_d$（线性相位）" },
      { "key": "B", "text": "$|H(j\omega)| = K\omega$，且 $\theta(\omega) = 0$" },
      { "key": "C", "text": "$|H(j\omega)| = 1$，且 $\theta(\omega) = -\omega^2 t_d$" },
      { "key": "D", "text": "$H(j\omega) = \delta(\omega - \omega_0)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：无失真传输系统的时域波形与频域幅相要求。

1. **时域定义**：输出响应波形仅允许发生幅度比例缩放 $K$ 和恒定时延 $t_d$，波形形状严格不变：
   $$y(t) = K f(t - t_d)$$
2. **频域推导**：对时域关系进行傅里叶变换：
   $$Y(j\omega) = K e^{-j\omega t_d} F(j\omega) \implies H(j\omega) = \frac{Y(j\omega)}{F(j\omega)} = K e^{-j\omega t_d}$$
3. **两个核心条件**：
   - **幅频特性恒定**：$|H(j\omega)| = K$（避免各频率分量增益不一导致的幅度失真）；
   - **相频特性线性**：$\theta(\omega) = -\omega t_d$（群时延 $\tau_g(\omega) = -\frac{d\theta}{d\omega} = t_d$ 为常数，避免各频率到达时间不一导致的相位失真）。
故选 **A**。"""
  },
  {
    "id": "ss-c3-06",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "傅里叶变换对称性",
    "type": "single",
    "difficulty": 2,
    "tags": ["经典概念", "实偶信号", "频域特性"],
    "source": "广东工业大学837核心题库与绝杀32专题",
    "stem": "若连续时间信号 $f(t)$ 为实偶信号（即 $f^*(t) = f(t)$ 且 $f(-t) = f(t)$），则其傅里叶变换 $F(j\omega)$ 必定是：",
    "options": [
      { "key": "A", "text": "实偶函数" },
      { "key": "B", "text": "虚奇函数" },
      { "key": "C", "text": "实奇函数" },
      { "key": "D", "text": "虚偶函数" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：傅里叶变换的时域奇偶性与频域对称性对应表。

1. 连续傅里叶变换定义：$F(j\omega) = \int_{-\infty}^\infty f(t) e^{-j\omega t} dt = \int_{-\infty}^\infty f(t)[\cos(\omega t) - j\sin(\omega t)] dt$；
2. 当 $f(t)$ 为实偶函数时：
   - $f(t)\cos(\omega t)$ 为偶函数，积分结果为实数且为 $\omega$ 的偶函数；
   - $f(t)\sin(\omega t)$ 为奇函数，在对称区间 $[-\infty, +\infty]$ 上积分为零；
3. 因此虚部完全为 0，$F(j\omega)$ 为纯**实偶函数**。
口诀记忆：
- 实偶对实偶
- 实奇对虚奇
选 **A**。"""
  },
  {
    "id": "ss-c3-07",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "符号函数傅里叶变换",
    "type": "single",
    "difficulty": 2,
    "tags": ["高频变换对", "符号函数", "奇异信号"],
    "source": "广东工业大学837/809真题高频题",
    "stem": "符号函数 $f(t) = \text{sgn}(t)$ 的傅里叶变换 $F(j\omega)$ 为：",
    "options": [
      { "key": "A", "text": "$\frac{2}{j\omega}$" },
      { "key": "B", "text": "$\frac{1}{j\omega}$" },
      { "key": "C", "text": "$\pi\delta(\omega) + \frac{1}{j\omega}$" },
      { "key": "D", "text": "$-\frac{2}{j\omega}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：符号函数 $\text{sgn}(t)$ 的标准傅里叶变换对。

1. 符号函数定义：
   $$\text{sgn}(t) = \begin{cases} 1, & t > 0 \\ -1, & t < 0 \end{cases} = \lim_{\alpha \to 0} [e^{-\alpha t}\varepsilon(t) - e^{\alpha t}\varepsilon(-t)]$$
2. 利用频域极限变换：
   $$F(j\omega) = \lim_{\alpha \to 0} \left( \frac{1}{\alpha + j\omega} - \frac{1}{\alpha - j\omega} \right) = \lim_{\alpha \to 0} \frac{-2j\omega}{\alpha^2 + \omega^2} = \frac{2}{j\omega}$$
3. 符号函数是实奇信号，其频谱为纯虚奇函数，完全吻合 $\frac{2}{j\omega} = -j \frac{2}{\omega}$。
故选 **A**。"""
  },
  {
    "id": "ss-c3-08",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "单位阶跃傅里叶变换",
    "type": "single",
    "difficulty": 2,
    "tags": ["考研必考", "阶跃函数", "直流分量"],
    "source": "广东工业大学837/809经典考题",
    "stem": "单位阶跃信号 $\varepsilon(t)$ 的傅里叶变换为：",
    "options": [
      { "key": "A", "text": "$\pi\delta(\omega) + \frac{1}{j\omega}$" },
      { "key": "B", "text": "$\frac{1}{j\omega}$" },
      { "key": "C", "text": "$2\pi\delta(\omega) + \frac{1}{j\omega}$" },
      { "key": "D", "text": "$\frac{1}{s}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：单位阶跃函数的奇偶分解法求傅里叶变换。

1. 将单位阶跃分解为直流直流直流分量与奇信号（符号函数）之和：
   $$\varepsilon(t) = \frac{1}{2} + \frac{1}{2}\text{sgn}(t)$$
2. 逐项应用常用傅里叶变换对：
   - 直流常数信号：$\frac{1}{2} \leftrightarrow \frac{1}{2} \times 2\pi \delta(\omega) = \pi \delta(\omega)$
   - 符号函数：$\frac{1}{2}\text{sgn}(t) \leftrightarrow \frac{1}{2} \times \frac{2}{j\omega} = \frac{1}{j\omega}$
3. 叠加得到：
   $$\varepsilon(t) \stackrel{\mathcal{F}}{\longleftrightarrow} \pi\delta(\omega) + \frac{1}{j\omega}$$
选 **A**。"""
  },
  {
    "id": "ss-c3-09",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "正弦平方信号傅里叶变换",
    "type": "single",
    "difficulty": 3,
    "tags": ["2025年809真题", "降幂公式", "频移冲激"],
    "source": "广东工业大学2025年809全国统考真题第8题",
    "stem": "计算正弦平方信号 $f(t) = \sin^2(t)$ 的傅里叶变换 $F(j\omega)$ 为：",
    "options": [
      { "key": "A", "text": "$\pi\delta(\omega) - \frac{\pi}{2}[\delta(\omega - 2) + \delta(\omega + 2)]$" },
      { "key": "B", "text": "$\pi\delta(\omega) + \frac{\pi}{2}[\delta(\omega - 2) + \delta(\omega + 2)]$" },
      { "key": "C", "text": "$2\pi\delta(\omega) - \pi\delta(\omega - 2)$" },
      { "key": "D", "text": "$\frac{\pi}{2}[\delta(\omega - 1) + \delta(\omega + 1)]$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：三角恒等变换与余弦信号的傅里叶变换对。

1. 利用三角降幂公式将平方展开：
   $$\sin^2(t) = \frac{1 - \cos(2t)}{2} = \frac{1}{2} - \frac{1}{2}\cos(2t)$$
2. 分别求两项的傅里叶变换：
   - 直流常数项：$\frac{1}{2} \leftrightarrow \frac{1}{2} \times 2\pi \delta(\omega) = \pi \delta(\omega)$；
   - 余弦交流项：$\cos(2t) \leftrightarrow \pi[\delta(\omega - 2) + \delta(\omega + 2)]$，带入系数 $-\frac{1}{2}$；
3. 合并得：
   $$F(j\omega) = \pi\delta(\omega) - \frac{\pi}{2}[\delta(\omega - 2) + \delta(\omega + 2)]$$
故选 **A**。"""
  },
  {
    "id": "ss-c3-10",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "频域符号逆变换",
    "type": "single",
    "difficulty": 3,
    "tags": ["2025年809真题", "对偶变换", "符号谱"],
    "source": "广东工业大学2025年809全国统考真题第9题",
    "stem": "已知频谱函数 $F(\omega) = \text{sgn}(\omega)$，则其对应的原时域信号 $f(t)$ 为：",
    "options": [
      { "key": "A", "text": "$\frac{j}{\pi t}$" },
      { "key": "B", "text": "$-\frac{j}{\pi t}$" },
      { "key": "C", "text": "$\frac{1}{\pi t}$" },
      { "key": "D", "text": "$\frac{2}{j t}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：傅里叶变换对偶性质对奇异信号的运用。

1. 熟知基础变换对：
   $$\text{sgn}(t) \stackrel{\mathcal{F}}{\longleftrightarrow} \frac{2}{j\omega} = -j \frac{2}{\omega}$$
2. 由对偶性质：若 $x(t) \leftrightarrow X(\omega)$，则 $X(t) \leftrightarrow 2\pi x(-\omega)$：
   $$-j \frac{2}{t} \stackrel{\mathcal{F}}{\longleftrightarrow} 2\pi \text{sgn}(-\omega) = -2\pi \text{sgn}(\omega)$$
3. 两边同乘以 $-\frac{1}{2\pi}$：
   $$\text{sgn}(\omega) \stackrel{\mathcal{F}^{-1}}{\longleftrightarrow} \left(-\frac{1}{2\pi}\right) \left(-j \frac{2}{t}\right) = \frac{j}{\pi t}$$
故逆变换结果为 **A**。"""
  },
  {
    "id": "ss-c3-11",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "双频连续系统稳态响应",
    "type": "single",
    "difficulty": 3,
    "tags": ["2025年809真题", "稳态响应", "频响增益"],
    "source": "广东工业大学2025年809全国统考真题第10题",
    "stem": "连续系统频响为 $H(j\omega) = \frac{1}{1 + j\omega}$，当输入为 $f(t) = \sin(2t)$ 时，其稳态响应 $y_{ss}(t)$ 为：",
    "options": [
      { "key": "A", "text": "$\frac{1}{\sqrt{5}}\sin(2t - \arctan 2)$" },
      { "key": "B", "text": "$\frac{1}{\sqrt{5}}\sin(2t + \arctan 2)$" },
      { "key": "C", "text": "$\frac{1}{3}\sin(2t)$" },
      { "key": "D", "text": "$\frac{1}{\sqrt{5}}\cos(2t - \arctan 2)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：稳态正弦响应的模值与相位角计算。

1. 正弦激励信号角频率 $\omega_0 = 2\text{ rad/s}$；
2. 计算系统在 $\omega_0 = 2$ 处的频响：
   $$H(j 2) = \frac{1}{1 + j 2}$$
   - 幅频特性：$|H(j 2)| = \frac{1}{\sqrt{1^2 + 2^2}} = \frac{1}{\sqrt{5}}$；
   - 相频特性：$\theta(2) = -\arctan(2)$；
3. 输出为同频正弦波，幅度乘模长，初相加相位偏移：
   $$y_{ss}(t) = \frac{1}{\sqrt{5}}\sin(2t - \arctan 2)$$
选 **A**。"""
  },
  {
    "id": "ss-c3-12",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "理想带通滤波器滤波输出",
    "type": "single",
    "difficulty": 3,
    "tags": ["2021年837真题", "带通滤波", "频率选择"],
    "source": "广东工业大学2021年837全国统考真题第7题",
    "stem": "某理想带通滤波器的通带频率范围为 $2 \le |\omega| \le 7\text{ rad/s}$，在此区间内增益为 1，其余频率增益为 0。若输入信号为 $f(t) = 2 + 3\cos(3t) - 5\sin(6t - 30^\circ) + 4\sin(13t - 20^\circ)$，则滤波器的稳态输出响应 $y(t)$ 为：",
    "options": [
      { "key": "A", "text": "$3\cos(3t) - 5\sin(6t - 30^\circ)$" },
      { "key": "B", "text": "$2 + 3\cos(3t) - 5\sin(6t - 30^\circ)$" },
      { "key": "C", "text": "$4\sin(13t - 20^\circ)$" },
      { "key": "D", "text": "0" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：频带选择滤波器的各频率分量判别。

1. 逐个分析输入信号各分量的角频率：
   - 直流分量：$2$，对应频率 $\omega = 0 \notin [2, 7]$，被完全滤除（增益为 0）；
   - 第二项：$3\cos(3t)$，对应频率 $\omega = 3 \in [2, 7]$，落在通带内，无衰减通过；
   - 第三项：$-5\sin(6t - 30^\circ)$，对应频率 $\omega = 6 \in [2, 7]$，落在通带内，无衰减通过；
   - 第四项：$4\sin(13t - 20^\circ)$，对应频率 $\omega = 13 \notin [2, 7]$，被完全滤除（增益为 0）；
2. 线性叠加通带内分量：
   $$y(t) = 3\cos(3t) - 5\sin(6t - 30^\circ)$$
选 **A**。"""
  },
  {
    "id": "ss-c3-13",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "频域模长逆变换",
    "type": "single",
    "difficulty": 3,
    "tags": ["2021年837真题", "对偶性质", "二阶导数"],
    "source": "广东工业大学2021年837全国统考真题第6题",
    "stem": "计算频谱函数 $F(\omega) = -\pi |\omega|$ 的傅里叶逆变换 $f(t)$ 为：",
    "options": [
      { "key": "A", "text": "$\frac{1}{t^2}$" },
      { "key": "B", "text": "$-\frac{1}{t^2}$" },
      { "key": "C", "text": "$\frac{1}{t}$" },
      { "key": "D", "text": "$\frac{2}{t^2}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：傅里叶变换的频域微分与时域对偶性质。

1. 已知基础对：$t \text{sgn}(t) = |t|$，其傅里叶变换为：
   $$|t| \stackrel{\mathcal{F}}{\longleftrightarrow} -\frac{2}{\omega^2}$$
2. 根据对偶性：若 $x(t) \leftrightarrow X(\omega)$，则 $X(t) \leftrightarrow 2\pi x(-\omega)$：
   $$-\frac{2}{t^2} \stackrel{\mathcal{F}}{\longleftrightarrow} 2\pi |-\omega| = 2\pi |\omega|$$
3. 两边同除以 $-2$：
   $$\frac{1}{t^2} \stackrel{\mathcal{F}}{\longleftrightarrow} -\pi |\omega|$$
故频谱 $F(\omega) = -\pi |\omega|$ 对应的时域信号为 $\frac{1}{t^2}$。选 **A**。"""
  },
  {
    "id": "ss-c3-14",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "时频测不准原理",
    "type": "single",
    "difficulty": 1,
    "tags": ["2024年809真题", "时宽频宽", "测不准原理"],
    "source": "广东工业大学2024年809全国统考真题第6题",
    "stem": "根据傅里叶变换的尺度变换性质，若一个脉冲信号的时域持续时间（脉冲宽度）越大，则其频带宽度将：",
    "options": [
      { "key": "A", "text": "越小（反比压缩）" },
      { "key": "B", "text": "越大（正比扩展）" },
      { "key": "C", "text": "保持不变" },
      { "key": "D", "text": "与脉冲宽度呈平方正比" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：时频测不准原理（Time-Bandwidth Product）。

1. 傅里叶变换尺度变换性质公式：
   $$f(at) \stackrel{\mathcal{F}}{\longleftrightarrow} \frac{1}{|a|} F\left(\frac{\omega}{a}\right)$$
2. 当时域波形在时间轴上展宽时（$|a| < 1$），频域自变量将被压缩除以 $a$，频带变窄；
3. 时域脉冲持续有效宽度 $\Delta t$ 与频域有效带宽 $\Delta \omega$ 满足乘积下界约束：
   $$\Delta t \cdot \Delta \omega \ge \text{Const}$$
4. 因此脉冲宽度越大，频带宽度必定越小。
选 **A**。"""
  },
  {
    "id": "ss-c3-15",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "奇谐函数傅氏级数性质",
    "type": "single",
    "difficulty": 2,
    "tags": ["经典真题", "奇谐函数", "半波对称"],
    "source": "广东工业大学837/809历年期末及考研真题",
    "stem": "周期为 $T$ 的连续信号满足半波对称关系 $f(t) = -f(t \pm \frac{T}{2})$（奇谐函数），则其傅里叶级数展开式中：",
    "options": [
      { "key": "A", "text": "只包含奇次谐波分量（$n = 1, 3, 5, \dots$），直流与偶次谐波为 0" },
      { "key": "B", "text": "只包含偶次谐波分量（$n = 2, 4, 6, \dots$）" },
      { "key": "C", "text": "只包含正弦项，余弦项全部为 0" },
      { "key": "D", "text": "所有谐波分量系数均不为 0" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：半波对称波形（奇谐函数）的频域级数特征。

1. 半波奇对称数学定义：$f(t) = -f(t - \frac{T}{2})$；
2. 计算其指数形式傅里叶级数系数 $F_n$：
   $$F_n = \frac{1}{T}\int_0^T f(t)e^{-jn\omega_0 t}dt = \frac{1}{T}\left[ \int_0^{T/2} f(t)e^{-jn\omega_0 t}dt + \int_{T/2}^T f(t)e^{-jn\omega_0 t}dt \right]$$
3. 对后半周做换元 $\tau = t - \frac{T}{2}$：
   $$F_n = \frac{1}{T}\int_0^{T/2} f(t)e^{-jn\omega_0 t}[1 - e^{-jn\pi}]dt = \frac{1 - (-1)^n}{T}\int_0^{T/2} f(t)e^{-jn\omega_0 t}dt$$
4. 显然：
   - 当 $n$ 为偶数时（包括 $n = 0$ 直流项），$1 - (-1)^n = 0$，系数恒为 0；
   - 当 $n$ 为奇数时，$1 - (-1)^n = 2$；
故奇谐函数**只含奇次谐波**。选 **A**。"""
  },
  {
    "id": "ss-c3-16",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "帕塞瓦尔能量守恒定理",
    "type": "single",
    "difficulty": 2,
    "tags": ["核心定理", "能量守恒", "帕塞瓦尔"],
    "source": "广东工业大学837核心考点专题",
    "stem": "连续能量信号 $f(t)$ 的傅里叶变换为 $F(j\omega)$，根据帕塞瓦尔定理（Parseval's Theorem），时域总能量与频域能量谱密度的定量关系为：",
    "options": [
      { "key": "A", "text": "$\int_{-\infty}^\infty |f(t)|^2 dt = \frac{1}{2\pi}\int_{-\infty}^\infty |F(j\omega)|^2 d\omega$" },
      { "key": "B", "text": "$\int_{-\infty}^\infty |f(t)|^2 dt = \int_{-\infty}^\infty |F(j\omega)|^2 d\omega$" },
      { "key": "C", "text": "$\int_{-\infty}^\infty |f(t)|^2 dt = 2\pi\int_{-\infty}^\infty |F(j\omega)|^2 d\omega$" },
      { "key": "D", "text": "$\int_{-\infty}^\infty |f(t)|^2 dt = \frac{1}{\pi}\int_{-\infty}^\infty |F(j\omega)|^2 d\omega$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：帕塞瓦尔能量守恒定理标准数学公式。

1. 物理本质：信号在时域的总能量与在频域全频带范围积分的总能量严格守恒；
2. 标准公式：
   $$E = \int_{-\infty}^{+\infty} |f(t)|^2 dt = \frac{1}{2\pi}\int_{-\infty}^{+\infty} |F(j\omega)|^2 d\omega = \int_{-\infty}^{+\infty} |F(j 2\pi f)|^2 df$$
   注意当对角频率 $\omega$ 积分时，公式前必须带系数 $\frac{1}{2\pi}$。
选 **A**。"""
  },
  {
    "id": "ss-c3-17",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "时域正余弦调幅频移",
    "type": "single",
    "difficulty": 2,
    "tags": ["通信原理", "正弦调制", "频谱搬移"],
    "source": "广东工业大学837历年真题",
    "stem": "基带信号 $f(t)$ 的最高截止角频率为 $\omega_m$。经载波调制后得到信号 $y(t) = f(t)\cos(\omega_c t)$（其中 $\omega_c \gg \omega_m$），则已调信号 $y(t)$ 的频谱范围为：",
    "options": [
      { "key": "A", "text": "$[\omega_c - \omega_m, \, \omega_c + \omega_m]$ 与 $[-\omega_c - \omega_m, \, -\omega_c + \omega_m]$" },
      { "key": "B", "text": "$[-\omega_m, \, \omega_m]$" },
      { "key": "C", "text": "$[0, \, \omega_c + \omega_m]$" },
      { "key": "D", "text": "$[2\omega_c - \omega_m, \, 2\omega_c + \omega_m]$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：频移特性与正弦调幅频谱搬移。

1. 傅里叶变换的频移定理：
   $$f(t)e^{\pm j\omega_c t} \stackrel{\mathcal{F}}{\longleftrightarrow} F(j(\omega \mp \omega_c))$$
2. 利用欧拉公式展开载波：
   $$y(t) = f(t) \left[ \frac{e^{j\omega_c t} + e^{-j\omega_c t}}{2} \right] = \frac{1}{2}f(t)e^{j\omega_c t} + \frac{1}{2}f(t)e^{-j\omega_c t}$$
3. 对应的频谱为：
   $$Y(j\omega) = \frac{1}{2}F(j(\omega - \omega_c)) + \frac{1}{2}F(j(\omega + \omega_c))$$
4. 原信号频谱集中在 $[-\omega_m, \omega_m]$，调制后被分别搬移至正负载频 $\pm \omega_c$ 处，正频带范围为 $[\omega_c - \omega_m, \omega_c + \omega_m]$，带宽加倍为 $2\omega_m$。
选 **A**。"""
  },
  {
    "id": "ss-c3-18",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "频域微分性质计算",
    "type": "single",
    "difficulty": 3,
    "tags": ["核心性质", "频域微分", "衰减斜坡"],
    "source": "广东工业大学837核心考点",
    "stem": "信号 $f(t) = t e^{-a t}\varepsilon(t)\, (a > 0)$ 的傅里叶变换 $F(j\omega)$ 为：",
    "options": [
      { "key": "A", "text": "$\frac{1}{(a + j\omega)^2}$" },
      { "key": "B", "text": "$\frac{j\omega}{(a + j\omega)^2}$" },
      { "key": "C", "text": "$\frac{1}{a^2 + \omega^2}$" },
      { "key": "D", "text": "$\frac{a}{(a + j\omega)^2}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：时域乘以自变量 $t$ 对应的频域微分性质。

1. 频域微分性质公式：
   $$t f(t) \stackrel{\mathcal{F}}{\longleftrightarrow} j \frac{d}{d\omega} F(j\omega)$$
2. 基础单边指数变换对：
   $$e^{-a t}\varepsilon(t) \stackrel{\mathcal{F}}{\longleftrightarrow} \frac{1}{a + j\omega}$$
3. 对频域表达式关于 $\omega$ 求导：
   $$\frac{d}{d\omega}\left[ \frac{1}{a + j\omega} \right] = -\frac{j}{(a + j\omega)^2}$$
4. 代入公式乘以虚数单位 $j$：
   $$j \left( -\frac{j}{(a + j\omega)^2} \right) = -j^2 \frac{1}{(a + j\omega)^2} = \frac{1}{(a + j\omega)^2}$$
故选 **A**。"""
  }
]

all_questions.extend(chapter3_questions)
print(f"Added Chapter 3: {len(chapter3_questions)} questions")

# ==========================================
# 第四章：拉普拉斯变换与复频域分析 (18 题)
# ==========================================
chapter4_questions = [
  {
    "id": "ss-c4-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "假分式部分分式展开",
    "type": "single",
    "difficulty": 3,
    "tags": ["经典题型", "拉氏反变换", "假分式"],
    "source": "广东工业大学837核心考点专题",
    "stem": "计算假分式象函数 $F(s) = \frac{s^2 + 4s + 5}{s^2 + 3s + 2}$（收敛域 $\text{Re}(s) > -1$）的拉普拉斯逆变换 $f(t)$：",
    "options": [
      { "key": "A", "text": "$\delta(t) + (2e^{-t} - e^{-2t})\varepsilon(t)$" },
      { "key": "B", "text": "$\delta(t) + (e^{-t} - 2e^{-2t})\varepsilon(t)$" },
      { "key": "C", "text": "$(2e^{-t} - e^{-2t})\varepsilon(t)$" },
      { "key": "D", "text": "$\delta(t) + (2e^{-t} + e^{-2t})\varepsilon(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：分子与分母同阶的假分式部分分式展开法。

1. **分离多项式多项式整式**：
   分子除以分母分离商数 1：
   $$F(s) = \frac{(s^2 + 3s + 2) + (s + 3)}{s^2 + 3s + 2} = 1 + \frac{s + 3}{(s + 1)(s + 2)}$$
2. **真分式留数法展开**：
   设 $\frac{s + 3}{(s + 1)(s + 2)} = \frac{A}{s + 1} + \frac{B}{s + 2}$：
   - $A = \left[ \frac{s + 3}{s + 2} \right]_{s = -1} = \frac{-1 + 3}{-1 + 2} = 2$；
   - $B = \left[ \frac{s + 3}{s + 1} \right]_{s = -2} = \frac{-2 + 3}{-2 + 1} = -1$；
   因此：
   $$F(s) = 1 + \frac{2}{s + 1} - \frac{1}{s + 2}$$
3. **查常用拉普拉斯逆变换对**（收敛域为最右极点右侧因果信号）：
   - $1 \stackrel{\mathcal{L}^{-1}}{\longleftrightarrow} \delta(t)$；
   - $\frac{1}{s + 1} \stackrel{\mathcal{L}^{-1}}{\longleftrightarrow} e^{-t}\varepsilon(t)$；
   - $\frac{1}{s + 2} \stackrel{\mathcal{L}^{-1}}{\longleftrightarrow} e^{-2t}\varepsilon(t)$；
4. 综合得到：
   $$f(t) = \delta(t) + (2e^{-t} - e^{-2t})\varepsilon(t)$$
选 **A**。"""
  },
  {
    "id": "ss-c4-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "连续全通系统判别",
    "type": "single",
    "difficulty": 2,
    "tags": ["全通系统", "幅频特性", "零极点对称"],
    "source": "广东工业大学837经典考题",
    "stem": "某稳定连续因果系统的系统函数为 $H(s) = \frac{s - 2}{s + 2}$，则该系统属于：",
    "options": [
      { "key": "A", "text": "全通系统（All-pass System）" },
      { "key": "B", "text": "低通系统" },
      { "key": "C", "text": "高通系统" },
      { "key": "D", "text": "带阻系统" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：一阶连续全通滤波器的零极点镜像对称性与幅频特性。

1. **零极点分布**：
   - 极点：$s_p = -2$（位于左半平面，系统因果稳定）；
   - 零点：$s_z = +2$（位于右半平面）；
   - 零点与极点关于虚轴呈镜像对称分布：$s_z = -s_p^*$。
2. **频响幅值计算**：令 $s = j\omega$：
   $$|H(j\omega)| = \left| \frac{j\omega - 2}{j\omega + 2} \right| = \frac{\sqrt{\omega^2 + (-2)^2}}{\sqrt{\omega^2 + 2^2}} = \frac{\sqrt{\omega^2 + 4}}{\sqrt{\omega^2 + 4}} = 1$$
3. 在全部频率 $-\infty < \omega < +\infty$ 上，幅频增益恒等于常数 1，仅对相位产生色散滞后；
4. 因此该系统为标准的**全通系统**。
选 **A**。"""
  },
  {
    "id": "ss-c4-03",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "共轭复根配方法逆变换",
    "type": "single",
    "difficulty": 3,
    "tags": ["拉氏反变换", "配方法", "阻尼振荡"],
    "source": "广东工业大学837/809核心考点",
    "stem": "已知象函数 $F(s) = \frac{s + 1}{s^2 + 2s + 10}$（收敛域 $\text{Re}(s) > -1$），其对应的时域原函数 $f(t)$ 为：",
    "options": [
      { "key": "A", "text": "$e^{-t}\cos(3t)\varepsilon(t)$" },
      { "key": "B", "text": "$e^{-t}\sin(3t)\varepsilon(t)$" },
      { "key": "C", "text": "$\cos(3t)\varepsilon(t)$" },
      { "key": "D", "text": "$e^{-2t}\cos(3t)\varepsilon(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：分母含共轭复极点的拉普拉斯配方逆变换。

1. **分母配平方**：
   $$s^2 + 2s + 10 = (s + 1)^2 + 9 = (s + 1)^2 + 3^2$$
2. **分子配凑对应项**：
   分子本身恰好为 $s + 1$：
   $$F(s) = \frac{s + 1}{(s + 1)^2 + 3^2}$$
3. **查经典衰减余弦变换对**：
   $$e^{-a t}\cos(\omega_0 t)\varepsilon(t) \stackrel{\mathcal{L}}{\longleftrightarrow} \frac{s + a}{(s + a)^2 + \omega_0^2}$$
4. 对比参数可知：$a = 1, \, \omega_0 = 3$：
   $$f(t) = e^{-t}\cos(3t)\varepsilon(t)$$
选 **A**。"""
  },
  {
    "id": "ss-c4-04",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "拉氏变换初值定理与终值定理",
    "type": "single",
    "difficulty": 2,
    "tags": ["初值定理", "终值定理", "极点判定"],
    "source": "广东工业大学837/809经典题型",
    "stem": "已知象函数 $F(s) = \frac{2s + 3}{s^2 + 5s + 6}$（$\text{Re}(s) > -2$），则其时域初值 $f(0_+)$ 与终值 $f(\infty)$ 分别为：",
    "options": [
      { "key": "A", "text": "$f(0_+) = 2, \, f(\infty) = 0$" },
      { "key": "B", "text": "$f(0_+) = 0, \, f(\infty) = 2$" },
      { "key": "C", "text": "$f(0_+) = 2, \, f(\infty) = 0.5$" },
      { "key": "D", "text": "$f(0_+) = 3, \, f(\infty) = 0$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：单边拉普拉斯变换的初值定理与终值定理。

1. **初值定理计算**：
   $$f(0_+) = \lim_{s \to \infty} s F(s) = \lim_{s \to \infty} \frac{s(2s + 3)}{s^2 + 5s + 6} = \lim_{s \to \infty} \frac{2s^2 + 3s}{s^2 + 5s + 6} = 2$$
2. **终值定理计算**：
   - 检验极点：分母 $s^2 + 5s + 6 = (s + 2)(s + 3) = 0 \implies s_1 = -2, s_2 = -3$；
   - 两个极点均严格位于左半开平面，信号时域必渐近收敛，满足终值定理适用条件；
   $$f(\infty) = \lim_{s \to 0} s F(s) = \lim_{s \to 0} \frac{s(2s + 3)}{s^2 + 5s + 6} = \frac{0 \times 3}{6} = 0$$
故选 **A**。"""
  },
  {
    "id": "ss-c4-05",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "因果稳定性收敛域判别",
    "type": "single",
    "difficulty": 3,
    "tags": ["系统函数", "收敛域ROC", "因果稳定性"],
    "source": "广东工业大学2021年837真题计算大题考点",
    "stem": "某 LTI 系统的系统函数为 $H(s) = \frac{s + 3}{(s + 1)(s + 2)}$。若已知该系统既是因果系统又是稳定系统，则其拉普拉斯收敛域（ROC）必须是：",
    "options": [
      { "key": "A", "text": "$\text{Re}(s) > -1$" },
      { "key": "B", "text": "$-2 < \text{Re}(s) < -1$" },
      { "key": "C", "text": "$\text{Re}(s) < -2$" },
      { "key": "D", "text": "整个复 $s$ 平面" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：连续系统因果性与 BIBO 稳定性对收敛域 ROC 的双重要求。

1. **极点位置**：系统极点为 $s_1 = -1$ 和 $s_2 = -2$；
2. **因果性要求**：因果系统的冲激响应为右边信号，其收敛域必须位于**最右边极点的右侧右半平面**：
   $$\text{ROC}: \text{Re}(s) > \max(-1, -2) = -1$$
3. **稳定性要求**：BIBO 稳定系统的充要条件是冲激响应绝对可积，对应收敛域**必须包含虚轴 $j\omega$（即包含 $\text{Re}(s) = 0$）**；
4. 当 $\text{ROC}: \text{Re}(s) > -1$ 时，原点及虚轴 $\text{Re}(s) = 0 > -1$ 包含在收敛域内，因此同时满足因果性与稳定性！
故选 **A**。"""
  },
  {
    "id": "ss-c4-06",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "时移阶跃拉普拉斯变换",
    "type": "single",
    "difficulty": 2,
    "tags": ["2022年837真题", "拉氏变换", "时移性质"],
    "source": "广东工业大学2022年837全国统考真题第9题",
    "stem": "计算时域信号 $f(t) = t \varepsilon(t - 1)$ 的单边拉普拉斯变换 $F(s)$ 为：",
    "options": [
      { "key": "A", "text": "$\frac{s + 1}{s^2}e^{-s}$" },
      { "key": "B", "text": "$\frac{1}{s^2}e^{-s}$" },
      { "key": "C", "text": "$\frac{s - 1}{s^2}e^{-s}$" },
      { "key": "D", "text": "$\frac{1}{s}e^{-s}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：自变量时移与阶跃函数的拉氏变换处理。

1. **配凑时移变量 $t - 1$**：
   $$f(t) = t \varepsilon(t - 1) = (t - 1 + 1)\varepsilon(t - 1) = (t - 1)\varepsilon(t - 1) + \varepsilon(t - 1)$$
2. **分别查经典变换对并应用时移性质**：
   - 斜坡项：$t \varepsilon(t) \leftrightarrow \frac{1}{s^2} \implies (t - 1)\varepsilon(t - 1) \leftrightarrow \frac{1}{s^2}e^{-s}$；
   - 阶跃项：$\varepsilon(t) \leftrightarrow \frac{1}{s} \implies \varepsilon(t - 1) \leftrightarrow \frac{1}{s}e^{-s}$；
3. **通分合并**：
   $$F(s) = \left( \frac{1}{s^2} + \frac{1}{s} \right) e^{-s} = \frac{s + 1}{s^2}e^{-s}$$
故选 **A**。"""
  },
  {
    "id": "ss-c4-07",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "衰减正弦单边拉氏变换",
    "type": "single",
    "difficulty": 2,
    "tags": ["2024年809真题", "拉氏变换", "衰减正弦"],
    "source": "广东工业大学2024年809全国统考真题第7题",
    "stem": "信号 $f(t) = e^{-a t}\sin(\omega_0 t)\varepsilon(t)$ 的单边拉普拉斯变换 $F(s)$ 及其收敛域为：",
    "options": [
      { "key": "A", "text": "$\frac{\omega_0}{(s + a)^2 + \omega_0^2}, \quad \text{Re}(s) > -a$" },
      { "key": "B", "text": "$\frac{s + a}{(s + a)^2 + \omega_0^2}, \quad \text{Re}(s) > -a$" },
      { "key": "C", "text": "$\frac{\omega_0}{s^2 + \omega_0^2}, \quad \text{Re}(s) > 0$" },
      { "key": "D", "text": "$\frac{1}{(s + a)^2 + \omega_0^2}, \quad \text{Re}(s) > a$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：单边拉普拉斯变换频移定理与正弦变换对。

1. 基本正弦信号的单边拉普拉斯变换：
   $$\sin(\omega_0 t)\varepsilon(t) \stackrel{\mathcal{L}}{\longleftrightarrow} \frac{\omega_0}{s^2 + \omega_0^2}, \quad \text{Re}(s) > 0$$
2. 根据复频移性质 $e^{-a t} f(t) \leftrightarrow F(s + a)$：
   将 $s$ 整体替换为 $s + a$：
   $$F(s) = \frac{\omega_0}{(s + a)^2 + \omega_0^2}$$
3. 收敛域平移：$\text{Re}(s + a) > 0 \implies \text{Re}(s) > -a$。
故选 **A**。"""
  },
  {
    "id": "ss-c4-08",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "初值与终值综合计算",
    "type": "single",
    "difficulty": 2,
    "tags": ["2024年809真题", "初值定理", "终值定理"],
    "source": "广东工业大学2024年809全国统考真题第4题",
    "stem": "已知某系统的系统函数为 $H(s) = \frac{10(s + 2)}{s(s + 5)}$，其单位冲激响应 $h(t)$ 的初值 $h(0_+)$ 与终值 $h(\infty)$ 分别为：",
    "options": [
      { "key": "A", "text": "$h(0_+) = 10, \, h(\infty) = 4$" },
      { "key": "B", "text": "$h(0_+) = 4, \, h(\infty) = 10$" },
      { "key": "C", "text": "$h(0_+) = 10, \, h(\infty) = 0$" },
      { "key": "D", "text": "$h(0_+) = 0, \, h(\infty) = 4$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：初值定理与终值定理在系统响应中的标准求解。

1. **计算初值 $h(0_+)$**：
   $$h(0_+) = \lim_{s \to \infty} s H(s) = \lim_{s \to \infty} s \cdot \frac{10(s + 2)}{s(s + 5)} = \lim_{s \to \infty} \frac{10(s + 2)}{s + 5} = 10$$
2. **计算终值 $h(\infty)$**：
   - 极点分析：$s(s + 5) = 0 \implies s_1 = 0, \, s_2 = -5$；极点除原点单极点外均在左半平面，满足终值定理适用条件；
   $$h(\infty) = \lim_{s \to 0} s H(s) = \lim_{s \to 0} s \cdot \frac{10(s + 2)}{s(s + 5)} = \lim_{s \to 0} \frac{10(s + 2)}{s + 5} = \frac{10 \times 2}{5} = 4$$
故初值为 10，终值为 4。选 **A**。"""
  },
  {
    "id": "ss-c4-09",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "稳定性与零极点关系辨析",
    "type": "judgment",
    "difficulty": 2,
    "tags": ["2024年809真题", "稳定性", "零极点"],
    "source": "广东工业大学2024年809全国统考真题第10题",
    "stem": "如果一个连续系统是稳定系统，那么它的零点和极点都必须严格位于 $s$ 平面的左半平面。",
    "options": [
      { "key": "A", "text": "正确（True）" },
      { "key": "B", "text": "错误（False）" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：连续因果系统稳定性的充要条件。

1. 因果连续系统稳定的充分必要条件是：**系统函数 $H(s)$ 的所有极点都必须位于左半开平面**（$\text{Re}(p_k) < 0$），收敛域包含虚轴；
2. **零点的位置完全不受限制**：零点可以位于左半平面、虚轴，也可以位于右半平面！
   - 例如全通滤波器 $H(s) = \frac{s - 2}{s + 2}$，其零点为 $s = +2$（位于右半平面），但极点为 $s = -2$（在左半平面），系统完全是 BIBO 稳定的！
   - 零点在右半平面仅说明该系统是“非最小相位系统”，绝不影响其稳定性。
故题干观点错误，选 **B**。"""
  },
  {
    "id": "ss-c4-10",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "时移象函数拉氏逆变换",
    "type": "single",
    "difficulty": 3,
    "tags": ["2025年809真题", "拉氏反变换", "时移性质"],
    "source": "广东工业大学2025年809全国统考真题第11题",
    "stem": "求象函数 $F(s) = \frac{e^{-3s}}{s^2 + 3s + 2}$ 的单边拉普拉斯逆变换 $f(t)$：",
    "options": [
      { "key": "A", "text": "$[e^{-(t - 3)} - e^{-2(t - 3)}]\varepsilon(t - 3)$" },
      { "key": "B", "text": "$(e^{-t} - e^{-2t})\varepsilon(t - 3)$" },
      { "key": "C", "text": "$[e^{-(t - 3)} + e^{-2(t - 3)}]\varepsilon(t - 3)$" },
      { "key": "D", "text": "$[2e^{-(t - 3)} - e^{-2(t - 3)}]\varepsilon(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：部分分式展开与时移性质的结合。

1. 先对不含时延因子的母函数展开：
   $$F_0(s) = \frac{1}{s^2 + 3s + 2} = \frac{1}{(s + 1)(s + 2)} = \frac{1}{s + 1} - \frac{1}{s + 2}$$
2. 求母函数的时域原函数：
   $$f_0(t) = (e^{-t} - e^{-2t})\varepsilon(t)$$
3. 乘以时延因子 $e^{-3s}$ 对应时域整体右移 3 个单位（延时 3）：
   $$f(t) = f_0(t - 3) = [e^{-(t - 3)} - e^{-2(t - 3)}]\varepsilon(t - 3)$$
选 **A**。"""
  },
  {
    "id": "ss-c4-11",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "零输入响应反推系统极点",
    "type": "single",
    "difficulty": 2,
    "tags": ["2025年809真题", "零输入响应", "特征极点"],
    "source": "广东工业大学2025年809全国统考真题第12题",
    "stem": "某连续时间系统的零输入响应为 $y_{zi}(t) = (e^{-t} - 2e^{-2t} + e^{-3t})\varepsilon(t)$，则该系统的极点必定包含：",
    "options": [
      { "key": "A", "text": "$-1, \, -2, \, -3$" },
      { "key": "B", "text": "$1, \, 2, \, 3$" },
      { "key": "C", "text": "$-1, \, -2$" },
      { "key": "D", "text": "$-1, \, 2, \, -3$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：零输入响应的模态形式与系统极点的严格对应。

1. 零输入响应 $y_{zi}(t)$ 是系统在没有外加输入激励的情况下，仅由初始状态所激发的自然响应；
2. 零输入响应的时域基底函数 $e^{\lambda_k t}$ 中的指数项系数 $\lambda_k$，即为系统特征方程的根（也是系统函数的固有极点）；
3. 观察题干表达式中的三项指数分量：
   - $e^{-t} \implies \lambda_1 = -1$；
   - $e^{-2t} \implies \lambda_2 = -2$；
   - $e^{-3t} \implies \lambda_3 = -3$；
4. 因此该系统的特征极点包含 $-1, -2, -3$。
选 **A**。"""
  },
  {
    "id": "ss-c4-12",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "系统函数判断滤波器类型",
    "type": "single",
    "difficulty": 2,
    "tags": ["2025年809真题", "滤波器类型", "极限定理"],
    "source": "广东工业大学2025年809全国统考真题第14题",
    "stem": "已知某连续稳定系统的系统函数为 $H(s) = \frac{s}{s + 3}$，则该滤波器属于：",
    "options": [
      { "key": "A", "text": "高通滤波器（High-pass Filter）" },
      { "key": "B", "text": "低通滤波器（Low-pass Filter）" },
      { "key": "C", "text": "带通滤波器" },
      { "key": "D", "text": "带阻滤波器" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：频率响应在零频与高频极限下的增益特性。

1. 令 $s = j\omega$，系统的频响为：
   $$H(j\omega) = \frac{j\omega}{j\omega + 3}$$
2. 计算直流（零频 $\omega = 0$）处的增益：
   $$|H(j 0)| = \frac{0}{0 + 3} = 0$$
   （低频完全被阻断）；
3. 计算高频（$\omega \to \infty$）处的增益：
   $$\lim_{\omega \to \infty} |H(j\omega)| = \lim_{\omega \to \infty} \frac{\omega}{\sqrt{\omega^2 + 9}} = 1$$
   （高频信号无衰减通过）；
4. 低频截止阻断、高频畅通，这是典型的**高通滤波器**特性。
选 **A**。"""
  },
  {
    "id": "ss-c4-13",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "微分方程全响应复频域求解",
    "type": "single",
    "difficulty": 3,
    "tags": ["2024年809真题", "微分方程", "S域求解"],
    "source": "广东工业大学2024年809全国统考真题大题第3题",
    "stem": "微分方程 $r''(t) + 6r'(t) + 5r(t) = e'(t) + 2e(t)$，初始条件 $r(0_-) = 1, \, r'(0_-) = 0$。则其零输入响应的拉普拉斯变换 $R_{zi}(s)$ 为：",
    "options": [
      { "key": "A", "text": "$\frac{s + 6}{s^2 + 6s + 5}$" },
      { "key": "B", "text": "$\frac{s + 2}{s^2 + 6s + 5}$" },
      { "key": "C", "text": "$\frac{1}{s^2 + 6s + 5}$" },
      { "key": "D", "text": "$\frac{s}{s^2 + 6s + 5}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：单边拉普拉斯变换时域微分定理（含 $0_-$ 状态模型）。

1. 二阶微分的单边拉普拉斯变换时域微分定理：
   $$\mathcal{L}\{r''(t)\} = s^2 R(s) - s r(0_-) - r'(0_-)$$
   $$\mathcal{L}\{r'(t)\} = s R(s) - r(0_-)$$
2. 求解零输入响应时，令外加激励 $e(t) = 0$：
   $$[s^2 R_{zi}(s) - s r(0_-) - r'(0_-)] + 6[s R_{zi}(s) - r(0_-)] + 5 R_{zi}(s) = 0$$
3. 代入初始状态 $r(0_-) = 1, \, r'(0_-) = 0$：
   $$(s^2 + 6s + 5)R_{zi}(s) - s(1) - 0 - 6(1) = 0$$
   $$(s^2 + 6s + 5)R_{zi}(s) = s + 6$$
4. 解得：
   $$R_{zi}(s) = \frac{s + 6}{s^2 + 6s + 5}$$
选 **A**。"""
  },
  {
    "id": "ss-c4-14",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "连续系统冲激响应求解",
    "type": "single",
    "difficulty": 3,
    "tags": ["2024年809真题", "冲激响应", "部分分式"],
    "source": "广东工业大学2024年809全国统考真题大题第3题(2)",
    "stem": "系统函数为 $H(s) = \frac{s + 2}{s^2 + 6s + 5}$（因果系统），则单位冲激响应 $h(t)$ 为：",
    "options": [
      { "key": "A", "text": "$[\frac{1}{4}e^{-t} + \frac{3}{4}e^{-5t}]\varepsilon(t)$" },
      { "key": "B", "text": "$[\frac{3}{4}e^{-t} + \frac{1}{4}e^{-5t}]\varepsilon(t)$" },
      { "key": "C", "text": "$(e^{-t} - e^{-5t})\varepsilon(t)$" },
      { "key": "D", "text": "$[\frac{1}{2}e^{-t} + \frac{1}{2}e^{-5t}]\varepsilon(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：部分分式展开法求因果系统单位冲激响应。

1. 分解分母多项式：
   $$s^2 + 6s + 5 = (s + 1)(s + 5)$$
2. 设部分分式：
   $$H(s) = \frac{s + 2}{(s + 1)(s + 5)} = \frac{A}{s + 1} + \frac{B}{s + 5}$$
3. 计算留数系数：
   - $A = \left[ \frac{s + 2}{s + 5} \right]_{s = -1} = \frac{-1 + 2}{-1 + 5} = \frac{1}{4}$；
   - $B = \left[ \frac{s + 2}{s + 1} \right]_{s = -5} = \frac{-5 + 2}{-5 + 1} = \frac{-3}{-4} = \frac{3}{4}$；
4. 取单边拉普拉斯逆变换：
   $$h(t) = \left( \frac{1}{4}e^{-t} + \frac{3}{4}e^{-5t} \right)\varepsilon(t)$$
故选 **A**。"""
  },
  {
    "id": "ss-c4-15",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "二阶系统微分方程全响应",
    "type": "single",
    "difficulty": 3,
    "tags": ["2025年809真题", "微分方程", "大题考点"],
    "source": "广东工业大学2025年809全国统考真题计算大题第1题",
    "stem": "连续因果 LTI 系统由方程 $y''(t) + 6y'(t) + 5y(t) = f'(t) + 5f(t)$ 描述，其系统函数 $H(s)$ 化简为：",
    "options": [
      { "key": "A", "text": "$\frac{1}{s + 1}$" },
      { "key": "B", "text": "$\frac{s + 5}{(s + 1)(s + 5)}$" },
      { "key": "C", "text": "$\frac{1}{s + 5}$" },
      { "key": "D", "text": "$\frac{s + 1}{s + 5}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：系统函数的零极点相消与一阶退化。

1. 对微分方程两端取拉普拉斯变换（零状态）：
   $$(s^2 + 6s + 5)Y(s) = (s + 5)F(s)$$
2. 得到系统函数：
   $$H(s) = \frac{Y(s)}{F(s)} = \frac{s + 5}{s^2 + 6s + 5} = \frac{s + 5}{(s + 1)(s + 5)}$$
3. 因子相消：零点 $s = -5$ 与极点 $s = -5$ 重合对消：
   $$H(s) = \frac{1}{s + 1}$$
4. 系统退化为一阶因果低通系统，单位冲激响应为 $h(t) = e^{-t}\varepsilon(t)$。
选 **A**。"""
  },
  {
    "id": "ss-c4-16",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "衰减斜坡拉氏变换收敛域",
    "type": "single",
    "difficulty": 2,
    "tags": ["2019年837真题", "拉氏变换", "收敛域"],
    "source": "广东工业大学2019年837全国统考真题第7题",
    "stem": "信号 $f(t) = t e^{-2t}\varepsilon(t)$ 的拉普拉斯变换 $F(s)$ 及其收敛域为：",
    "options": [
      { "key": "A", "text": "$\frac{1}{(s + 2)^2}, \quad \text{Re}(s) > -2$" },
      { "key": "B", "text": "$\frac{1}{(s + 2)^2}, \quad \text{Re}(s) > 2$" },
      { "key": "C", "text": "$\frac{1}{s + 2}, \quad \text{Re}(s) > -2$" },
      { "key": "D", "text": "$\frac{2}{(s + 2)^2}, \quad \text{Re}(s) > -2$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：频域微分性质在拉普拉斯变换中的应用。

1. 基本衰减指数信号变换：
   $$e^{-2t}\varepsilon(t) \stackrel{\mathcal{L}}{\longleftrightarrow} \frac{1}{s + 2}, \quad \text{Re}(s) > -2$$
2. 利用复频域微分性质 $t f(t) \leftrightarrow -\frac{dF(s)}{ds}$：
   $$F(s) = -\frac{d}{ds}\left( \frac{1}{s + 2} \right) = -\left( -\frac{1}{(s + 2)^2} \right) = \frac{1}{(s + 2)^2}$$
3. 因果信号收敛域为极点右侧：$\text{Re}(s) > -2$。
选 **A**。"""
  },
  {
    "id": "ss-c4-17",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "最小相位系统判据",
    "type": "judgment",
    "difficulty": 3,
    "tags": ["最小相位", "因果系统", "高频难点"],
    "source": "广东工业大学837核心考点",
    "stem": "一个因果稳定的连续 LTI 系统，若其逆系统也是因果稳定的，则该系统必定是最小相位系统（Minimum Phase System）。",
    "options": [
      { "key": "A", "text": "正确（True）" },
      { "key": "B", "text": "错误（False）" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：最小相位系统的定义与逆系统因果稳定性。

1. **原系统因果稳定**：$H(s)$ 的所有极点必须严格位于左半平面；
2. **逆系统因果稳定**：逆系统的系统函数为 $H_{inv}(s) = \frac{1}{H(s)}$，其极点正是原系统的**零点**！
   - 逆系统因果稳定要求逆系统的所有极点（即原系统的零点）也必须严格位于左半平面；
3. **最小相位系统定义**：系统的所有极点与所有零点都严格位于复平面的左半开平面；
4. 综合以上两点，原系统与逆系统均因果稳定的充分必要条件就是该系统为**最小相位系统**。
故陈述正确，选 **A**。"""
  },
  {
    "id": "ss-c4-18",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "电路复频域模型求解",
    "type": "single",
    "difficulty": 3,
    "tags": ["电路模型", "S域模型", "储能元件"],
    "source": "广东工业大学837历年真题核心考点",
    "stem": "在复频域 $s$ 域中，初始电压为 $u_C(0_-)$ 的电容元件 $C$，其等效戴维宁（Thevenin）串联模型为：",
    "options": [
      { "key": "A", "text": "容抗阻抗 $\frac{1}{sC}$ 串联电压源 $\frac{u_C(0_-)}{s}$" },
      { "key": "B", "text": "容抗阻抗 $sC$ 串联电压源 $u_C(0_-)$" },
      { "key": "C", "text": "容抗阻抗 $\frac{1}{sC}$ 并联电流源 $C u_C(0_-)$" },
      { "key": "D", "text": "容抗阻抗 $\frac{1}{sC}$ 串联电压源 $C u_C(0_-)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：储能元件的复频域戴维宁与诺顿等效模型。

1. 电容时域伏安方程：$i_C(t) = C \frac{du_C(t)}{dt}$；
2. 积分形式：$u_C(t) = u_C(0_-) + \frac{1}{C}\int_{0_-}^t i_C(\tau)d\tau$；
3. 取单边拉普拉斯变换：
   $$U_C(s) = \frac{u_C(0_-)}{s} + \frac{1}{sC} I_C(s)$$
4. 该式直接对应一个等效阻抗为 $Z_C(s) = \frac{1}{sC}$，与一个大小为 $\frac{u_C(0_-)}{s}$ 的冲激步阶电压源相串联。
选 **A**。"""
  }
]

all_questions.extend(chapter4_questions)
print(f"Added Chapter 4: {len(chapter4_questions)} questions")


# ==========================================
# 第五章：Z变换与离散系统 (18 题)
# ==========================================
chapter5_questions = [
  {
    "id": "ss-c5-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "离散稳定系统收敛域条件",
    "type": "single",
    "difficulty": 2,
    "tags": ["2023年837真题", "离散稳定性", "单位圆ROC"],
    "source": "广东工业大学2023年837全国统考真题第5题",
    "stem": "已知某离散时间 LTI 系统的系统函数为 $H(z) = \frac{z^2 + 2}{z^2 - 1.5z - 1}$。若已知该系统是稳定系统（BIBO Stable），则其收敛域 ROC 必须是：",
    "options": [
      { "key": "A", "text": "$0.5 < |z| < 2$" },
      { "key": "B", "text": "$|z| > 2$" },
      { "key": "C", "text": "$|z| < 0.5$" },
      { "key": "D", "text": "$|z| > 1$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散系统 BIBO 稳定的充要条件与收敛域 ROC 约束。

1. **求系统函数极点**：
   分母多项式因式分解：$z^2 - 1.5z - 1 = (z - 2)(z + 0.5) = 0$；
   极点为 $z_1 = 2$ 和 $z_2 = -0.5$；
2. **极点模长**：$|z_2| = 0.5$，\, $|z_1| = 2$；
3. **稳定性充要条件**：
   离散 LTI 系统稳定的充分必要条件是：**系统收敛域 ROC 必须包含单位圆 $|z| = 1$**；
4. 检验候选的三个同心圆环区域：
   - 区域一：$|z| < 0.5$（不包含 $|z| = 1$）；
   - 区域二：$|z| > 2$（不包含 $|z| = 1$）；
   - 区域三：$0.5 < |z| < 2$（此时 $0.5 < 1 < 2$，严格包含单位圆！）；
因此稳定系统的收敛域必须是环状区域 $0.5 < |z| < 2$（此时系统对应双边非因果序列）。
选 **A**。"""
  },
  {
    "id": "ss-c5-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "离散梳状滤波器结构",
    "type": "single",
    "difficulty": 3,
    "tags": ["2024年837真题", "梳状滤波", "离散频响"],
    "source": "广东工业大学2024年837全国统考真题第10题",
    "stem": "离散梳状滤波器的系统函数为 $H(z) = 1 - z^{-6} = \frac{z^6 - 1}{z^6}$，则该滤波器在区间 $[0, \pi]$ 内幅频响应 $|H(e^{j\Omega})|$ 的零点（陷波点）个数为：",
    "options": [
      { "key": "A", "text": "4 个（含 0 和 $\pi$）" },
      { "key": "B", "text": "3 个" },
      { "key": "C", "text": "6 个" },
      { "key": "D", "text": "2 个" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：梳状滤波器（Comb Filter）的单位圆零点分布与幅频陷波点。

1. **求系统的传输零点**：
   分子多项式令为零：$z^6 - 1 = 0 \implies z_k = e^{j \frac{2\pi k}{6}} = e^{j \frac{k\pi}{3}}, \quad (k = 0, 1, 2, 3, 4, 5)$；
2. 六个零点严格均匀分布在单位圆 $|z| = 1$ 上；
3. **统计区间 $[0, \pi]$ 内的零点**：
   - $k = 0$: $\Omega_0 = 0$
   - $k = 1$: $\Omega_1 = \frac{\pi}{3}$
   - $k = 2$: $\Omega_2 = \frac{2\pi}{3}$
   - $k = 3$: $\Omega_3 = \pi$
4. 在 $[0, \pi]$ 区间内共有 4 个零点，在这些数字角频率上系统的幅频响应严格为 0（陷波），形成周期梳状凹陷。
选 **A**。"""
  },
  {
    "id": "ss-c5-03",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "单边指数序列Z变换",
    "type": "single",
    "difficulty": 2,
    "tags": ["常用变换对", "Z变换", "收敛域"],
    "source": "广东工业大学837/809经典考题",
    "stem": "指数序列 $f(k) = a^k \varepsilon(k)$（其中 $|a| < 1$）的 Z 变换 $F(z)$ 及其收敛域为：",
    "options": [
      { "key": "A", "text": "$\frac{z}{z - a}, \quad |z| > |a|$" },
      { "key": "B", "text": "$\frac{1}{z - a}, \quad |z| > |a|$" },
      { "key": "C", "text": "$\frac{z}{z - a}, \quad |z| < |a|$" },
      { "key": "D", "text": "$\frac{z}{z + a}, \quad |z| > |a|$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：单边因果指数序列的 Z 变换级数求和与收敛域定义。

1. 由单边 Z 变换定义式：
   $$F(z) = \sum_{k=0}^\infty a^k z^{-k} = \sum_{k=0}^\infty (a z^{-1})^k$$
2. 利用等比无穷级数求和公式（当公比 $|a z^{-1}| < 1 \implies |z| > |a|$ 时收敛）：
   $$F(z) = \frac{1}{1 - a z^{-1}} = \frac{z}{z - a}$$
3. 因果序列的收敛域必为最外层极点之外的外圆区域：$|z| > |a|$。
故选 **A**。"""
  },
  {
    "id": "ss-c5-04",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "交替阶跃序列Z变换",
    "type": "single",
    "difficulty": 2,
    "tags": ["经典真题", "交替序列", "单位圆边界"],
    "source": "广东工业大学837基础题库",
    "stem": "交替阶跃序列 $f(k) = (-1)^k \varepsilon(k)$ 的 Z 变换为：",
    "options": [
      { "key": "A", "text": "$\frac{z}{z + 1}, \quad |z| > 1$" },
      { "key": "B", "text": "$\frac{z}{z - 1}, \quad |z| > 1$" },
      { "key": "C", "text": "$\frac{1}{z + 1}, \quad |z| > 1$" },
      { "key": "D", "text": "$\frac{z}{z + 1}, \quad |z| < 1$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：单边指数序列的 $a = -1$ 特例计算。

1. 代入标准公式 $a^k \varepsilon[k] \leftrightarrow \frac{z}{z - a}$；
2. 取 $a = -1$：
   $$F(z) = \frac{z}{z - (-1)} = \frac{z}{z + 1}$$
3. 收敛域为 $|z| > |-1| = 1$。
选 **A**。"""
  },
  {
    "id": "ss-c5-05",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "二阶差分系统因果稳定性判别",
    "type": "single",
    "difficulty": 3,
    "tags": ["2025年809真题", "差分方程", "极点因果稳定"],
    "source": "广东工业大学2025年809全国统考真题大题第2题",
    "stem": "已知某离散因果 LTI 系统的差分方程为 $y(n) - 0.3y(n - 1) - 0.4y(n - 2) = x(n - 1)$，则该系统的系统函数 $H(z)$ 及其因果稳定性为：",
    "options": [
      { "key": "A", "text": "$H(z) = \frac{z}{z^2 - 0.3z - 0.4}$，系统稳定" },
      { "key": "B", "text": "$H(z) = \frac{1}{z^2 - 0.3z - 0.4}$，系统不稳定" },
      { "key": "C", "text": "$H(z) = \frac{z^2}{z^2 - 0.3z - 0.4}$，系统处于临界稳定" },
      { "key": "D", "text": "$H(z) = \frac{z - 1}{z^2 - 0.3z - 0.4}$，系统不稳定" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散系统差分方程的 Z 域转换与单位圆极点判据。

1. **求系统函数 $H(z)$**：
   两边取 Z 变换：
   $$Y(z)(1 - 0.3z^{-1} - 0.4z^{-2}) = X(z)z^{-1}$$
   $$H(z) = \frac{Y(z)}{X(z)} = \frac{z^{-1}}{1 - 0.3z^{-1} - 0.4z^{-2}} = \frac{z}{z^2 - 0.3z - 0.4}$$
2. **求解系统极点**：
   分母因式分解：
   $$z^2 - 0.3z - 0.4 = (z - 0.8)(z + 0.5) = 0$$
   极点为 $z_1 = 0.8, \, z_2 = -0.5$；
3. **稳定性判定**：
   - 极点模长分别为 $|0.8| = 0.8 < 1$，$|-0.5| = 0.5 < 1$；
   - 因果系统所有极点均严格位于单位圆内部（$|z_k| < 1$）；
4. 因此该因果系统是严格的**稳定系统**。
选 **A**。"""
  },
  {
    "id": "ss-c5-06",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "离散斜坡序列Z变换",
    "type": "single",
    "difficulty": 2,
    "tags": ["2024年809真题", "Z域微分", "斜坡序列"],
    "source": "广东工业大学2024年809全国统考真题第12题",
    "stem": "计算离散序列 $x(n) = n a^n u(n)$ 的 Z 变换 $X(z)$ 为：",
    "options": [
      { "key": "A", "text": "$\frac{a z}{(z - a)^2}, \quad |z| > |a|$" },
      { "key": "B", "text": "$\frac{z}{(z - a)^2}, \quad |z| > |a|$" },
      { "key": "C", "text": "$\frac{a z}{z - a}, \quad |z| > |a|$" },
      { "key": "D", "text": "$\frac{a}{(z - a)^2}, \quad |z| > |a|$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：Z 变换的 Z 域微分性质（乘以时域序列序号 $n$）。

1. 基础单边指数序列：
   $$a^n u(n) \stackrel{\mathcal{Z}}{\longleftrightarrow} \frac{z}{z - a} = \frac{1}{1 - a z^{-1}}, \quad |z| > |a|$$
2. 利用 Z 域微分性质：$n x(n) \leftrightarrow -z \frac{d X(z)}{dz}$：
   $$\frac{d}{dz}\left( \frac{z}{z - a} \right) = \frac{(z - a) - z}{(z - a)^2} = -\frac{a}{(z - a)^2}$$
3. 代入性质公式乘以 $-z$：
   $$X(z) = -z \left( -\frac{a}{(z - a)^2} \right) = \frac{a z}{(z - a)^2} = \frac{a z^{-1}}{(1 - a z^{-1})^2}$$
故选 **A**。"""
  },
  {
    "id": "ss-c5-07",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "双边复合序列Z变换收敛域",
    "type": "single",
    "difficulty": 3,
    "tags": ["2025年809真题", "双边序列", "环状ROC"],
    "source": "广东工业大学2025年809全国统考真题第16题",
    "stem": "求序列 $x(n) = 3^n u(-n - 1) + 2^{n+1}u(n)$ 的双边 Z 变换及收敛域 ROC：",
    "options": [
      { "key": "A", "text": "$X(z) = -\frac{z}{z - 3} + \frac{2z}{z - 2}, \quad 2 < |z| < 3$" },
      { "key": "B", "text": "$X(z) = \frac{z}{z - 3} + \frac{2z}{z - 2}, \quad |z| > 3$" },
      { "key": "C", "text": "$X(z) = -\frac{z}{z - 3} + \frac{z}{z - 2}, \quad |z| < 2$" },
      { "key": "D", "text": "收敛域为空集，Z 变换不存在" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：左边反因果序列与右边因果序列叠加的环状收敛域。

1. **第一项（反因果左边序列）**：
   由标准反因果公式 $-a^n u(-n - 1) \leftrightarrow \frac{z}{z - a}, \, |z| < |a|$；
   因此 $3^n u(-n - 1) = -[-3^n u(-n - 1)] \leftrightarrow -\frac{z}{z - 3}$，其收敛域为内圆：$|z| < 3$；
2. **第二项（因果右边序列）**：
   $2^{n+1}u(n) = 2 \cdot [2^n u(n)] \leftrightarrow 2 \cdot \frac{z}{z - 2} = \frac{2z}{z - 2}$，其收敛域为外圆：$|z| > 2$；
3. **求总收敛域交集**：
   $$\text{ROC} = \{|z| < 3\} \cap \{|z| > 2\} = 2 < |z| < 3$$
4. 两圆环相交不为空，因此变换存在，解析式为：
   $$X(z) = -\frac{z}{z - 3} + \frac{2z}{z - 2}, \quad 2 < |z| < 3$$
选 **A**。"""
  },
  {
    "id": "ss-c5-08",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "反因果序列Z变换",
    "type": "single",
    "difficulty": 2,
    "tags": ["2019年837真题", "反因果序列", "左边序列"],
    "source": "广东工业大学2019年837全国统考真题第8题",
    "stem": "计算序列 $x(k) = (-3)^k u(-k - 1)$ 的 Z 变换及其收敛域：",
    "options": [
      { "key": "A", "text": "$-\frac{z}{z + 3}, \quad |z| < 3$" },
      { "key": "B", "text": "$\frac{z}{z + 3}, \quad |z| > 3$" },
      { "key": "C", "text": "$\frac{z}{z - 3}, \quad |z| < 3$" },
      { "key": "D", "text": "$-\frac{z}{z - 3}, \quad |z| > 3$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：反因果左边序列的 Z 变换求解与收敛域判别。

1. 标准反因果左边序列变换公式：
   $$-a^k u(-k - 1) \stackrel{\mathcal{Z}}{\longleftrightarrow} \frac{z}{z - a}, \quad |z| < |a|$$
2. 取 $a = -3$：
   $$-(-3)^k u(-k - 1) \stackrel{\mathcal{Z}}{\longleftrightarrow} \frac{z}{z - (-3)} = \frac{z}{z + 3}, \quad |z| < |-3| = 3$$
3. 两端同乘以 $-1$：
   $$(-3)^k u(-k - 1) \stackrel{\mathcal{Z}}{\longleftrightarrow} -\frac{z}{z + 3}, \quad |z| < 3$$
故选 **A**。"""
  },
  {
    "id": "ss-c5-09",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "单位样值响应与阶跃响应关系",
    "type": "single",
    "difficulty": 1,
    "tags": ["2019年837真题", "差分关系", "离散冲激响应"],
    "source": "广东工业大学2019年837全国统考真题第6题",
    "stem": "离散 LTI 系统的单位样值响应 $h(k)$ 与单位阶跃响应 $g(k)$ 之间的数学关系为：",
    "options": [
      { "key": "A", "text": "$h(k) = g(k) - g(k - 1)$" },
      { "key": "B", "text": "$h(k) = g(k) + g(k - 1)$" },
      { "key": "C", "text": "$h(k) = \sum_{m=-\infty}^k g(m)$" },
      { "key": "D", "text": "$h(k) = \frac{d g(k)}{dk}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散单位冲激响应与阶跃响应的一阶后向差分关系。

1. 连续系统中冲激响应是阶跃响应的一阶导数：$h(t) = \frac{dg(t)}{dt}$；
2. 离散系统中微分由**一阶后向差分**取代：
   $$\delta(k) = \varepsilon(k) - \varepsilon(k - 1)$$
3. 由 LTI 系统的线性时不变性质：
   $$h(k) = g(k) - g(k - 1)$$
选 **A**。"""
  },
  {
    "id": "ss-c5-10",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "朱利稳定性准则判据",
    "type": "single",
    "difficulty": 3,
    "tags": ["朱利准则", "离散稳定性", "高频大题"],
    "source": "广东工业大学837/809历年真题及绝杀32专题26",
    "stem": "二阶因果离散系统的特征多项式为 $A(z) = z^2 + a_1 z + a_0$。根据朱利稳定性准则（Jury Test），该系统渐近稳定的充分必要条件是：",
    "options": [
      { "key": "A", "text": "$|a_0| < 1$, 且 $A(1) > 0$, 且 $A(-1) > 0$" },
      { "key": "B", "text": "$|a_0| > 1$, 且 $a_1 > 0$" },
      { "key": "C", "text": "$a_1^2 - 4a_0 > 0$" },
      { "key": "D", "text": "$A(1) > 0$, 且 $A(-1) < 0$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：二阶离散系统朱利准则判据的三大不等式。

1. 二阶离散多项式 $A(z) = z^2 + a_1 z + a_0$ 的特征根均位于单位圆内的充要条件为：
   - 边界条件 1：$|a_0| < 1$（常数项模长小于首项系数 1）；
   - 边界条件 2：$A(1) = 1 + a_1 + a_0 > 0$（在 $z = 1$ 点的值为正）；
   - 边界条件 3：$A(-1) = 1 - a_1 + a_0 > 0$（在 $z = -1$ 点的值为正）；
2. 这三条不等式构成参数空间内著名的“朱利三角形”，缺一不可。
选 **A**。"""
  },
  {
    "id": "ss-c5-11",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "DTFT周期性特征",
    "type": "single",
    "difficulty": 2,
    "tags": ["DTFT", "离散频谱", "周期性"],
    "source": "广东工业大学837核心考点",
    "stem": "任意离散时间序列 $x(n)$ 的离散时间傅里叶变换（DTFT）$X(e^{j\Omega}) = \sum_{n=-\infty}^\infty x(n)e^{-j\Omega n}$，必定是：",
    "options": [
      { "key": "A", "text": "以 $2\pi$ 为周期的连续周期函数" },
      { "key": "B", "text": "非周期的连续函数" },
      { "key": "C", "text": "以 $\pi$ 为周期的离散函数" },
      { "key": "D", "text": "非周期的离散序列" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散时间傅里叶变换（DTFT）的天然周期性。

1. 考察数字角频率平移 $2\pi$：
   $$X(e^{j(\Omega + 2\pi)}) = \sum_{n=-\infty}^\infty x(n) e^{-j(\Omega + 2\pi)n} = \sum_{n=-\infty}^\infty x(n) e^{-j\Omega n} \cdot e^{-j 2\pi n}$$
2. 因为对于任意整数 $n$，$e^{-j 2\pi n} = \cos(2\pi n) - j\sin(2\pi n) = 1$；
3. 所以恒有：
   $$X(e^{j(\Omega + 2\pi)}) = X(e^{j\Omega})$$
4. 因此 DTFT 的频谱必然是**以 $2\pi$ 为周期的连续频域函数**。
选 **A**。"""
  },
  {
    "id": "ss-c5-12",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "Z变换初值与终值定理",
    "type": "single",
    "difficulty": 2,
    "tags": ["Z变换性质", "初值定理", "极限运算"],
    "source": "广东工业大学837/809经典考题",
    "stem": "因果序列 $f(k)$ 的 Z 变换为 $F(z) = \frac{z^2 + 2z}{z^2 - 1.2z + 0.32}$，则序列初始值 $f(0)$ 为：",
    "options": [
      { "key": "A", "text": "1" },
      { "key": "B", "text": "2" },
      { "key": "C", "text": "0" },
      { "key": "D", "text": "3.2" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：单边 Z 变换初值定理的计算。

1. 单边因果序列初值定理公式：
   $$f(0) = \lim_{z \to \infty} F(z)$$
2. 代入分式求极限：
   $$f(0) = \lim_{z \to \infty} \frac{z^2 + 2z}{z^2 - 1.2z + 0.32} = \lim_{z \to \infty} \frac{1 + \frac{2}{z}}{1 - \frac{1.2}{z} + \frac{0.32}{z^2}} = \frac{1}{1} = 1$$
故选 **A**。"""
  },
  {
    "id": "ss-c5-13",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "离散全通零极点共轭倒数",
    "type": "judgment",
    "difficulty": 3,
    "tags": ["全通系统", "镜像倒数", "单位圆对称"],
    "source": "广东工业大学837历年真题及绝杀32专题20",
    "stem": "离散因果稳定全通系统（All-pass Filter）如果存在一个位于单位圆内的极点 $z_p = r e^{j\theta}\,(r < 1)$，则其对应的传输零点必定位于单位圆外共轭镜像倒数位置 $z_0 = \frac{1}{z_p^*} = \frac{1}{r}e^{j\theta}$ 处。",
    "options": [
      { "key": "A", "text": "正确（True）" },
      { "key": "B", "text": "错误（False）" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散全通系统零极点在单位圆内外的几何倒数对称性。

1. 一阶离散全通滤波器的标准形式为：
   $$H_{ap}(z) = \frac{z^{-1} - z_p^*}{1 - z_p z^{-1}} = \frac{1 - z_p^* z}{z - z_p}$$
2. 求其极点与零点：
   - 极点由分母决定：$z = z_p$（位于单位圆内）；
   - 零点由分子决定：$1 - z_p^* z = 0 \implies z = \frac{1}{z_p^*}$；
3. 若极点为 $r e^{j\theta}$，则零点为 $\frac{1}{r e^{-j\theta}} = \frac{1}{r}e^{j\theta}$，模长为 $\frac{1}{r} > 1$，严格位于单位圆外部的共轭径向射线延长线上；
4. 这种几何对称性保证了在单位圆上矢量长度比值恒为常数，从而保持幅频响应恒等于 1。
故陈述正确，选 **A**。"""
  },
  {
    "id": "ss-c5-14",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "部分分式展开求逆Z变换",
    "type": "single",
    "difficulty": 3,
    "tags": ["逆Z变换", "部分分式", "除z展开法"],
    "source": "广东工业大学837典型计算题",
    "stem": "求象函数 $F(z) = \frac{z}{(z - 1)(z - 2)}$（因果收敛域 $|z| > 2$）的逆 Z 变换 $f(k)$：",
    "options": [
      { "key": "A", "text": "$[2^k - 1]\varepsilon(k)$" },
      { "key": "B", "text": "$[1 - 2^k]\varepsilon(k)$" },
      { "key": "C", "text": "$[2^{k+1} - 1]\varepsilon(k)$" },
      { "key": "D", "text": "$[2^k + 1]\varepsilon(k)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散 Z 变换的“除以 $z$ 部分分式展开法”。

1. 先将两边除以 $z$：
   $$\frac{F(z)}{z} = \frac{1}{(z - 1)(z - 2)} = \frac{A}{z - 1} + \frac{B}{z - 2}$$
2. 留数法求系数：
   - $A = \left[ \frac{1}{z - 2} \right]_{z = 1} = \frac{1}{1 - 2} = -1$；
   - $B = \left[ \frac{1}{z - 1} \right]_{z = 2} = \frac{1}{2 - 1} = 1$；
3. 将 $z$ 乘回分子：
   $$F(z) = -\frac{z}{z - 1} + \frac{z}{z - 2}$$
4. 查标准因果逆变换对：
   - $\frac{z}{z - 1} \leftrightarrow \varepsilon(k)$；
   - $\frac{z}{z - 2} \leftrightarrow 2^k \varepsilon(k)$；
5. 合并得：
   $$f(k) = (2^k - 1)\varepsilon(k)$$
选 **A**。"""
  },
  {
    "id": "ss-c5-15",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "离散系统极点位置与冲激响应波形",
    "type": "single",
    "difficulty": 2,
    "tags": ["极点映射", "时域波形", "振荡衰减"],
    "source": "广东工业大学837概念题",
    "stem": "若离散一阶系统函数只有一个实数极点 $z_p = -0.6$，则该系统的单位样值响应 $h(k)$ 在时域呈现的波形特征是：",
    "options": [
      { "key": "A", "text": "交替正负振荡且幅度指数衰减" },
      { "key": "B", "text": "单调指数衰减，保持正值" },
      { "key": "C", "text": "交替正负振荡且幅度指数发散" },
      { "key": "D", "text": "等幅持续正弦振荡" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散系统极点在实轴负半轴上的时域响应特征。

1. 一阶因果系统冲激响应形式为：
   $$h(k) = (z_p)^k \varepsilon(k) = (-0.6)^k \varepsilon(k)$$
2. 符号变化：由于底数为负数，当 $k$ 取偶数时数值为正，当 $k$ 取奇数时数值为负，表现出**一正一负交替振荡跳变**；
3. 模长变化：由于极点模长 $|z_p| = 0.6 < 1$，包络线按 $(0.6)^k$ 指数衰减趋向于 0；
4. 综合特征为：**正负交替振荡且幅度按指数包络衰减**。
选 **A**。"""
  },
  {
    "id": "ss-c5-16",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "单位圆上极点与临界稳定",
    "type": "judgment",
    "difficulty": 3,
    "tags": ["单位圆极点", "重极点", "发散判据"],
    "source": "广东工业大学837/809稳定性专题",
    "stem": "若离散系统的系统函数在单位圆 $|z| = 1$ 上具有二重或更高重数的极点，则该系统必定是不稳定的（响应随时间发散）。",
    "options": [
      { "key": "A", "text": "正确（True）" },
      { "key": "B", "text": "错误（False）" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：单位圆重极点的时域发散性质。

1. 若在单位圆 $z = 1$ 上有单极点，时域对应阶跃信号 $\varepsilon(k)$（等幅有界，为临界稳定）；
2. 但若在单位圆上有 $m$ 阶（$m \ge 2$）重极点，根据 Z 域微分性质，部分分式逆变换后将激发出自变量正比例项：
   $$\frac{z}{(z - 1)^2} \stackrel{\mathcal{Z}^{-1}}{\longleftrightarrow} k \varepsilon(k)$$
3. 随着时间 $k \to \infty$，项 $k$ 将线性无限增大发散；
4. 因此单位圆上只要存在重极点，系统冲激响应必发散，必定属于**不稳定系统**。
故陈述正确，选 **A**。"""
  },
  {
    "id": "ss-c5-17",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "时域卷积频域乘积性质",
    "type": "single",
    "difficulty": 2,
    "tags": ["Z变换性质", "时域卷积", "基本定理"],
    "source": "广东工业大学837大纲核心知识点",
    "stem": "若序列 $x_1(k)$ 的 Z 变换为 $X_1(z)$（收敛域 $R_1$），$x_2(k)$ 的 Z 变换为 $X_2(z)$（收敛域 $R_2$），则两者的卷积和 $y(k) = x_1(k) * x_2(k)$ 的 Z 变换 $Y(z)$ 为：",
    "options": [
      { "key": "A", "text": "$X_1(z) X_2(z)$，收敛域至少为 $R_1 \cap R_2$" },
      { "key": "B", "text": "$X_1(z) + X_2(z)$，收敛域为 $R_1 \cup R_2$" },
      { "key": "C", "text": "$\frac{1}{2\pi j}\oint X_1(v) X_2(z/v) v^{-1} dv$" },
      { "key": "D", "text": "$X_1(z) * X_2(z)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：时域卷积对应 Z 域代数乘积定理及收敛域交集。

1. 时域卷积定理：
   $$\mathcal{Z}\{x_1(k) * x_2(k)\} = X_1(z) \cdot X_2(z)$$
2. 收敛域规则：两信号乘积的收敛域至少包含各自收敛域的交集（即 $R_1 \cap R_2$），若乘积中存在零极点对消，收敛域还可能进一步扩大。
选 **A**。"""
  },
  {
    "id": "ss-c5-18",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "离散系统的频率响应几何确定法",
    "type": "single",
    "difficulty": 3,
    "tags": ["几何确定法", "幅频响应", "零极点向量"],
    "source": "广东工业大学837/809期末与考研真题",
    "stem": "在复 $z$ 平面上采用几何矢量法确定离散系统在频率 $\Omega$ 处的幅频响应时，若在单位圆上的测试点 $e^{j\Omega}$ 极度靠近系统的某个极点 $z_p$，则该频率处的幅频增益响应将：",
    "options": [
      { "key": "A", "text": "出现尖锐峰值（增益极大）" },
      { "key": "B", "text": "出现深坑下陷（增益衰减为零）" },
      { "key": "C", "text": "保持为 1 不变" },
      { "key": "D", "text": "发生 $180^\circ$ 相位反转且增益不变" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散系统频率响应的零极点几何矢量法。

1. 几何确定法幅频公式：
   $$|H(e^{j\Omega})| = \frac{\prod_{m} |e^{j\Omega} - z_{0m}|}{\prod_{n} |e^{j\Omega} - z_{pn}|} = \frac{\text{各零点矢量的长度之积}}{\text{各极点矢量的长度之积}}$$
2. 当测试点 $e^{j\Omega}$ 沿单位圆逆时针移动到某个靠近单位圆的极点 $z_p$ 附近时，对应的分母极点矢量长度 $|e^{j\Omega} - z_p|$ 变得极小；
3. 分母极小导致整个商数急剧增大，从而在幅频特性曲线上形成尖锐的**增益峰值（共振峰）**。
（反之，若靠近零点则由于分子极小而形成深坑陷波）。
选 **A**。"""
  }
]

all_questions.extend(chapter5_questions)
print(f"Added Chapter 5: {len(chapter5_questions)} questions")

# ==========================================
# 第六章：系统状态变量与信号流图 (10 题)
# ==========================================
chapter6_questions = [
  {
    "id": "ss-c6-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第六章：系统状态变量与信号流图",
    "section": "梅森增益公式",
    "type": "single",
    "difficulty": 2,
    "tags": ["梅森公式", "信号流图", "系统函数"],
    "source": "广东工业大学837/809核心考点",
    "stem": "应用梅森增益公式（Mason Gain Formula）求解系统的传递函数 $H(s) = \frac{1}{\Delta} \sum_{k} P_k \Delta_k$ 中，特征行列式 $\Delta$ 的表达式为：",
    "options": [
      { "key": "A", "text": "$1 - \sum L_i + \sum L_i L_j - \sum L_i L_j L_k + \dots$" },
      { "key": "B", "text": "$1 + \sum L_i + \sum L_i L_j + \dots$" },
      { "key": "C", "text": "$1 - \sum L_i - \sum L_i L_j - \dots$" },
      { "key": "D", "text": "$\sum P_k L_k$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：梅森增益公式特征多项式 $\Delta$ 的标准定义式。

1. 梅森增益公式是求解复杂信号流图或控制框图系统函数的通用法则：
   $$H(s) = \frac{1}{\Delta} \sum_{k} P_k \Delta_k$$
2. 系统特征行列式 $\Delta$ 的定义：
   $$\Delta = 1 - \sum L_i + \sum L_i L_j - \sum L_i L_j L_k + \dots$$
   - $\sum L_i$ 为所有单独回路的回路增益之和；
   - $\sum L_i L_j$ 为两两互不接触回路的增益乘积之和；
   - $\sum L_i L_j L_k$ 为三个互不接触回路增益乘积之和；
   - 正负号交替变换（一负一正）。
选 **A**。"""
  },
  {
    "id": "ss-c6-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第六章：系统状态变量与信号流图",
    "section": "连续状态方程矩阵表达",
    "type": "single",
    "difficulty": 2,
    "tags": ["状态方程", "输出方程", "矩阵形式"],
    "source": "广东工业大学837/809典型真题",
    "stem": "对于连续单输入单输出系统，一阶向量状态方程和代数输出方程的标准形式表示为：",
    "options": [
      { "key": "A", "text": "$\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{b}f(t), \quad y(t) = \mathbf{c}^T \mathbf{x}(t) + d f(t)$" },
      { "key": "B", "text": "$\mathbf{x}(t) = \mathbf{A}\dot{\mathbf{x}}(t) + \mathbf{b}f(t), \quad y(t) = \mathbf{c}^T \mathbf{x}(t)$" },
      { "key": "C", "text": "$\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{b}y(t), \quad f(t) = \mathbf{c}^T \mathbf{x}(t)$" },
      { "key": "D", "text": "$\ddot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{b}f(t), \quad y(t) = \mathbf{c}^T \dot{\mathbf{x}}(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：状态空间表达式（State-space Representation）标准形式。

1. **状态方程**：由一阶常微分方程组组成，描述内部状态变量向量 $\mathbf{x}(t)$ 的时域变化率：
   $$\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{b}f(t)$$
   其中 $\mathbf{A}$ 为 $n \times n$ 系统矩阵，$\mathbf{b}$ 为输入向量；
2. **输出方程**：由代数方程组成，描述系统外部输出 $y(t)$ 与当前状态和当前输入的代数映射：
   $$y(t) = \mathbf{c}^T \mathbf{x}(t) + d f(t)$$
   其中 $\mathbf{c}^T$ 为输出向量，$d$ 为直接传输标量。
选 **A**。"""
  },
  {
    "id": "ss-c6-03",
    "subject": "广工837/809-信号与系统",
    "chapter": "第六章：系统状态变量与信号流图",
    "section": "状态空间求系统函数",
    "type": "single",
    "difficulty": 3,
    "tags": ["状态空间", "系统函数", "矩阵逆"],
    "source": "广东工业大学837核心考点",
    "stem": "由状态空间矩阵 $(\mathbf{A}, \mathbf{b}, \mathbf{c}^T, d)$ 求解连续系统的系统传递函数 $H(s)$ 的闭式公式为：",
    "options": [
      { "key": "A", "text": "$H(s) = \mathbf{c}^T(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{b} + d$" },
      { "key": "B", "text": "$H(s) = \mathbf{c}^T(s\mathbf{I} + \mathbf{A})^{-1}\mathbf{b} + d$" },
      { "key": "C", "text": "$H(s) = (s\mathbf{I} - \mathbf{A})^{-1}\mathbf{b} + d$" },
      { "key": "D", "text": "$H(s) = \mathbf{c}^T \mathbf{A}^{-1}\mathbf{b} + d$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：状态方程复频域求解与系统函数公式推导。

1. 对状态方程取拉普拉斯变换（零状态）：
   $$s \mathbf{X}(s) = \mathbf{A}\mathbf{X}(s) + \mathbf{b}F(s) \implies (s\mathbf{I} - \mathbf{A})\mathbf{X}(s) = \mathbf{b}F(s)$$
2. 求解状态向量：
   $$\mathbf{X}(s) = (s\mathbf{I} - \mathbf{A})^{-1}\mathbf{b}F(s)$$
3. 对输出方程取拉氏变换：
   $$Y(s) = \mathbf{c}^T \mathbf{X}(s) + d F(s) = [\mathbf{c}^T(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{b} + d] F(s)$$
4. 两边除以输入 $F(s)$ 得系统函数：
   $$H(s) = \frac{Y(s)}{F(s)} = \mathbf{c}^T(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{b} + d$$
选 **A**。"""
  },
  {
    "id": "ss-c6-04",
    "subject": "广工837/809-信号与系统",
    "chapter": "第六章：系统状态变量与信号流图",
    "section": "状态变量选取原则",
    "type": "single",
    "difficulty": 2,
    "tags": ["状态变量", "物理电路", "独立储能"],
    "source": "广东工业大学837基础概念",
    "stem": "在集中参数动态电路系统中，选取状态变量的标准物理原则通常是选取：",
    "options": [
      { "key": "A", "text": "各独立电容的电压 $u_C$ 与各独立电感的电流 $i_L$" },
      { "key": "B", "text": "各电阻两端的端电压 $u_R$" },
      { "key": "C", "text": "输入电压源与电流源的大小" },
      { "key": "D", "text": "电路中任意节点的电位" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：电路网络状态变量的物理本质与选取准则。

1. 状态变量必须能够完全表征系统在任意时刻所积蓄的全部物理能量和历史信息；
2. 在电网络中，储能元件为电容（电场储能 $W_E = \frac{1}{2}C u_C^2$）和电感（磁场储能 $W_M = \frac{1}{2}L i_L^2$）；
3. 且根据换路定则，电容电压 $u_C$ 与电感电流 $i_L$ 不能突变，连续记忆系统状态；
4. 因此标准状态变量应选取**各独立电容的端电压 $u_C$** 和**各独立电感的支路电流 $i_L$**。
选 **A**。"""
  },
  {
    "id": "ss-c6-05",
    "subject": "广工837/809-信号与系统",
    "chapter": "第六章：系统状态变量与信号流图",
    "section": "离散系统直接II型框图状态",
    "type": "single",
    "difficulty": 3,
    "tags": ["直接II型", "典范型", "延迟单元"],
    "source": "广东工业大学837/809经典真题",
    "stem": "对于二阶离散系统，直接 II 型（Direct Form II，又称典范型/规范型）结构相比于直接 I 型结构的最显著工程优势是：",
    "options": [
      { "key": "A", "text": "所需单位延迟单元（$z^{-1}$ 存储器）数量减半，达到理论最少个数" },
      { "key": "B", "text": "不需要任何加法器" },
      { "key": "C", "text": "系统绝对不会产生溢出失真" },
      { "key": "D", "text": "只能用于全通滤波器" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散系统直接 II 型（Canonical Form 典范型）结构特性。

1. 直接 I 型结构分别对分子（前馈多项式）和分母（反馈多项式）实现延迟，对于 $N$ 阶系统总共需要 $2N$ 个延迟单元；
2. 直接 II 型利用 LTI 子系统级联的可交换性，将极点反馈部分移到前端、零点前馈部分移到后端，共享同一组延迟抽头链；
3. 对于 $N$ 阶差分系统，直接 II 型只需要 $N$ 个延迟单元（存储器数量直接减半），达到了实现该传输函数所需的最小延迟器数量，因而被称为**典范型（Canonical Form）**。
选 **A**。"""
  },
  {
    "id": "ss-c6-06",
    "subject": "广工837/809-信号与系统",
    "chapter": "第六章：系统状态变量与信号流图",
    "section": "不接触回路判别",
    "type": "single",
    "difficulty": 2,
    "tags": ["信号流图", "回路增益", "梅森公式"],
    "source": "广东工业大学837考研真题",
    "stem": "在信号流图中，“两回路互不接触”的严格拓扑定义是：",
    "options": [
      { "key": "A", "text": "两回路没有任何公共节点（甚至不共享任何支路与节点）" },
      { "key": "B", "text": "两回路的传输方向相反" },
      { "key": "C", "text": "两回路的增益乘积为零" },
      { "key": "D", "text": "两回路只共享同一个输入源节点" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：信号流图中不接触回路（Non-touching Loops）的拓扑定义。

1. 信号流图中的回路是指沿支路箭头方向闭合且除起点/终点外不重复经过任何节点的闭合路径；
2. 如果两个回路**没有任何公共节点**（Non-touching），即两个回路在几何与拓扑上完全隔离独立，则称它们互不接触；
3. 只要它们之间共用了哪怕一个节点，即视为相互接触回路，在 $\Delta$ 展开式中不能作为互不接触对相乘。
选 **A**。"""
  },
  {
    "id": "ss-c6-07",
    "subject": "广工837/809-信号与系统",
    "chapter": "第六章：系统状态变量与信号流图",
    "section": "离散状态方程标准形式",
    "type": "single",
    "difficulty": 2,
    "tags": ["离散系统", "状态方程", "差分矩阵"],
    "source": "广东工业大学837核心考点",
    "stem": "离散时间单输入单输出系统的标准一阶矩阵差分状态方程形式为：",
    "options": [
      { "key": "A", "text": "$\mathbf{x}(k + 1) = \mathbf{A}\mathbf{x}(k) + \mathbf{b}f(k), \quad y(k) = \mathbf{c}^T\mathbf{x}(k) + d f(k)$" },
      { "key": "B", "text": "$\mathbf{x}(k) = \mathbf{A}\mathbf{x}(k - 1) + \mathbf{b}y(k), \quad f(k) = \mathbf{c}^T\mathbf{x}(k)$" },
      { "key": "C", "text": "$\Delta\mathbf{x}(k) = \mathbf{A}\mathbf{x}(k) + \mathbf{b}f(k)$" },
      { "key": "D", "text": "$\mathbf{x}(k + 2) = \mathbf{A}\mathbf{x}(k) + \mathbf{b}f(k)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散时不变系统的状态空间方程标准表述。

1. 离散状态方程描述下一时刻状态向量 $\mathbf{x}(k + 1)$ 与当前状态 $\mathbf{x}(k)$ 及当前输入 $f(k)$ 的线性递推关系：
   $$\mathbf{x}(k + 1) = \mathbf{A}\mathbf{x}(k) + \mathbf{b}f(k)$$
2. 离散输出方程描述当前时刻系统响应输出：
   $$y(k) = \mathbf{c}^T\mathbf{x}(k) + d f(k)$$
选 **A**。"""
  },
  {
    "id": "ss-c6-08",
    "subject": "广工837/809-信号与系统",
    "chapter": "第六章：系统状态变量与信号流图",
    "section": "特征多项式与系统极点",
    "type": "single",
    "difficulty": 2,
    "tags": ["特征方程", "系统矩阵", "极点求解"],
    "source": "广东工业大学837高频题",
    "stem": "已知连续系统的状态矩阵为 $\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix}$，则该系统的特征多项式 $\det(s\mathbf{I} - \mathbf{A})$ 及其特征根（极点）为：",
    "options": [
      { "key": "A", "text": "$s^2 + 3s + 2 = 0$，极点为 $-1, -2$" },
      { "key": "B", "text": "$s^2 - 3s + 2 = 0$，极点为 $1, 2$" },
      { "key": "C", "text": "$s^2 + 2s + 3 = 0$，极点为 $-1, -3$" },
      { "key": "D", "text": "$s^2 - 2 = 0$，极点为 $\pm \sqrt{2}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：由状态矩阵 $\mathbf{A}$ 求解系统特征方程与固有极点。

1. 构造特征矩阵 $s\mathbf{I} - \mathbf{A}$：
   $$s\mathbf{I} - \mathbf{A} = s \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} - \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix} = \begin{bmatrix} s & -1 \\ 2 & s + 3 \end{bmatrix}$$
2. 计算行列式：
   $$\det(s\mathbf{I} - \mathbf{A}) = s(s + 3) - (-1)(2) = s^2 + 3s + 2$$
3. 特征方程令为零：
   $$s^2 + 3s + 2 = (s + 1)(s + 2) = 0 \implies s_1 = -1, \, s_2 = -2$$
故极点为 $-1$ 和 $-2$。选 **A**。"""
  },
  {
    "id": "ss-c6-09",
    "subject": "广工837/809-信号与系统",
    "chapter": "第六章：系统状态变量与信号流图",
    "section": "单回路反馈梅森公式",
    "type": "single",
    "difficulty": 2,
    "tags": ["反馈控制", "闭环增益", "单回路"],
    "source": "广东工业大学837/809经典基础题",
    "stem": "前向通路增益为 $G(s)$、负反馈支路增益为 $H_b(s)$ 的典型负反馈控制系统，其闭环传递函数为：",
    "options": [
      { "key": "A", "text": "$\frac{G(s)}{1 + G(s)H_b(s)}$" },
      { "key": "B", "text": "$\frac{G(s)}{1 - G(s)H_b(s)}$" },
      { "key": "C", "text": "$\frac{1}{1 + G(s)H_b(s)}$" },
      { "key": "D", "text": "$G(s)[1 + H_b(s)]$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：闭环负反馈系统的梅森公式推导。

1. 只有一条前向通路：$P_1 = G(s)$；
2. 只有一个负反馈回路：由于反馈为负，回路增益为 $L_1 = -G(s)H_b(s)$；
3. 特征行列式：
   $$\Delta = 1 - L_1 = 1 - [-G(s)H_b(s)] = 1 + G(s)H_b(s)$$
4. 回路与前向通路相接触，其余子式 $\Delta_1 = 1$；
5. 由梅森公式：
   $$H(s) = \frac{P_1 \Delta_1}{\Delta} = \frac{G(s)}{1 + G(s)H_b(s)}$$
选 **A**。"""
  },
  {
    "id": "ss-c6-10",
    "subject": "广工837/809-信号与系统",
    "chapter": "第六章：系统状态变量与信号流图",
    "section": "状态变量微分积分器对应",
    "type": "single",
    "difficulty": 2,
    "tags": ["模拟框图", "积分器输出", "状态空间"],
    "source": "广东工业大学837核心考点",
    "stem": "在模拟计算机连续系统模拟结构图（由积分器、加法器、数乘器组成）中，通常规定选择哪个节点作为系统的状态变量：",
    "options": [
      { "key": "A", "text": "每个积分器的输出端信号" },
      { "key": "B", "text": "每个积分器的输入端信号" },
      { "key": "C", "text": "每个加法器的输入端信号" },
      { "key": "D", "text": "系统的最终输出端" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：连续系统框图中状态变量的经典选取规范。

1. 积分器的时域关系为：输出 $x_i(t) = \int_{-\infty}^t u_i(\tau)d\tau \implies \dot{x}_i(t) = u_i(t)$；
2. 若将**每个积分器的输出端信号**定义为状态变量 $x_i(t)$，则**积分器的输入端信号恰好自动对应其一阶导数 $\dot{x}_i(t)$**；
3. 这样一来，积分器输入端所汇聚的加法器代数式，直接自然构成了状态微分方程 $\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{b}f(t)$！
4. 这种选取方法简洁、严谨且标准化。
选 **A**。"""
  }
]

all_questions.extend(chapter6_questions)
print(f"Added Chapter 6: {len(chapter6_questions)} questions")


# ==========================================
# 第七章：时域抽样与恢复 (12 题)
# ==========================================
chapter7_questions = [
  {
    "id": "ss-c7-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第七章：时域抽样与恢复",
    "section": "信号平方频带扩展抽样率",
    "type": "single",
    "difficulty": 3,
    "tags": ["2023年837真题", "抽样定理", "频带展宽"],
    "source": "广东工业大学2023年837全国统考真题第6题",
    "stem": "已知带限信号 $f(t)$ 的最高截止角频率为 $\omega_m$。若构造信号 $y(t) = f^2(t)$，则对信号 $y(t)$ 进行无失真恢复所需的最小奈奎斯特抽样角频率 $\omega_s$ 为：",
    "options": [
      { "key": "A", "text": "$4\omega_m$" },
      { "key": "B", "text": "$2\omega_m$" },
      { "key": "C", "text": "$\omega_m$" },
      { "key": "D", "text": "$8\omega_m$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：时域相乘对应频域卷积后的频带展宽规律。

1. 时域信号自身相乘：$y(t) = f(t) \cdot f(t)$；
2. 由频域卷积定理：
   $$Y(j\omega) = \frac{1}{2\pi} [F(j\omega) * F(j\omega)]$$
3. 频带展宽法则：
   原信号频谱 $F(j\omega)$ 限带于 $[-\omega_m, \omega_m]$；
   两个区间长度为 $2\omega_m$ 的频谱做卷积，非零区域变为 $[-\omega_m - \omega_m, \omega_m + \omega_m] = [-2\omega_m, 2\omega_m]$；
   因此 $y(t)$ 的最高截止角频率扩大为 $\omega_{m, y} = 2\omega_m$；
4. 由奈奎斯特抽样定理，最小抽样频率为最高频率的 2 倍：
   $$\omega_s \ge 2 \omega_{m, y} = 2(2\omega_m) = 4\omega_m$$
故选 **A**。"""
  },
  {
    "id": "ss-c7-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第七章：时域抽样与恢复",
    "section": "双频相乘信号采样率",
    "type": "single",
    "difficulty": 2,
    "tags": ["2022年837真题", "抽样频率", "频带叠加"],
    "source": "广东工业大学2022年837全国统考真题第8题",
    "stem": "已知连续信号 $f_1(t)$ 的最高频率为 $100\text{ Hz}$，$f_2(t)$ 的最高频率为 $200\text{ Hz}$。若将两信号相乘构成新信号 $y(t) = f_1(t)f_2(t)$，则对 $y(t)$ 进行理想抽样时的奈奎斯特频率为：",
    "options": [
      { "key": "A", "text": "$600\text{ Hz}$" },
      { "key": "B", "text": "$400\text{ Hz}$" },
      { "key": "C", "text": "$300\text{ Hz}$" },
      { "key": "D", "text": "$200\text{ Hz}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：两不同带限信号时域相乘后的奈奎斯特抽样速率计算。

1. 时域相乘对应频域卷积：$Y(\omega) = \frac{1}{2\pi}[F_1(\omega) * F_2(\omega)]$；
2. 卷积后新信号的最高上限频率等于两信号上限频率之和：
   $$f_{m, y} = f_{m1} + f_{m2} = 100\text{ Hz} + 200\text{ Hz} = 300\text{ Hz}$$
3. 根据低通奈奎斯特抽样定理：
   $$f_s \ge 2 f_{m, y} = 2 \times 300\text{ Hz} = 600\text{ Hz}$$
故该信号的奈奎斯特频率为 **600 Hz**。选 **A**。"""
  },
  {
    "id": "ss-c7-03",
    "subject": "广工837/809-信号与系统",
    "chapter": "第七章：时域抽样与恢复",
    "section": "理想低通滤波信号重构",
    "type": "single",
    "difficulty": 3,
    "tags": ["抽样定理", "信号恢复", "内插公式"],
    "source": "广东工业大学837/809核心考点",
    "stem": "以采样间隔 $T_s$ 对带限信号 $f(t)$（最高截止频率 $\omega_m$ 满足 $\omega_s = \frac{2\pi}{T_s} \ge 2\omega_m$）进行理想冲激抽样后，通过截止频率为 $\frac{\omega_s}{2}$、增益为 $T_s$ 的理想低通滤波器恢复原信号的内插重构公式（Whittaker-Shannon 抽样公式）为：",
    "options": [
      { "key": "A", "text": "$f(t) = \sum_{n=-\infty}^\infty f(n T_s) \text{Sa}\left(\frac{\omega_s}{2}(t - n T_s)\right)$" },
      { "key": "B", "text": "$f(t) = \sum_{n=-\infty}^\infty f(n T_s) \delta(t - n T_s)$" },
      { "key": "C", "text": "$f(t) = \sum_{n=-\infty}^\infty f(n T_s) \cos(\omega_s t)$" },
      { "key": "D", "text": "$f(t) = \frac{1}{T_s} \sum_{n=-\infty}^\infty f(n T_s) \text{rect}(t - n T_s)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：时域抽样定理的 Whittaker-Shannon 信号重构内插公式。

1. 冲激抽样信号为：
   $$f_s(t) = \sum_{n=-\infty}^\infty f(n T_s) \delta(t - n T_s)$$
2. 理想低通滤波器的冲激响应为抽样函数：
   $$h(t) = \text{Sa}\left(\frac{\omega_s}{2} t\right)$$
3. 抽样信号通过低通滤波器时，时域响应等于两者做卷积：
   $$f(t) = f_s(t) * h(t) = \left[ \sum_{n=-\infty}^\infty f(n T_s) \delta(t - n T_s) \right] * \text{Sa}\left(\frac{\omega_s}{2} t\right)$$
4. 利用冲激卷积的平移性质得到：
   $$f(t) = \sum_{n=-\infty}^\infty f(n T_s) \text{Sa}\left(\frac{\omega_s}{2}(t - n T_s)\right)$$
选 **A**。"""
  },
  {
    "id": "ss-c7-04",
    "subject": "广工837/809-信号与系统",
    "chapter": "第七章：时域抽样与恢复",
    "section": "尺度与时移抽样频率",
    "type": "single",
    "difficulty": 2,
    "tags": ["2025年809真题", "尺度变换", "抽样频率"],
    "source": "广东工业大学2025年809全国统考真题第7题",
    "stem": "若对带限连续信号 $f(t)$ 进行理想采样，其奈奎斯特频率为 $f_s\text{ Hz}$。则时移与尺度变换信号 $f\left(\frac{1}{3}t - 2\right)$ 的奈奎斯特采样频率为：",
    "options": [
      { "key": "A", "text": "$\frac{1}{3}f_s\text{ Hz}$" },
      { "key": "B", "text": "$3f_s\text{ Hz}$" },
      { "key": "C", "text": "$f_s\text{ Hz}$" },
      { "key": "D", "text": "$\frac{1}{9}f_s\text{ Hz}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：傅里叶变换时移与尺度变换对最高带宽的影响。

1. 设原信号 $f(t)$ 的最高截止频率为 $f_m$，其奈奎斯特采样频率为 $f_s = 2f_m$；
2. 对信号进行自变量变换 $g(t) = f(\frac{1}{3}t - 2)$：
   - 时移 $-2$ 产生频域线性相位偏移 $e^{-j 2\omega}$，完全不改变频带幅度范围；
   - 尺度变换因子为 $a = \frac{1}{3} < 1$，时域信号被展宽为原来的 3 倍；
3. 由尺度性质 $f(at) \leftrightarrow \frac{1}{|a|}F(\frac{\omega}{a})$：
   频域被压缩除以 3，新信号的最高上限频率缩小为原信号的 $\frac{1}{3}$：
   $$f_{m, g} = \frac{1}{3}f_m$$
4. 因此新信号的奈奎斯特抽样频率为：
   $$f_{s, g} = 2 f_{m, g} = 2 \left(\frac{1}{3}f_m\right) = \frac{1}{3} (2f_m) = \frac{1}{3}f_s$$
选 **A**。"""
  },
  {
    "id": "ss-c7-05",
    "subject": "广工837/809-信号与系统",
    "chapter": "第七章：时域抽样与恢复",
    "section": "卷积信号奈奎斯特抽样频率",
    "type": "single",
    "difficulty": 3,
    "tags": ["时域卷积", "频域相乘", "最小带宽"],
    "source": "广东工业大学837/809经典题型",
    "stem": "已知信号 $f_1(t)$ 的最高角频率为 $\omega_{m1} = 100\pi$，信号 $f_2(t)$ 的最高角频率为 $\omega_{m2} = 300\pi$。若新信号为时域卷积信号 $y(t) = f_1(t) * f_2(t)$，则对其无失真抽样的最小奈奎斯特角频率 $\omega_s$ 为：",
    "options": [
      { "key": "A", "text": "$200\pi\text{ rad/s}$" },
      { "key": "B", "text": "$400\pi\text{ rad/s}$" },
      { "key": "C", "text": "$600\pi\text{ rad/s}$" },
      { "key": "D", "text": "$800\pi\text{ rad/s}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：两信号卷积后频域为代数相乘，频带取交集（以窄带为准）。

1. 时域卷积定理：
   $$Y(j\omega) = F_1(j\omega) \cdot F_2(j\omega)$$
2. 频带分析：
   - $F_1(j\omega)$ 在 $|\omega| > 100\pi$ 时严格为 0；
   - $F_2(j\omega)$ 在 $|\omega| > 300\pi$ 时严格为 0；
   - 两者相乘后，只要超出窄带 $|\omega| > 100\pi$，乘积 $Y(j\omega)$ 就必定为 0；
3. 因此卷积信号的最高频率受限于较窄的那个信号：
   $$\omega_{m, y} = \min(\omega_{m1}, \omega_{m2}) = 100\pi$$
4. 奈奎斯特抽样角频率为：
   $$\omega_s \ge 2 \omega_{m, y} = 2 \times 100\pi = 200\pi\text{ rad/s}$$
【注意辨析】：
- 时域相乘 $\implies$ 频域卷积 $\implies$ 频带相加；
- 时域卷积 $\implies$ 频域相乘 $\implies$ 频带取小（取交集）。
故选 **A**。"""
  },
  {
    "id": "ss-c7-06",
    "subject": "广工837/809-信号与系统",
    "chapter": "第七章：时域抽样与恢复",
    "section": "时域压缩尺度变换采样率",
    "type": "single",
    "difficulty": 2,
    "tags": ["2022年837真题", "尺度变换", "采样频率"],
    "source": "广东工业大学2022年837全国统考真题第8题变式",
    "stem": "已知基带信号 $f(t)$ 的最高频率为 $f_m\text{ Hz}$。若构造时域压缩信号 $g(t) = f(4t)$，则对 $g(t)$ 抽样的奈奎斯特频率为：",
    "options": [
      { "key": "A", "text": "$8f_m\text{ Hz}$" },
      { "key": "B", "text": "$2f_m\text{ Hz}$" },
      { "key": "C", "text": "$4f_m\text{ Hz}$" },
      { "key": "D", "text": "$\frac{1}{2}f_m\text{ Hz}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：尺度变换参数 $a > 1$ 时的频带扩展与采样频率成倍增长。

1. 原信号 $f(t)$ 的频带范围为 $[-f_m, f_m]$；
2. 当尺度变换为 $g(t) = f(4t)$ 时，时域被压缩为原来的 $\frac{1}{4}$，频带被展宽 4 倍；
   $$G(f) = \frac{1}{4}F\left(\frac{f}{4}\right)$$
3. 新信号的最高截止频率扩展为 $f_{m, g} = 4 f_m$；
4. 奈奎斯特抽样频率：
   $$f_{s, g} = 2 f_{m, g} = 2(4f_m) = 8f_m$$
故选 **A**。"""
  },
  {
    "id": "ss-c7-07",
    "subject": "广工837/809-信号与系统",
    "chapter": "第七章：时域抽样与恢复",
    "section": "混叠失真根本原因",
    "type": "single",
    "difficulty": 1,
    "tags": ["混叠失真", "频域延拓", "基础考点"],
    "source": "广东工业大学837/809经典考题",
    "stem": "时域理想抽样过程中，当采样角频率 $\omega_s < 2\omega_m$ 时，抽样信号将发生混叠失真（Aliasing），其频域机理是：",
    "options": [
      { "key": "A", "text": "以 $\omega_s$ 为周期延拓的频谱在相邻周期之间发生频谱重叠交错" },
      { "key": "B", "text": "信号的高频部分被滤波器完全滤除" },
      { "key": "C", "text": "时域信号产生了非线性畸变" },
      { "key": "D", "text": "冲激脉冲的幅度发生了衰减" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：抽样频谱周期延拓与混叠失真的本质几何机理。

1. 冲激抽样信号的傅里叶变换为原信号频谱按 $\omega_s$ 周期的无限次平移叠加：
   $$F_s(j\omega) = \frac{1}{T_s}\sum_{k=-\infty}^\infty F(j(\omega - k\omega_s))$$
2. 当 $\omega_s \ge 2\omega_m$ 时，相邻两个延拓频谱的间隔 $\omega_s - 2\omega_m \ge 0$，频谱互不重叠，可以用低通滤波器完美分离出基带；
3. 当 $\omega_s < 2\omega_m$ 时，高频分量侵入相邻周期的基带区域，彼此重叠交错，破坏了原始频带的信息完整性，导致无法通过线性滤波无失真复原。
选 **A**。"""
  },
  {
    "id": "ss-c7-08",
    "subject": "广工837/809-信号与系统",
    "chapter": "第七章：时域抽样与恢复",
    "section": "奈奎斯特采样间隔计算",
    "type": "single",
    "difficulty": 2,
    "tags": ["采样间隔", "最高频率", "经典计算"],
    "source": "广东工业大学837历年真题",
    "stem": "已知带限信号 $f(t) = 10\text{Sa}(200\pi t)$，为保证无失真恢复，最大的允许抽样时间间隔 $T_{s,\max}$ 为：",
    "options": [
      { "key": "A", "text": "$5\text{ ms} = 0.005\text{ s}$" },
      { "key": "B", "text": "$10\text{ ms} = 0.01\text{ s}$" },
      { "key": "C", "text": "$2.5\text{ ms} = 0.0025\text{ s}$" },
      { "key": "D", "text": "$1\text{ ms}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：抽样函数频谱最高截止频率与最大采样间隔计算。

1. 抽样函数傅里叶变换对：
   $$\text{Sa}(W t) \stackrel{\mathcal{F}}{\longleftrightarrow} \frac{\pi}{W} \text{rect}\left(\frac{\omega}{2W}\right)$$
2. 本题中 $W = 200\pi$，因此信号的最高截止角频率为：
   $$\omega_m = 200\pi\text{ rad/s} \implies f_m = \frac{\omega_m}{2\pi} = \frac{200\pi}{2\pi} = 100\text{ Hz}$$
3. 奈奎斯特最小抽样频率为：
   $$f_s \ge 2 f_m = 200\text{ Hz}$$
4. 对应最大的抽样时间间隔为：
   $$T_{s,\max} = \frac{1}{f_s} = \frac{1}{200} = 0.005\text{ s} = 5\text{ ms}$$
选 **A**。"""
  },
  {
    "id": "ss-c7-09",
    "subject": "广工837/809-信号与系统",
    "chapter": "第七章：时域抽样与恢复",
    "section": "抗混叠滤波器工程作用",
    "type": "single",
    "difficulty": 1,
    "tags": ["抗混叠", "工程应用", "低通滤波"],
    "source": "广东工业大学837概念题",
    "stem": "在实际数字信号处理系统的前端，通常在抽样保持（A/D 转换）电路之前串联一个低通滤波器，该滤波器的主要作用是：",
    "options": [
      { "key": "A", "text": "作为抗混叠滤波器（Anti-aliasing Filter），滤除高于 $\frac{f_s}{2}$ 的带外高频噪声与无用干扰" },
      { "key": "B", "text": "放大输入信号的幅度" },
      { "key": "C", "text": "将模拟信号转换为离散序列" },
      { "key": "D", "text": "消除低频直流漂移" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：抗混叠前置低通滤波器的工程原理。

1. 现实中的实际物理信号和环境噪声往往具有很宽的频谱，不是严格有限带限的；
2. 如果直接按采样率 $f_s$ 进行采样，高于奈奎斯特折叠频率 $\frac{f_s}{2}$ 的所有高频分量和高频噪声都将折叠回基带内部，产生不可消除的混叠噪声；
3. 因此在采样之前，必须先经过一个截止频率为 $f_c \le \frac{f_s}{2}$ 的低通滤波器（称为抗混叠滤波器），强行消除带外高频分量，确保满足采样定理要求。
选 **A**。"""
  },
  {
    "id": "ss-c7-10",
    "subject": "广工837/809-信号与系统",
    "chapter": "第七章：时域抽样与恢复",
    "section": "周期冲激串抽样频谱公式",
    "type": "single",
    "difficulty": 2,
    "tags": ["冲激序列", "频域延拓", "抽样定理"],
    "source": "广东工业大学837/809经典基础",
    "stem": "以周期为 $T_s$ 的理想冲激串 $p(t) = \sum_{n=-\infty}^\infty \delta(t - n T_s)$ 对连续信号 $f(t)$ 进行时域抽样，所得抽样信号 $f_s(t) = f(t)p(t)$ 的频谱表达式为：",
    "options": [
      { "key": "A", "text": "$F_s(j\omega) = \frac{1}{T_s} \sum_{k=-\infty}^\infty F\left(j(\omega - k\omega_s)\right)$" },
      { "key": "B", "text": "$F_s(j\omega) = \sum_{k=-\infty}^\infty F\left(j(\omega - k\omega_s)\right)$" },
      { "key": "C", "text": "$F_s(j\omega) = \frac{1}{2\pi} \sum_{k=-\infty}^\infty F\left(j(\omega - k\omega_s)\right)$" },
      { "key": "D", "text": "$F_s(j\omega) = F(j\omega) * \delta(\omega - \omega_s)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：时域周期冲激串抽样的频域严格推导。

1. 周期为 $T_s$ 的冲激序列的傅里叶级数展开式为：
   $$p(t) = \sum_{n=-\infty}^\infty \delta(t - nT_s) = \frac{1}{T_s}\sum_{k=-\infty}^\infty e^{jk\omega_s t}, \quad \omega_s = \frac{2\pi}{T_s}$$
2. 时域抽样信号表示为：
   $$f_s(t) = f(t)p(t) = \frac{1}{T_s}\sum_{k=-\infty}^\infty f(t)e^{jk\omega_s t}$$
3. 对两端取傅里叶变换，利用频移定理：
   $$F_s(j\omega) = \frac{1}{T_s}\sum_{k=-\infty}^\infty F(j(\omega - k\omega_s))$$
选 **A**。"""
  },
  {
    "id": "ss-c7-11",
    "subject": "广工837/809-信号与系统",
    "chapter": "第七章：时域抽样与恢复",
    "section": "带通抽样定理",
    "type": "judgment",
    "difficulty": 3,
    "tags": ["带通采样", "中频采样", "前沿考点"],
    "source": "广东工业大学837/809拓展真题",
    "stem": "对于频带范围在 $[f_L, f_H]$ 之间的高频窄带带通信号（带宽 $B = f_H - f_L \ll f_H$），最低采样频率必须大于其最高频率的 2 倍（即 $f_s \ge 2 f_H$）。",
    "options": [
      { "key": "A", "text": "正确（True）" },
      { "key": "B", "text": "错误（False）" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：带通抽样定理（Bandpass Sampling Theorem）。

1. 奈奎斯特采样定理 $f_s \ge 2 f_H$ 严格适用于**低通信号（频谱从 0 延伸到 $f_H$）**；
2. 对于高频窄带带通信号，其中间 $[0, f_L]$ 大段频谱为空，若依然按 $2f_H$ 采样会造成严重的计算量与硬件浪费；
3. **带通抽样定理**指出：只要合理选择采样频率 $f_s$，使得周期延拓后的各个带通谱带恰好插空落入空余频隙而不产生重叠，其采样率只需满足：
   $$f_s \ge 2 B = 2(f_H - f_L)$$
   （远小于 $2f_H$），即可实现完全无失真重构！
因此题干断言“必须大于其最高频率的 2 倍”是错误的。选 **B**。"""
  },
  {
    "id": "ss-c7-12",
    "subject": "广工837/809-信号与系统",
    "chapter": "第七章：时域抽样与恢复",
    "section": "正弦信号临界抽样混叠判别",
    "type": "single",
    "difficulty": 2,
    "tags": ["正弦采样", "临界采样", "退化全零"],
    "source": "广东工业大学837核心考点",
    "stem": "对于单一频率正弦信号 $f(t) = \sin(\omega_0 t)$，若恰好按临界奈奎斯特采样角频率 $\omega_s = 2\omega_0$ 进行均匀抽样（采样时刻 $t_n = n T_s = n \frac{\pi}{\omega_0}$），则采样得到的离散序列值 $f(n T_s)$ 将：",
    "options": [
      { "key": "A", "text": "全部恒等于 0（完全丢失信号信息）" },
      { "key": "B", "text": "完美恢复出正弦波" },
      { "key": "C", "text": "呈现交替正负 1 的方波" },
      { "key": "D", "text": "幅度变为原信号的 2 倍" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：单一正弦信号临界抽样 $\omega_s = 2\omega_0$ 的相位敏感陷阱（奈奎斯特准则的严格大于要求）。

1. 抽样间隔为 $T_s = \frac{2\pi}{\omega_s} = \frac{2\pi}{2\omega_0} = \frac{\pi}{\omega_0}$；
2. 代入抽样时刻 $t_n = n T_s = n \frac{\pi}{\omega_0}$：
   $$f(n T_s) = \sin\left(\omega_0 \cdot n \frac{\pi}{\omega_0}\right) = \sin(n \pi) = 0, \quad (\forall n \in \mathbb{Z})$$
3. 抽样点恰好每一次都精准落在了正弦波的**过零点**上，导致采到的所有离散样值恒为 0！
4. 这正是为什么抽样定理中严格要求 $\omega_s > 2\omega_m$（大于而不是等于），或者需要正交双通道采样的根本原因。
选 **A**。"""
  }
]

all_questions.extend(chapter7_questions)
print(f"Added Chapter 7: {len(chapter7_questions)} questions")
print(f"Total accumulated questions: {len(all_questions)}")

# Export as TypeScript
def export_to_typescript(output_path):
    header = """import { Question } from '../types';

export const signalsAndSystemsQuestions: Question[] = """
    
    formatted_json = json.dumps(all_questions, ensure_ascii=False, indent=2)
    
    with open(output_path, 'w', encoding='utf-8') as out:
        out.write(header + formatted_json + ";\n")
    print(f"Successfully generated {output_path} with {len(all_questions)} questions!")

if __name__ == '__main__':
    print("Total questions in bank:", len(all_questions))
    export_to_typescript('src/data/signalsQuestions.ts')
