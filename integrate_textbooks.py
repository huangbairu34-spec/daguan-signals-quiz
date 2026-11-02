# -*- coding: utf-8 -*-
"""
Integrate Zheng Junli and Oppenheim textbook question drill collections
into the Signals and Systems question database.
"""

import json
import os

textbook_questions = [
  # ==========================================
  # 第一章：信号与系统基础 (新增 5 题)
  # ==========================================
  {
    "id": "ss-c1-zjl-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "信号奇偶分量分解",
    "type": "single",
    "difficulty": 2,
    "tags": ["郑君里考研题", "教材核心考点", "奇偶分量"],
    "source": "郑君里《信号与系统》(第3版)课后习题1.8",
    "stem": "设单边指数信号 $f(t) = e^{-2t}\\varepsilon(t)$，将其分解为偶分量 $f_e(t)$ 和奇分量 $f_o(t)$，则其奇分量 $f_o(t)$ 的闭式解析表达式为：",
    "options": [
      { "key": "A", "text": "$\\frac{1}{2}[e^{-2t}\\varepsilon(t) - e^{2t}\\varepsilon(-t)]$" },
      { "key": "B", "text": "$\\frac{1}{2}[e^{-2t}\\varepsilon(t) + e^{2t}\\varepsilon(-t)]$" },
      { "key": "C", "text": "$e^{-2t}\\text{sgn}(t)$" },
      { "key": "D", "text": "$\\frac{1}{2}e^{-2|t|}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：任意连续时间信号的奇偶分量分解法则。

1. **基本分解公式**：
   任何连续信号 $f(t)$ 均可唯一分解为偶分量 $f_e(t)$ 与奇分量 $f_o(t)$ 之和：
   $$f(t) = f_e(t) + f_o(t)$$
   其中：
   $$f_e(t) = \\frac{1}{2}[f(t) + f(-t)]$$
   $$f_o(t) = \\frac{1}{2}[f(t) - f(-t)]$$
2. **计算 $f(-t)$**：
   将 $t$ 替换为 $-t$：
   $$f(-t) = e^{-2(-t)}\\varepsilon(-t) = e^{2t}\\varepsilon(-t)$$
3. **求奇分量 $f_o(t)$**：
   $$f_o(t) = \\frac{1}{2}[f(t) - f(-t)] = \\frac{1}{2}[e^{-2t}\\varepsilon(t) - e^{2t}\\varepsilon(-t)]$$
4. 该奇分量亦可紧凑表示为 $\\frac{1}{2}e^{-2|t|}\\text{sgn}(t)$。
故选 **A**。"""
  },
  {
    "id": "ss-c1-zjl-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "时域自变量变换顺序辨析",
    "type": "single",
    "difficulty": 3,
    "tags": ["郑君里考研题", "自变量变换", "易错考点"],
    "source": "郑君里《信号与系统》(第3版)课后习题1.5",
    "stem": "已知时域波形 $f(t)$，欲由 $f(t)$ 通过平移和尺度反折变换获得波形 $f(t_0 - at)$（其中常数 $a > 0, t_0 > 0$）。若选择“先平移、后反折与展缩”的操作流程，正确的变换顺序是：",
    "options": [
      { "key": "A", "text": "先将 $f(t)$ 左移 $t_0$ 得到 $f(t + t_0)$，再将自变量 $t$ 替换为 $-at$" },
      { "key": "B", "text": "先将 $f(t)$ 右移 $t_0$ 得到 $f(t - t_0)$，再将自变量 $t$ 替换为 $-at$" },
      { "key": "C", "text": "先将 $f(t)$ 右移 $\\frac{t_0}{a}$，再将自变量 $t$ 替换为 $-at$" },
      { "key": "D", "text": "先将 $f(t)$ 左移 $\\frac{t_0}{a}$，再将自变量 $t$ 替换为 $-at$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：信号时域平移与尺度反折的自变量运算律（只对 $t$ 变换原则）。

1. **核心原则**：“只对时间自变量 $t$ 本身进行代换”。
2. **分析步骤**：
   - 第一步（平移）：将 $f(t)$ 沿时间轴**向左平移 $t_0$**，得到：
     $$f_1(t) = f(t + t_0)$$
   - 第二步（展缩与反折）：将自变量 $t$ 替换为 $-at$，直接得到：
     $$f_1(-at) = f(-at + t_0) = f(t_0 - at)$$
3. **常见误区警示**：
   - 若误将 $f(t)$ 先右移 $t_0$ 得到 $f(t - t_0)$，再将 $t$ 替换为 $-at$，将得到 $f(-at - t_0) \\ne f(t_0 - at)$，符号错误！
   - 若采用“先展缩反折、后平移”：先将 $f(t)$ 变为 $f(-at)$，再将 $t$ 整体右移 $\\frac{t_0}{a}$，替换 $t \\to t - \\frac{t_0}{a}$，得到 $f(-a(t - \\frac{t_0}{a})) = f(-at + t_0)$。
故选 **A**。"""
  },
  {
    "id": "ss-c1-obh-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "离散指数衰减序列能量计算",
    "type": "single",
    "difficulty": 2,
    "tags": ["奥本海姆经典", "离散能量", "无穷级数"],
    "source": "奥本海姆《信号与系统》(第2版)课后习题1.3(d)",
    "stem": "离散单边指数序列 $x[n] = \\left(\\frac{1}{2}\\right)^n u[n]$ 的总能量 $E$ 与平均功率 $P$ 分别为：",
    "options": [
      { "key": "A", "text": "$E = \\frac{4}{3}\\text{ J}, \\, P = 0\\text{ W}$" },
      { "key": "B", "text": "$E = 2\\text{ J}, \\, P = 0\\text{ W}$" },
      { "key": "C", "text": "$E = \\frac{4}{3}\\text{ J}, \\, P = \\frac{2}{3}\\text{ W}$" },
      { "key": "D", "text": "$E = \\infty, \\, P = 0\\text{ W}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散时间序列的总能量级数定义。

1. 离散信号总能量定义公式：
   $$E = \\sum_{n=-\\infty}^\\infty |x[n]|^2$$
2. 将 $x[n] = (\\frac{1}{2})^n u[n]$ 代入公式：
   $$E = \\sum_{n=0}^\\infty \\left[\\left(\\frac{1}{2}\\right)^n\\right]^2 = \\sum_{n=0}^\\infty \\left(\\frac{1}{4}\\right)^n$$
3. 这是一个公比 $q = \\frac{1}{4} < 1$ 的首项为 1 的无穷递缩等比级数：
   $$E = \\frac{1}{1 - \\frac{1}{4}} = \\frac{1}{\\frac{3}{4}} = \\frac{4}{3}\\text{ J}$$
4. 由于总能量 $0 < E < \\infty$ 为有限正值，该序列为典型**离散能量信号**，其在全时域的平均功率恒为 **0**。
选 **A**。"""
  },
  {
    "id": "ss-c1-obh-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "奇偶分量能量正交性",
    "type": "single",
    "difficulty": 3,
    "tags": ["奥本海姆经典", "能量正交", "经典定理"],
    "source": "奥本海姆《信号与系统》(第2版)课后习题1.7",
    "stem": "任意实值能量信号 $x(t)$ 的奇偶分量分别表示为 $x_e(t)$ 和 $x_o(t)$。根据正交性，信号的总能量 $E_x$ 与两分量能量 $E_{xe}, E_{xo}$ 的定量关系为：",
    "options": [
      { "key": "A", "text": "$E_x = E_{xe} + E_{xo}$" },
      { "key": "B", "text": "$E_x = E_{xe} - E_{xo}$" },
      { "key": "C", "text": "$E_x = 2(E_{xe} + E_{xo})$" },
      { "key": "D", "text": "$E_x = \\sqrt{E_{xe}^2 + E_{xo}^2}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：实信号奇偶分解的能量正交守恒性。

1. 信号与其奇偶分量的关系：$x(t) = x_e(t) + x_o(t)$；
2. 计算总能量：
   $$E_x = \\int_{-\\infty}^\\infty [x_e(t) + x_o(t)]^2 dt = \\int_{-\\infty}^\\infty x_e^2(t)dt + \\int_{-\\infty}^\\infty x_o^2(t)dt + 2\\int_{-\\infty}^\\infty x_e(t)x_o(t)dt$$
3. 考察交叉互乘积项：
   因为 $x_e(t)$ 是偶函数，$x_o(t)$ 是奇函数，两者的乘积 $x_e(t)x_o(t)$ 必定是**纯奇函数**；
   奇函数在关于原点对称的区间 $[-\\infty, +\\infty]$ 上的积分为零：
   $$\\int_{-\\infty}^\\infty x_e(t)x_o(t)dt = 0$$
4. 因此交叉项为 0，能量直接代数相加：
   $$E_x = E_{xe} + E_{xo}$$
故选 **A**。"""
  },
  {
    "id": "ss-c1-obh-03",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "离散系统记忆性与因果性判断",
    "type": "single",
    "difficulty": 2,
    "tags": ["奥本海姆经典", "五大特性", "记忆系统"],
    "source": "奥本海姆《信号与系统》(第2版)课后习题1.16",
    "stem": "离散系统输入输出方程为 $y[n] = 2 x[n] + \\frac{1}{x[n - 1]}$，则该系统属于：",
    "options": [
      { "key": "A", "text": "有记忆、非线性、因果系统" },
      { "key": "B", "text": "无记忆、线性、因果系统" },
      { "key": "C", "text": "有记忆、线性、非因果系统" },
      { "key": "D", "text": "无记忆、非线性、非因果系统" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散系统记忆性、因果性与线性的定义逐项检验。

1. **记忆性（Memory）**：
   在时刻 $n$，输出 $y[n]$ 包含了 $x[n-1]$（依赖过去的输入值），因此系统**具有记忆（有记忆系统）**；
2. **因果性（Causality）**：
   输出 $y[n]$ 仅取决于当前时刻 $n$ 和过去时刻 $n - 1$ 的输入，完全不依赖未来时刻（如 $n + 1$）的输入，因此为**因果系统**；
3. **线性（Linearity）**：
   方程第二项 $\\frac{1}{x[n-1]}$ 中输入信号出现在分母上，违背齐次性 $T[a x] \\ne a T[x]$，因此为**非线性系统**。
综上，该系统是有记忆、非线性、因果系统。选 **A**。"""
  },

  # ==========================================
  # 第二章：系统的时域分析 (新增 4 题)
  # ==========================================
  {
    "id": "ss-c2-obh-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "时移因果指数时域卷积积分",
    "type": "single",
    "difficulty": 3,
    "tags": ["奥本海姆经典", "连续卷积", "分段积分"],
    "source": "奥本海姆《信号与系统》(第2版)课后习题2.21",
    "stem": "计算连续时间卷积积分 $y(t) = [e^{-2t}u(t)] * u(t - 2)$ 的闭式解析表达式为：",
    "options": [
      { "key": "A", "text": "$\\frac{1}{2}[1 - e^{-2(t - 2)}]u(t - 2)$" },
      { "key": "B", "text": "$\\frac{1}{2}[1 - e^{-2t}]u(t - 2)$" },
      { "key": "C", "text": "$[1 - e^{-2(t - 2)}]u(t - 2)$" },
      { "key": "D", "text": "$\\frac{1}{2}[1 - e^{-2(t - 2)}]u(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：时移阶跃信号的卷积积分与时不变平移性质。

1. **法一：先算基准卷积再时移**：
   - 设 $y_0(t) = [e^{-2t}u(t)] * u(t)$；
   - 信号与阶跃卷积即对信号进行时域积分：
     $$y_0(t) = \\int_0^t e^{-2\\tau}d\\tau = \\left[ -\\frac{1}{2}e^{-2\\tau} \\right]_0^t = \\frac{1}{2}(1 - e^{-2t})u(t)$$
   - 第二个信号为时移信号 $u(t - 2)$，时延 $t_0 = 2$；
   - 由时不变系统的时移性质：
     $$y(t) = y_0(t - 2) = \\frac{1}{2}[1 - e^{-2(t - 2)}]u(t - 2)$$
2. 验证分段：当 $t < 2$ 时两波形无重叠，$y(t) = 0$；当 $t \\ge 2$ 时波形平滑建立。
选 **A**。"""
  },
  {
    "id": "ss-c2-obh-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "离散衰减指数与阶跃卷积和",
    "type": "single",
    "difficulty": 2,
    "tags": ["奥本海姆经典", "离散卷积", "等比求和"],
    "source": "奥本海姆《信号与系统》(第2版)课后习题2.22",
    "stem": "计算离散序列卷积和 $y[n] = \\left(\\frac{1}{3}\\right)^n u[n] * u[n]$ 的闭式表达式为：",
    "options": [
      { "key": "A", "text": "$\\frac{3}{2}\\left[1 - \\left(\\frac{1}{3}\\right)^{n+1}\\right]u[n]$" },
      { "key": "B", "text": "$\\frac{3}{2}\\left[1 - \\left(\\frac{1}{3}\\right)^n\\right]u[n]$" },
      { "key": "C", "text": "$3\\left[1 - \\left(\\frac{1}{3}\\right)^{n+1}\\right]u[n]$" },
      { "key": "D", "text": "$\\left[1 - \\left(\\frac{1}{3}\\right)^{n+1}\\right]u[n]$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：单边离散指数序列与阶跃序列的卷积和计算。

1. 离散卷积和定义：
   $$y[n] = \\sum_{k=-\\infty}^\\infty x[k] h[n - k] = \\sum_{k=0}^n \\left(\\frac{1}{3}\\right)^k \\cdot 1 \\quad (n \\ge 0)$$
2. 利用有限项等比级数求和公式（共 $n + 1$ 项）：
   $$S = \\sum_{k=0}^n q^k = \\frac{1 - q^{n+1}}{1 - q}$$
3. 代入公比 $q = \\frac{1}{3}$：
   $$y[n] = \\frac{1 - (\\frac{1}{3})^{n+1}}{1 - \\frac{1}{3}} = \\frac{1 - (\\frac{1}{3})^{n+1}}{\\frac{2}{3}} = \\frac{3}{2}\\left[ 1 - \\left(\\frac{1}{3}\\right)^{n+1} \\right]u[n]$$
选 **A**。"""
  },
  {
    "id": "ss-c2-zjl-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "微分方程二阶重根零输入响应",
    "type": "single",
    "difficulty": 3,
    "tags": ["郑君里考研题", "特征重根", "零输入响应"],
    "source": "郑君里《信号与系统》(第3版)课后习题2.6",
    "stem": "某连续系统微分方程为 $y''(t) + 4y'(t) + 4y(t) = f(t)$，已知初始状态为 $y(0_-) = 1, y'(0_-) = 1$。则该系统的零输入响应 $y_{zi}(t)\\,(t \\ge 0)$ 为：",
    "options": [
      { "key": "A", "text": "$(1 + 3t)e^{-2t}\\varepsilon(t)$" },
      { "key": "B", "text": "$(1 + t)e^{-2t}\\varepsilon(t)$" },
      { "key": "C", "text": "$(1 - 2t)e^{-2t}\\varepsilon(t)$" },
      { "key": "D", "text": "$e^{-2t}\\varepsilon(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：常系数微分方程特征二重根时的零输入响应时域古典解法。

1. **写出特征方程并求根**：
   $$\\lambda^2 + 4\\lambda + 4 = (\\lambda + 2)^2 = 0 \\implies \\lambda_1 = \\lambda_2 = -2$$
   特征根为实二重根；
2. **写出通解形式**：
   $$y_{zi}(t) = (C_1 + C_2 t)e^{-2t}$$
3. **利用 $0_-$ 初始状态定系数**（零输入响应在 $t = 0$ 处连续无跃变）：
   - $y_{zi}(0) = C_1 = 1$；
   - 求导：$y_{zi}'(t) = C_2 e^{-2t} - 2(C_1 + C_2 t)e^{-2t}$；
   - 代入 $t = 0$：$y_{zi}'(0) = C_2 - 2C_1 = 1 \\implies C_2 - 2(1) = 1 \\implies C_2 = 3$；
4. 综合得到：
   $$y_{zi}(t) = (1 + 3t)e^{-2t}\\varepsilon(t)$$
选 **A**。"""
  },
  {
    "id": "ss-c2-zjl-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "阶跃响应与冲激响应导数关联",
    "type": "single",
    "difficulty": 2,
    "tags": ["郑君里考研题", "阶跃响应", "冲激响应"],
    "source": "郑君里《信号与系统》(第3版)课后习题2.12",
    "stem": "已知某因果 LTI 系统的阶跃响应为 $g(t) = [2 - 3e^{-t} + e^{-2t}]\\varepsilon(t)$，则系统的单位冲激响应 $h(t)$ 为：",
    "options": [
      { "key": "A", "text": "$[3e^{-t} - 2e^{-2t}]\\varepsilon(t)$" },
      { "key": "B", "text": "$[3e^{-t} - 2e^{-2t}]\\varepsilon(t) + \\delta(t)$" },
      { "key": "C", "text": "$[-3e^{-t} + 2e^{-2t}]\\varepsilon(t)$" },
      { "key": "D", "text": "$[2 - 3e^{-t}]\\varepsilon(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：阶跃响应求导得到冲激响应及跃变点 $\\delta(t)$ 项判别。

1. 连续 LTI 系统冲激响应是阶跃响应的一阶广义导数：
   $$h(t) = \\frac{dg(t)}{dt} = g'(t)\\varepsilon(t) + g(0_+)\\delta(t)$$
2. 检验阶跃响应在 $t = 0_+$ 处的初始值：
   $$g(0_+) = 2 - 3e^0 + e^0 = 2 - 3 + 1 = 0$$
   由于 $g(0_+) = 0$，阶跃响应在原点处**连续、无阶跃突跳**，因此不激发出 $\\delta(t)$ 冲激项！
3. 对平滑段直接求常规导数：
   $$g'(t) = \\frac{d}{dt}[2 - 3e^{-t} + e^{-2t}] = 3e^{-t} - 2e^{-2t}$$
4. 综合得到：
   $$h(t) = [3e^{-t} - 2e^{-2t}]\\varepsilon(t)$$
选 **A**。"""
  },

  # ==========================================
  # 第三章：频域分析与傅里叶变换 (新增 4 题)
  # ==========================================
  {
    "id": "ss-c3-obh-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "周期对称方波傅氏级数系数",
    "type": "single",
    "difficulty": 2,
    "tags": ["奥本海姆经典", "傅里叶级数", "指数形式"],
    "source": "奥本海姆《信号与系统》(第2版)课后习题3.22",
    "stem": "周期为 $T$、基波角频率 $\\omega_0 = \\frac{2\\pi}{T}$ 的周期矩形脉冲信号，在单个周期内定义为：当 $|t| \\le T_1$（其中 $T_1 < \\frac{T}{2}$）时 $f(t) = 1$，其余时间为 0。则其指数形式傅里叶级数系数 $a_k$ 为：",
    "options": [
      { "key": "A", "text": "$\\frac{\\sin(k\\omega_0 T_1)}{k\\pi}$（当 $k \\ne 0$ 时）" },
      { "key": "B", "text": "$\\frac{\\cos(k\\omega_0 T_1)}{k\\pi}$" },
      { "key": "C", "text": "$\\frac{2\\sin(k\\omega_0 T_1)}{T}$" },
      { "key": "D", "text": "$\\frac{\\sin(k\\pi)}{k\\omega_0}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：周期矩形脉冲的复指数傅氏级数系数推导。

1. 指数傅氏级数系数定义公式：
   $$a_k = \\frac{1}{T}\\int_{-T/2}^{T/2} f(t)e^{-jk\\omega_0 t}dt$$
2. 将非零区间 $[-T_1, T_1]$ 代入积分：
   $$a_k = \\frac{1}{T}\\int_{-T_1}^{T_1} e^{-jk\\omega_0 t}dt = \\frac{1}{T} \\left[ -\\frac{1}{jk\\omega_0} e^{-jk\\omega_0 t} \\right]_{-T_1}^{T_1}$$
3. 利用欧拉公式化简：
   $$a_k = \\frac{1}{T} \\cdot \\frac{e^{jk\\omega_0 T_1} - e^{-jk\\omega_0 T_1}}{jk\\omega_0} = \\frac{2j\\sin(k\\omega_0 T_1)}{jk\\omega_0 T} = \\frac{2\\sin(k\\omega_0 T_1)}{k\\omega_0 T}$$
4. 将 $\\omega_0 T = 2\\pi$ 代入分母：
   $$a_k = \\frac{2\\sin(k\\omega_0 T_1)}{k(2\\pi)} = \\frac{\\sin(k\\omega_0 T_1)}{k\\pi} = \\frac{2T_1}{T}\\text{Sa}(k\\omega_0 T_1)$$
故选 **A**。"""
  },
  {
    "id": "ss-c3-obh-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "双边实指数信号傅里叶变换",
    "type": "single",
    "difficulty": 2,
    "tags": ["奥本海姆经典", "实偶信号", "常用变换对"],
    "source": "奥本海姆《信号与系统》(第2版)课后习题4.21",
    "stem": "计算双边对称实指数信号 $f(t) = e^{-a|t|}\\,(a > 0)$ 的傅里叶变换 $F(j\\omega)$ 为：",
    "options": [
      { "key": "A", "text": "$\\frac{2a}{a^2 + \\omega^2}$" },
      { "key": "B", "text": "$\\frac{2}{a + j\\omega}$" },
      { "key": "C", "text": "$\\frac{a}{a^2 + \\omega^2}$" },
      { "key": "D", "text": "$\\frac{2\\omega}{a^2 + \\omega^2}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：双边实指数信号的时域分段积分与欧拉公式。

1. 将绝对值分段拆开积分：
   $$F(j\\omega) = \\int_{-\\infty}^0 e^{at}e^{-j\\omega t}dt + \\int_0^\\infty e^{-at}e^{-j\\omega t}dt$$
2. 分别计算两个半平面的反常积分：
   - 负半轴：$\\int_{-\\infty}^0 e^{(a - j\\omega)t}dt = \\left[ \\frac{e^{(a - j\\omega)t}}{a - j\\omega} \\right]_{-\\infty}^0 = \\frac{1}{a - j\\omega}$；
   - 正半轴：$\\int_0^\\infty e^{-(a + j\\omega)t}dt = \\left[ -\\frac{e^{-(a + j\\omega)t}}{a + j\\omega} \\right]_0^\\infty = \\frac{1}{a + j\\omega}$；
3. 通分相加：
   $$F(j\\omega) = \\frac{1}{a - j\\omega} + \\frac{1}{a + j\\omega} = \\frac{(a + j\\omega) + (a - j\\omega)}{(a - j\\omega)(a + j\\omega)} = \\frac{2a}{a^2 + \\omega^2}$$
4. 验证：由于 $f(t)$ 为实偶信号，其频谱严格为**实偶函数**，完全符合定理。
选 **A**。"""
  },
  {
    "id": "ss-c3-zjl-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "吉布斯现象理论极限",
    "type": "single",
    "difficulty": 2,
    "tags": ["郑君里考研题", "吉布斯现象", "名校高频"],
    "source": "郑君里《信号与系统》(第3版)课后习题3.14",
    "stem": "当具有间断点（如阶跃跳变）的信号通过频带有限的理想低通滤波器时，在截断边缘处会产生高频衰减振荡的“吉布斯现象（Gibbs Phenomenon）”。当滤波器截止频率 $\\omega_c \\to \\infty$ 时，其阶跃响应在间断点处的最大超调量百分比将：",
    "options": [
      { "key": "A", "text": "保持约为 $8.95\\% \\approx 9\\%$ 的常数不变，仅振荡向间断点压缩" },
      { "key": "B", "text": "趋近于 0，超调彻底消失" },
      { "key": "C", "text": "线性增大到 $50\\%$" },
      { "key": "D", "text": "趋向于无穷大" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：吉布斯现象（Gibbs Phenomenon）的数学极限特性。

1. 当连续信号在某点存在第一类可去/跳变间断点时，利用有限项傅氏级数或有限带宽滤波近似重构，在跳变点两翼必然出现超调尖峰；
2. 数学积分极限表明，超调峰值由正弦积分函数决定：
   $$\\frac{1}{\\pi}\\int_0^\\pi \\frac{\\sin x}{x}dx - \\frac{1}{2} \\approx 0.089490$$
3. 即使截止频率 $\\omega_c \\to \\infty$，最大跳变超调量**始终恒定在跳变幅度的约 $8.95\\%$（常记为 $9\\%$）**，绝不随带宽增加而减小；
4. 带宽增加的唯一效果是使振荡波纹的周期变密，向间断点无限挤压靠拢。
选 **A**。"""
  },
  {
    "id": "ss-c3-zjl-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "希尔伯特变换器频响",
    "type": "single",
    "difficulty": 3,
    "tags": ["郑君里考研题", "希尔伯特变换", "SSB调制"],
    "source": "郑君里《信号与系统》(第3版)课后习题3.19",
    "stem": "在通信与信号处理系统中，理想希尔伯特变换器（Hilbert Transformer）是一个宽带 $90^\\circ$ 移相网络，其系统频率响应 $H(j\\omega)$ 为：",
    "options": [
      { "key": "A", "text": "$-j\\text{sgn}(\\omega)$" },
      { "key": "B", "text": "$j\\text{sgn}(\\omega)$" },
      { "key": "C", "text": "$\\text{sgn}(\\omega)$" },
      { "key": "D", "text": "$-j\\omega$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：希尔伯特变换的频域传输特性定义。

1. 希尔伯特变换的时域冲激响应为：
   $$h(t) = \\frac{1}{\\pi t}$$
2. 求其傅里叶变换：
   由符号函数的对偶性 $\\text{sgn}(t) \\leftrightarrow \\frac{2}{j\\omega} \\implies \\frac{1}{\\pi t} \\stackrel{\\mathcal{F}}{\\longleftrightarrow} -j\\text{sgn}(\\omega)$；
3. 其物理意义：
   - 当 $\\omega > 0$ 时：$H(j\\omega) = -j = e^{-j \\frac{\\pi}{2}}$（产生 $-90^\\circ$ 相移）；
   - 当 $\\omega < 0$ 时：$H(j\\omega) = +j = e^{+j \\frac{\\pi}{2}}$（产生 $+90^\\circ$ 相移）；
   - 幅度响应 $|H(j\\omega)| = 1$ 保持全频带全通。
4. 希尔伯特变换是构造解析信号（Analytic Signal）和单边带调制（SSB）的核心理论基础。
选 **A**。"""
  },

  # ==========================================
  # 第四章：拉普拉斯变换与复频域分析 (新增 4 题)
  # ==========================================
  {
    "id": "ss-c4-obh-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "双边拉氏变换带状收敛域",
    "type": "single",
    "difficulty": 3,
    "tags": ["奥本海姆经典", "双边拉氏变换", "带状ROC"],
    "source": "奥本海姆《信号与系统》(第2版)课后习题9.21",
    "stem": "双边时间信号 $x(t) = e^{-2t}u(t) + e^{t}u(-t)$，其双边拉普拉斯变换 $X(s)$ 的极点与收敛域 ROC 为：",
    "options": [
      { "key": "A", "text": "极点为 $-2$ 和 $1$，收敛域为带状区域 $-2 < \\text{Re}(s) < 1$" },
      { "key": "B", "text": "极点为 $-2$ 和 $1$，收敛域为 $\\text{Re}(s) > 1$" },
      { "key": "C", "text": "极点为 $-2$ 和 $1$，收敛域为 $\\text{Re}(s) < -2$" },
      { "key": "D", "text": "收敛域为空集，拉氏变换不存在" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：双边拉普拉斯变换的因果右边带与反因果左边带求交集。

1. **第一项（因果右边信号）**：
   $e^{-2t}u(t) \\leftrightarrow \\frac{1}{s + 2}$，极点为 $s_1 = -2$，右边信号收敛域为：$\\text{Re}(s) > -2$；
2. **第二项（反因果左边信号）**：
   $e^t u(-t) = -[-e^t u(-t)] \\leftrightarrow -\\frac{1}{s - 1} = \\frac{1}{1 - s}$，极点为 $s_2 = 1$，左边信号收敛域为：$\\text{Re}(s) < 1$；
3. **求总收敛域交集**：
   $$\\text{ROC} = \\{\\text{Re}(s) > -2\\} \\cap \\{\\text{Re}(s) < 1\\} = -2 < \\text{Re}(s) < 1$$
4. 该区域为包含虚轴 $\\text{Re}(s) = 0$ 的带状平行区域，因此变换存在且原信号在全时域绝对可积。
选 **A**。"""
  },
  {
    "id": "ss-c4-obh-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "右半平面极点与反因果稳定",
    "type": "single",
    "difficulty": 3,
    "tags": ["奥本海姆经典", "反因果系统", "BIBO稳定"],
    "source": "奥本海姆《信号与系统》(第2版)课后习题9.22",
    "stem": "某 LTI 系统的系统函数为 $H(s) = \\frac{1}{s - 2}$。若已知该系统是 BIBO 稳定系统，则其单位冲激响应 $h(t)$ 必为：",
    "options": [
      { "key": "A", "text": "$-e^{2t}u(-t)$（反因果信号）" },
      { "key": "B", "text": "$e^{2t}u(t)$（因果信号）" },
      { "key": "C", "text": "$e^{-2t}u(t)$" },
      { "key": "D", "text": "$-e^{-2t}u(-t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：极点位置与系统 BIBO 稳定性收敛域的严格绑定。

1. 系统函数只有一个极点：$s = 2$（位于右半平面）；
2. **稳定系统的充要条件**：冲激响应绝对可积，拉氏变换收敛域**必须包含虚轴 $\\text{Re}(s) = 0$**；
3. 由于极点在 $s = 2$，包含虚轴的收敛域只能位于该极点的左侧：
   $$\\text{ROC}: \\text{Re}(s) < 2$$
4. 收敛域位于最左极点左侧对应的原函数必定为**左边反因果信号**：
   $$h(t) = -e^{2t}u(-t)$$
   （当 $t \\to -\\infty$ 时 $e^{2t} \\to 0$ 指数衰减收敛，$\int_{-\infty}^0 e^{2t}dt = 1/2 < \infty$）。
故选 **A**。"""
  },
  {
    "id": "ss-c4-zjl-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "LC并联谐振网络复频域阻抗",
    "type": "single",
    "difficulty": 2,
    "tags": ["郑君里考研题", "电路S域阻抗", "谐振网络"],
    "source": "郑君里《信号与系统》(第3版)课后习题4.8",
    "stem": "在复频域 $s$ 域中，理想电感 $L$ 与理想电容 $C$ 并联支路的等效复频域阻抗 $Z(s)$ 为：",
    "options": [
      { "key": "A", "text": "$\\frac{s/C}{s^2 + \\frac{1}{LC}}$" },
      { "key": "B", "text": "$\\frac{sL}{s^2 LC - 1}$" },
      { "key": "C", "text": "$sL + \\frac{1}{sC}$" },
      { "key": "D", "text": "$\\frac{1}{s^2 LC + 1}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：复频域电路阻抗的并联运算法则。

1. 电感阻抗为 $Z_L(s) = sL$，电容阻抗为 $Z_C(s) = \\frac{1}{sC}$；
2. 两元件并联等效阻抗：
   $$Z(s) = \\frac{Z_L(s) Z_C(s)}{Z_L(s) + Z_C(s)} = \\frac{sL \\cdot \\frac{1}{sC}}{sL + \\frac{1}{sC}} = \\frac{sL/sC}{\\frac{s^2 LC + 1}{sC}} = \\frac{sL}{s^2 LC + 1}$$
3. 分子分母同除以 $LC$：
   $$Z(s) = \\frac{\\frac{sL}{LC}}{s^2 + \\frac{1}{LC}} = \\frac{s/C}{s^2 + \\frac{1}{LC}} = \\frac{s/C}{s^2 + \\omega_0^2}$$
   其中谐振角频率 $\\omega_0 = \\frac{1}{\\sqrt{LC}}$。
选 **A**。"""
  },
  {
    "id": "ss-c4-zjl-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "二阶系统谐振峰值频率",
    "type": "single",
    "difficulty": 3,
    "tags": ["郑君里考研题", "谐振峰值", "欠阻尼二阶"],
    "source": "郑君里《信号与系统》(第3版)课后习题4.15",
    "stem": "典型二阶欠阻尼系统函数为 $H(s) = \\frac{\\omega_0^2}{s^2 + 2\\zeta\\omega_0 s + \\omega_0^2}$（阻尼比 $0 < \\zeta < \\frac{1}{\\sqrt{2}}$）。该系统幅频响应曲线 $|H(j\\omega)|$ 出现极大值峰值的谐振角频率 $\\omega_r$ 为：",
    "options": [
      { "key": "A", "text": "$\\omega_r = \\omega_0 \\sqrt{1 - 2\\zeta^2}$" },
      { "key": "B", "text": "$\\omega_r = \\omega_0 \\sqrt{1 - \\zeta^2}$" },
      { "key": "C", "text": "$\\omega_r = \\omega_0$" },
      { "key": "D", "text": "$\\omega_r = 2\\zeta\\omega_0$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：连续二阶系统幅频特性峰值点（谐振频率）推导。

1. 代入 $s = j\\omega$ 计算频响模长平方：
   $$|H(j\\omega)|^2 = \\frac{\\omega_0^4}{(\\omega_0^2 - \\omega^2)^2 + (2\\zeta\\omega_0 \\omega)^2}$$
2. 要使增益最大，只需分母多项式 $D(\\omega) = (\\omega_0^2 - \\omega^2)^2 + 4\\zeta^2 \\omega_0^2 \\omega^2$ 取极小值；
3. 令 $u = \\omega^2$，$D(u) = (\\omega_0^2 - u)^2 + 4\\zeta^2 \\omega_0^2 u = u^2 - 2\\omega_0^2(1 - 2\\zeta^2)u + \\omega_0^4$；
4. 这是一个关于 $u$ 的抛物线，顶点极小值点位于：
   $$u_r = \\omega_r^2 = \\omega_0^2(1 - 2\\zeta^2)$$
5. 开平方得到谐振角频率：
   $$\\omega_r = \\omega_0 \\sqrt{1 - 2\\zeta^2}$$
【名师提示】：
- 阻尼固有振荡角频率为 $\\omega_d = \\omega_0\\sqrt{1 - \\zeta^2}$；
- 谐振角频率为 $\\omega_r = \\omega_0\\sqrt{1 - 2\\zeta^2}$；
- 只有当 $0 < \\zeta < \\frac{1}{\\sqrt{2}} \\approx 0.707$ 时，$1 - 2\\zeta^2 > 0$ 才有峰值。
选 **A**。"""
  },

  # ==========================================
  # 第五章：Z变换与离散系统 (新增 4 题)
  # ==========================================
  {
    "id": "ss-c5-obh-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "双边离散序列Z变换环状收敛域",
    "type": "single",
    "difficulty": 3,
    "tags": ["奥本海姆经典", "双边Z变换", "环形ROC"],
    "source": "奥本海姆《信号与系统》(第2版)课后习题10.21",
    "stem": "双边序列 $x[n] = \\left(\\frac{1}{2}\\right)^n u[n] - \\left(\\frac{3}{4}\\right)^n u[-n - 1]$，其 Z 变换 $X(z)$ 的收敛域 ROC 为：",
    "options": [
      { "key": "A", "text": "$\\frac{1}{2} < |z| < \\frac{3}{4}$" },
      { "key": "B", "text": "$|z| > \\frac{3}{4}$" },
      { "key": "C", "text": "$|z| < \\frac{1}{2}$" },
      { "key": "D", "text": "收敛域为空集" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：因果外圆与反因果内圆的交集判定。

1. **第一项（因果右边序列）**：
   $(\\frac{1}{2})^n u[n] \\leftrightarrow \\frac{z}{z - 1/2}$，极点在 $z = \\frac{1}{2}$，因果收敛域为圆外：$|z| > \\frac{1}{2}$；
2. **第二项（反因果左边序列）**：
   $-(\\frac{3}{4})^n u[-n - 1] \\leftrightarrow \\frac{z}{z - 3/4}$，极点在 $z = \\frac{3}{4}$，反因果收敛域为圆内：$|z| < \\frac{3}{4}$；
3. **总收敛域为公共交集**：
   $$\\text{ROC} = \\left\\{|z| > \\frac{1}{2}\\right\\} \\cap \\left\\{|z| < \\frac{3}{4}\\right\\} = \\frac{1}{2} < |z| < \\frac{3}{4}$$
4. 该环形区域不包含单位圆 $|z| = 1$，因此该双边序列不存在离散时间傅里叶变换（DTFT 发散）。
选 **A**。"""
  },
  {
    "id": "ss-c5-obh-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "离散矩形窗DTFT狄利克雷核",
    "type": "single",
    "difficulty": 3,
    "tags": ["奥本海姆经典", "DTFT", "狄利克雷核"],
    "source": "奥本海姆《信号与系统》(第2版)课后习题5.21",
    "stem": "对称有限长离散矩形序列 $x[n] = 1\\,(|n| \\le N_1)$，在其余点为 0。则其离散时间傅里叶变换（DTFT）$X(e^{j\\Omega})$ 为：",
    "options": [
      { "key": "A", "text": "$\\frac{\\sin\\left(\\Omega(N_1 + \\frac{1}{2})\\right)}{\\sin(\\Omega/2)}$" },
      { "key": "B", "text": "$\\frac{\\sin(\\Omega N_1)}{\\Omega}$" },
      { "key": "C", "text": "$\\frac{\\cos(\\Omega N_1)}{\\cos(\\Omega/2)}$" },
      { "key": "D", "text": "$\\frac{\\sin(2\\Omega N_1)}{\\sin(\\Omega)}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散有限长对称矩形序列的 DTFT 闭式推导（狄利克雷核 Dirichlet Kernel）。

1. 根据 DTFT 定义：
   $$X(e^{j\\Omega}) = \\sum_{n=-N_1}^{N_1} 1 \\cdot e^{-j\\Omega n}$$
2. 提取对称中心等比求和（首项 $e^{j\\Omega N_1}$，公比 $e^{-j\\Omega}$，共 $2N_1 + 1$ 项）：
   $$X(e^{j\\Omega}) = e^{j\\Omega N_1} \\frac{1 - (e^{-j\\Omega})^{2N_1 + 1}}{1 - e^{-j\\Omega}} = \\frac{e^{j\\Omega(N_1 + 1/2)} - e^{-j\\Omega(N_1 + 1/2)}}{e^{j\\Omega/2} - e^{-j\\Omega/2}}$$
3. 分子分母同时化为正弦：
   $$X(e^{j\\Omega}) = \\frac{2j\\sin\\left(\\Omega(N_1 + \\frac{1}{2})\\right)}{2j\\sin(\\Omega/2)} = \\frac{\\sin\\left(\\Omega(N_1 + \\frac{1}{2})\\right)}{\\sin(\\Omega/2)}$$
4. 这是连续抽样函数 $\\text{Sa}(x)$ 在离散频域的对应形式，具有严格的 $2\\pi$ 周期性。
选 **A**。"""
  },
  {
    "id": "ss-c5-zjl-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "共振激励差分方程Z域解法",
    "type": "single",
    "difficulty": 3,
    "tags": ["郑君里考研题", "Z变换求解", "共振重极点"],
    "source": "郑君里《信号与系统》(第3版)课后习题6.8",
    "stem": "某离散因果系统差分方程为 $y[k] - 0.5y[k - 1] = f[k]$。若外加激励为同模态信号 $f[k] = (0.5)^k \\varepsilon[k]$，初始状态为零，则系统的零状态响应 $y_{zs}[k]$ 为：",
    "options": [
      { "key": "A", "text": "$(k + 1)(0.5)^k \\varepsilon[k]$" },
      { "key": "B", "text": "$k (0.5)^k \\varepsilon[k]$" },
      { "key": "C", "text": "$[(0.5)^k - 1]\\varepsilon[k]$" },
      { "key": "D", "text": "$2(0.5)^k \\varepsilon[k]$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：外加激励与系统固有特征极点重合时的离散共振响应。

1. **求系统函数 $H(z)$ 与输入 $F(z)$**：
   $$H(z) = \\frac{1}{1 - 0.5z^{-1}} = \\frac{z}{z - 0.5}$$
   $$F(z) = \\frac{z}{z - 0.5}$$
2. **求零状态响应的象函数**：
   $$Y_{zs}(z) = H(z)F(z) = \\frac{z^2}{(z - 0.5)^2}$$
3. **求逆 Z 变换**：
   - 方式一：两边除以 $z$：$\\frac{Y_{zs}(z)}{z} = \\frac{z}{(z - 0.5)^2} = \\frac{1}{z - 0.5} + \\frac{0.5}{(z - 0.5)^2}$；
   - 乘回 $z$：$Y_{zs}(z) = \\frac{z}{z - 0.5} + \\frac{0.5z}{(z - 0.5)^2}$；
   - 对应时域：$(0.5)^k \\varepsilon[k] + k (0.5)^k \\varepsilon[k] = (k + 1)(0.5)^k \\varepsilon[k]$；
   - 方式二：利用序列卷积公式 $(0.5)^k \\varepsilon[k] * (0.5)^k \\varepsilon[k] = \\sum_{m=0}^k (0.5)^m (0.5)^{k-m} = (0.5)^k \\sum_{m=0}^k 1 = (k + 1)(0.5)^k \\varepsilon[k]$。
选 **A**。"""
  },
  {
    "id": "ss-c5-zjl-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "朱利准则临界稳定边界判据",
    "type": "judgment",
    "difficulty": 3,
    "tags": ["郑君里考研题", "朱利准则", "临界稳定"],
    "source": "郑君里《信号与系统》(第3版)课后习题6.14",
    "stem": "某三阶因果离散系统的特征多项式为 $A(z) = z^3 - 1.1z^2 - 0.1z + 0.2$。经朱利准则计算发现 $A(1) = 1 - 1.1 - 0.1 + 0.2 = 0$。据此可判定该系统属于渐近稳定系统。",
    "options": [
      { "key": "A", "text": "正确（True）" },
      { "key": "B", "text": "错误（False）" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：朱利稳定性准则在 $z = 1$ 点的充要条件判据。

1. 根据朱利准则（Jury Test），因果离散系统**渐近稳定**（所有极点严格在单位圆内 $|z_i| < 1$）的必要前提条件之一是：
   $$A(1) > 0$$
   （严格大于零）；
2. 若计算发现 $A(1) = 0$，说明多项式必含有因式 $(z - 1)$，即 $z = 1$ 恰好是该系统的特征极点；
3. 极点 $z = 1$ 的模长 $|z| = 1$，正好落在**单位圆周边界**上，对应的时域模态为单位阶跃 $\\varepsilon[k]$（等幅持续）；
4. 因此该系统属于**临界稳定**，而非“渐近稳定”。若存在重根更会引起发散不稳定。
故题干陈述错误，选 **B**。"""
  },

  # ==========================================
  # 第六章：系统状态变量与信号流图 (新增 2 题)
  # ==========================================
  {
    "id": "ss-c6-zjl-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第六章：系统状态变量与信号流图",
    "section": "RLC串联电路状态矩阵建立",
    "type": "single",
    "difficulty": 3,
    "tags": ["郑君里考研题", "状态方程", "RLC电路"],
    "source": "郑君里《信号与系统》(第3版)课后习题7.3",
    "stem": "在电阻 $R$、电感 $L$、电容 $C$ 与电压源 $e(t)$ 串联的闭合回路中，选取电容电压 $u_C(t)$ 和电感电流 $i_L(t)$ 构成状态向量 $\\mathbf{x}(t) = [u_C(t), \\, i_L(t)]^T$。则系统的状态转移矩阵 $\\mathbf{A}$ 为：",
    "options": [
      { "key": "A", "text": "$\\begin{bmatrix} 0 & \\frac{1}{C} \\\\ -\\frac{1}{L} & -\\frac{R}{L} \\end{bmatrix}$" },
      { "key": "B", "text": "$\\begin{bmatrix} 0 & -\\frac{1}{C} \\\\ \\frac{1}{L} & -\\frac{R}{L} \\end{bmatrix}$" },
      { "key": "C", "text": "$\\begin{bmatrix} -\\frac{R}{L} & -\\frac{1}{L} \\\\ \\frac{1}{C} & 0 \\end{bmatrix}$" },
      { "key": "D", "text": "$\\begin{bmatrix} 0 & 1 \\\\ -\\frac{1}{LC} & -\\frac{R}{L} \\end{bmatrix}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：动态电路拓扑建立标准状态方程 $\\dot{\\mathbf{x}} = \\mathbf{A}\\mathbf{x} + \\mathbf{b}e$。

1. **根据电容伏安关系**：
   串联回路中流过电容的电流即为电感电流 $i_L(t)$：
   $$C \\frac{du_C(t)}{dt} = i_L(t) \\implies \\dot{u}_C(t) = 0 \\cdot u_C(t) + \\frac{1}{C} i_L(t)$$
2. **根据回路 KVL 定律**：
   沿回路绕行：$L \\frac{di_L(t)}{dt} + R i_L(t) + u_C(t) = e(t)$；
   整理出电感电流导数：
   $$\\dot{i}_L(t) = -\\frac{1}{L} u_C(t) - \\frac{R}{L} i_L(t) + \\frac{1}{L} e(t)$$
3. **写成矩阵形式**：
   $$\\begin{bmatrix} \\dot{u}_C \\\\ \\dot{i}_L \\end{bmatrix} = \\begin{bmatrix} 0 & \\frac{1}{C} \\\\ -\\frac{1}{L} & -\\frac{R}{L} \\end{bmatrix} \\begin{bmatrix} u_C \\\\ i_L \\end{bmatrix} + \\begin{bmatrix} 0 \\\\ \\frac{1}{L} \\end{bmatrix} e(t)$$
故状态矩阵 $\\mathbf{A} = \\begin{bmatrix} 0 & \\frac{1}{C} \\\\ -\\frac{1}{L} & -\\frac{R}{L} \\end{bmatrix}$。选 **A**。"""
  },
  {
    "id": "ss-c6-zjl-02",
    "subject": "广工837/809-信号与系统",
    "chapter": "第六章：系统状态变量与信号流图",
    "section": "互不接触双回路梅森增益公式",
    "type": "single",
    "difficulty": 3,
    "tags": ["郑君里考研题", "梅森公式", "不接触回路"],
    "source": "郑君里《信号与系统》(第3版)课后习题7.8",
    "stem": "某控制系统信号流图仅有单条前向通路 $P_1 = G_1 G_2 G_3$，且系统中仅包含两个互不接触的局部负反馈回路，回路增益分别为 $L_1 = -H_1$ 和 $L_2 = -H_2$。若两回路均与前向通路相接触，则系统的闭环传输函数 $H(s)$ 为：",
    "options": [
      { "key": "A", "text": "$\\frac{G_1 G_2 G_3}{(1 + H_1)(1 + H_2)}$" },
      { "key": "B", "text": "$\\frac{G_1 G_2 G_3}{1 + H_1 + H_2}$" },
      { "key": "C", "text": "$\\frac{G_1 G_2 G_3}{1 - H_1 - H_2 + H_1 H_2}$" },
      { "key": "D", "text": "$\\frac{G_1 G_2 G_3}{1 + H_1 H_2}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：含互不接触回路时梅森公式行列式 $\\Delta$ 的精确展开。

1. **计算特征行列式 $\\Delta$**：
   $$\\Delta = 1 - \\sum L_i + \\sum L_i L_j$$
   代入两回路增益：
   - 所有单独回路之和：$\\sum L_i = L_1 + L_2 = -H_1 - H_2$；
   - 两两互不接触回路乘积：$L_1 L_2 = (-H_1)(-H_2) = H_1 H_2$；
   因此：
   $$\\Delta = 1 - (-H_1 - H_2) + H_1 H_2 = 1 + H_1 + H_2 + H_1 H_2 = (1 + H_1)(1 + H_2)$$
2. **计算余子式 $\\Delta_1$**：
   因为 $L_1$ 与 $L_2$ 均与前向通路 $P_1$ 相接触，当抹去前向通路后没有任何孤立回路剩余，故 $\\Delta_1 = 1$；
3. **套用梅森增益公式**：
   $$H(s) = \\frac{P_1 \\Delta_1}{\\Delta} = \\frac{G_1 G_2 G_3}{(1 + H_1)(1 + H_2)}$$
选 **A**。"""
  },

  # ==========================================
  # 第七章：时域抽样与恢复 (新增 2 题)
  # ==========================================
  {
    "id": "ss-c7-obh-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第七章：时域抽样与恢复",
    "section": "双余弦调幅信号奈奎斯特采样率",
    "type": "single",
    "difficulty": 2,
    "tags": ["奥本海姆经典", "积化和差", "奈氏频率"],
    "source": "奥本海姆《信号与系统》(第2版)课后习题7.21",
    "stem": "连续信号 $x(t) = \\cos(150\\pi t)\\cos(350\\pi t)$，为保证无失真采样并恢复原信号，理论最小奈奎斯特抽样频率 $f_s$ 为：",
    "options": [
      { "key": "A", "text": "$500\\text{ Hz}$" },
      { "key": "B", "text": "$250\\text{ Hz}$" },
      { "key": "C", "text": "$350\\text{ Hz}$" },
      { "key": "D", "text": "$1000\\text{ Hz}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：三角积化和差展开与最高截止频率判别。

1. 利用三角积化和差公式展开两余弦相乘：
   $$x(t) = \\frac{1}{2}[\\cos((350\\pi + 150\\pi)t) + \\cos((350\\pi - 150\\pi)t)] = \\frac{1}{2}\\cos(500\\pi t) + \\frac{1}{2}\\cos(200\\pi t)$$
2. 确定最高角频率：
   - 信号包含两个频率分量：$\\omega_1 = 200\\pi\\text{ rad/s}$，$\\omega_2 = 500\\pi\\text{ rad/s}$；
   - 信号的最高截止角频率为 $\\omega_m = 500\\pi\\text{ rad/s}$；
   - 对应的最高模拟频率为 $f_m = \\frac{\\omega_m}{2\\pi} = \\frac{500\\pi}{2\\pi} = 250\\text{ Hz}$；
3. 由奈奎斯特抽样定理：
   $$f_s \\ge 2 f_m = 2 \\times 250\\text{ Hz} = 500\\text{ Hz}$$
选 **A**。"""
  },
  {
    "id": "ss-c7-zjl-01",
    "subject": "广工837/809-信号与系统",
    "chapter": "第七章：时域抽样与恢复",
    "section": "平顶抽样孔径效应失真与均衡补偿",
    "type": "single",
    "difficulty": 3,
    "tags": ["郑君里考研题", "平顶抽样", "孔径效应"],
    "source": "郑君里《信号与系统》(第3版)课后习题3.24",
    "stem": "在脉冲振幅调制（PAM）工程中，实际通常使用脉宽为 $\\tau$ 的窄矩形脉冲进行平顶抽样（Flat-top Sampling）。相比于理想冲激抽样，平顶抽样恢复后的信号高频分量会产生滚降衰减失真（孔径效应 Aperture Effect）。为消除该失真，所串联的均衡滤波器（Equalizer）的频响幅值应正比于：",
    "options": [
      { "key": "A", "text": "$\\frac{1}{\\text{Sa}\\left(\\frac{\\omega\\tau}{2}\\right)}$" },
      { "key": "B", "text": "$\\text{Sa}\\left(\\frac{\\omega\\tau}{2}\\right)$" },
      { "key": "C", "text": "$\\frac{1}{\\cos\\left(\\frac{\\omega\\tau}{2}\\right)}$" },
      { "key": "D", "text": "$\\frac{\\omega\\tau}{2}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：平顶抽样孔径效应失真（Aperture Distortion）的数学机理与均衡器原理。

1. **时域机理**：平顶抽样信号可视为理想冲激抽样信号 $f_s(t)$ 与宽度为 $\\tau$ 的单矩形脉冲 $p(t) = \\text{rect}(t/\\tau)$ 的时域卷积：
   $$f_{pam}(t) = f_s(t) * p(t)$$
2. **频域机理**：频域表现为相乘：
   $$F_{pam}(j\\omega) = F_s(j\\omega) \\cdot P(j\\omega) = F_s(j\\omega) \\cdot \\tau\\text{Sa}\\left(\\frac{\\omega\\tau}{2}\\right)$$
3. **孔径失真分析**：
   矩形脉冲频谱是一个采样函数 $\\text{Sa}(\\frac{\\omega\\tau}{2})$，随着频率 $\\omega$ 增大，增益不断下降，导致抽样信号的高频分量被衰减，产生失真；
4. **均衡补偿方案**：
   在接收端低通滤波器后串联一个幅频特性反比于 $\\text{Sa}(\\frac{\\omega\\tau}{2})$ 的均衡网络：
   $$H_{eq}(j\\omega) = \\frac{1}{\\text{Sa}\\left(\\frac{\\omega\\tau}{2}\\right)}$$
   两者相乘即可精确对消孔径衰减，完全复原基带频谱。
故选 **A**。"""
  }
]

print(f"Total new textbook questions: {len(textbook_questions)}")

# Load existing signalsQuestions.ts
existing_path = 'src/data/signalsQuestions.ts'
with open(existing_path, 'r', encoding='utf-8') as f:
    text = f.read()

prefix = "import { Question } from '../types';\n\nexport const signalsAndSystemsQuestions: Question[] = "
json_str = text[len(prefix):].rstrip(';\n')
existing_questions = json.loads(json_str)

print(f"Loaded {len(existing_questions)} existing questions.")

# Merge and deduplicate by ID
merged_dict = {q['id']: q for q in existing_questions}
added_count = 0
for q in textbook_questions:
    if q['id'] not in merged_dict:
        merged_dict[q['id']] = q
        added_count += 1
    else:
        # Update existing with refreshed textbook content
        merged_dict[q['id']] = q

merged_list = list(merged_dict.values())

# Sort strictly by curriculum chapter order and ID
chapter_order = [
  '第一章：信号与系统基础',
  '第二章：系统的时域分析',
  '第三章：频域分析与傅里叶变换',
  '第四章：拉普拉斯变换与复频域分析',
  '第五章：Z变换与离散系统',
  '第六章：系统状态变量与信号流图',
  '第七章：时域抽样与恢复'
]

def sort_key(q):
    ch = q.get('chapter', '')
    ch_idx = chapter_order.index(ch) if ch in chapter_order else 99
    qid = q.get('id', '')
    return (ch_idx, qid)

merged_list.sort(key=sort_key)

print(f"Total merged questions: {len(merged_list)} (newly added: {added_count})")

# Write back to src/data/signalsQuestions.ts
formatted_json = json.dumps(merged_list, ensure_ascii=False, indent=2)
with open(existing_path, 'w', encoding='utf-8') as out:
    out.write(prefix + formatted_json + ";\n")

print("Successfully written to src/data/signalsQuestions.ts!")
