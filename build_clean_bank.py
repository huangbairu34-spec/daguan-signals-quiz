import json

questions = [
  # ==========================================
  # 第一章：信号与系统基本概念及特性
  # ==========================================
  {
    "id": "ss-ch1-001",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "离散序列周期判定",
    "type": "single",
    "difficulty": 3,
    "tags": ["2024年837真题", "周期判定", "经典必考"],
    "source": "广东工业大学2024年837真题第1题",
    "stem": "已知离散序列 $f(k) = \\sin\\left(\\frac{3}{4}\\pi k + \\frac{\\pi}{3}\\right) + 2\\cos\\left(\\frac{5}{6}\\pi k + \\frac{\\pi}{4}\\right)$，则该序列的周期 $N$ 为：",
    "options": [
      { "key": "A", "text": "12" },
      { "key": "B", "text": "24" },
      { "key": "C", "text": "48" },
      { "key": "D", "text": "该序列不是周期序列" }
    ],
    "answer": "B",
    "analysis": `【核心考点】：离散正弦序列的周期性判定及最小公倍数法。

1. **第一分量分析**：
   对于 $f_1(k) = \\sin\\left(\\frac{3}{4}\\pi k + \\frac{\\pi}{3}\\right)$，其数字角频率为 $\\Omega_1 = \\frac{3}{4}\\pi$。
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
故该序列的周期为 **24**。选 **B**。`
  },
  {
    "id": "ss-ch1-002",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "连续正弦复合信号周期",
    "type": "single",
    "difficulty": 2,
    "tags": ["2022年837真题", "连续信号周期", "高频基础"],
    "source": "广东工业大学2022年837真题第1题",
    "stem": "连续时间信号 $f(t) = \\cos\\left(10t + \\frac{\\pi}{2}\\right) + \\sin\\left(20t + \\frac{\\pi}{3}\\right)$ 的基波周期 $T$ 为：",
    "options": [
      { "key": "A", "text": "$\\frac{\\pi}{10}$" },
      { "key": "B", "text": "$\\frac{\\pi}{5}$" },
      { "key": "C", "text": "$\\frac{\\pi}{20}$" },
      { "key": "D", "text": "非周期信号" }
    ],
    "answer": "B",
    "analysis": `【核心考点】：连续信号的周期性条件。

1. 第一个分量角频率 $\\omega_1 = 10\\text{ rad/s}$，周期 $T_1 = \\frac{2\\pi}{\\omega_1} = \\frac{2\\pi}{10} = \\frac{\\pi}{5}$；
2. 第二个分量角频率 $\\omega_2 = 20\\text{ rad/s}$，周期 $T_2 = \\frac{2\\pi}{\\omega_2} = \\frac{2\\pi}{20} = \\frac{\\pi}{10}$；
3. 两分量周期之比：
   $$\\frac{T_1}{T_2} = \\frac{\\pi / 5}{\\pi / 10} = 2$$
   比值为有理数，因此连续信号复合后依然为严格周期信号。
4. 总周期为 $T_1$ 和 $T_2$ 的最小公倍数：$T = \\frac{\\pi}{5}$。
故正确答案为 **B**。`
  },
  {
    "id": "ss-ch1-003",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "冲激函数微分与筛选性质",
    "type": "single",
    "difficulty": 3,
    "tags": ["2021年837真题", "广义导数", "冲激函数"],
    "source": "广东工业大学2021年837真题第1题",
    "stem": "计算广义导数 $\\frac{d}{dt} \\left\\{ [\\cos(2t) + \\sin(t)] \\varepsilon(t) \\right\\}$ 的化简结果为：",
    "options": [
      { "key": "A", "text": "$[-2\\sin(2t) + \\cos(t)]\\varepsilon(t) + \\delta(t)$" },
      { "key": "B", "text": "$[-2\\sin(2t) + \\cos(t)]\\varepsilon(t)$" },
      { "key": "C", "text": "$[-2\\sin(2t) + \\cos(t)]\\varepsilon(t) + [\\cos(2t) + \\sin(t)]\\delta(t)$" },
      { "key": "D", "text": "$-2\\sin(2t) + \\cos(t) + \\delta(t)$" }
    ],
    "answer": "A",
    "analysis": `【核心考点】：阶跃信号的导数与冲激函数筛选性质。

1. 根据乘积求导法则：
   $$\\frac{d}{dt} [f(t)\\varepsilon(t)] = f'(t)\\varepsilon(t) + f(t)\\varepsilon'(t) = f'(t)\\varepsilon(t) + f(t)\\delta(t)$$
2. 设 $f(t) = \\cos(2t) + \\sin(t)$，求导得：
   $$f'(t) = -2\\sin(2t) + \\cos(t)$$
3. 对于项 $f(t)\\delta(t)$，利用冲激函数的筛选性质 $f(t)\\delta(t) = f(0)\\delta(t)$：
   $$f(0) = \\cos(0) + \\sin(0) = 1 + 0 = 1$$
   因此：$f(t)\\delta(t) = 1 \\cdot \\delta(t) = \\delta(t)$。
4. 整理得：
   $$\\frac{d}{dt} \\left\\{ [\\cos(2t) + \\sin(t)] \\varepsilon(t) \\right\\} = [-2\\sin(2t) + \\cos(t)]\\varepsilon(t) + \\delta(t)$$
故正确选项为 **A**。`
  },
  {
    "id": "ss-ch1-004",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "冲激偶函数性质",
    "type": "single",
    "difficulty": 3,
    "tags": ["2023年837真题", "冲激偶积分", "经典必做"],
    "source": "广东工业大学2023年837真题第2题",
    "stem": "计算广义积分 $\\int_{-\\infty}^\\infty (1 - x)\\delta'(x) \\, dx$ 的值为：",
    "options": [
      { "key": "A", "text": "0" },
      { "key": "B", "text": "1" },
      { "key": "C", "text": "-1" },
      { "key": "D", "text": "2" }
    ],
    "answer": "B",
    "analysis": `【核心考点】：冲激偶函数 $\\delta'(t)$ 的积分筛选性质。

1. 冲激偶函数的积分性质公式为：
   $$\\int_{-\\infty}^\\infty f(x)\\delta'(x) \\, dx = -f'(0)$$
   （推导：分部积分法 $\\int_{-\\infty}^\\infty f(x)\\delta'(x)dx = [f(x)\\delta(x)]_{-\\infty}^\\infty - \\int_{-\\infty}^\\infty f'(x)\\delta(x)dx = 0 - f'(0) = -f'(0)$）
2. 本题中 $f(x) = 1 - x$，对 $x$ 求一阶导数：
   $$f'(x) = -1$$
   在 $x = 0$ 处的值为 $f'(0) = -1$。
3. 代入积分性质公式：
   $$\\int_{-\\infty}^\\infty (1 - x)\\delta'(x) \\, dx = -(-1) = 1$$
故正确答案为 **B**。`
  },
  {
    "id": "ss-ch1-005",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "系统的线性和时不变性判定",
    "type": "single",
    "difficulty": 3,
    "tags": ["2022年837真题", "2021年837真题", "系统特性"],
    "source": "广工837真题高频题",
    "stem": "判断系统方程 $y(k) - k y(k - 1) + y(k - 2) = f(k)$ 所描述的离散系统，其线性和时不变性属于：",
    "options": [
      { "key": "A", "text": "线性、时不变系统" },
      { "key": "B", "text": "线性、时变系统" },
      { "key": "C", "text": "非线性、时变系统" },
      { "key": "D", "text": "非线性、时不变系统" }
    ],
    "answer": "B",
    "analysis": `【核心考点】：系统五大特性的严格判定。

1. **线性判定**：
   方程中所有的激励项 $f(k)$ 与响应项 $y(k), y(k-1), y(k-2)$ 均是一次齐次项，不含非线性运算（如平方、正弦、取整）且无常数偏置项，满足可加性与齐次性：
   $$T[a f_1(k) + b f_2(k)] = a T[f_1(k)] + b T[f_2(k)]$$
   因此该系统是**线性系统**。
2. **时不变判定**：
   观察方程第二项 $-k y(k - 1)$，其系数中包含自变量 $k$。
   若输入延迟为 $f(k - k_0)$，响应所满足的方程变为：
   $$y_1(k) - k y_1(k - 1) + y_1(k - 2) = f(k - k_0)$$
   而原响应延时 $y(k - k_0)$ 满足的是：
   $$y(k - k_0) - (k - k_0) y(k - k_0 - 1) + y(k - k_0 - 2) = f(k - k_0)$$
   两者方程不相等！系数随时间推进而变，故系统是**时变系统**。
综上，该系统为**线性、时变系统**。选 **B**。`
  },

  # ==========================================
  # 第二章：连续与离散系统的时域分析
  # ==========================================
  {
    "id": "ss-ch2-001",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "离散卷积不进位乘法",
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
    "analysis": `【核心考点】：离散卷积和定义与不进位乘法。

根据离散卷积和定义式：
$$f(k) = \\sum_{m=-\\infty}^\\infty f_1(m) f_2(k - m)$$
当 $k = 3$ 时：
$$f(3) = \\sum_{m=0}^2 f_1(m) f_2(3 - m) = f_1(0)f_2(3) + f_1(1)f_2(2) + f_1(2)f_2(1)$$
由题意：
- $f_1(0) = 3, f_1(1) = 2, f_1(2) = 1$
- $f_2(0) = 1, f_2(1) = 2, f_2(2) = 2, f_2(3) = 2, f_2(4) = 6$
利用整段对齐快速计算（或不进位乘法展开式）：
展开计算 $f(3) = 24$。故选 **C**。`
  },
  {
    "id": "ss-ch2-002",
    "subject": "广工837/809-信号与系统",
    "chapter": "第二章：系统的时域分析",
    "section": "全响应分解与线性性",
    "type": "single",
    "difficulty": 4,
    "tags": ["837经典必刷", "全响应分解", "高频大题必备"],
    "source": "广工837上岸经典必刷题第7题",
    "stem": "某 LTI 连续系统具有一定的起始状态。当激励为 $f_1(t)$ 时，全响应 $y_1(t) = (2e^{-t} - \\cos\\pi t)\\varepsilon(t)$；当激励为 $2f_1(t)$ 且起始状态不变时，全响应 $y_2(t) = 3\\cos\\pi t\\,\\varepsilon(t)$。若起始状态仍不变，输入为 $4f_1(t)$ 时，全响应 $y_3(t)$ 为：",
    "options": [
      { "key": "A", "text": "$(4e^{-t} + 7\\cos\\pi t)\\varepsilon(t)$" },
      { "key": "B", "text": "$(-4e^{-t} + 11\\cos\\pi t)\\varepsilon(t)$" },
      { "key": "C", "text": "$(8e^{-t} - 5\\cos\\pi t)\\varepsilon(t)$" },
      { "key": "D", "text": "$(2e^{-t} + 5\\cos\\pi t)\\varepsilon(t)$" }
    ],
    "answer": "B",
    "analysis": `【核心考点】：全响应的双重线性分解定理。

由 LTI 系统的响应分解：
$$y(t) = y_{zi}(t) + y_{zs}(t)$$
其中：
- 零输入响应 $y_{zi}(t)$ 由历史状态决定，与当前输入无关（输入倍增时 $y_{zi}$ 保持不变）；
- 零状态响应 $y_{zs}(t)$ 由当前激励线性产生，满足齐次性与可加性（输入变为 $k$ 倍，$y_{zs}$ 变为 $k$ 倍）。

1. 建立方程：
   对于 $f_1(t)$：$y_1(t) = y_{zi}(t) + y_{zs1}(t) = 2e^{-t} - \\cos\\pi t$ ①
   对于 $2f_1(t)$：$y_2(t) = y_{zi}(t) + 2y_{zs1}(t) = 3\\cos\\pi t$ ②
2. 联立求解分量：
   ② - ① 解得零状态响应：
   $$y_{zs1}(t) = 3\\cos\\pi t - (2e^{-t} - \\cos\\pi t) = 4\\cos\\pi t - 2e^{-t}$$
   代回 ① 解得零输入响应：
   $$y_{zi}(t) = (2e^{-t} - \\cos\\pi t) - (4\\cos\\pi t - 2e^{-t}) = 4e^{-t} - 5\\cos\\pi t$$
3. 计算当激励为 $4f_1(t)$ 时的全响应：
   $$y_3(t) = y_{zi}(t) + 4 y_{zs1}(t) = (4e^{-t} - 5\\cos\\pi t) + 4(4\\cos\\pi t - 2e^{-t})$$
   $$y_3(t) = 4e^{-t} - 8e^{-t} - 5\\cos\\pi t + 16\\cos\\pi t = -4e^{-t} + 11\\cos\\pi t$$
故正确答案为 **B**。`
  },

  # ==========================================
  # 第三章：连续与离散系统的频域分析
  # ==========================================
  {
    "id": "ss-ch3-001",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "傅里叶对偶性与常用对",
    "type": "single",
    "difficulty": 3,
    "tags": ["2021年837真题", "对偶性质", "傅里叶变换"],
    "source": "广东工业大学2021年837真题第5题",
    "stem": "信号 $f(t) = \\frac{1}{t^2 + 1}$ 的傅里叶变换 $F(j\\omega)$ 为：",
    "options": [
      { "key": "A", "text": "$\\pi e^{-|\\omega|}$" },
      { "key": "B", "text": "$2\\pi e^{-|\\omega|}$" },
      { "key": "C", "text": "$\\frac{1}{1 + \\omega^2}$" },
      { "key": "D", "text": "$\\pi e^{-\\omega}$" }
    ],
    "answer": "A",
    "analysis": `【核心考点】：双边指数衰减与对偶性质求傅里叶变换。

1. **基本傅里叶变换对**：
   $$e^{-a|t|} \\stackrel{\\mathcal{F}}{\\longleftrightarrow} \\frac{2a}{a^2 + \\omega^2} \\quad (a > 0)$$
   令 $a = 1$，得到：
   $$e^{-|t|} \\stackrel{\\mathcal{F}}{\\longleftrightarrow} \\frac{2}{1 + \\omega^2}$$
2. **运用对偶性质（Duality）**：
   若 $x(t) \\stackrel{\\mathcal{F}}{\\longleftrightarrow} X(j\\omega)$，则 $X(jt) \\stackrel{\\mathcal{F}}{\\longleftrightarrow} 2\\pi x(-\\omega)$。
   将 $X(j\\omega) = \\frac{2}{1 + \\omega^2}$ 换元为 $t$：
   $$\\frac{2}{1 + t^2} \\stackrel{\\mathcal{F}}{\\longleftrightarrow} 2\\pi e^{-|-\\omega|} = 2\\pi e^{-|\\omega|}$$
3. **两边同除以 2**：
   $$\\frac{1}{t^2 + 1} \\stackrel{\\mathcal{F}}{\\longleftrightarrow} \\pi e^{-|\\omega|}$$
故正确答案为 **A**。`
  },
  {
    "id": "ss-ch3-002",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "奈奎斯特采样频率计算",
    "type": "single",
    "difficulty": 4,
    "tags": ["2024年837真题", "抽样定理", "高频考点"],
    "source": "广东工业大学2024年837真题第7题",
    "stem": "已知基带信号 $f(t) = \\text{Sa}(200\\pi t) e^{j 200\\pi t}$，则对该信号进行无失真时域取样时的最低奈奎斯特取样频率 $f_s$ 为：",
    "options": [
      { "key": "A", "text": "100 Hz" },
      { "key": "B", "text": "200 Hz" },
      { "key": "C", "text": "300 Hz" },
      { "key": "D", "text": "400 Hz" }
    ],
    "answer": "D",
    "analysis": `【核心考点】：抽样函数的频谱与频移性质综合分析。

1. **求 Sa 函数的频带范围**：
   已知 $\\text{Sa}(W t) \\stackrel{\\mathcal{F}}{\\longleftrightarrow} \\frac{\\pi}{W} G_{2W}(\\omega)$（以 $\\omega = 0$ 为中心的对称门函数，宽度为 $2W$）。
   对于 $\\text{Sa}(200\\pi t)$，其 $W = 200\\pi$，频谱分布范围为 $[-200\\pi, 200\\pi]\\text{ rad/s}$。
2. **复指数调制的频移特性**：
   根据频移性质 $x(t)e^{j \\omega_0 t} \\stackrel{\\mathcal{F}}{\\longleftrightarrow} X(j(\\omega - \\omega_0))$；
   本题中 $\\omega_0 = 200\\pi$，原频谱整体向右平移 $200\\pi$；
   搬移后的频谱范围为：
   $$[-200\\pi + 200\\pi, 200\\pi + 200\\pi] = [0, 400\\pi]\\text{ rad/s}$$
3. **确定最高截止频率与最低抽样率**：
   信号中的最高角频率为 $\\omega_{\\max} = 400\\pi\\text{ rad/s}$；
   对应物理频率为 $f_{\\max} = \\frac{\\omega_{\\max}}{2\\pi} = \\frac{400\\pi}{2\\pi} = 200\\text{ Hz}$；
   根据时域抽样定理，最低奈奎斯特抽样频率：
   $$f_s = 2 f_{\\max} = 2 \\times 200\\text{ Hz} = 400\\text{ Hz}$$
故正确答案为 **D**。`
  },
  {
    "id": "ss-ch3-003",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "LTI稳态正弦响应",
    "type": "single",
    "difficulty": 3,
    "tags": ["2025年809真题", "稳态响应", "频响特性"],
    "source": "广东工业大学2025年809真题第10题",
    "stem": "已知某 LTI 系统的频率响应为 $H(j\\omega) = \\frac{1}{1 + j\\omega}$。当输入信号为 $f(t) = \\sin(t)$ 时，系统的稳态输出 $y(t)$ 为：",
    "options": [
      { "key": "A", "text": "$\\frac{\\sqrt{2}}{2} \\sin\\left(t - \\frac{\\pi}{4}\\right)$" },
      { "key": "B", "text": "$\\frac{\\sqrt{2}}{2} \\cos\\left(t - \\frac{\\pi}{4}\\right)$" },
      { "key": "C", "text": "$\\sin\\left(t - \\frac{\\pi}{4}\\right)$" },
      { "key": "D", "text": "$\\frac{1}{2} \\sin(t)$" }
    ],
    "answer": "A",
    "analysis": `【核心考点】：频率响应对正弦激励的稳态滤波计算。

1. 输入信号为 $f(t) = \\sin(t)$，其角频率为 $\\omega = 1\\text{ rad/s}$。
2. 系统在 $\\omega = 1$ 处的频率响应：
   $$H(j 1) = \\frac{1}{1 + j 1} = \\frac{1}{\\sqrt{2} e^{j \\pi/4}} = \\frac{\\sqrt{2}}{2} e^{-j \\pi/4}$$
   其幅频增益 $|H(j 1)| = \\frac{\\sqrt{2}}{2}$，相位滞后 $\\theta = -\\frac{\\pi}{4}$。
3. 稳态输出响应为：
   $$y(t) = |H(j 1)| \\sin(t + \\theta) = \\frac{\\sqrt{2}}{2} \\sin\\left(t - \\frac{\\pi}{4}\\right)$$
故正确答案为 **A**。`
  },

  # ==========================================
  # 第四章：连续系统的复频域分析（拉普拉斯变换）
  # ==========================================
  {
    "id": "ss-ch4-001",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "部分分式展开求逆变换",
    "type": "single",
    "difficulty": 3,
    "tags": ["2023年837真题", "拉氏逆变换", "象函数展开"],
    "source": "广东工业大学2023年837真题第4题",
    "stem": "象函数 $F(s) = \\frac{s^2 + 4s + 5}{s^2 + 3s + 2}$（收敛域 $\\text{Re}(s) > -1$）的单边拉普拉斯逆变换 $f(t)$（$t \\ge 0$）为：",
    "options": [
      { "key": "A", "text": "$\\delta(t) + (2e^{-t} - e^{-2t})\\varepsilon(t)$" },
      { "key": "B", "text": "$\\delta(t) + (e^{-t} + 2e^{-2t})\\varepsilon(t)$" },
      { "key": "C", "text": "$(2e^{-t} - e^{-2t})\\varepsilon(t)$" },
      { "key": "D", "text": "$\\delta(t) - (2e^{-t} + e^{-2t})\\varepsilon(t)$" }
    ],
    "answer": "A",
    "analysis": `【核心考点】：假分式长除法与部分分式展开法。

1. 分子多项式与分母多项式阶数同为 2 阶，属于假分式，先进行多项式长除分离常数项：
   $$F(s) = \\frac{(s^2 + 3s + 2) + (s + 3)}{s^2 + 3s + 2} = 1 + \\frac{s + 3}{(s + 1)(s + 2)}$$
2. 对真分式部分进行留数展开：
   $$\\frac{s + 3}{(s + 1)(s + 2)} = \\frac{k_1}{s + 1} + \\frac{k_2}{s + 2}$$
   $$k_1 = \\left. \\frac{s + 3}{s + 2} \\right|_{s = -1} = \\frac{-1 + 3}{-1 + 2} = 2$$
   $$k_2 = \\left. \\frac{s + 3}{s + 1} \\right|_{s = -2} = \\frac{-2 + 3}{-2 + 1} = -1$$
3. 得到象函数的标准形式：
   $$F(s) = 1 + \\frac{2}{s + 1} - \\frac{1}{s + 2}$$
4. 逐项查常用拉氏变换对求逆变换：
   $$\\mathcal{L}^{-1}[1] = \\delta(t)$$
   $$\\mathcal{L}^{-1}\\left[\\frac{2}{s + 1}\\right] = 2e^{-t}\\varepsilon(t)$$
   $$\\mathcal{L}^{-1}\\left[\\frac{1}{s + 2}\\right] = e^{-2t}\\varepsilon(t)$$
5. 综合得：$f(t) = \\delta(t) + (2e^{-t} - e^{-2t})\\varepsilon(t)$。
故正确答案为 **A**。`
  },
  {
    "id": "ss-ch4-002",
    "subject": "广工837/809-信号与系统",
    "chapter": "第四章：拉普拉斯变换与复频域分析",
    "section": "最小相移与全通系统分解",
    "type": "single",
    "difficulty": 4,
    "tags": ["2024年837真题", "最小相移", "全通网络"],
    "source": "广东工业大学2024年837真题画图/分析题",
    "stem": "某稳定因果连续系统的系统函数为 $H(s) = \\frac{s - 2}{s^2 + 4s + 5}$。下列关于该系统的说法中，正确的是：",
    "options": [
      { "key": "A", "text": "零点为 $s = 2$，极点为 $s = -2 \\pm j$，该系统属于最小相移系统" },
      { "key": "B", "text": "零点位于右半开平面，该系统不是最小相移系统，但可分解为一个最小相移系统和一个全通系统" },
      { "key": "C", "text": "由于分子存在 $s - 2$，该系统不稳定" },
      { "key": "D", "text": "该系统的幅频响应为常数，属于全通系统" }
    ],
    "answer": "B",
    "analysis": `【核心考点】：最小相移系统的定义与全通分解定理。

1. **极点与稳定性**：
   分母 $s^2 + 4s + 5 = 0 \\implies s = -2 \\pm j$。极点全部严格位于左半开平面（$\\text{Re}(s) = -2 < 0$），因果系统稳定。
2. **零点与最小相移判别**：
   分子 $s - 2 = 0 \\implies s = 2$。零点位于复平面的**右半开平面**。
   根据定义：如果因果稳定系统的所有零点和极点都位于左半开平面，则称之为**最小相移系统（Minimum Phase System）**。因此该系统**不是最小相移系统**！
3. **全通分解原理**：
   将右半平面的零点反射到左半平面（$s - 2 \\to s + 2$）：
   $$H(s) = \\left( \\frac{s + 2}{s^2 + 4s + 5} \\right) \\cdot \\left( \\frac{s - 2}{s + 2} \\right) = H_{\\min}(s) \\cdot H_{ap}(s)$$
   - $H_{\\min}(s) = \\frac{s + 2}{s^2 + 4s + 5}$ 的零点与极点全在左半平面，为最小相移系统；
   - $H_{ap}(s) = \\frac{s - 2}{s + 2}$ 零极点关于虚轴对称，幅频响应 $|H_{ap}(j\\omega)| \\equiv 1$，为标准全通系统。
故正确答案为 **B**。`
  },

  # ==========================================
  # 第五章：离散系统的 Z 域分析
  # ==========================================
  {
    "id": "ss-ch5-001",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "稳定性与收敛域ROC",
    "type": "single",
    "difficulty": 3,
    "tags": ["2024年837真题", "ROC收敛域", "系统稳定性"],
    "source": "广东工业大学2024年837真题第9题",
    "stem": "已知某稳定离散系统的系统函数为 $H(z) = \\frac{z^2 + 2}{(z - 0.5)(z - 3)}$。若该系统为稳定系统，则其收敛域（ROC）应为：",
    "options": [
      { "key": "A", "text": "$|z| > 3$" },
      { "key": "B", "text": "$|z| < 0.5$" },
      { "key": "C", "text": "$0.5 < |z| < 3$" },
      { "key": "D", "text": "$|z| > 0.5$" }
    ],
    "answer": "C",
    "analysis": `【核心考点】：离散系统稳定性与收敛域（ROC）的关系。

1. **求极点分布**：
   系统函数的极点为分母根：$z_1 = 0.5, z_2 = 3$。
2. **稳定性的充要条件**：
   离散系统 BIBO 稳定的充要条件是：系统函数 $H(z)$ 的收敛域（ROC）**必须包含单位圆（$|z| = 1$）**！
3. **收敛域的三种可能形态**：
   - 若系统因果：$|z| > 3$（不包含单位圆 $|z|=1$，故不稳定）；
   - 若系统反因果：$|z| < 0.5$（不包含单位圆，不稳定）；
   - 若系统为双边非因果系统：ROC 位于两极点形成的环状区域，即 $0.5 < |z| < 3$。此时单位圆 $|z| = 1$ 恰好落在该环域内！
因此为保证系统稳定，收敛域必为 **$0.5 < |z| < 3$**。选 **C**。`
  },
  {
    "id": "ss-ch5-002",
    "subject": "广工837/809-信号与系统",
    "chapter": "第五章：Z变换与离散系统",
    "section": "离散梳状滤波器特性",
    "type": "single",
    "difficulty": 4,
    "tags": ["2022年837真题", "梳状滤波器", "幅频特性"],
    "source": "广东工业大学2022年837真题画图题",
    "stem": "离散梳状滤波器的系统函数为 $H(z) = 1 - z^{-6} = \\frac{z^6 - 1}{z^6}$。关于该系统的零极点与幅频特性，描述正确的是：",
    "options": [
      { "key": "A", "text": "原点处有 6 阶极点，单位圆上均匀分布 6 个零点 $z_k = e^{j k \\pi / 3}$（$k=0,1,\\dots,5$）" },
      { "key": "B", "text": "单位圆上有 6 个极点，原点处有 6 个零点" },
      { "key": "C", "text": "零点均在单位圆外，系统不稳定" },
      { "key": "D", "text": "幅频特性为常数 1" }
    ],
    "answer": "A",
    "analysis": `【核心考点】：梳状滤波器（Comb Filter）的零极点结构。

1. **求解极点**：
   分母为 $z^6 = 0$，故在原点 $z = 0$ 处有 6 阶重极点。因所有极点位于单位圆内，系统因果稳定。
2. **求解零点**：
   分子 $z^6 - 1 = 0 \\implies z^6 = 1 = e^{j 2\\pi k}$（$k \\in \\mathbb{Z}$）。
   解得 6 个一阶单零点为：
   $$z_k = e^{j \\frac{2\\pi k}{6}} = e^{j \\frac{\\pi k}{3}} \\quad (k = 0, 1, 2, 3, 4, 5)$$
   它们对称、均匀地分布在复平面的单位圆周上。
3. **幅频响应**：
   当 $\\omega$ 取到 $\\frac{k\\pi}{3}$ 时，单位圆上的点与零点重合，频率响应幅度骤降为零，形成若干尖锐陷波槽，外形如梳齿，故称梳状滤波器。
故正确答案为 **A**。`
  },

  # ==========================================
  # 综合真题大题与难点专攻（填空/多选/判断强化）
  # ==========================================
  {
    "id": "ss-mix-001",
    "subject": "广工837/809-信号与系统",
    "chapter": "第三章：频域分析与傅里叶变换",
    "section": "信号无失真传输条件",
    "type": "multiple",
    "difficulty": 3,
    "tags": ["无失真传输", "多选题", "高频理论"],
    "source": "广工837考研理论精选",
    "stem": "一个线性时不变（LTI）系统能够对输入信号实现“无失真传输（Distortionless Transmission）”，下列条件必须同时满足的有（多选）：",
    "options": [
      { "key": "A", "text": "系统的幅频特性必须为与频率无关的恒定常数，即 $|H(j\\omega)| = K$" },
      { "key": "B", "text": "系统的相频特性必须是通过原点的负斜率直线，即 $\\theta(\\omega) = -\\omega t_0$" },
      { "key": "C", "text": "系统冲激响应必须为时延冲激函数，即 $h(t) = K\\delta(t - t_0)$" },
      { "key": "D", "text": "系统的群时延（Group Delay）必须随频率增大而呈指数衰减" }
    ],
    "answer": ["A", "B", "C"],
    "analysis": `【核心考点】：无失真传输的充要条件。

- **无失真传输的定义**：输出信号仅允许比输入信号产生常数倍的幅度缩放和固定时间的纯时延，即：
  $$y(t) = K f(t - t_0) \\quad (K > 0, t_0 > 0)$$
- **频域分析**：
  两边取傅里叶变换：$Y(j\\omega) = K F(j\\omega) e^{-j\\omega t_0}$；
  故系统频率响应：
  $$H(j\\omega) = K e^{-j\\omega t_0}$$
  - 幅频特性 $|H(j\\omega)| = K$（常数），**A 正确**；
  - 相频特性 $\\theta(\\omega) = -\\omega t_0$（线性相位），**B 正确**；
  - 群时延 $\\tau_g(\\omega) = -\\frac{d\\theta(\\omega)}{d\\omega} = t_0$ 为恒定常数，**D 错误**；
  - 频响求傅氏逆变换得冲激响应 $h(t) = K\\delta(t - t_0)$，**C 正确**。
因此正确选项为 **A、B、C**。`
  },
  {
    "id": "ss-mix-002",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "信号功率与能量特性",
    "type": "single",
    "difficulty": 2,
    "tags": ["2022年837真题", "能量信号与功率信号", "考点点睛"],
    "source": "广东工业大学2022年837真题计算题第2题",
    "stem": "信号 $f_1(t) = e^{-2t}\\varepsilon(t)$ 的总能量 $E_1$ 和平均功率 $P_1$ 分别为：",
    "options": [
      { "key": "A", "text": "$E_1 = \\frac{1}{4}$，属于能量信号（$P_1 = 0$）" },
      { "key": "B", "text": "$E_1 = \\frac{1}{2}$，属于能量信号（$P_1 = 0$）" },
      { "key": "C", "text": "$E_1 = \\infty$，$P_1 = \\frac{1}{4}$，属于功率信号" },
      { "key": "D", "text": "$E_1 = \\infty, P_1 = 0$" }
    ],
    "answer": "A",
    "analysis": `【核心考点】：信号的能量与功率积分计算。

1. **计算总能量**：
   $$E_1 = \\int_{-\\infty}^\\infty |f_1(t)|^2 \\, dt = \\int_0^\\infty (e^{-2t})^2 \\, dt = \\int_0^\\infty e^{-4t} \\, dt$$
   $$E_1 = \\left[ -\\frac{1}{4} e^{-4t} \\right]_0^\\infty = 0 - \\left(-\\frac{1}{4}\\right) = \\frac{1}{4}$$
2. **计算平均功率**：
   $$P_1 = \\lim_{T \\to \\infty} \\frac{1}{T} \\int_{-T/2}^{T/2} |f_1(t)|^2 \\, dt = \\lim_{T \\to \\infty} \\frac{E_1}{T} = 0$$
3. **结论**：总能量有限（$0 < E_1 < \\infty$）且平均功率为 0 的信号称为**能量信号**。
故正确答案为 **A**。`
  },
  {
    "id": "ss-mix-003",
    "subject": "广工837/809-信号与系统",
    "chapter": "第一章：信号与系统基础",
    "section": "复指数信号的功率",
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
    "analysis": `【核心考点】：复指数信号与功率信号。

1. 模值计算：对于任意时间 $t$：
   $$|f_2(t)| = \\left|e^{j(2t + \\frac{\\pi}{4})}\\right| = 1$$
2. 平均功率计算：
   $$P_2 = \\lim_{T \\to \\infty} \\frac{1}{T} \\int_{-T/2}^{T/2} |f_2(t)|^2 \\, dt = \\lim_{T \\to \\infty} \\frac{1}{T} \\int_{-T/2}^{T/2} 1 \\, dt = \\lim_{T \\to \\infty} \\frac{T}{T} = 1$$
3. 总能量：
   $$E_2 = \\int_{-\\infty}^\\infty 1 \\, dt = \\infty$$
因为 $0 < P_2 < \\infty$ 且 $E_2 = \\infty$，该信号为典型的**功率信号**。选 **B**。`
  }
]

open('clean_signals_bank.json', 'w', encoding='utf-8').write(json.dumps(questions, ensure_ascii=False, indent=2))
print("Compiled", len(questions), "high-yield questions.")
