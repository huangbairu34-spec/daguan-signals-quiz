import json

# Load existing questions
with open('generate_all_signals_questions.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect how many questions are in generate_all_signals_questions.py right now
from generate_all_signals_questions import questions

print("Current questions count:", len(questions))

more_questions = [
  # --- 第一章 补全 ---
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

  # --- 第二章 补全 ---
  {
    "id": "ss-c2-06",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "时域积分性求零状态响应",
    "type": "single",
    "difficulty": 3,
    "tags": ["2018年837真题", "时域积分", "斜坡响应"],
    "source": "广东工业大学2018年837全国统考真题第2题",
    "stem": "已知某 LTI 连续系统当输入阶跃信号 $f(t) = \\varepsilon(t)$ 时，系统的零状态响应为 $y_{zs}(t) = e^{-2t}\\varepsilon(t)$。若输入改为斜坡信号 $f_2(t) = t\\varepsilon(t)$，则系统的零状态响应为：",
    "options": [
      { "key": "A", "text": "$\\frac{1}{2}(1 - e^{-2t})\\varepsilon(t)$" },
      { "key": "B", "text": "$2(1 - e^{-2t})\\varepsilon(t)$" },
      { "key": "C", "text": "$-2e^{-2t}\\varepsilon(t)$" },
      { "key": "D", "text": "$t e^{-2t}\\varepsilon(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：LTI 系统的时域微分与积分特性。

1. **观察输入信号关系**：
   $$f_2(t) = t\\varepsilon(t) = \\int_{-\\infty}^t \\varepsilon(\\tau) d\\tau$$
   即新输入信号是原输入信号的时域积分。
2. **利用时不变与积分性质**：
   由 LTI 系统特性，若 $f(t) \\to y_{zs}(t)$，则：
   $$\\int_{-\\infty}^t f(\\tau)d\\tau \\longrightarrow \\int_{-\\infty}^t y_{zs}(\\tau)d\\tau$$
3. **计算输出响应**：
   对于 $t > 0$：
   $$y_{zs2}(t) = \\int_0^t e^{-2\\tau} d\\tau = \\left[ -\\frac{1}{2} e^{-2\\tau} \\right]_0^t = -\\frac{1}{2} e^{-2t} - \\left(-\\frac{1}{2}\\right) = \\frac{1}{2}(1 - e^{-2t})$$
4. 综合因果形式：$y_{zs2}(t) = \\frac{1}{2}(1 - e^{-2t})\\varepsilon(t)$。
故正确答案为 **A**。"""
  },

  # --- 第三章 补全 ---
  {
    "id": "ss-c3-07",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "常用符号函数傅里叶变换",
    "type": "single",
    "difficulty": 2,
    "tags": ["符号函数", "常用变换对", "基础题"],
    "source": "广东工业大学2017年837真题",
    "stem": "符号函数 $f(t) = \\text{sgn}(t)$ 的傅里叶变换 $F(j\\omega)$ 为：",
    "options": [
      { "key": "A", "text": "$\\frac{2}{j\\omega}$" },
      { "key": "B", "text": "$\\frac{1}{j\\omega}$" },
      { "key": "C", "text": "$\\pi \\delta(\\omega)$" },
      { "key": "D", "text": "$\\frac{2}{\\omega}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：符号函数 $\\text{sgn}(t)$ 的傅里叶变换。

1. 符号函数可以看作双边对称指数衰减信号的极限：
   $$\\text{sgn}(t) = \\lim_{\\alpha \\to 0^+} [e^{-\\alpha t}\\varepsilon(t) - e^{\\alpha t}\\varepsilon(-t)]$$
2. 求傅氏变换：
   $$\\mathcal{F}[e^{-\\alpha t}\\varepsilon(t)] = \\frac{1}{\\alpha + j\\omega}, \\quad \\mathcal{F}[-e^{\\alpha t}\\varepsilon(-t)] = -\\frac{1}{\\alpha - j\\omega}$$
   $$F_\\alpha(j\\omega) = \\frac{1}{\\alpha + j\\omega} - \\frac{1}{\\alpha - j\\omega} = \\frac{-2j\\omega}{\\alpha^2 + \\omega^2}$$
3. 取极限 $\\alpha \\to 0^+$：
   $$F(j\\omega) = \\frac{-2j\\omega}{\\omega^2} = \\frac{-2j}{\\omega} = \\frac{2}{j\\omega}$$
故正确答案为 **A**。"""
  },
  {
    "id": "ss-c3-08",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "单位阶跃函数傅氏变换",
    "type": "single",
    "difficulty": 2,
    "tags": ["2016年837真题", "阶跃函数", "高频基础"],
    "source": "广东工业大学2016年837全国统考真题第3题",
    "stem": "单位阶跃信号 $\\varepsilon(t)$ 的傅里叶变换为：",
    "options": [
      { "key": "A", "text": "$\\frac{1}{j\\omega} + \\pi \\delta(\\omega)$" },
      { "key": "B", "text": "$\\frac{1}{j\\omega}$" },
      { "key": "C", "text": "$\\pi \\delta(\\omega)$" },
      { "key": "D", "text": "$\\frac{1}{\\omega} + \\pi \\delta(\\omega)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：单位阶跃信号 $\\varepsilon(t)$ 的奇异傅氏变换。

1. 阶跃信号可分解为直流分量与奇对称符号函数之和：
   $$\\varepsilon(t) = \\frac{1}{2} + \\frac{1}{2}\\text{sgn}(t)$$
2. 分别求傅里叶变换：
   - 直流常数 $\\frac{1}{2} \\stackrel{\\mathcal{F}}{\\longleftrightarrow} \\pi \\delta(\\omega)$；
   - 符号函数 $\\frac{1}{2}\\text{sgn}(t) \\stackrel{\\mathcal{F}}{\\longleftrightarrow} \\frac{1}{2} \\cdot \\frac{2}{j\\omega} = \\frac{1}{j\\omega}$；
3. 线性叠加得：
   $$\\varepsilon(t) \\stackrel{\\mathcal{F}}{\\longleftrightarrow} \\frac{1}{j\\omega} + \\pi \\delta(\\omega)$$
故选 **A**。"""
  },

  # --- 第四章 补全 ---
  {
    "id": "ss-c4-05",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "连续系统滤波器类型判定",
    "type": "single",
    "difficulty": 3,
    "tags": ["2025年809真题", "低通滤波器", "频响分析"],
    "source": "广东工业大学2025年809真题第14题",
    "stem": "已知某连续因果系统的系统函数为 $H(s) = \\frac{e^{-3s}}{s + 3}$，则该系统属于下列哪种滤波器类型：",
    "options": [
      { "key": "A", "text": "低通滤波器（Low-Pass）" },
      { "key": "B", "text": "高通滤波器（High-Pass）" },
      { "key": "C", "text": "带通滤波器（Band-Pass）" },
      { "key": "D", "text": "带阻滤波器（Band-Stop）" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：连续系统函数幅频响应与滤波器分类判定。

1. 系统包含一个负实轴极点 $s = -3$（位于左半开平面，因果稳定）；
2. 频响函数为：
   $$H(j\\omega) = \\left. H(s) \\right|_{s = j\\omega} = \\frac{e^{-j 3\\omega}}{j\\omega + 3}$$
3. 计算幅频响应 $|H(j\\omega)|$：
   由于 $|e^{-j 3\\omega}| = 1$（纯时延不改变幅度），因此：
   $$|H(j\\omega)| = \\frac{1}{|j\\omega + 3|} = \\frac{1}{\\sqrt{\\omega^2 + 9}}$$
4. 观察幅频随频率的变化趋势：
   - 直流分量 $\\omega = 0$ 处：$|H(0)| = \\frac{1}{3}$（最大增益）；
   - 随角频率 $\\omega$ 增大，分母单调递增，幅值单调递减趋向于 0；
   - 当 $\\omega \\to \\infty$ 时：$|H(j\\infty)| = 0$。
因此该系统允许低频信号通过，衰减高频分量，属于标准的**低通滤波器**。选 **A**。"""
  },

  # --- 第五章 补全 ---
  {
    "id": "ss-c5-04",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "交替序列Z变换",
    "type": "single",
    "difficulty": 2,
    "tags": ["2019年837真题", "Z变换对", "交替符号"],
    "source": "广东工业大学2019年837全国统考真题",
    "stem": "交变阶跃序列 $f(k) = (-1)^k \\varepsilon(k)$ 的单边 Z 变换及收敛域为：",
    "options": [
      { "key": "A", "text": "$\\frac{z}{z + 1}$，收敛域 $|z| > 1$" },
      { "key": "B", "text": "$\\frac{z}{z - 1}$，收敛域 $|z| > 1$" },
      { "key": "C", "text": "$\\frac{1}{z + 1}$，收敛域 $|z| > 1$" },
      { "key": "D", "text": "$\\frac{z}{z + 1}$，收敛域 $|z| < 1$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：指数序列 Z 变换基本公式。

1. 由标准因果序列 Z 变换对：
   $$a^k \\varepsilon(k) \\stackrel{\\mathcal{Z}}{\\longleftrightarrow} \\frac{z}{z - a} \\quad (|z| > |a|)$$
2. 令 $a = -1$，代入可得：
   $$(-1)^k \\varepsilon(k) \\stackrel{\\mathcal{Z}}{\\longleftrightarrow} \\frac{z}{z - (-1)} = \\frac{z}{z + 1}$$
   收敛域为：$|z| > |-1| = 1$。
故正确答案为 **A**。"""
  },
  {
    "id": "ss-c5-05",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "二阶差分方程系统函数与稳定性",
    "type": "single",
    "difficulty": 3,
    "tags": ["2025年809真题", "差分方程", "离散极点分析"],
    "source": "广东工业大学2025年809真题大题第2题",
    "stem": "已知某因果离散 LTI 系统的差分方程为 $y(n) - 0.3y(n - 1) - 0.4y(n - 2) = x(n - 1)$，则该系统的系统函数 $H(z)$ 与稳定性结论为：",
    "options": [
      { "key": "A", "text": "$H(z) = \\frac{z}{(z - 0.8)(z + 0.5)}$，系统极点在单位圆内，系统因果稳定" },
      { "key": "B", "text": "$H(z) = \\frac{z}{(z - 0.8)(z + 0.5)}$，系统不稳定" },
      { "key": "C", "text": "$H(z) = \\frac{z^2}{(z - 0.4)(z + 1)}$，系统临界稳定" },
      { "key": "D", "text": "$H(z) = \\frac{1}{z^2 - 0.3z - 0.4}$，系统非因果" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散时不变系统的差分方程 Z 域求解与极点稳定性判定。

1. **两边取 Z 变换**（设初始状态为零）：
   $$Y(z) - 0.3 z^{-1}Y(z) - 0.4 z^{-2}Y(z) = z^{-1}X(z)$$
   $$Y(z)(1 - 0.3 z^{-1} - 0.4 z^{-2}) = z^{-1}X(z)$$
2. **求解系统函数 $H(z)$**：
   $$H(z) = \\frac{Y(z)}{X(z)} = \\frac{z^{-1}}{1 - 0.3 z^{-1} - 0.4 z^{-2}} = \\frac{z}{z^2 - 0.3z - 0.4}$$
3. **因式分解分母多项式求极点**：
   $$z^2 - 0.3z - 0.4 = (z - 0.8)(z + 0.5) = 0$$
   解得系统两极点为：
   $$z_1 = 0.8, \\quad z_2 = -0.5$$
4. **稳定性判定**：
   极点模值分别为 $|z_1| = 0.8 < 1$，$|z_2| = |-0.5| = 0.5 < 1$。
   所有极点严格位于单位圆内，对于因果系统，其收敛域为 $|z| > 0.8$，自然包含单位圆 $|z| = 1$。
因此该系统**因果稳定**。选 **A**。"""
  }
]

# Append more questions
all_questions = questions + more_questions

# Write out
ts_content = "import { Question } from '../types';\n\n"
ts_content += "export const signalsAndSystemsQuestions: Question[] = "
ts_content += json.dumps(all_questions, ensure_ascii=False, indent=2) + ";\n"

with open('src/data/signalsQuestions.ts', 'w', encoding='utf-8') as f:
    f.write(ts_content)

print(f"Total pure Signals & Systems questions now: {len(all_questions)}")
