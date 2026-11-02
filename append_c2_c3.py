# -*- coding: utf-8 -*-
import json

c2_c3_code = '''
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
    "stem": "已知序列 $f_1(k) = \\{\\underline{3}, 2, 1\\}$，$f_2(k) = \\{\\underline{2}, 1, 2\\}$（带下划线处为 $k = 0$ 点），则卷积和 $f(k) = f_1(k) * f_2(k)$ 在 $k = 3$ 处的值 $f(3)$ 为：",
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
   由离散卷积定义公式 $f(3) = \\sum_{m=-\\infty}^\\infty f_1(m)f_2(3 - m)$：
   - 当 $m = 1$ 时：$f_1(1) f_2(2) = 2 \\times 2 = 4$；
   - 当 $m = 2$ 时：$f_1(2) f_2(1) = 1 \\times 1 = 1$；
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
    "stem": "计算离散序列卷积和 $[(0.2)^k \\varepsilon(k)] * [(0.4)^k \\varepsilon(k)]$ 的化简解析式为：",
    "options": [
      { "key": "A", "text": "$[2(0.4)^k - (0.2)^k]\\varepsilon(k)$" },
      { "key": "B", "text": "$[(0.4)^k - (0.2)^k]\\varepsilon(k)$" },
      { "key": "C", "text": "$[2(0.4)^k - 2(0.2)^k]\\varepsilon(k)$" },
      { "key": "D", "text": "$5[(0.4)^{k+1} - (0.2)^{k+1}]\\varepsilon(k)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：单边指数阶跃序列的卷积公式。

1. 经典离散卷积公式（$a \\ne b$ 时）：
   $$(a^k \\varepsilon[k]) * (b^k \\varepsilon[k]) = \\frac{a^{k+1} - b^{k+1}}{a - b}\\varepsilon[k]$$
2. 代入 $a = 0.4, \\, b = 0.2$：
   $$y(k) = \\frac{(0.4)^{k+1} - (0.2)^{k+1}}{0.4 - 0.2}\\varepsilon[k] = \\frac{0.4(0.4)^k - 0.2(0.2)^k}{0.2}\\varepsilon[k]$$
3. 提取分母约分：
   $$y(k) = \\left[ \\frac{0.4}{0.2}(0.4)^k - \\frac{0.2}{0.2}(0.2)^k \\right] \\varepsilon[k] = [2(0.4)^k - (0.2)^k]\\varepsilon[k]$$
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
    "stem": "已知离散系统单位样值响应 $h(n) = \\delta(n) + 2\\delta(n - 1) - \\delta(n - 3)$，输入激励为 $x(n) = 2\\delta(n - 1)$，则系统在 $n = 0$ 和 $n = 2$ 处的响应值 $y(0)$ 与 $y(2)$ 分别为：",
    "options": [
      { "key": "A", "text": "$y(0) = 0, \\, y(2) = 4$" },
      { "key": "B", "text": "$y(0) = 2, \\, y(2) = 2$" },
      { "key": "C", "text": "$y(0) = 0, \\, y(2) = 2$" },
      { "key": "D", "text": "$y(0) = 1, \\, y(2) = 4$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散时不变系统的卷积性质。

1. 根据卷积的时移和数乘性质：
   $$y(n) = x(n) * h(n) = 2\\delta(n - 1) * [\\delta(n) + 2\\delta(n - 1) - \\delta(n - 3)]$$
2. 逐项展开：
   $$y(n) = 2\\delta(n - 1) + 4\\delta(n - 2) - 2\\delta(n - 4)$$
3. 计算指定点数值：
   - 当 $n = 0$ 时，由于各项冲激位置分别为 $1, 2, 4$，故 $y(0) = 0$；
   - 当 $n = 2$ 时，只有中间项 $4\\delta(n - 2)$ 在 $n = 2$ 处激发出脉冲，故 $y(2) = 4$；
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
    "stem": "计算连续时间卷积积分 $t\\varepsilon(t) * \\varepsilon(t)$ 的化简结果为：",
    "options": [
      { "key": "A", "text": "$\\frac{1}{2}t^2 \\varepsilon(t)$" },
      { "key": "B", "text": "$t^2 \\varepsilon(t)$" },
      { "key": "C", "text": "$t \\varepsilon(t)$" },
      { "key": "D", "text": "$\\frac{1}{6}t^3 \\varepsilon(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：任意因果信号与单位阶跃信号的卷积积分等价于时域积分。

1. 任何信号 $f(t)$ 与单位阶跃函数 $\\varepsilon(t)$ 卷积，其物理实质为其积分运算：
   $$f(t) * \\varepsilon(t) = \\int_{-\\infty}^t f(\\tau) \\, d\\tau$$
2. 本题中 $f(t) = t\\varepsilon(t)$ 是因果信号，因此当 $t > 0$ 时：
   $$y(t) = \\int_0^t \\tau \\, d\\tau = \\left[ \\frac{1}{2}\\tau^2 \\right]_0^t = \\frac{1}{2}t^2$$
   当 $t < 0$ 时，$y(t) = 0$。
3. 写作统一因果表达式：
   $$y(t) = \\frac{1}{2}t^2 \\varepsilon(t)$$
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
    "stem": "已知某 LTI 系统的冲激响应为 $h(t) = e^{-2t}\\varepsilon(t)$，当输入激励为斜坡信号 $f(t) = t\\varepsilon(t)$ 时，系统的零状态响应 $y_{zs}(t)$ 为：",
    "options": [
      { "key": "A", "text": "$\\frac{1}{4}[2t - 1 + e^{-2t}]\\varepsilon(t)$" },
      { "key": "B", "text": "$\\frac{1}{2}[t - e^{-2t}]\\varepsilon(t)$" },
      { "key": "C", "text": "$\\frac{1}{2}[1 - e^{-2t}]\\varepsilon(t)$" },
      { "key": "D", "text": "$[t e^{-2t}]\\varepsilon(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：阶跃响应与斜坡响应的时域积分关联。

1. 当输入为单位阶跃 $\\varepsilon(t)$ 时，系统的阶跃响应为：
   $$g(t) = \\int_0^t h(\\tau)d\\tau = \\int_0^t e^{-2\\tau}d\\tau = \\frac{1}{2}(1 - e^{-2t})\\varepsilon(t)$$
2. 斜坡信号 $t\\varepsilon(t)$ 是阶跃信号的时域积分：$t\\varepsilon(t) = \\int_0^t \\varepsilon(\\tau)d\\tau$。
3. 由 LTI 系统的积分性质，零状态响应等于阶跃响应的二次积分：
   $$y_{zs}(t) = \\int_0^t g(\\tau)d\\tau = \\int_0^t \\frac{1}{2}(1 - e^{-2\\tau})d\\tau = \\frac{1}{2}\\left[ \\tau + \\frac{1}{2}e^{-2\\tau} \\right]_0^t$$
4. 代入限值化简：
   $$y_{zs}(t) = \\frac{1}{2}\\left[ t + \\frac{1}{2}e^{-2t} - \\frac{1}{2} \\right] = \\frac{1}{4}(2t - 1 + e^{-2t})\\varepsilon(t)$$
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
   - 乘以 2：$2 \\times [3, 1, 7, 2] = [6, 2, 14, 4]$
   - 乘以 3（错开 1 位）：$3 \\times [3, 1, 7, 2] = [0, 9, 3, 21, 6]$
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
    "stem": "已知连续信号满足 $f(t) * \\delta(t + 1) * g(t) = s(t)$，则二阶导数 $s''(t)$ 等于：",
    "options": [
      { "key": "A", "text": "$g''(t) * f(t + 1)$" },
      { "key": "B", "text": "$g''(t) * f(t - 1)$" },
      { "key": "C", "text": "$g'(t) * f'(t + 1)$" },
      { "key": "D", "text": "$g(t) * f''(t - 1)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：时域卷积的微分性质与冲激平移性质。

1. 冲激函数的卷积平移性质：
   $$f(t) * \\delta(t + 1) = f(t + 1)$$
   因此原式化简为：
   $$s(t) = f(t + 1) * g(t)$$
2. 根据卷积的微分性质：
   $$\\frac{d^2}{dt^2}[x(t) * y(t)] = x''(t) * y(t) = x(t) * y''(t) = x'(t) * y'(t)$$
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
    "stem": "已知序列 $f_1(k) = \\{\\underline{1}, 2, 3\\}$，$f_2(k) = \\{\\underline{1}, 1, 1, 1\\}$，令 $f(k) = f_1(k) * f_2(k)$，则 $f(2)$ 的数值为：",
    "options": [
      { "key": "A", "text": "3" },
      { "key": "B", "text": "6" },
      { "key": "C", "text": "5" },
      { "key": "D", "text": "1" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：离散卷积单点数值的定义求法。

1. 根据卷积和公式：
   $$f(2) = \\sum_{m=0}^2 f_1(m) f_2(2 - m)$$
2. 展开各项相加：
   - $m = 0$: $f_1(0)f_2(2) = 1 \\times 1 = 1$
   - $m = 1$: $f_1(1)f_2(1) = 2 \\times 1 = 2$
   - $m = 2$: $f_1(2)f_2(0) = 3 \\times 1 = 3$
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
    "stem": "计算连续卷积表达式 $t\\varepsilon(t) * \\varepsilon(t - 1)$ 的化简结果为：",
    "options": [
      { "key": "A", "text": "$\\frac{1}{2}(t - 1)^2 \\varepsilon(t - 1)$" },
      { "key": "B", "text": "$\\frac{1}{2}t^2 \\varepsilon(t - 1)$" },
      { "key": "C", "text": "$(t - 1)\\varepsilon(t - 1)$" },
      { "key": "D", "text": "$\\frac{1}{2}(t^2 - 1)\\varepsilon(t - 1)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：连续卷积的时移性质 $x(t) * y(t - t_0) = [x * y](t - t_0)$。

1. 已知基础卷积：
   $$t\\varepsilon(t) * \\varepsilon(t) = \\frac{1}{2}t^2 \\varepsilon(t)$$
2. 由于第二个信号为时移信号 $\\varepsilon(t - 1)$，时延 $t_0 = 1$；
3. 根据时不变系统的时移性质，总输出结果只需在基础卷积结果上整体右移 1：
   $$t\\varepsilon(t) * \\varepsilon(t - 1) = \\left[ \\frac{1}{2}t^2 \\varepsilon(t) \\right]_{t \\to t-1} = \\frac{1}{2}(t - 1)^2 \\varepsilon(t - 1)$$
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
    "stem": "宽度为 $\\tau$、高度为 1 的对称门函数 $f(t) = \\text{rect}(t/\\tau)$（即 $-\\frac{\\tau}{2} \\le t \\le \\frac{\\tau}{2}$ 时为 1），其自身卷积 $f(t) * f(t)$ 的波形是：",
    "options": [
      { "key": "A", "text": "底宽为 $2\\tau$、峰值为 $\\tau$ 的对称三角脉冲" },
      { "key": "B", "text": "底宽为 $\\tau$、峰值为 1 的对称三角脉冲" },
      { "key": "C", "text": "宽度为 $2\\tau$、高度为 1 的矩形脉冲" },
      { "key": "D", "text": "宽度为 $2\\tau$、高度为 $\\tau$ 的梯形脉冲" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：矩形脉冲时域自卷积的几何特性。

1. 时长叠加法则：两个时长均为 $\\tau$ 的时间有限信号做卷积，卷积结果的时长严格为 $\\tau + \\tau = 2\\tau$，非零区间为 $[-\\tau, \\tau]$；
2. 几何图解：两个高度为 1、宽度为 $\\tau$ 的矩形在相对滑动时，重叠面积随移动距离 $|t|$ 呈线性增减：
   $$[f * f](t) = (\\tau - |t|), \\quad |t| \\le \\tau$$
3. 在 $t = 0$ 处重叠面积达到最大值，即峰值为 $\\tau$；
4. 因此卷积波形为底宽 $2\\tau$、高度为 $\\tau$ 的等腰三角脉冲。
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
    "stem": "已知离散系统满足差分方程 $y(k) - 0.5y(k - 1) = \\varepsilon(k)$，初始状态 $y(-1) = 2$，则系统的全响应 $y(k)\\,(k \\ge 0)$ 为：",
    "options": [
      { "key": "A", "text": "$[2 - (0.5)^k]\\varepsilon(k)$" },
      { "key": "B", "text": "$2\\varepsilon(k)$" },
      { "key": "C", "text": "$[1 + (0.5)^k]\\varepsilon(k)$" },
      { "key": "D", "text": "$[(0.5)^k]\\varepsilon(k)$" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：一阶差分方程时域古典法求解（零输入 + 零状态响应）。

1. **求特征根与齐次解形式**：
   特征方程 $\\alpha - 0.5 = 0 \\implies \\alpha = 0.5$；
   齐次解形式为 $C (0.5)^k$；
2. **零输入响应 $y_{zi}(k)$**：
   由无激励方程 $y(k) - 0.5y(k-1) = 0$：
   当 $k = 0$ 时，$y_{zi}(0) = 0.5 y(-1) = 0.5 \\times 2 = 1$；
   由于 $y_{zi}(k) = C_{zi}(0.5)^k$，故 $C_{zi} = 1 \\implies y_{zi}(k) = (0.5)^k \\varepsilon(k)$；
3. **零状态响应 $y_{zs}(k)$**：
   特解设为常数 $K$：$K - 0.5K = 1 \\implies K = 2$；
   全零状态解 $y_{zs}(k) = 2 + C_{zs}(0.5)^k$；
   因零状态条件 $y_{zs}(-1) = 0 \\implies y_{zs}(0) = 0.5(0) + 1 = 1$；
   代入 $k = 0$：$2 + C_{zs} = 1 \\implies C_{zs} = -1$；
   $$y_{zs}(k) = [2 - (0.5)^k]\\varepsilon(k)$$
4. **全响应叠加**：
   $$y(k) = y_{zi}(k) + y_{zs}(k) = (0.5)^k + 2 - (0.5)^k = 2\\varepsilon(k)$$
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
    "stem": "已知离散单位样值响应 $h(n) = u(n) - u(n - 3)$，输入序列为 $x(n) = u(n)$，则卷积输出 $y(n) = h(n) * x(n)$ 在 $n \\ge 2$ 时的稳态数值恒为：",
    "options": [
      { "key": "A", "text": "3" },
      { "key": "B", "text": "2" },
      { "key": "C", "text": "1" },
      { "key": "D", "text": "$n + 1$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：有限长矩形窗序列与单位阶跃序列的时域卷积。

1. 单位样值响应 $h(n) = u(n) - u(n - 3) = \\delta(n) + \\delta(n - 1) + \\delta(n - 2)$，非零样值点只有 3 个，且幅度均为 1；
2. 由卷积分配律：
   $$y(n) = x(n) * h(n) = u(n) * [\\delta(n) + \\delta(n - 1) + \\delta(n - 2)] = u(n) + u(n - 1) + u(n - 2)$$
3. 当 $n \\ge 2$ 时：
   三个阶跃项 $u(n), u(n-1), u(n-2)$ 均已触发并保持为 1；
   $$y(n) = 1 + 1 + 1 = 3$$
故在 $n \\ge 2$ 时其数值恒为 **3**。选 **A**。"""
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
   - 正常情况下，$y_{zs}(t) = y_{zs, \\text{nat}} + y_{zs, \\text{forced}}$。
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
    "stem": "已知实信号 $f(t) = 5 - 6\\cos\\left(t - \\frac{\\pi}{6}\\right) + 4\\sin\\left(\\frac{3}{2}t + \\frac{\\pi}{4}\\right)$，则该信号的基波角频率 $\\omega_0$ 为：",
    "options": [
      { "key": "A", "text": "$0.5\\text{ rad/s}$" },
      { "key": "B", "text": "$1.0\\text{ rad/s}$" },
      { "key": "C", "text": "$1.5\\text{ rad/s}$" },
      { "key": "D", "text": "$2.0\\text{ rad/s}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：复合周期信号的基波角频率求解（最大公约数法）。

1. 信号中包含两个非直流正弦分量：
   - 第一个交流分量角频率：$\\omega_1 = 1\\text{ rad/s}$；
   - 第二个交流分量角频率：$\\omega_2 = \\frac{3}{2} = 1.5\\text{ rad/s}$；
2. 连续复合周期信号的基波角频率 $\\omega_0$ 是各分量角频率的最大公约数：
   $$\\omega_0 = \\gcd\\left(1, \\frac{3}{2}\\right) = \\gcd\\left(\\frac{2}{2}, \\frac{3}{2}\\right) = \\frac{\\gcd(2, 3)}{2} = \\frac{1}{2} = 0.5\\text{ rad/s}$$
3. 验证谐波次数：
   - $\\omega_1 = 2\\omega_0$（2次谐波）；
   - $\\omega_2 = 3\\omega_0$（3次谐波）；
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
    "stem": "已知某稳定连续 LTI 系统，当输入 $f(t) = e^{j 5t}$ 时，稳态响应为 $y(t) = e^{j 3t}$；当输入 $f(t) = e^{-j 5t}$ 时，稳态响应为 $y(t) = e^{-j 3t}$。若输入信号为 $f(t) = \\cos(5t - 2)$，则系统的稳态输出 $y(t)$ 为：",
    "options": [
      { "key": "A", "text": "$\\cos(3t - 2)$" },
      { "key": "B", "text": "$\\cos(5t - 2)$" },
      { "key": "C", "text": "$\\sin(3t - 2)$" },
      { "key": "D", "text": "$e^{j(3t - 2)}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：连续线性系统的频域特征映射与欧拉公式分解。

1. 由欧拉公式展开实余弦激励信号：
   $$f(t) = \\cos(5t - 2) = \\frac{1}{2}e^{j(5t - 2)} + \\frac{1}{2}e^{-j(5t - 2)} = \\frac{1}{2}e^{-j 2} \\cdot e^{j 5t} + \\frac{1}{2}e^{j 2} \\cdot e^{-j 5t}$$
2. 由题意，系统对基底虚指数信号的频域映射关系为：
   - $e^{j 5t} \\to e^{j 3t}$
   - $e^{-j 5t} \\to e^{-j 3t}$
3. 由线性系统的齐次性与可加性，稳态响应为：
   $$y(t) = \\frac{1}{2}e^{-j 2} \\cdot e^{j 3t} + \\frac{1}{2}e^{j 2} \\cdot e^{-j 3t} = \\frac{1}{2}e^{j(3t - 2)} + \\frac{1}{2}e^{-j(3t - 2)} = \\cos(3t - 2)$$
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
    "stem": "信号 $f(t) = \\frac{1}{t^2 + 1}$ 的傅里叶变换 $F(j\\omega)$ 为：",
    "options": [
      { "key": "A", "text": "$\\pi e^{-|\\omega|}$" },
      { "key": "B", "text": "$2\\pi e^{-|\\omega|}$" },
      { "key": "C", "text": "$\\frac{1}{2}\\pi e^{-|\\omega|}$" },
      { "key": "D", "text": "$e^{-|\\omega|}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：傅里叶变换的对称性质（对偶性 Duality Property）。

1. 熟知基本双边实指数信号的傅里叶变换对：
   $$e^{-a |t|} \\stackrel{\\mathcal{F}}{\\longleftrightarrow} \\frac{2a}{\\omega^2 + a^2}$$
   当 $a = 1$ 时：
   $$e^{-|t|} \\stackrel{\\mathcal{F}}{\\longleftrightarrow} \\frac{2}{\\omega^2 + 1}$$
2. 根据傅里叶变换的对偶性原理：若 $f(t) \\leftrightarrow F(\\omega)$，则 $F(t) \\leftrightarrow 2\\pi f(-\\omega)$：
   $$\\frac{2}{t^2 + 1} \\stackrel{\\mathcal{F}}{\\longleftrightarrow} 2\\pi e^{-|-\\omega|} = 2\\pi e^{-|\\omega|}$$
3. 两边同除以 2 得到：
   $$\\frac{1}{t^2 + 1} \\stackrel{\\mathcal{F}}{\\longleftrightarrow} \\pi e^{-|\\omega|}$$
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
    "stem": "已知某稳定连续 LTI 系统的频率响应为 $H(j\\omega) = \\frac{1}{1 + j\\omega}$，当输入激励为 $f(t) = \\cos(t)$ 时，系统的稳态响应 $y_{ss}(t)$ 为：",
    "options": [
      { "key": "A", "text": "$\\frac{1}{\\sqrt{2}}\\cos\\left(t - \\frac{\\pi}{4}\\right)$" },
      { "key": "B", "text": "$\\frac{1}{\\sqrt{2}}\\cos\\left(t + \\frac{\\pi}{4}\\right)$" },
      { "key": "C", "text": "$\\cos\\left(t - \\frac{\\pi}{4}\\right)$" },
      { "key": "D", "text": "$\\frac{1}{2}\\cos(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：稳定 LTI 系统的稳态正弦响应计算。

1. 输入信号频率为 $\\omega_0 = 1\\text{ rad/s}$；
2. 计算系统在 $\\omega_0 = 1$ 处的频率响应复数值：
   $$H(j 1) = \\frac{1}{1 + j 1} = \\frac{1}{\\sqrt{2}}e^{-j \\frac{\\pi}{4}}$$
   - 幅度增益：$|H(j 1)| = \\frac{1}{\\sqrt{1^2 + 1^2}} = \\frac{1}{\\sqrt{2}}$；
   - 相位滞后：$\\theta(1) = -\\arctan(1) = -\\frac{\\pi}{4}$；
3. 稳态输出响应为：
   $$y_{ss}(t) = |H(j 1)| \\cos(t + \\theta(1)) = \\frac{1}{\\sqrt{2}}\\cos\\left(t - \\frac{\\pi}{4}\\right)$$
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
    "stem": "一个连续 LTI 系统若要实现信号的无失真传输（Distortionless Transmission），其系统频率响应 $H(j\\omega)$ 必须满足的条件是：",
    "options": [
      { "key": "A", "text": "$|H(j\\omega)| = K$（常数），且 $\\theta(\\omega) = -\\omega t_d$（线性相位）" },
      { "key": "B", "text": "$|H(j\\omega)| = K\\omega$，且 $\\theta(\\omega) = 0$" },
      { "key": "C", "text": "$|H(j\\omega)| = 1$，且 $\\theta(\\omega) = -\\omega^2 t_d$" },
      { "key": "D", "text": "$H(j\\omega) = \\delta(\\omega - \\omega_0)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：无失真传输系统的时域波形与频域幅相要求。

1. **时域定义**：输出响应波形仅允许发生幅度比例缩放 $K$ 和恒定时延 $t_d$，波形形状严格不变：
   $$y(t) = K f(t - t_d)$$
2. **频域推导**：对时域关系进行傅里叶变换：
   $$Y(j\\omega) = K e^{-j\\omega t_d} F(j\\omega) \\implies H(j\\omega) = \\frac{Y(j\\omega)}{F(j\\omega)} = K e^{-j\\omega t_d}$$
3. **两个核心条件**：
   - **幅频特性恒定**：$|H(j\\omega)| = K$（避免各频率分量增益不一导致的幅度失真）；
   - **相频特性线性**：$\\theta(\\omega) = -\\omega t_d$（群时延 $\\tau_g(\\omega) = -\\frac{d\\theta}{d\\omega} = t_d$ 为常数，避免各频率到达时间不一导致的相位失真）。
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
    "stem": "若连续时间信号 $f(t)$ 为实偶信号（即 $f^*(t) = f(t)$ 且 $f(-t) = f(t)$），则其傅里叶变换 $F(j\\omega)$ 必定是：",
    "options": [
      { "key": "A", "text": "实偶函数" },
      { "key": "B", "text": "虚奇函数" },
      { "key": "C", "text": "实奇函数" },
      { "key": "D", "text": "虚偶函数" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：傅里叶变换的时域奇偶性与频域对称性对应表。

1. 连续傅里叶变换定义：$F(j\\omega) = \\int_{-\\infty}^\\infty f(t) e^{-j\\omega t} dt = \\int_{-\\infty}^\\infty f(t)[\\cos(\\omega t) - j\\sin(\\omega t)] dt$；
2. 当 $f(t)$ 为实偶函数时：
   - $f(t)\\cos(\\omega t)$ 为偶函数，积分结果为实数且为 $\\omega$ 的偶函数；
   - $f(t)\\sin(\\omega t)$ 为奇函数，在对称区间 $[-\\infty, +\\infty]$ 上积分为零；
3. 因此虚部完全为 0，$F(j\\omega)$ 为纯**实偶函数**。
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
    "stem": "符号函数 $f(t) = \\text{sgn}(t)$ 的傅里叶变换 $F(j\\omega)$ 为：",
    "options": [
      { "key": "A", "text": "$\\frac{2}{j\\omega}$" },
      { "key": "B", "text": "$\\frac{1}{j\\omega}$" },
      { "key": "C", "text": "$\\pi\\delta(\\omega) + \\frac{1}{j\\omega}$" },
      { "key": "D", "text": "$-\\frac{2}{j\\omega}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：符号函数 $\\text{sgn}(t)$ 的标准傅里叶变换对。

1. 符号函数定义：
   $$\\text{sgn}(t) = \\begin{cases} 1, & t > 0 \\\\ -1, & t < 0 \\end{cases} = \\lim_{\\alpha \\to 0} [e^{-\\alpha t}\\varepsilon(t) - e^{\\alpha t}\\varepsilon(-t)]$$
2. 利用频域极限变换：
   $$F(j\\omega) = \\lim_{\\alpha \\to 0} \\left( \\frac{1}{\\alpha + j\\omega} - \\frac{1}{\\alpha - j\\omega} \\right) = \\lim_{\\alpha \\to 0} \\frac{-2j\\omega}{\\alpha^2 + \\omega^2} = \\frac{2}{j\\omega}$$
3. 符号函数是实奇信号，其频谱为纯虚奇函数，完全吻合 $\\frac{2}{j\\omega} = -j \\frac{2}{\\omega}$。
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
    "stem": "单位阶跃信号 $\\varepsilon(t)$ 的傅里叶变换为：",
    "options": [
      { "key": "A", "text": "$\\pi\\delta(\\omega) + \\frac{1}{j\\omega}$" },
      { "key": "B", "text": "$\\frac{1}{j\\omega}$" },
      { "key": "C", "text": "$2\\pi\\delta(\\omega) + \\frac{1}{j\\omega}$" },
      { "key": "D", "text": "$\\frac{1}{s}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：单位阶跃函数的奇偶分解法求傅里叶变换。

1. 将单位阶跃分解为直流直流直流分量与奇信号（符号函数）之和：
   $$\\varepsilon(t) = \\frac{1}{2} + \\frac{1}{2}\\text{sgn}(t)$$
2. 逐项应用常用傅里叶变换对：
   - 直流常数信号：$\\frac{1}{2} \\leftrightarrow \\frac{1}{2} \\times 2\\pi \\delta(\\omega) = \\pi \\delta(\\omega)$
   - 符号函数：$\\frac{1}{2}\\text{sgn}(t) \\leftrightarrow \\frac{1}{2} \\times \\frac{2}{j\\omega} = \\frac{1}{j\\omega}$
3. 叠加得到：
   $$\\varepsilon(t) \\stackrel{\\mathcal{F}}{\\longleftrightarrow} \\pi\\delta(\\omega) + \\frac{1}{j\\omega}$$
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
    "stem": "计算正弦平方信号 $f(t) = \\sin^2(t)$ 的傅里叶变换 $F(j\\omega)$ 为：",
    "options": [
      { "key": "A", "text": "$\\pi\\delta(\\omega) - \\frac{\\pi}{2}[\\delta(\\omega - 2) + \\delta(\\omega + 2)]$" },
      { "key": "B", "text": "$\\pi\\delta(\\omega) + \\frac{\\pi}{2}[\\delta(\\omega - 2) + \\delta(\\omega + 2)]$" },
      { "key": "C", "text": "$2\\pi\\delta(\\omega) - \\pi\\delta(\\omega - 2)$" },
      { "key": "D", "text": "$\\frac{\\pi}{2}[\\delta(\\omega - 1) + \\delta(\\omega + 1)]$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：三角恒等变换与余弦信号的傅里叶变换对。

1. 利用三角降幂公式将平方展开：
   $$\\sin^2(t) = \\frac{1 - \\cos(2t)}{2} = \\frac{1}{2} - \\frac{1}{2}\\cos(2t)$$
2. 分别求两项的傅里叶变换：
   - 直流常数项：$\\frac{1}{2} \\leftrightarrow \\frac{1}{2} \\times 2\\pi \\delta(\\omega) = \\pi \\delta(\\omega)$；
   - 余弦交流项：$\\cos(2t) \\leftrightarrow \\pi[\\delta(\\omega - 2) + \\delta(\\omega + 2)]$，带入系数 $-\\frac{1}{2}$；
3. 合并得：
   $$F(j\\omega) = \\pi\\delta(\\omega) - \\frac{\\pi}{2}[\\delta(\\omega - 2) + \\delta(\\omega + 2)]$$
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
    "stem": "已知频谱函数 $F(\\omega) = \\text{sgn}(\\omega)$，则其对应的原时域信号 $f(t)$ 为：",
    "options": [
      { "key": "A", "text": "$\\frac{j}{\\pi t}$" },
      { "key": "B", "text": "$-\\frac{j}{\\pi t}$" },
      { "key": "C", "text": "$\\frac{1}{\\pi t}$" },
      { "key": "D", "text": "$\\frac{2}{j t}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：傅里叶变换对偶性质对奇异信号的运用。

1. 熟知基础变换对：
   $$\\text{sgn}(t) \\stackrel{\\mathcal{F}}{\\longleftrightarrow} \\frac{2}{j\\omega} = -j \\frac{2}{\\omega}$$
2. 由对偶性质：若 $x(t) \\leftrightarrow X(\\omega)$，则 $X(t) \\leftrightarrow 2\\pi x(-\\omega)$：
   $$-j \\frac{2}{t} \\stackrel{\\mathcal{F}}{\\longleftrightarrow} 2\\pi \\text{sgn}(-\\omega) = -2\\pi \\text{sgn}(\\omega)$$
3. 两边同乘以 $-\\frac{1}{2\\pi}$：
   $$\\text{sgn}(\\omega) \\stackrel{\\mathcal{F}^{-1}}{\\longleftrightarrow} \\left(-\\frac{1}{2\\pi}\\right) \\left(-j \\frac{2}{t}\\right) = \\frac{j}{\\pi t}$$
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
    "stem": "连续系统频响为 $H(j\\omega) = \\frac{1}{1 + j\\omega}$，当输入为 $f(t) = \\sin(2t)$ 时，其稳态响应 $y_{ss}(t)$ 为：",
    "options": [
      { "key": "A", "text": "$\\frac{1}{\\sqrt{5}}\\sin(2t - \\arctan 2)$" },
      { "key": "B", "text": "$\\frac{1}{\\sqrt{5}}\\sin(2t + \\arctan 2)$" },
      { "key": "C", "text": "$\\frac{1}{3}\\sin(2t)$" },
      { "key": "D", "text": "$\\frac{1}{\\sqrt{5}}\\cos(2t - \\arctan 2)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：稳态正弦响应的模值与相位角计算。

1. 正弦激励信号角频率 $\\omega_0 = 2\\text{ rad/s}$；
2. 计算系统在 $\\omega_0 = 2$ 处的频响：
   $$H(j 2) = \\frac{1}{1 + j 2}$$
   - 幅频特性：$|H(j 2)| = \\frac{1}{\\sqrt{1^2 + 2^2}} = \\frac{1}{\\sqrt{5}}$；
   - 相频特性：$\\theta(2) = -\\arctan(2)$；
3. 输出为同频正弦波，幅度乘模长，初相加相位偏移：
   $$y_{ss}(t) = \\frac{1}{\\sqrt{5}}\\sin(2t - \\arctan 2)$$
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
    "stem": "某理想带通滤波器的通带频率范围为 $2 \\le |\\omega| \\le 7\\text{ rad/s}$，在此区间内增益为 1，其余频率增益为 0。若输入信号为 $f(t) = 2 + 3\\cos(3t) - 5\\sin(6t - 30^\\circ) + 4\\sin(13t - 20^\\circ)$，则滤波器的稳态输出响应 $y(t)$ 为：",
    "options": [
      { "key": "A", "text": "$3\\cos(3t) - 5\\sin(6t - 30^\\circ)$" },
      { "key": "B", "text": "$2 + 3\\cos(3t) - 5\\sin(6t - 30^\\circ)$" },
      { "key": "C", "text": "$4\\sin(13t - 20^\\circ)$" },
      { "key": "D", "text": "0" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：频带选择滤波器的各频率分量判别。

1. 逐个分析输入信号各分量的角频率：
   - 直流分量：$2$，对应频率 $\\omega = 0 \\notin [2, 7]$，被完全滤除（增益为 0）；
   - 第二项：$3\\cos(3t)$，对应频率 $\\omega = 3 \\in [2, 7]$，落在通带内，无衰减通过；
   - 第三项：$-5\\sin(6t - 30^\\circ)$，对应频率 $\\omega = 6 \\in [2, 7]$，落在通带内，无衰减通过；
   - 第四项：$4\\sin(13t - 20^\\circ)$，对应频率 $\\omega = 13 \\notin [2, 7]$，被完全滤除（增益为 0）；
2. 线性叠加通带内分量：
   $$y(t) = 3\\cos(3t) - 5\\sin(6t - 30^\\circ)$$
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
    "stem": "计算频谱函数 $F(\\omega) = -\\pi |\\omega|$ 的傅里叶逆变换 $f(t)$ 为：",
    "options": [
      { "key": "A", "text": "$\\frac{1}{t^2}$" },
      { "key": "B", "text": "$-\\frac{1}{t^2}$" },
      { "key": "C", "text": "$\\frac{1}{t}$" },
      { "key": "D", "text": "$\\frac{2}{t^2}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：傅里叶变换的频域微分与时域对偶性质。

1. 已知基础对：$t \\text{sgn}(t) = |t|$，其傅里叶变换为：
   $$|t| \\stackrel{\\mathcal{F}}{\\longleftrightarrow} -\\frac{2}{\\omega^2}$$
2. 根据对偶性：若 $x(t) \\leftrightarrow X(\\omega)$，则 $X(t) \\leftrightarrow 2\\pi x(-\\omega)$：
   $$-\\frac{2}{t^2} \\stackrel{\\mathcal{F}}{\\longleftrightarrow} 2\\pi |-\\omega| = 2\\pi |\\omega|$$
3. 两边同除以 $-2$：
   $$\\frac{1}{t^2} \\stackrel{\\mathcal{F}}{\\longleftrightarrow} -\\pi |\\omega|$$
故频谱 $F(\\omega) = -\\pi |\\omega|$ 对应的时域信号为 $\\frac{1}{t^2}$。选 **A**。"""
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
   $$f(at) \\stackrel{\\mathcal{F}}{\\longleftrightarrow} \\frac{1}{|a|} F\\left(\\frac{\\omega}{a}\\right)$$
2. 当时域波形在时间轴上展宽时（$|a| < 1$），频域自变量将被压缩除以 $a$，频带变窄；
3. 时域脉冲持续有效宽度 $\\Delta t$ 与频域有效带宽 $\\Delta \\omega$ 满足乘积下界约束：
   $$\\Delta t \\cdot \\Delta \\omega \\ge \\text{Const}$$
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
    "stem": "周期为 $T$ 的连续信号满足半波对称关系 $f(t) = -f(t \\pm \\frac{T}{2})$（奇谐函数），则其傅里叶级数展开式中：",
    "options": [
      { "key": "A", "text": "只包含奇次谐波分量（$n = 1, 3, 5, \\dots$），直流与偶次谐波为 0" },
      { "key": "B", "text": "只包含偶次谐波分量（$n = 2, 4, 6, \\dots$）" },
      { "key": "C", "text": "只包含正弦项，余弦项全部为 0" },
      { "key": "D", "text": "所有谐波分量系数均不为 0" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：半波对称波形（奇谐函数）的频域级数特征。

1. 半波奇对称数学定义：$f(t) = -f(t - \\frac{T}{2})$；
2. 计算其指数形式傅里叶级数系数 $F_n$：
   $$F_n = \\frac{1}{T}\\int_0^T f(t)e^{-jn\\omega_0 t}dt = \\frac{1}{T}\\left[ \\int_0^{T/2} f(t)e^{-jn\\omega_0 t}dt + \\int_{T/2}^T f(t)e^{-jn\\omega_0 t}dt \\right]$$
3. 对后半周做换元 $\\tau = t - \\frac{T}{2}$：
   $$F_n = \\frac{1}{T}\\int_0^{T/2} f(t)e^{-jn\\omega_0 t}[1 - e^{-jn\\pi}]dt = \\frac{1 - (-1)^n}{T}\\int_0^{T/2} f(t)e^{-jn\\omega_0 t}dt$$
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
    "stem": "连续能量信号 $f(t)$ 的傅里叶变换为 $F(j\\omega)$，根据帕塞瓦尔定理（Parseval's Theorem），时域总能量与频域能量谱密度的定量关系为：",
    "options": [
      { "key": "A", "text": "$\\int_{-\\infty}^\\infty |f(t)|^2 dt = \\frac{1}{2\\pi}\\int_{-\\infty}^\\infty |F(j\\omega)|^2 d\\omega$" },
      { "key": "B", "text": "$\\int_{-\\infty}^\\infty |f(t)|^2 dt = \\int_{-\\infty}^\\infty |F(j\\omega)|^2 d\\omega$" },
      { "key": "C", "text": "$\\int_{-\\infty}^\\infty |f(t)|^2 dt = 2\\pi\\int_{-\\infty}^\\infty |F(j\\omega)|^2 d\\omega$" },
      { "key": "D", "text": "$\\int_{-\\infty}^\\infty |f(t)|^2 dt = \\frac{1}{\\pi}\\int_{-\\infty}^\\infty |F(j\\omega)|^2 d\\omega$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：帕塞瓦尔能量守恒定理标准数学公式。

1. 物理本质：信号在时域的总能量与在频域全频带范围积分的总能量严格守恒；
2. 标准公式：
   $$E = \\int_{-\\infty}^{+\\infty} |f(t)|^2 dt = \\frac{1}{2\\pi}\\int_{-\\infty}^{+\\infty} |F(j\\omega)|^2 d\\omega = \\int_{-\\infty}^{+\\infty} |F(j 2\\pi f)|^2 df$$
   注意当对角频率 $\\omega$ 积分时，公式前必须带系数 $\\frac{1}{2\\pi}$。
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
    "stem": "基带信号 $f(t)$ 的最高截止角频率为 $\\omega_m$。经载波调制后得到信号 $y(t) = f(t)\\cos(\\omega_c t)$（其中 $\\omega_c \\gg \\omega_m$），则已调信号 $y(t)$ 的频谱范围为：",
    "options": [
      { "key": "A", "text": "$[\\omega_c - \\omega_m, \\, \\omega_c + \\omega_m]$ 与 $[-\\omega_c - \\omega_m, \\, -\\omega_c + \\omega_m]$" },
      { "key": "B", "text": "$[-\\omega_m, \\, \\omega_m]$" },
      { "key": "C", "text": "$[0, \\, \\omega_c + \\omega_m]$" },
      { "key": "D", "text": "$[2\\omega_c - \\omega_m, \\, 2\\omega_c + \\omega_m]$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：频移特性与正弦调幅频谱搬移。

1. 傅里叶变换的频移定理：
   $$f(t)e^{\\pm j\\omega_c t} \\stackrel{\\mathcal{F}}{\\longleftrightarrow} F(j(\\omega \\mp \\omega_c))$$
2. 利用欧拉公式展开载波：
   $$y(t) = f(t) \\left[ \\frac{e^{j\\omega_c t} + e^{-j\\omega_c t}}{2} \\right] = \\frac{1}{2}f(t)e^{j\\omega_c t} + \\frac{1}{2}f(t)e^{-j\\omega_c t}$$
3. 对应的频谱为：
   $$Y(j\\omega) = \\frac{1}{2}F(j(\\omega - \\omega_c)) + \\frac{1}{2}F(j(\\omega + \\omega_c))$$
4. 原信号频谱集中在 $[-\\omega_m, \\omega_m]$，调制后被分别搬移至正负载频 $\\pm \\omega_c$ 处，正频带范围为 $[\\omega_c - \\omega_m, \\omega_c + \\omega_m]$，带宽加倍为 $2\\omega_m$。
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
    "stem": "信号 $f(t) = t e^{-a t}\\varepsilon(t)\\, (a > 0)$ 的傅里叶变换 $F(j\\omega)$ 为：",
    "options": [
      { "key": "A", "text": "$\\frac{1}{(a + j\\omega)^2}$" },
      { "key": "B", "text": "$\\frac{j\\omega}{(a + j\\omega)^2}$" },
      { "key": "C", "text": "$\\frac{1}{a^2 + \\omega^2}$" },
      { "key": "D", "text": "$\\frac{a}{(a + j\\omega)^2}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：时域乘以自变量 $t$ 对应的频域微分性质。

1. 频域微分性质公式：
   $$t f(t) \\stackrel{\\mathcal{F}}{\\longleftrightarrow} j \\frac{d}{d\\omega} F(j\\omega)$$
2. 基础单边指数变换对：
   $$e^{-a t}\\varepsilon(t) \\stackrel{\\mathcal{F}}{\\longleftrightarrow} \\frac{1}{a + j\\omega}$$
3. 对频域表达式关于 $\\omega$ 求导：
   $$\\frac{d}{d\\omega}\\left[ \\frac{1}{a + j\\omega} \\right] = -\\frac{j}{(a + j\\omega)^2}$$
4. 代入公式乘以虚数单位 $j$：
   $$j \\left( -\\frac{j}{(a + j\\omega)^2} \\right) = -j^2 \\frac{1}{(a + j\\omega)^2} = \\frac{1}{(a + j\\omega)^2}$$
故选 **A**。"""
  }
]

all_questions.extend(chapter3_questions)
print(f"Added Chapter 3: {len(chapter3_questions)} questions")
'''

with open('build_full_database.py', 'a', encoding='utf-8') as f:
    f.write(c2_c3_code)

print("Appended C2 and C3 successfully!")
