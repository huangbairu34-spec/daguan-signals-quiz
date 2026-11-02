import json
import os

questions = [
  # ==========================================
  # 第一章：信号与系统基本概念及特性
  # ==========================================
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
    "stem": "连续时间信号 $f(t) = \\cos\\left(10t + \\frac{\\pi}{2}\\right) + \\sin\\left(20t + \\frac{\\pi}{3}\\right)$ 的基波周期 $T$ 为：",
    "options": [
      { "key": "A", "text": "$\\frac{\\pi}{10}$" },
      { "key": "B", "text": "$\\frac{\\pi}{5}$" },
      { "key": "C", "text": "$\\frac{\\pi}{20}$" },
      { "key": "D", "text": "非周期信号" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：连续正弦复合信号的周期判定。

1. 第一个分量角频率 $\\omega_1 = 10\\text{ rad/s}$，周期 $T_1 = \\frac{2\\pi}{\\omega_1} = \\frac{2\\pi}{10} = \\frac{\\pi}{5}$；
2. 第二个分量角频率 $\\omega_2 = 20\\text{ rad/s}$，周期 $T_2 = \\frac{2\\pi}{\\omega_2} = \\frac{2\\pi}{20} = \\frac{\\pi}{10}$；
3. 两分量周期之比：
   $$\\frac{T_1}{T_2} = \\frac{\\pi / 5}{\\pi / 10} = 2$$
   比值为有理数，因此连续信号复合后依然为严格周期信号。
4. 总周期为 $T_1$ 和 $T_2$ 的最小公倍数：$T = \\frac{\\pi}{5}$。
故正确答案为 **B**。"""
  },
  {
    "id": "ss-c1-03",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "离散非周期序列判断",
    "type": "judgment",
    "difficulty": 2,
    "tags": ["离散周期", "概念辨析", "真题高频"],
    "source": "广东工业大学历年考研考点总结",
    "stem": "离散时间余弦序列 $f(k) = \\cos(3k)$ 具有周期性。这种说法是否正确？",
    "options": [
      { "key": "T", "text": "正确（True）" },
      { "key": "F", "text": "错误（False）" }
    ],
    "answer": "F",
    "analysis": """【核心考点】：离散正弦序列具有周期性的充要条件。

1. 离散正弦序列 $f(k) = \\cos(\\Omega k)$ 是周期序列的**充要条件**是：
   $$\\frac{2\\pi}{\\Omega} = \\frac{N}{m} \\in \\mathbb{Q} \\quad (\\text{必须为有理数})$$
2. 本题中数字角频率 $\\Omega = 3$，则：
   $$\\frac{2\\pi}{\\Omega} = \\frac{2\\pi}{3}$$
   因为 $\\pi$ 是无理数，故 $\\frac{2\\pi}{3}$ 为无理数，永远找不到正整数 $N$ 和 $m$ 使得 $N \\Omega = 2\\pi m$ 成立。
3. 因此该离散余弦序列**不是周期序列**！
说法错误，故选 **F**。"""
  },
  {
    "id": "ss-c1-04",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "广义导数与冲激筛选",
    "type": "single",
    "difficulty": 3,
    "tags": ["2021年837真题", "冲激函数", "广义微积分"],
    "source": "广东工业大学2021年837全国统考真题第1题",
    "stem": "计算广义导数 $\\frac{d}{dt} \\left\\{ [\\cos(2t) + \\sin(t)] \\varepsilon(t) \\right\\}$ 的化简结果为：",
    "options": [
      { "key": "A", "text": "$[-2\\sin(2t) + \\cos(t)]\\varepsilon(t) + \\delta(t)$" },
      { "key": "B", "text": "$[-2\\sin(2t) + \\cos(t)]\\varepsilon(t)$" },
      { "key": "C", "text": "$[-2\\sin(2t) + \\cos(t)]\\varepsilon(t) + [\\cos(2t) + \\sin(t)]\\delta(t)$" },
      { "key": "D", "text": "$-2\\sin(2t) + \\cos(t) + \\delta(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：阶跃函数的导数与冲激函数乘积筛选性质。

1. 根据复合函数求导法则：
   $$\\frac{d}{dt} [f(t)\\varepsilon(t)] = f'(t)\\varepsilon(t) + f(t)\\varepsilon'(t) = f'(t)\\varepsilon(t) + f(t)\\delta(t)$$
2. 设 $f(t) = \\cos(2t) + \\sin(t)$，求普通导数得：
   $$f'(t) = -2\\sin(2t) + \\cos(t)$$
3. 对于项 $f(t)\\delta(t)$，利用冲激函数的筛选性质 $f(t)\\delta(t) = f(0)\\delta(t)$：
   $$f(0) = \\cos(0) + \\sin(0) = 1 + 0 = 1$$
   因此：$f(t)\\delta(t) = 1 \\cdot \\delta(t) = \\delta(t)$。
4. 综合整理可得：
   $$\\frac{d}{dt} \\left\\{ [\\cos(2t) + \\sin(t)] \\varepsilon(t) \\right\\} = [-2\\sin(2t) + \\cos(t)]\\varepsilon(t) + \\delta(t)$$
故正确选项为 **A**。"""
  },
  {
    "id": "ss-c1-05",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "冲激偶积分性质",
    "type": "single",
    "difficulty": 3,
    "tags": ["2023年837真题", "冲激偶", "分部积分"],
    "source": "广东工业大学2023年837全国统考真题第2题",
    "stem": "计算广义积分 $\\int_{-\\infty}^\\infty (1 - x)\\delta'(x) \\, dx$ 的值为：",
    "options": [
      { "key": "A", "text": "0" },
      { "key": "B", "text": "1" },
      { "key": "C", "text": "-1" },
      { "key": "D", "text": "2" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：冲激偶函数 $\\delta'(t)$ 的积分筛选性质。

1. 冲激偶函数的积分筛选公式为：
   $$\\int_{-\\infty}^\\infty f(x)\\delta'(x) \\, dx = -f'(0)$$
2. 本题中 $f(x) = 1 - x$，对 $x$ 求一阶导数：
   $$f'(x) = -1 \\implies f'(0) = -1$$
3. 代入积分性质公式：
   $$\\int_{-\\infty}^\\infty (1 - x)\\delta'(x) \\, dx = -(-1) = 1$$
故正确答案为 **B**。"""
  },
  {
    "id": "ss-c1-06",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "冲激尺度变换与极限积分",
    "type": "single",
    "difficulty": 3,
    "tags": ["2024年837真题", "冲激尺度性质", "洛必达法则"],
    "source": "广东工业大学2024年837全国统考真题第2题",
    "stem": "计算广义积分 $\\int_{-\\infty}^\\infty \\frac{\\sin(\\pi t)}{t} \\delta(2t) \\, dt$ 的值为：",
    "options": [
      { "key": "A", "text": "0" },
      { "key": "B", "text": "$\\pi$" },
      { "key": "C", "text": "$\\frac{\\pi}{2}$" },
      { "key": "D", "text": "$2\\pi$" }
    ],
    "answer": "C",
    "analysis": """【核心考点】：冲激函数的尺度变换性质与筛选取值。

1. 根据冲激函数尺度变换公式 $\\delta(at) = \\frac{1}{|a|} \\delta(t)$：
   $$\\delta(2t) = \\frac{1}{2} \\delta(t)$$
2. 代入原积分中：
   $$\\int_{-\\infty}^\\infty \\frac{\\sin(\\pi t)}{t} \\delta(2t) \\, dt = \\frac{1}{2} \\int_{-\\infty}^\\infty \\frac{\\sin(\\pi t)}{t} \\delta(t) \\, dt$$
3. 利用冲激函数的筛选性质 $\\int_{-\\infty}^\\infty f(t)\\delta(t)dt = f(0)$，其中：
   $$f(0) = \\lim_{t \\to 0} \\frac{\\sin(\\pi t)}{t} = \\pi$$
4. 计算最终结果：
   $$\\frac{1}{2} \\times \\pi = \\frac{\\pi}{2}$$
故正确答案为 **C**。"""
  },
  {
    "id": "ss-c1-07",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "冲激偶二次多项式积分",
    "type": "single",
    "difficulty": 3,
    "tags": ["2018年837真题", "冲激微积分", "必刷题"],
    "source": "广东工业大学2018年837真题填空题",
    "stem": "计算广义积分 $\\int_{-\\infty}^\\infty (t^2 - 2)\\delta'(t) \\, dt$ 的值为：",
    "options": [
      { "key": "A", "text": "0" },
      { "key": "B", "text": "-2" },
      { "key": "C", "text": "2" },
      { "key": "D", "text": "4" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：冲激偶导数筛选性质。

1. 冲激偶积分公式：
   $$\\int_{-\\infty}^\\infty f(t)\\delta'(t)dt = -f'(0)$$
2. 设 $f(t) = t^2 - 2$，求一阶导数：
   $$f'(t) = 2t$$
3. 在 $t = 0$ 处的值为：
   $$f'(0) = 2 \\times 0 = 0$$
4. 因此积分值：
   $$\\int_{-\\infty}^\\infty (t^2 - 2)\\delta'(t)dt = -(0) = 0$$
故选 **A**。"""
  },
  {
    "id": "ss-c1-08",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "时变差分方程判定",
    "type": "single",
    "difficulty": 3,
    "tags": ["2021年837真题", "系统特性", "时变判定"],
    "source": "广东工业大学2021年837真题第3题",
    "stem": "差分方程 $y(k) - k y(k - 1) + y(k - 2) = f(k)$ 所描述的离散系统，其线性和时不变性属于：",
    "options": [
      { "key": "A", "text": "线性、时不变系统" },
      { "key": "B", "text": "线性、时变系统" },
      { "key": "C", "text": "非线性、时变系统" },
      { "key": "D", "text": "非线性、时不变系统" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：离散系统的线性与时变性辨析。

1. **线性判定**：
   方程中所有关于 $y$ 与 $f$ 的项均为一次幂，且不存在独立的非零常数项偏置，满足叠加性与齐次性：
   $$T[a f_1(k) + b f_2(k)] = a T[f_1(k)] + b T[f_2(k)]$$
   因此该系统是**线性系统**。
2. **时变判定**：
   第二项系数为 $-k$，显式依赖于离散时间自变量 $k$（非恒定常数）。
   由于系统参数随时间流逝而发生变化，不满足时不变性定义 $T[f(k - k_0)] = y(k - k_0)$。
故该系统为**线性、时变系统**。选 **B**。"""
  },
  {
    "id": "ss-c1-09",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "非线性时不变判定",
    "type": "single",
    "difficulty": 2,
    "tags": ["2022年837真题", "非线性判定", "系统分类"],
    "source": "广东工业大学2022年837真题第4题",
    "stem": "若某连续系统的输入激励为 $e(t)$，输出响应为 $r(t) = \\cos[e(t)]$（$t > 0$），则该系统是：",
    "options": [
      { "key": "A", "text": "线性、时不变系统" },
      { "key": "B", "text": "非线性、时不变系统" },
      { "key": "C", "text": "线性、时变系统" },
      { "key": "D", "text": "非线性、时变系统" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：非线性运算与时不变性。

1. **线性判定**：
   输入为 $e(t)$ 时输出为 $\\cos[e(t)]$；
   若输入加倍为 $2e(t)$，响应变为 $\\cos[2e(t)] \\ne 2\\cos[e(t)]$，严重破坏可加性与齐次性，属于典型的**非线性系统**。
2. **时不变判定**：
   若输入产生延时 $e(t - t_0)$，系统的响应变为 $\\cos[e(t - t_0)]$；
   而原输出的纯时延也是 $r(t - t_0) = \\cos[e(t - t_0)]$。
   两者完全等价，系统运算符中不含显时间 $t$ 因子，因此是**时不变系统**。
综上，该系统是**非线性、时不变系统**。选 **B**。"""
  },
  {
    "id": "ss-c1-10",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "能量信号与功率信号计算",
    "type": "single",
    "difficulty": 2,
    "tags": ["2022年837真题", "能量与功率", "经典计算"],
    "source": "广东工业大学2022年837真题计算题第2题",
    "stem": "单边指数衰减信号 $f_1(t) = e^{-2t}\\varepsilon(t)$ 的总能量 $E$ 和平均功率 $P$ 分别为：",
    "options": [
      { "key": "A", "text": "$E = \\frac{1}{4}$，属于能量信号（$P = 0$）" },
      { "key": "B", "text": "$E = \\frac{1}{2}$，属于能量信号（$P = 0$）" },
      { "key": "C", "text": "$E = \\infty$，$P = \\frac{1}{4}$，属于功率信号" },
      { "key": "D", "text": "$E = \\infty, P = 0$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：连续时间信号的总能量与平均功率定义。

1. **总能量计算**：
   $$E = \\int_{-\\infty}^\\infty |f_1(t)|^2 \\, dt = \\int_0^\\infty (e^{-2t})^2 \\, dt = \\int_0^\\infty e^{-4t} \\, dt$$
   $$E = \\left[ -\\frac{1}{4} e^{-4t} \\right]_0^\\infty = 0 - \\left(-\\frac{1}{4}\\right) = \\frac{1}{4}$$
2. **平均功率计算**：
   $$P = \\lim_{T \\to \\infty} \\frac{1}{T} \\int_{-T/2}^{T/2} |f_1(t)|^2 \\, dt = \\lim_{T \\to \\infty} \\frac{E}{T} = 0$$
3. **信号分类**：因为 $0 < E < \\infty$，平均功率 $P = 0$，故属于**能量信号**。
选 **A**。"""
  },
  {
    "id": "ss-c1-11",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "复指数信号的能量与功率",
    "type": "single",
    "difficulty": 2,
    "tags": ["2022年837真题", "功率信号", "复指数"],
    "source": "广东工业大学2022年837真题计算题第2题",
    "stem": "复指数周期信号 $f_2(t) = e^{j(2t + \\frac{\\pi}{4})}$ 的能量与功率特性为：",
    "options": [
      { "key": "A", "text": "能量有限，属于能量信号" },
      { "key": "B", "text": "总能量 $E = \\infty$，平均功率 $P = 1$，属于功率信号" },
      { "key": "C", "text": "平均功率 $P = 2$，属于功率信号" },
      { "key": "D", "text": "既非能量信号也非功率信号" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：复指数信号与功率信号。

1. 模值计算：对于任意时间 $t$：
   $$|f_2(t)| = \\left|e^{j(2t + \\frac{\\pi}{4})}\\right| = 1$$
2. 平均功率计算：
   $$P_2 = \\lim_{T \\to \\infty} \\frac{1}{T} \\int_{-T/2}^{T/2} |f_2(t)|^2 \\, dt = \\lim_{T \\to \\infty} \\frac{1}{T} \\int_{-T/2}^{T/2} 1 \\, dt = 1$$
3. 总能量：
   $$E_2 = \\int_{-\\infty}^\\infty 1 \\, dt = \\infty$$
因为 $0 < P_2 < \\infty$ 且 $E_2 = \\infty$，该信号为典型的**功率信号**。选 **B**。"""
  },
  {
    "id": "ss-c1-12",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "系统的记忆性判定",
    "type": "judgment",
    "difficulty": 2,
    "tags": ["2025年809真题", "记忆系统", "动态系统"],
    "source": "广东工业大学2025年809信号与系统全国统考真题",
    "stem": "微分方程描述的连续系统 $\\frac{df(t)}{dt} + 3f(t) + 5y(0_-) = 0$，该系统属于有记忆（动态）系统。这种说法是否正确？",
    "options": [
      { "key": "T", "text": "正确（True）" },
      { "key": "F", "text": "错误（False）" }
    ],
    "answer": "T",
    "analysis": """【核心考点】：记忆系统（Memory System / Dynamic System）的概念判定。

- **无记忆系统（即时系统）**：任何时刻的输出仅取决于该时刻的输入，与过去的输入或历史状态完全无关（如纯电阻网络 $y(t) = R f(t)$）。
- **有记忆系统（动态系统）**：系统的响应不仅取决于当前输入，还依赖于过去的输入或过去的历史储能状态（如电容、电感、初始状态 $y(0_-)$、微分和积分算子）。
该方程中显式包含历史初始状态 $y(0_-)$ 及微分算子，属于典型的**有记忆系统**。判断为 **正确 (True)**。"""
  },
  {
    "id": "ss-c1-13",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "因果性时域判定",
    "type": "single",
    "difficulty": 2,
    "tags": ["因果系统", "系统概念", "基础题"],
    "source": "广工信号与系统绝杀专题精选",
    "stem": "下列系统方程所描述的系统中，属于因果系统（Causal System）的是：",
    "options": [
      { "key": "A", "text": "$y(t) = f(2t)$" },
      { "key": "B", "text": "$y(t) = f(t - 2) + f(t)$" },
      { "key": "C", "text": "$y(t) = f(t + 1)$" },
      { "key": "D", "text": "$y(t) = f(-t)$" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：因果系统的物理可实现性判定。

- **因果系统定义**：系统在任意时刻 $t_0$ 的输出 $y(t_0)$，仅取决于当前时刻 $t \\le t_0$ 的输入，绝不依赖于未来时刻 $t > t_0$ 的输入信号。
- **逐项分析**：
  - A：$y(t) = f(2t)$，当 $t = 1$ 时 $y(1) = f(2)$，当前响应取决于未来输入 $f(2)$，**非因果**；
  - B：$y(t) = f(t - 2) + f(t)$，仅取决于过去时刻 $t-2$ 和当前时刻 $t$ 的输入，**因果系统**；
  - C：$y(t) = f(t + 1)$，依赖于未来输入 $f(t+1)$，**非因果**；
  - D：$y(t) = f(-t)$，当 $t = -1$ 时 $y(-1) = f(1)$，依赖于未来，**非因果**。
故选 **B**。"""
  },
  {
    "id": "ss-c1-14",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "系统的稳定性判定",
    "type": "single",
    "difficulty": 2,
    "tags": ["BIBO稳定性", "系统特性", "积分器"],
    "source": "广工837考研理论精选",
    "stem": "连续积分器系统 $y(t) = \\int_{-\\infty}^t f(\\tau) \\, d\\tau$ 的 BIBO 稳定性属于：",
    "options": [
      { "key": "A", "text": "稳定系统" },
      { "key": "B", "text": "不稳定系统" },
      { "key": "C", "text": "临界稳定且 BIBO 稳定" },
      { "key": "D", "text": "与输入幅度无关恒稳定" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：BIBO（有界输入有界输出）稳定性判定。

1. **反例法检验**：
   输入有界信号阶跃函数 $f(t) = \\varepsilon(t)$，显然 $|f(t)| \\le 1$ 是严格有界输入。
2. **计算输出响应**：
   $$y(t) = \\int_{-\\infty}^t \\varepsilon(\\tau) d\\tau = t \\varepsilon(t)$$
   当 $t \\to \\infty$ 时，$y(t) \\to \\infty$，输出无界！
3. 因此积分器**不是 BIBO 稳定系统**。
故选 **B**。"""
  },

  # ==========================================
  # 第二章：连续与离散系统的时域分析
  # ==========================================
  {
    "id": "ss-c2-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "离散卷积和计算",
    "type": "single",
    "difficulty": 3,
    "tags": ["2024年837真题", "离散卷积", "不进位乘法"],
    "source": "广东工业大学2024年837真题第3题",
    "stem": "已知序列 $f_1(k) = \\{\\underline{3}, 2, 1\\}$（$k=0$ 时为 3），$f_2(k) = \\{\\underline{1}, 2, 2, 2, 6\\}$（$k=0$ 时为 1），卷积和 $f(k) = f_1(k) * f_2(k)$，则 $f(3)$ 的值为：",
    "options": [
      { "key": "A", "text": "12" },
      { "key": "B", "text": "18" },
      { "key": "C", "text": "24" },
      { "key": "D", "text": "30" }
    ],
    "answer": "C",
    "analysis": """【核心考点】：离散卷积和与快速不进位乘法展开。

根据离散卷积公式：
$$f(k) = \\sum_{m=-\\infty}^\\infty f_1(m) f_2(k - m)$$
当 $k = 3$ 时：
$$f(3) = f_1(0)f_2(3) + f_1(1)f_2(2) + f_1(2)f_2(1)$$
由题意与不进位乘法列表展开，综合计算得 $f(3) = 24$。故选 **C**。"""
  },
  {
    "id": "ss-c2-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "全响应分解定理",
    "type": "single",
    "difficulty": 4,
    "tags": ["837必刷经典", "全响应分解", "高频必考"],
    "source": "广东工业大学837上岸经典必刷真题第7题",
    "stem": "某 LTI 连续系统具有初始储能。当激励为 $f_1(t)$ 时，全响应 $y_1(t) = (2e^{-t} - \\cos\\pi t)\\varepsilon(t)$；当激励为 $2f_1(t)$ 且起始状态不变时，全响应 $y_2(t) = 3\\cos\\pi t\\,\\varepsilon(t)$。若初始状态仍保持不变，当输入变为 $4f_1(t)$ 时，全响应 $y_3(t)$ 为：",
    "options": [
      { "key": "A", "text": "$(4e^{-t} + 7\\cos\\pi t)\\varepsilon(t)$" },
      { "key": "B", "text": "$(-4e^{-t} + 11\\cos\\pi t)\\varepsilon(t)$" },
      { "key": "C", "text": "$(8e^{-t} - 5\\cos\\pi t)\\varepsilon(t)$" },
      { "key": "D", "text": "$(2e^{-t} + 5\\cos\\pi t)\\varepsilon(t)$" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：全响应的双重线性分解定理。

由 LTI 系统的响应分解：
$$y(t) = y_{zi}(t) + y_{zs}(t)$$
1. 列方程组：
   输入 $f_1(t)$：$y_1(t) = y_{zi}(t) + y_{zs1}(t) = 2e^{-t} - \\cos\\pi t$ ①
   输入 $2f_1(t)$：$y_2(t) = y_{zi}(t) + 2y_{zs1}(t) = 3\\cos\\pi t$ ②
2. ② - ① 解出零状态响应分量：
   $$y_{zs1}(t) = 3\\cos\\pi t - (2e^{-t} - \\cos\\pi t) = 4\\cos\\pi t - 2e^{-t}$$
   代入 ① 得零输入响应分量：
   $$y_{zi}(t) = (2e^{-t} - \\cos\\pi t) - (4\\cos\\pi t - 2e^{-t}) = 4e^{-t} - 5\\cos\\pi t$$
3. 计算激励为 $4f_1(t)$ 时的全响应：
   $$y_3(t) = y_{zi}(t) + 4 y_{zs1}(t) = (4e^{-t} - 5\\cos\\pi t) + 4(4\\cos\\pi t - 2e^{-t})$$
   $$y_3(t) = (4 - 8)e^{-t} + (-5 + 16)\\cos\\pi t = -4e^{-t} + 11\\cos\\pi t$$
故正确答案为 **B**。"""
  },
  {
    "id": "ss-c2-03",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "指数序列卷积和",
    "type": "single",
    "difficulty": 3,
    "tags": ["离散卷积", "等比求和", "基础过关"],
    "source": "广工837经典题库精选题",
    "stem": "计算离散序列卷积和 $(2)^k \\varepsilon(k) * \\varepsilon(k)$ 的化简结果为：",
    "options": [
      { "key": "A", "text": "$(2^{k+1} - 1)\\varepsilon(k)$" },
      { "key": "B", "text": "$(2^k - 1)\\varepsilon(k)$" },
      { "key": "C", "text": "$2^{k+1}\\varepsilon(k)$" },
      { "key": "D", "text": "$(2^{k-1} + 1)\\varepsilon(k)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散卷积定义与等比数列求和。

由卷积和定义式：
$$y(k) = \\sum_{m=-\\infty}^\\infty 2^m \\varepsilon(m) \\varepsilon(k - m)$$
当 $k \\ge 0$ 时，求和区间为 $m \\in [0, k]$：
$$y(k) = \\sum_{m=0}^k 2^m = \\frac{1 \\cdot (1 - 2^{k+1})}{1 - 2} = 2^{k+1} - 1$$
当 $k < 0$ 时，$y(k) = 0$。
统一写为因果形式：$y(k) = (2^{k+1} - 1)\\varepsilon(k)$。选 **A**。"""
  },
  {
    "id": "ss-c2-04",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "离散样值响应响应计算",
    "type": "single",
    "difficulty": 3,
    "tags": ["2025年809真题", "冲激响应", "离散系统"],
    "source": "广东工业大学2025年809真题第15题",
    "stem": "已知离散系统单位样值响应 $h(n) = \\delta(n) + 2\\delta(n - 1) - \\delta(n - 3)$，激励序列为 $x(n) = 2\\delta(n - 1)$，则输出序列在 $n = 0$ 处的值 $y(0)$ 为：",
    "options": [
      { "key": "A", "text": "0" },
      { "key": "B", "text": "2" },
      { "key": "C", "text": "4" },
      { "key": "D", "text": "-2" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散时不变系统的卷积输出。

1. 系统响应输出：
   $$y(n) = x(n) * h(n) = [2\\delta(n - 1)] * [\\delta(n) + 2\\delta(n - 1) - \\delta(n - 3)]$$
2. 利用分配律与时移性质：
   $$y(n) = 2\\delta(n - 1) + 4\\delta(n - 2) - 2\\delta(n - 4)$$
3. 观察在 $n = 0$ 处的取值：
   上式中只有在 $n = 1, 2, 4$ 处有冲激脉冲，在 $n = 0$ 处为 0。
故 $y(0) = 0$。选 **A**。"""
  },
  {
    "id": "ss-c2-05",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "斜坡与阶跃信号卷积",
    "type": "single",
    "difficulty": 2,
    "tags": ["2018年837真题", "卷积积分", "积分性质"],
    "source": "广东工业大学2018年837全国统考真题第3题",
    "stem": "计算卷积积分 $t\\varepsilon(t) * \\varepsilon(t)$ 的化简结果为：",
    "options": [
      { "key": "A", "text": "$\\frac{1}{2}t^2 \\varepsilon(t)$" },
      { "key": "B", "text": "$t^2 \\varepsilon(t)$" },
      { "key": "C", "text": "$\\frac{1}{2}t \\varepsilon(t)$" },
      { "key": "D", "text": "$\\frac{1}{6}t^3 \\varepsilon(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：与阶跃信号卷积的时域积分特性。

1. 任何信号与单位阶跃信号 $\\varepsilon(t)$ 做卷积，等价于对该信号求变上限积分：
   $$f(t) * \\varepsilon(t) = \\int_{-\\infty}^t f(\\tau) \\, d\\tau$$
2. 代入 $f(t) = t\\varepsilon(t)$：
   对于 $t > 0$：
   $$y(t) = \\int_0^t \\tau \\, d\\tau = \\left[ \\frac{1}{2}\\tau^2 \\right]_0^t = \\frac{1}{2}t^2$$
3. 因果表示形式：$y(t) = \\frac{1}{2}t^2 \\varepsilon(t)$。
故正确答案为 **A**。"""
  },

  # ==========================================
  # 第三章：连续与离散系统的频域分析
  # ==========================================
  {
    "id": "ss-c3-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "实周期信号基波频率与傅氏级数",
    "type": "single",
    "difficulty": 3,
    "tags": ["2024年837真题", "傅里叶级数", "基波角频率"],
    "source": "广东工业大学2024年837全国统考真题第4题",
    "stem": "已知实周期信号 $f(t) = 5 - 6\\cos\\left(t - \\frac{\\pi}{3}\\right) + 4\\sin\\left(\\frac{3}{2}t + \\frac{\\pi}{6}\\right)$，则该周期信号的基波角频率 $\\omega_0$ 为：",
    "options": [
      { "key": "A", "text": "$1\\text{ rad/s}$" },
      { "key": "B", "text": "$0.5\\text{ rad/s}$" },
      { "key": "C", "text": "$1.5\\text{ rad/s}$" },
      { "key": "D", "text": "$2\\text{ rad/s}$" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：复合实周期信号的基波角频率求解。

1. 信号中包含的各交流分量角频率为：
   $$\\omega_1 = 1\\text{ rad/s}, \\quad \\omega_2 = \\frac{3}{2} = 1.5\\text{ rad/s}$$
2. 基波角频率 $\\omega_0$ 为各分量角频率的最大公约数：
   $$\\omega_0 = \\gcd\\left(1, \\frac{3}{2}\\right) = \\frac{\\gcd(2, 3)}{2} = 0.5\\text{ rad/s}$$
3. 验证各次谐波：
   $\\omega_1 = 2\\omega_0$（二次谐波），$\\omega_2 = 3\\omega_0$（三次谐波）。
故基波角频率为 **$0.5\\text{ rad/s}$**。选 **B**。"""
  },
  {
    "id": "ss-c3-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "LTI系统的正弦响应",
    "type": "single",
    "difficulty": 3,
    "tags": ["2024年837真题", "LTI特性", "频域稳态"],
    "source": "广东工业大学2024年837全国统考真题第6题",
    "stem": "已知 LTI 连续系统输入 $f(t) = e^{j 5t}$ 时，稳态响应 $y(t) = e^{j 3t}$；输入 $f(t) = e^{-j 5t}$ 时，稳态响应 $y(t) = e^{-j 3t}$。则当输入 $f(t) = \\cos(5t - 2)$ 时，系统的输出 $y(t)$ 为：",
    "options": [
      { "key": "A", "text": "$\\cos(3t - 2)$" },
      { "key": "B", "text": "$\\cos(5t - 2)$" },
      { "key": "C", "text": "$\\sin(3t - 2)$" },
      { "key": "D", "text": "$\\cos(3t + 2)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：线性叠加原理与复指数展开。

1. 由欧拉公式将激励展开为复指数分量：
   $$f(t) = \\cos(5t - 2) = \\frac{1}{2} e^{j(5t - 2)} + \\frac{1}{2} e^{-j(5t - 2)} = \\frac{1}{2} e^{-j 2} e^{j 5t} + \\frac{1}{2} e^{j 2} e^{-j 5t}$$
2. 系统为线性系统，利用已知输入与输出的线性叠加：
   $$y(t) = \\frac{1}{2} e^{-j 2} (e^{j 3t}) + \\frac{1}{2} e^{j 2} (e^{-j 3t}) = \\frac{1}{2} e^{j(3t - 2)} + \\frac{1}{2} e^{-j(3t - 2)}$$
3. 合并为余弦函数：
   $$y(t) = \\cos(3t - 2)$$
故正确答案为 **A**。"""
  },
  {
    "id": "ss-c3-03",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "傅里叶对偶性",
    "type": "single",
    "difficulty": 3,
    "tags": ["2021年837真题", "对偶性质", "常用变换对"],
    "source": "广东工业大学2021年837真题第5题",
    "stem": "连续信号 $f(t) = \\frac{1}{t^2 + 1}$ 的傅里叶变换 $F(j\\omega)$ 为：",
    "options": [
      { "key": "A", "text": "$\\pi e^{-|\\omega|}$" },
      { "key": "B", "text": "$2\\pi e^{-|\\omega|}$" },
      { "key": "C", "text": "$\\frac{1}{1 + \\omega^2}$" },
      { "key": "D", "text": "$\\pi e^{-\\omega}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：双边指数信号的傅里叶变换与对偶性质。

1. 已知常用变换对：$e^{-a|t|} \\stackrel{\\mathcal{F}}{\\longleftrightarrow} \\frac{2a}{a^2 + \\omega^2}$。
   令 $a = 1$，有：$e^{-|t|} \\stackrel{\\mathcal{F}}{\\longleftrightarrow} \\frac{2}{1 + \\omega^2}$。
2. 依据傅里叶变换对偶性：若 $f(t) \\leftrightarrow F(j\\omega)$，则 $F(jt) \\leftrightarrow 2\\pi f(-\\omega)$；
   将频域象函数变量换为时间 $t$：
   $$\\frac{2}{1 + t^2} \\stackrel{\\mathcal{F}}{\\longleftrightarrow} 2\\pi e^{-|-\\omega|} = 2\\pi e^{-|\\omega|}$$
3. 等式两边同时除以 2：
   $$\\frac{1}{t^2 + 1} \\stackrel{\\mathcal{F}}{\\longleftrightarrow} \\pi e^{-|\\omega|}$$
故正确答案为 **A**。"""
  },
  {
    "id": "ss-c3-04",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "稳态正弦响应",
    "type": "single",
    "difficulty": 3,
    "tags": ["2025年809真题", "频响函数", "正弦稳态"],
    "source": "广东工业大学2025年809真题第10题",
    "stem": "已知某连续 LTI 系统的频率响应为 $H(j\\omega) = \\frac{1}{1 + j\\omega}$。当输入信号为 $f(t) = \\sin(t)$ 时，系统的稳态输出响应 $y(t)$ 为：",
    "options": [
      { "key": "A", "text": "$\\frac{\\sqrt{2}}{2} \\sin\\left(t - \\frac{\\pi}{4}\\right)$" },
      { "key": "B", "text": "$\\frac{\\sqrt{2}}{2} \\cos\\left(t - \\frac{\\pi}{4}\\right)$" },
      { "key": "C", "text": "$\\sin\\left(t - \\frac{\\pi}{4}\\right)$" },
      { "key": "D", "text": "$\\frac{1}{2} \\sin(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：LTI 系统的频响特性对正弦信号的幅相响应。

1. 输入角频率 $\\omega = 1\\text{ rad/s}$；
2. 计算系统在 $\\omega = 1$ 处的频率响应：
   $$H(j 1) = \\frac{1}{1 + j} = \\frac{1}{\\sqrt{2} e^{j \\pi/4}} = \\frac{\\sqrt{2}}{2} e^{-j \\pi/4}$$
   其幅频响应增益 $|H(j 1)| = \\frac{\\sqrt{2}}{2}$，相位偏移量 $\\theta = -\\frac{\\pi}{4}$。
3. 稳态输出响应为：
   $$y(t) = |H(j 1)| \\sin(t + \\theta) = \\frac{\\sqrt{2}}{2} \\sin\\left(t - \\frac{\\pi}{4}\\right)$$
故选 **A**。"""
  },
  {
    "id": "ss-c3-05",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "无失真传输充要条件",
    "type": "multiple",
    "difficulty": 3,
    "tags": ["无失真传输", "多选题", "考研重点"],
    "source": "广东工业大学837重点理论真题",
    "stem": "一个连续 LTI 系统若要实现信号的无失真传输（Distortionless Transmission），必须同时满足下列哪些条件（多选）：",
    "options": [
      { "key": "A", "text": "系统的幅频特性必须为恒定常数，即 $|H(j\\omega)| = K$" },
      { "key": "B", "text": "系统的相频特性必须是通过原点的负斜率直线，即 $\\theta(\\omega) = -\\omega t_0$" },
      { "key": "C", "text": "系统的单位冲激响应为时延冲激，即 $h(t) = K\\delta(t - t_0)$" },
      { "key": "D", "text": "系统的群时延必须随频率增大而线性增大" }
    ],
    "answer": ["A", "B", "C"],
    "analysis": """【核心考点】：无失真传输的定义与频域、时域特征。

1. **无失真传输定义**：输出信号仅仅是输入信号的幅值放大/缩小以及固定时间延迟：
   $$y(t) = K f(t - t_0) \\quad (K > 0, t_0 > 0)$$
2. **频域特性**：
   取傅里叶变换得 $H(j\\omega) = K e^{-j\\omega t_0}$：
   - 幅频特性 $|H(j\\omega)| = K$（常数），**A 正确**；
   - 相频特性 $\\theta(\\omega) = -\\omega t_0$（严格线性相位），**B 正确**；
   - 群时延 $\\tau_g(\\omega) = -\\frac{d\\theta(\\omega)}{d\\omega} = t_0$ 为恒定常数，非线性变化，**D 错误**。
3. **时域特性**：
   对 $H(j\\omega)$ 求傅氏逆变换得 $h(t) = K\\delta(t - t_0)$，**C 正确**。
因此正确选项为 **A、B、C**。"""
  },
  {
    "id": "ss-c3-06",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "傅里叶变换对称性",
    "type": "single",
    "difficulty": 2,
    "tags": ["傅氏性质", "实偶虚奇", "经典理论"],
    "source": "奥本海姆信号与系统精选",
    "stem": "若实信号 $f(t)$ 为实偶信号（即 $f(-t) = f(t)$），则其傅里叶变换 $F(j\\omega)$ 必然具有的性质为：",
    "options": [
      { "key": "A", "text": "实偶函数" },
      { "key": "B", "text": "虚奇函数" },
      { "key": "C", "text": "实奇函数" },
      { "key": "D", "text": "纯虚数且偶对称" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：实信号的傅里叶变换对称性质。

由傅里叶变换公式：
$$F(j\\omega) = \\int_{-\\infty}^\\infty f(t) e^{-j\\omega t} dt = \\int_{-\\infty}^\\infty f(t)\\cos(\\omega t)dt - j\\int_{-\\infty}^\\infty f(t)\\sin(\\omega t)dt$$
- 当 $f(t)$ 为实偶信号时：
  $f(t)\\cos(\\omega t)$ 是偶函数，积分存在；
  $f(t)\\sin(\\omega t)$ 是奇函数，在对称区间积分恒为零；
  因此虚部完全抵消为零，只留下实部，且实部对 $\\omega$ 仍为偶函数！
故 $F(j\\omega)$ 是**实偶函数**。选 **A**。"""
  },

  # ==========================================
  # 第四章：连续系统的复频域分析（拉普拉斯变换）
  # ==========================================
  {
    "id": "ss-c4-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "假分式部分分式展开",
    "type": "single",
    "difficulty": 3,
    "tags": ["2023年837真题", "拉氏反变换", "部分分式"],
    "source": "广东工业大学2023年837真题第4题",
    "stem": "象函数 $F(s) = \\frac{s^2 + 4s + 5}{s^2 + 3s + 2}$（收敛域 $\\text{Re}(s) > -1$）的单边拉普拉斯逆变换 $f(t)$（$t \\ge 0$）为：",
    "options": [
      { "key": "A", "text": "$\\delta(t) + (2e^{-t} - e^{-2t})\\varepsilon(t)$" },
      { "key": "B", "text": "$\\delta(t) + (e^{-t} + 2e^{-2t})\\varepsilon(t)$" },
      { "key": "C", "text": "$(2e^{-t} - e^{-2t})\\varepsilon(t)$" },
      { "key": "D", "text": "$\\delta(t) - (2e^{-t} + e^{-2t})\\varepsilon(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：假分式多项式长除法与部分分式展开。

1. 分子分母均为 2 次方，长除提取常数 1：
   $$F(s) = \\frac{(s^2 + 3s + 2) + (s + 3)}{s^2 + 3s + 2} = 1 + \\frac{s + 3}{(s + 1)(s + 2)}$$
2. 部分分式展开：
   $$\\frac{s + 3}{(s + 1)(s + 2)} = \\frac{k_1}{s + 1} + \\frac{k_2}{s + 2}$$
   $$k_1 = \\left. \\frac{s + 3}{s + 2} \\right|_{s = -1} = \\frac{2}{1} = 2$$
   $$k_2 = \\left. \\frac{s + 3}{s + 1} \\right|_{s = -2} = \\frac{1}{-1} = -1$$
3. 标准象函数形式：
   $$F(s) = 1 + \\frac{2}{s + 1} - \\frac{1}{s + 2}$$
4. 查表求逆变换：
   $$f(t) = \\delta(t) + (2e^{-t} - e^{-2t})\\varepsilon(t)$$
故选 **A**。"""
  },
  {
    "id": "ss-c4-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "最小相移与全通网络",
    "type": "single",
    "difficulty": 4,
    "tags": ["2024年837真题", "最小相移", "全通系统"],
    "source": "广东工业大学2024年837真题画图题",
    "stem": "某稳定因果连续系统的系统函数为 $H(s) = \\frac{s - 2}{s^2 + 4s + 5}$。下列关于该系统的说法中，正确的是：",
    "options": [
      { "key": "A", "text": "零点为 $s = 2$，极点为 $s = -2 \\pm j$，属于最小相移系统" },
      { "key": "B", "text": "零点位于右半开平面，该系统不是最小相移系统，但可分解为一个最小相移系统与一个全通系统" },
      { "key": "C", "text": "由于分子存在 $s - 2$，该系统不稳定" },
      { "key": "D", "text": "该系统的幅频响应为恒定常数，属于全通系统" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：最小相移系统（Minimum Phase System）的判定与全通系统分解。

1. **零极点位置分析**：
   - 极点求解：$s^2 + 4s + 5 = 0 \\implies s = -2 \\pm j$，实部为 $-2 < 0$，均在左半开平面，因果系统稳定；
   - 零点求解：$s - 2 = 0 \\implies s = 2$，实部为 $+2 > 0$，零点落在**右半开平面**。
2. **最小相移判定**：
   因果稳定系统若要成为最小相移系统，其全部零点和极点均必须严格分布在左半开平面（或虚轴上单阶零极点）。由于存在右半平面零点 $s = 2$，故**不是最小相移系统**。
3. **全通分解**：
   $$H(s) = \\underbrace{\\frac{s + 2}{s^2 + 4s + 5}}_{H_{\\min}(s)} \\cdot \\underbrace{\\frac{s - 2}{s + 2}}_{H_{ap}(s)}$$
   - $H_{\\min}(s)$ 的零极点全在左半平面，为最小相移系统；
   - $H_{ap}(s)$ 的极点在 $-2$，零点在 $+2$，零极点关于虚轴对称，幅频响应 $|H_{ap}(j\\omega)| \\equiv 1$，为标准全通系统。
故正确答案为 **B**。"""
  },
  {
    "id": "ss-c4-03",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "复频移与正弦变换",
    "type": "single",
    "difficulty": 3,
    "tags": ["拉氏变换", "复频移", "经典考题"],
    "source": "广工837经典真题解析",
    "stem": "已知象函数 $F(s) = \\frac{s + 1}{s^2 + 2s + 10}$（收敛域 $\\text{Re}(s) > -1$），求其对应的原函数 $f(t)$ 为：",
    "options": [
      { "key": "A", "text": "$e^{-t} \\cos(3t)\\varepsilon(t)$" },
      { "key": "B", "text": "$e^{-t} \\sin(3t)\\varepsilon(t)$" },
      { "key": "C", "text": "$e^{-2t} \\cos(3t)\\varepsilon(t)$" },
      { "key": "D", "text": "$\\cos(3t)\\varepsilon(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：复频移性质与衰减正弦/余弦信号的逆变换。

1. 对分母进行配方：
   $$s^2 + 2s + 10 = (s + 1)^2 + 9 = (s + 1)^2 + 3^2$$
2. 观察分子形式：恰为 $s + 1$。
3. 由拉普拉斯常用公式：
   $$\\mathcal{L}[e^{-at} \\cos(\\omega_0 t)\\varepsilon(t)] = \\frac{s + a}{(s + a)^2 + \\omega_0^2}$$
   令 $a = 1, \\omega_0 = 3$，直接对应：
   $$f(t) = e^{-t} \\cos(3t)\\varepsilon(t)$$
故选 **A**。"""
  },
  {
    "id": "ss-c4-04",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "拉氏变换初值定理",
    "type": "single",
    "difficulty": 2,
    "tags": ["初值定理", "极限性质", "基础计算"],
    "source": "广工837上岸经典必刷题",
    "stem": "已知象函数 $F(s) = \\frac{2s + 3}{s^2 + 5s + 6}$，则由初值定理计算原信号在 $t = 0_+$ 处的取值 $f(0_+)$ 为：",
    "options": [
      { "key": "A", "text": "2" },
      { "key": "B", "text": "3" },
      { "key": "C", "text": "0" },
      { "key": "D", "text": "0.5" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：拉普拉斯变换初值定理。

1. 初值定理表达式：
   $$f(0_+) = \\lim_{s \\to \\infty} s F(s)$$
2. 代入象函数计算：
   $$s F(s) = \\frac{s(2s + 3)}{s^2 + 5s + 6} = \\frac{2s^2 + 3s}{s^2 + 5s + 6}$$
3. 当 $s \\to \\infty$ 时：
   $$\\lim_{s \\to \\infty} \\frac{2 + 3/s}{1 + 5/s + 6/s^2} = 2$$
故 $f(0_+) = 2$。选 **A**。"""
  },

  # ==========================================
  # 第五章：离散系统的 Z 域分析
  # ==========================================
  {
    "id": "ss-c5-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "稳定性充要条件与收敛域",
    "type": "single",
    "difficulty": 3,
    "tags": ["2024年837真题", "Z变换", "系统稳定性"],
    "source": "广东工业大学2024年837真题第9题",
    "stem": "已知某稳定离散系统的系统函数为 $H(z) = \\frac{z^2 + 2}{(z - 0.5)(z - 3)}$。若该系统为稳定系统，则其收敛域（ROC）应为：",
    "options": [
      { "key": "A", "text": "$|z| > 3$" },
      { "key": "B", "text": "$|z| < 0.5$" },
      { "key": "C", "text": "$0.5 < |z| < 3$" },
      { "key": "D", "text": "$|z| > 0.5$" }
    ],
    "answer": "C",
    "analysis": """【核心考点】：离散系统稳定性充要条件与收敛域 ROC 判定。

1. **求系统极点**：极点为 $z_1 = 0.5, z_2 = 3$。
2. **系统稳定性的充要条件**：
   系统函数 $H(z)$ 的收敛域（ROC）**必须包含单位圆（$|z| = 1$）**！
3. **三种可能收敛域辨析**：
   - 因果系统收敛域：$|z| > 3$（未包含单位圆 $|z|=1$，不稳定）；
   - 反因果系统收敛域：$|z| < 0.5$（未包含单位圆，不稳定）；
   - 双边非因果系统收敛域：$0.5 < |z| < 3$（环域恰好将单位圆 $|z| = 1$ 包含在内！）。
因此为保证系统稳定，收敛域必为 **$0.5 < |z| < 3$**。选 **C**。"""
  },
  {
    "id": "ss-c5-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "梳状滤波结构",
    "type": "single",
    "difficulty": 4,
    "tags": ["2022年837真题", "梳状滤波", "零极点图"],
    "source": "广东工业大学2022年837真题画图题",
    "stem": "离散梳状滤波器的系统函数为 $H(z) = 1 - z^{-6} = \\frac{z^6 - 1}{z^6}$。关于该系统的零极点与幅频特性，描述正确的是：",
    "options": [
      { "key": "A", "text": "原点处有 6 阶极点，单位圆上均匀分布 6 个零点 $z_k = e^{j k \\pi / 3}$（$k=0,1,\\dots,5$）" },
      { "key": "B", "text": "单位圆上有 6 个极点，原点处有 6 个零点" },
      { "key": "C", "text": "零点均在单位圆外，系统不稳定" },
      { "key": "D", "text": "幅频特性恒等于 1" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：梳状滤波器（Comb Filter）的零极点结构。

1. **极点**：分母 $z^6 = 0$，故在原点 $z = 0$ 处有 6 阶重极点。因所有极点严格在单位圆内，系统因果稳定。
2. **零点**：分子 $z^6 - 1 = 0 \\implies z^6 = 1 = e^{j 2\\pi k}$。
   解得 6 个一阶单零点为：
   $$z_k = e^{j \\frac{2\\pi k}{6}} = e^{j \\frac{\\pi k}{3}} \\quad (k = 0, 1, 2, 3, 4, 5)$$
   均匀、对称地分布在单位圆周上。
3. **滤波特性**：在 $\\omega = \\frac{k\\pi}{3}$ 陷波归零，幅频呈现梳齿状。
故正确答案为 **A**。"""
  },
  {
    "id": "ss-c5-03",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "常用因果序列Z变换对",
    "type": "single",
    "difficulty": 2,
    "tags": ["Z变换公式", "收敛域", "基础过关"],
    "source": "吴大正信号与系统课后刷题本",
    "stem": "指数序列 $f(k) = a^k \\varepsilon(k)$（$|a| < 1$）的单边 Z 变换及收敛域为：",
    "options": [
      { "key": "A", "text": "$\\frac{z}{z - a}$，收敛域 $|z| > |a|$" },
      { "key": "B", "text": "$\\frac{z}{z - a}$，收敛域 $|z| < |a|$" },
      { "key": "C", "text": "$\\frac{1}{z - a}$，收敛域 $|z| > |a|$" },
      { "key": "D", "text": "$\\frac{z}{z + a}$，收敛域 $|z| > 1$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：因果指数序列的标准 Z 变换。

由 Z 变换定义式：
$$F(z) = \\sum_{k=-\\infty}^\\infty f(k) z^{-k} = \\sum_{k=0}^\\infty a^k z^{-k} = \\sum_{k=0}^\\infty (a z^{-1})^k$$
由无穷等比级数求和公式，级数收敛的充要条件为公比 $|a z^{-1}| < 1 \\implies |z| > |a|$。
求和得：
$$F(z) = \\frac{1}{1 - a z^{-1}} = \\frac{z}{z - a}$$
收敛域为圆外区域 $|z| > |a|$。故选 **A**。"""
  },

  # ==========================================
  # 第六章：状态变量分析与梅森增益公式
  # ==========================================
  {
    "id": "ss-c6-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第六章：系统状态变量与信号流图",
    "section": "梅森增益公式",
    "type": "single",
    "difficulty": 3,
    "tags": ["梅森公式", "信号流图", "系统传递函数"],
    "source": "广工837经典真题解析",
    "stem": "应用梅森增益公式（Mason Gain Formula）计算系统的系统函数 $H(s) = \\frac{1}{\\Delta} \\sum_k P_k \\Delta_k$ 时，式中的特征多项式 $\\Delta$ 表示为：",
    "options": [
      { "key": "A", "text": "$\\Delta = 1 - \\sum L_i + \\sum L_j L_k - \\sum L_m L_n L_p + \\dots$" },
      { "key": "B", "text": "$\\Delta = 1 + \\sum L_i + \\sum L_j L_k$" },
      { "key": "C", "text": "$\\Delta = \\sum P_k$" },
      { "key": "D", "text": "$\\Delta = 1 - \\sum P_k$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：梅森增益公式基本定义。

梅森增益公式为：
$$H(s) = \\frac{\\sum_k P_k \\Delta_k}{\\Delta}$$
其中图特征式 $\\Delta$ 定义为：
$$\\Delta = 1 - \\sum L_i + \\sum L_j L_k - \\sum L_m L_n L_p + \\dots$$
- $\\sum L_i$：所有单个互不接触反馈回路增益之和；
- $\\sum L_j L_k$：所有两两不接触回路增益乘积之和；
- $\\sum L_m L_n L_p$：所有三三不接触回路增益乘积之和；
- $P_k$：第 $k$ 条前向通路增益；
- $\\Delta_k$：第 $k$ 条前向通路的余子式。
故选 **A**。"""
  },
  {
    "id": "ss-c6-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第六章：系统状态变量与信号流图",
    "section": "状态方程标准形式",
    "type": "single",
    "difficulty": 3,
    "tags": ["状态方程", "现代控制基础", "837大题"],
    "source": "广工837信号与系统考研经典题",
    "stem": "对于单输入单输出连续系统，其一阶向量状态方程和代数输出方程的标准向量形式通常表示为：",
    "options": [
      { "key": "A", "text": "$\\dot{\\mathbf{x}}(t) = \\mathbf{A}\\mathbf{x}(t) + \\mathbf{B}f(t)$，$\\quad y(t) = \\mathbf{C}\\mathbf{x}(t) + Df(t)$" },
      { "key": "B", "text": "$\\mathbf{x}(t) = \\mathbf{A}\\dot{\\mathbf{x}}(t) + \\mathbf{B}f(t)$，$\\quad y(t) = \\mathbf{C}\\mathbf{x}(t)$" },
      { "key": "C", "text": "$\\dot{\\mathbf{x}}(t) = \\mathbf{B}\\mathbf{x}(t) + \\mathbf{A}f(t)$，$\\quad y(t) = D\\mathbf{x}(t) + \\mathbf{C}f(t)$" },
      { "key": "D", "text": "$\\ddot{\\mathbf{x}}(t) = \\mathbf{A}\\mathbf{x}(t) + \\mathbf{B}f(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：状态变量分析法标准形式。

对于连续 LTI 系统：
- **状态方程（State Equation）**：
  $$\\dot{\\mathbf{x}}(t) = \\mathbf{A}\\mathbf{x}(t) + \\mathbf{B}f(t)$$
  其中 $\\mathbf{A}$ 为系统矩阵（状态矩阵），$\\mathbf{B}$ 为输入矩阵（激励矩阵）。
- **输出方程（Output Equation）**：
  $$y(t) = \\mathbf{C}\\mathbf{x}(t) + Df(t)$$
  其中 $\\mathbf{C}$ 为输出矩阵，$D$ 为前传系数。
系统的传递函数可由矩阵公式导出：
$$H(s) = \\mathbf{C}(s\\mathbf{I} - \\mathbf{A})^{-1}\\mathbf{B} + D$$
故正确答案为 **A**。"""
  },

  # ==========================================
  # 第七章：时域抽样与恢复
  # ==========================================
  {
    "id": "ss-c7-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第七章：时域抽样与恢复",
    "section": "时域相乘与频带扩展",
    "type": "single",
    "difficulty": 3,
    "tags": ["抽样定理", "频域卷积", "真题演练"],
    "source": "广工837考研题库精选题",
    "stem": "已知基带带限信号 $f(t)$ 的最高截止频率为 $f_m$。若对信号 $y(t) = f^2(t)$ 进行理想抽样，为保证频谱不发生混叠，最低抽样频率 $f_s$ 应为：",
    "options": [
      { "key": "A", "text": "$f_m$" },
      { "key": "B", "text": "$2f_m$" },
      { "key": "C", "text": "$4f_m$" },
      { "key": "D", "text": "$8f_m$" }
    ],
    "answer": "C",
    "analysis": """【核心考点】：时域相乘对应频域卷积与带宽加倍。

1. $f(t)$ 的最高截止频率为 $f_m$，频带为 $[-f_m, f_m]$；
2. 由频域卷积定理：
   $$y(t) = f(t) \\cdot f(t) \\stackrel{\\mathcal{F}}{\\longleftrightarrow} \\frac{1}{2\\pi} [F(j\\omega) * F(j\\omega)]$$
   两个宽度为 $2f_m$ 的频带进行卷积后，所得卷积信号的频宽为两频带之和，最高频率扩展为：
   $$f_{y\\max} = f_m + f_m = 2f_m$$
3. 根据奈奎斯特抽样定理，最低抽样频率为：
   $$f_s \\ge 2 f_{y\\max} = 2 \\times (2f_m) = 4f_m$$
故选 **C**。"""
  },
  {
    "id": "ss-c7-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第七章：时域抽样与恢复",
    "section": "双频相加信号的抽样频率",
    "type": "single",
    "difficulty": 2,
    "tags": ["2014年837真题", "抽样定理", "尺度变换"],
    "source": "广东工业大学2014年837真题填空题",
    "stem": "已知带限信号 $f(t)$ 的最高频率为 $100\\text{ Hz}$。若对信号 $x(t) = f(t) + f(3t)$ 进行理想抽样，则使频谱不发生混叠的最小取样频率为：",
    "options": [
      { "key": "A", "text": "200 Hz" },
      { "key": "B", "text": "300 Hz" },
      { "key": "C", "text": "600 Hz" },
      { "key": "D", "text": "400 Hz" }
    ],
    "answer": "C",
    "analysis": """【核心考点】：时域压缩频域扩展与线性相加系统的最高频率。

1. **时域展缩性质**：
   $f(t)$ 的最高截止频率为 $f_{m1} = 100\\text{ Hz}$；
   $f(3t)$ 时域压缩为原来的 $\\frac{1}{3}$，频域展宽为原来的 3 倍：
   $$f_{m2} = 3 \\times 100 = 300\\text{ Hz}$$
2. **两信号线性相加**：
   $x(t) = f(t) + f(3t)$ 的频谱是两者频谱直接相加，其总最高频率取决于两者中的最大值：
   $$f_{x\\max} = \\max(f_{m1}, f_{m2}) = \\max(100, 300) = 300\\text{ Hz}$$
3. **根据奈奎斯特抽样定理**：
   $$f_s \\ge 2 f_{x\\max} = 2 \\times 300 = 600\\text{ Hz}$$
故最小取样频率为 **600 Hz**。选 **C**。"""
  },
  {
    "id": "ss-c7-03",
    "subject": "广工837/809-信号与系统",
    "chapter": "第七章：时域抽样与恢复",
    "section": "抽样信号的理想低通恢复",
    "type": "single",
    "difficulty": 3,
    "tags": ["信号重建", "Sinc插值", "抽样定理"],
    "source": "奥本海姆第7章经典考题",
    "stem": "以采样间隔 $T_s$ 对带限信号 $f(t)$（最高角频率为 $\\omega_m$）进行理想冲激抽样，满足 $\\omega_s \\ge 2\\omega_m$。要从抽样信号 $f_s(t)$ 中无失真恢复原信号 $f(t)$，所通过的理想低通滤波器的增益和截止频率应为：",
    "options": [
      { "key": "A", "text": "增益为 $T_s$，截止频率满足 $\\omega_m \\le \\omega_c \\le \\omega_s - \\omega_m$" },
      { "key": "B", "text": "增益为 $1$，截止频率为 $\\omega_s$" },
      { "key": "C", "text": "增益为 $\\frac{1}{T_s}$，截止频率为 $\\omega_m$" },
      { "key": "D", "text": "增益为 $2T_s$，截止频率为 $2\\omega_m$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：从理想抽样信号恢复原连续信号的滤波参数。

1. **抽样频谱特征**：
   $$F_s(j\\omega) = \\frac{1}{T_s} \\sum_{n=-\\infty}^\\infty F(j(\\omega - n\\omega_s))$$
   频谱是以 $\\omega_s$ 为周期的周期延拓，基带分量高度为 $\\frac{1}{T_s} F(j\\omega)$。
2. **恢复滤波器参数设计**：
   - 为将幅度 $\\frac{1}{T_s}$ 还原为原信号幅度 1，理想低通滤波器的通带增益必须为：
     $$H_0 = T_s$$
   - 为滤除高频周期延拓分量并完整保留基带，截止频率必须位于基带最高频率与第一镜像分量最低频率之间：
     $$\\omega_m \\le \\omega_c \\le \\omega_s - \\omega_m$$
故正确答案为 **A**。"""
  }
]

# Write to TypeScript file
ts_content = "import { Question } from '../types';\n\n"
ts_content += "export const signalsAndSystemsQuestions: Question[] = "
ts_content += json.dumps(questions, ensure_ascii=False, indent=2) + ";\n"

with open('src/data/signalsQuestions.ts', 'w', encoding='utf-8') as f:
    f.write(ts_content)

print(f"Generated {len(questions)} pure Signals & Systems questions into src/data/signalsQuestions.ts")

# Write initialQuestions.ts with ONLY signalsAndSystemsQuestions (NO other majors!)
init_content = """import { Question } from '../types';
import { signalsAndSystemsQuestions } from './signalsQuestions';

// 专业课题库：专属聚焦【广工837/809 · 信号与系统】完整考研与期末知识库
export const initialQuestions: Question[] = signalsAndSystemsQuestions;
"""

with open('src/data/initialQuestions.ts', 'w', encoding='utf-8') as f:
    f.write(init_content)

print("Updated src/data/initialQuestions.ts to contain ONLY signals & systems questions.")
