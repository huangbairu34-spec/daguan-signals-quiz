# -*- coding: utf-8 -*-
import json

c6_c7_code = '''
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
    "stem": "应用梅森增益公式（Mason Gain Formula）求解系统的传递函数 $H(s) = \\frac{1}{\\Delta} \\sum_{k} P_k \\Delta_k$ 中，特征行列式 $\\Delta$ 的表达式为：",
    "options": [
      { "key": "A", "text": "$1 - \\sum L_i + \\sum L_i L_j - \\sum L_i L_j L_k + \\dots$" },
      { "key": "B", "text": "$1 + \\sum L_i + \\sum L_i L_j + \\dots$" },
      { "key": "C", "text": "$1 - \\sum L_i - \\sum L_i L_j - \\dots$" },
      { "key": "D", "text": "$\\sum P_k L_k$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：梅森增益公式特征多项式 $\\Delta$ 的标准定义式。

1. 梅森增益公式是求解复杂信号流图或控制框图系统函数的通用法则：
   $$H(s) = \\frac{1}{\\Delta} \\sum_{k} P_k \\Delta_k$$
2. 系统特征行列式 $\\Delta$ 的定义：
   $$\\Delta = 1 - \\sum L_i + \\sum L_i L_j - \\sum L_i L_j L_k + \\dots$$
   - $\\sum L_i$ 为所有单独回路的回路增益之和；
   - $\\sum L_i L_j$ 为两两互不接触回路的增益乘积之和；
   - $\\sum L_i L_j L_k$ 为三个互不接触回路增益乘积之和；
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
      { "key": "A", "text": "$\\dot{\\mathbf{x}}(t) = \\mathbf{A}\\mathbf{x}(t) + \\mathbf{b}f(t), \\quad y(t) = \\mathbf{c}^T \\mathbf{x}(t) + d f(t)$" },
      { "key": "B", "text": "$\\mathbf{x}(t) = \\mathbf{A}\\dot{\\mathbf{x}}(t) + \\mathbf{b}f(t), \\quad y(t) = \\mathbf{c}^T \\mathbf{x}(t)$" },
      { "key": "C", "text": "$\\dot{\\mathbf{x}}(t) = \\mathbf{A}\\mathbf{x}(t) + \\mathbf{b}y(t), \\quad f(t) = \\mathbf{c}^T \\mathbf{x}(t)$" },
      { "key": "D", "text": "$\\ddot{\\mathbf{x}}(t) = \\mathbf{A}\\mathbf{x}(t) + \\mathbf{b}f(t), \\quad y(t) = \\mathbf{c}^T \\dot{\\mathbf{x}}(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：状态空间表达式（State-space Representation）标准形式。

1. **状态方程**：由一阶常微分方程组组成，描述内部状态变量向量 $\\mathbf{x}(t)$ 的时域变化率：
   $$\\dot{\\mathbf{x}}(t) = \\mathbf{A}\\mathbf{x}(t) + \\mathbf{b}f(t)$$
   其中 $\\mathbf{A}$ 为 $n \\times n$ 系统矩阵，$\\mathbf{b}$ 为输入向量；
2. **输出方程**：由代数方程组成，描述系统外部输出 $y(t)$ 与当前状态和当前输入的代数映射：
   $$y(t) = \\mathbf{c}^T \\mathbf{x}(t) + d f(t)$$
   其中 $\\mathbf{c}^T$ 为输出向量，$d$ 为直接传输标量。
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
    "stem": "由状态空间矩阵 $(\\mathbf{A}, \\mathbf{b}, \\mathbf{c}^T, d)$ 求解连续系统的系统传递函数 $H(s)$ 的闭式公式为：",
    "options": [
      { "key": "A", "text": "$H(s) = \\mathbf{c}^T(s\\mathbf{I} - \\mathbf{A})^{-1}\\mathbf{b} + d$" },
      { "key": "B", "text": "$H(s) = \\mathbf{c}^T(s\\mathbf{I} + \\mathbf{A})^{-1}\\mathbf{b} + d$" },
      { "key": "C", "text": "$H(s) = (s\\mathbf{I} - \\mathbf{A})^{-1}\\mathbf{b} + d$" },
      { "key": "D", "text": "$H(s) = \\mathbf{c}^T \\mathbf{A}^{-1}\\mathbf{b} + d$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：状态方程复频域求解与系统函数公式推导。

1. 对状态方程取拉普拉斯变换（零状态）：
   $$s \\mathbf{X}(s) = \\mathbf{A}\\mathbf{X}(s) + \\mathbf{b}F(s) \\implies (s\\mathbf{I} - \\mathbf{A})\\mathbf{X}(s) = \\mathbf{b}F(s)$$
2. 求解状态向量：
   $$\\mathbf{X}(s) = (s\\mathbf{I} - \\mathbf{A})^{-1}\\mathbf{b}F(s)$$
3. 对输出方程取拉氏变换：
   $$Y(s) = \\mathbf{c}^T \\mathbf{X}(s) + d F(s) = [\\mathbf{c}^T(s\\mathbf{I} - \\mathbf{A})^{-1}\\mathbf{b} + d] F(s)$$
4. 两边除以输入 $F(s)$ 得系统函数：
   $$H(s) = \\frac{Y(s)}{F(s)} = \\mathbf{c}^T(s\\mathbf{I} - \\mathbf{A})^{-1}\\mathbf{b} + d$$
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
2. 在电网络中，储能元件为电容（电场储能 $W_E = \\frac{1}{2}C u_C^2$）和电感（磁场储能 $W_M = \\frac{1}{2}L i_L^2$）；
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
3. 只要它们之间共用了哪怕一个节点，即视为相互接触回路，在 $\\Delta$ 展开式中不能作为互不接触对相乘。
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
      { "key": "A", "text": "$\\mathbf{x}(k + 1) = \\mathbf{A}\\mathbf{x}(k) + \\mathbf{b}f(k), \\quad y(k) = \\mathbf{c}^T\\mathbf{x}(k) + d f(k)$" },
      { "key": "B", "text": "$\\mathbf{x}(k) = \\mathbf{A}\\mathbf{x}(k - 1) + \\mathbf{b}y(k), \\quad f(k) = \\mathbf{c}^T\\mathbf{x}(k)$" },
      { "key": "C", "text": "$\\Delta\\mathbf{x}(k) = \\mathbf{A}\\mathbf{x}(k) + \\mathbf{b}f(k)$" },
      { "key": "D", "text": "$\\mathbf{x}(k + 2) = \\mathbf{A}\\mathbf{x}(k) + \\mathbf{b}f(k)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散时不变系统的状态空间方程标准表述。

1. 离散状态方程描述下一时刻状态向量 $\\mathbf{x}(k + 1)$ 与当前状态 $\\mathbf{x}(k)$ 及当前输入 $f(k)$ 的线性递推关系：
   $$\\mathbf{x}(k + 1) = \\mathbf{A}\\mathbf{x}(k) + \\mathbf{b}f(k)$$
2. 离散输出方程描述当前时刻系统响应输出：
   $$y(k) = \\mathbf{c}^T\\mathbf{x}(k) + d f(k)$$
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
    "stem": "已知连续系统的状态矩阵为 $\\mathbf{A} = \\begin{bmatrix} 0 & 1 \\\\ -2 & -3 \\end{bmatrix}$，则该系统的特征多项式 $\\det(s\\mathbf{I} - \\mathbf{A})$ 及其特征根（极点）为：",
    "options": [
      { "key": "A", "text": "$s^2 + 3s + 2 = 0$，极点为 $-1, -2$" },
      { "key": "B", "text": "$s^2 - 3s + 2 = 0$，极点为 $1, 2$" },
      { "key": "C", "text": "$s^2 + 2s + 3 = 0$，极点为 $-1, -3$" },
      { "key": "D", "text": "$s^2 - 2 = 0$，极点为 $\\pm \\sqrt{2}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：由状态矩阵 $\\mathbf{A}$ 求解系统特征方程与固有极点。

1. 构造特征矩阵 $s\\mathbf{I} - \\mathbf{A}$：
   $$s\\mathbf{I} - \\mathbf{A} = s \\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\end{bmatrix} - \\begin{bmatrix} 0 & 1 \\\\ -2 & -3 \\end{bmatrix} = \\begin{bmatrix} s & -1 \\\\ 2 & s + 3 \\end{bmatrix}$$
2. 计算行列式：
   $$\\det(s\\mathbf{I} - \\mathbf{A}) = s(s + 3) - (-1)(2) = s^2 + 3s + 2$$
3. 特征方程令为零：
   $$s^2 + 3s + 2 = (s + 1)(s + 2) = 0 \\implies s_1 = -1, \\, s_2 = -2$$
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
      { "key": "A", "text": "$\\frac{G(s)}{1 + G(s)H_b(s)}$" },
      { "key": "B", "text": "$\\frac{G(s)}{1 - G(s)H_b(s)}$" },
      { "key": "C", "text": "$\\frac{1}{1 + G(s)H_b(s)}$" },
      { "key": "D", "text": "$G(s)[1 + H_b(s)]$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：闭环负反馈系统的梅森公式推导。

1. 只有一条前向通路：$P_1 = G(s)$；
2. 只有一个负反馈回路：由于反馈为负，回路增益为 $L_1 = -G(s)H_b(s)$；
3. 特征行列式：
   $$\\Delta = 1 - L_1 = 1 - [-G(s)H_b(s)] = 1 + G(s)H_b(s)$$
4. 回路与前向通路相接触，其余子式 $\\Delta_1 = 1$；
5. 由梅森公式：
   $$H(s) = \\frac{P_1 \\Delta_1}{\\Delta} = \\frac{G(s)}{1 + G(s)H_b(s)}$$
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

1. 积分器的时域关系为：输出 $x_i(t) = \\int_{-\\infty}^t u_i(\\tau)d\\tau \\implies \\dot{x}_i(t) = u_i(t)$；
2. 若将**每个积分器的输出端信号**定义为状态变量 $x_i(t)$，则**积分器的输入端信号恰好自动对应其一阶导数 $\\dot{x}_i(t)$**；
3. 这样一来，积分器输入端所汇聚的加法器代数式，直接自然构成了状态微分方程 $\\dot{\\mathbf{x}}(t) = \\mathbf{A}\\mathbf{x}(t) + \\mathbf{b}f(t)$！
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
    "stem": "已知带限信号 $f(t)$ 的最高截止角频率为 $\\omega_m$。若构造信号 $y(t) = f^2(t)$，则对信号 $y(t)$ 进行无失真恢复所需的最小奈奎斯特抽样角频率 $\\omega_s$ 为：",
    "options": [
      { "key": "A", "text": "$4\\omega_m$" },
      { "key": "B", "text": "$2\\omega_m$" },
      { "key": "C", "text": "$\\omega_m$" },
      { "key": "D", "text": "$8\\omega_m$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：时域相乘对应频域卷积后的频带展宽规律。

1. 时域信号自身相乘：$y(t) = f(t) \\cdot f(t)$；
2. 由频域卷积定理：
   $$Y(j\\omega) = \\frac{1}{2\\pi} [F(j\\omega) * F(j\\omega)]$$
3. 频带展宽法则：
   原信号频谱 $F(j\\omega)$ 限带于 $[-\\omega_m, \\omega_m]$；
   两个区间长度为 $2\\omega_m$ 的频谱做卷积，非零区域变为 $[-\\omega_m - \\omega_m, \\omega_m + \\omega_m] = [-2\\omega_m, 2\\omega_m]$；
   因此 $y(t)$ 的最高截止角频率扩大为 $\\omega_{m, y} = 2\\omega_m$；
4. 由奈奎斯特抽样定理，最小抽样频率为最高频率的 2 倍：
   $$\\omega_s \\ge 2 \\omega_{m, y} = 2(2\\omega_m) = 4\\omega_m$$
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
    "stem": "已知连续信号 $f_1(t)$ 的最高频率为 $100\\text{ Hz}$，$f_2(t)$ 的最高频率为 $200\\text{ Hz}$。若将两信号相乘构成新信号 $y(t) = f_1(t)f_2(t)$，则对 $y(t)$ 进行理想抽样时的奈奎斯特频率为：",
    "options": [
      { "key": "A", "text": "$600\\text{ Hz}$" },
      { "key": "B", "text": "$400\\text{ Hz}$" },
      { "key": "C", "text": "$300\\text{ Hz}$" },
      { "key": "D", "text": "$200\\text{ Hz}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：两不同带限信号时域相乘后的奈奎斯特抽样速率计算。

1. 时域相乘对应频域卷积：$Y(\\omega) = \\frac{1}{2\\pi}[F_1(\\omega) * F_2(\\omega)]$；
2. 卷积后新信号的最高上限频率等于两信号上限频率之和：
   $$f_{m, y} = f_{m1} + f_{m2} = 100\\text{ Hz} + 200\\text{ Hz} = 300\\text{ Hz}$$
3. 根据低通奈奎斯特抽样定理：
   $$f_s \\ge 2 f_{m, y} = 2 \\times 300\\text{ Hz} = 600\\text{ Hz}$$
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
    "stem": "以采样间隔 $T_s$ 对带限信号 $f(t)$（最高截止频率 $\\omega_m$ 满足 $\\omega_s = \\frac{2\\pi}{T_s} \\ge 2\\omega_m$）进行理想冲激抽样后，通过截止频率为 $\\frac{\\omega_s}{2}$、增益为 $T_s$ 的理想低通滤波器恢复原信号的内插重构公式（Whittaker-Shannon 抽样公式）为：",
    "options": [
      { "key": "A", "text": "$f(t) = \\sum_{n=-\\infty}^\\infty f(n T_s) \\text{Sa}\\left(\\frac{\\omega_s}{2}(t - n T_s)\\right)$" },
      { "key": "B", "text": "$f(t) = \\sum_{n=-\\infty}^\\infty f(n T_s) \\delta(t - n T_s)$" },
      { "key": "C", "text": "$f(t) = \\sum_{n=-\\infty}^\\infty f(n T_s) \\cos(\\omega_s t)$" },
      { "key": "D", "text": "$f(t) = \\frac{1}{T_s} \\sum_{n=-\\infty}^\\infty f(n T_s) \\text{rect}(t - n T_s)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：时域抽样定理的 Whittaker-Shannon 信号重构内插公式。

1. 冲激抽样信号为：
   $$f_s(t) = \\sum_{n=-\\infty}^\\infty f(n T_s) \\delta(t - n T_s)$$
2. 理想低通滤波器的冲激响应为抽样函数：
   $$h(t) = \\text{Sa}\\left(\\frac{\\omega_s}{2} t\\right)$$
3. 抽样信号通过低通滤波器时，时域响应等于两者做卷积：
   $$f(t) = f_s(t) * h(t) = \\left[ \\sum_{n=-\\infty}^\\infty f(n T_s) \\delta(t - n T_s) \\right] * \\text{Sa}\\left(\\frac{\\omega_s}{2} t\\right)$$
4. 利用冲激卷积的平移性质得到：
   $$f(t) = \\sum_{n=-\\infty}^\\infty f(n T_s) \\text{Sa}\\left(\\frac{\\omega_s}{2}(t - n T_s)\\right)$$
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
    "stem": "若对带限连续信号 $f(t)$ 进行理想采样，其奈奎斯特频率为 $f_s\\text{ Hz}$。则时移与尺度变换信号 $f\\left(\\frac{1}{3}t - 2\\right)$ 的奈奎斯特采样频率为：",
    "options": [
      { "key": "A", "text": "$\\frac{1}{3}f_s\\text{ Hz}$" },
      { "key": "B", "text": "$3f_s\\text{ Hz}$" },
      { "key": "C", "text": "$f_s\\text{ Hz}$" },
      { "key": "D", "text": "$\\frac{1}{9}f_s\\text{ Hz}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：傅里叶变换时移与尺度变换对最高带宽的影响。

1. 设原信号 $f(t)$ 的最高截止频率为 $f_m$，其奈奎斯特采样频率为 $f_s = 2f_m$；
2. 对信号进行自变量变换 $g(t) = f(\\frac{1}{3}t - 2)$：
   - 时移 $-2$ 产生频域线性相位偏移 $e^{-j 2\\omega}$，完全不改变频带幅度范围；
   - 尺度变换因子为 $a = \\frac{1}{3} < 1$，时域信号被展宽为原来的 3 倍；
3. 由尺度性质 $f(at) \\leftrightarrow \\frac{1}{|a|}F(\\frac{\\omega}{a})$：
   频域被压缩除以 3，新信号的最高上限频率缩小为原信号的 $\\frac{1}{3}$：
   $$f_{m, g} = \\frac{1}{3}f_m$$
4. 因此新信号的奈奎斯特抽样频率为：
   $$f_{s, g} = 2 f_{m, g} = 2 \\left(\\frac{1}{3}f_m\\right) = \\frac{1}{3} (2f_m) = \\frac{1}{3}f_s$$
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
    "stem": "已知信号 $f_1(t)$ 的最高角频率为 $\\omega_{m1} = 100\\pi$，信号 $f_2(t)$ 的最高角频率为 $\\omega_{m2} = 300\\pi$。若新信号为时域卷积信号 $y(t) = f_1(t) * f_2(t)$，则对其无失真抽样的最小奈奎斯特角频率 $\\omega_s$ 为：",
    "options": [
      { "key": "A", "text": "$200\\pi\\text{ rad/s}$" },
      { "key": "B", "text": "$400\\pi\\text{ rad/s}$" },
      { "key": "C", "text": "$600\\pi\\text{ rad/s}$" },
      { "key": "D", "text": "$800\\pi\\text{ rad/s}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：两信号卷积后频域为代数相乘，频带取交集（以窄带为准）。

1. 时域卷积定理：
   $$Y(j\\omega) = F_1(j\\omega) \\cdot F_2(j\\omega)$$
2. 频带分析：
   - $F_1(j\\omega)$ 在 $|\\omega| > 100\\pi$ 时严格为 0；
   - $F_2(j\\omega)$ 在 $|\\omega| > 300\\pi$ 时严格为 0；
   - 两者相乘后，只要超出窄带 $|\\omega| > 100\\pi$，乘积 $Y(j\\omega)$ 就必定为 0；
3. 因此卷积信号的最高频率受限于较窄的那个信号：
   $$\\omega_{m, y} = \\min(\\omega_{m1}, \\omega_{m2}) = 100\\pi$$
4. 奈奎斯特抽样角频率为：
   $$\\omega_s \\ge 2 \\omega_{m, y} = 2 \\times 100\\pi = 200\\pi\\text{ rad/s}$$
【注意辨析】：
- 时域相乘 $\\implies$ 频域卷积 $\\implies$ 频带相加；
- 时域卷积 $\\implies$ 频域相乘 $\\implies$ 频带取小（取交集）。
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
    "stem": "已知基带信号 $f(t)$ 的最高频率为 $f_m\\text{ Hz}$。若构造时域压缩信号 $g(t) = f(4t)$，则对 $g(t)$ 抽样的奈奎斯特频率为：",
    "options": [
      { "key": "A", "text": "$8f_m\\text{ Hz}$" },
      { "key": "B", "text": "$2f_m\\text{ Hz}$" },
      { "key": "C", "text": "$4f_m\\text{ Hz}$" },
      { "key": "D", "text": "$\\frac{1}{2}f_m\\text{ Hz}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：尺度变换参数 $a > 1$ 时的频带扩展与采样频率成倍增长。

1. 原信号 $f(t)$ 的频带范围为 $[-f_m, f_m]$；
2. 当尺度变换为 $g(t) = f(4t)$ 时，时域被压缩为原来的 $\\frac{1}{4}$，频带被展宽 4 倍；
   $$G(f) = \\frac{1}{4}F\\left(\\frac{f}{4}\\right)$$
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
    "stem": "时域理想抽样过程中，当采样角频率 $\\omega_s < 2\\omega_m$ 时，抽样信号将发生混叠失真（Aliasing），其频域机理是：",
    "options": [
      { "key": "A", "text": "以 $\\omega_s$ 为周期延拓的频谱在相邻周期之间发生频谱重叠交错" },
      { "key": "B", "text": "信号的高频部分被滤波器完全滤除" },
      { "key": "C", "text": "时域信号产生了非线性畸变" },
      { "key": "D", "text": "冲激脉冲的幅度发生了衰减" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：抽样频谱周期延拓与混叠失真的本质几何机理。

1. 冲激抽样信号的傅里叶变换为原信号频谱按 $\\omega_s$ 周期的无限次平移叠加：
   $$F_s(j\\omega) = \\frac{1}{T_s}\\sum_{k=-\\infty}^\\infty F(j(\\omega - k\\omega_s))$$
2. 当 $\\omega_s \\ge 2\\omega_m$ 时，相邻两个延拓频谱的间隔 $\\omega_s - 2\\omega_m \\ge 0$，频谱互不重叠，可以用低通滤波器完美分离出基带；
3. 当 $\\omega_s < 2\\omega_m$ 时，高频分量侵入相邻周期的基带区域，彼此重叠交错，破坏了原始频带的信息完整性，导致无法通过线性滤波无失真复原。
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
    "stem": "已知带限信号 $f(t) = 10\\text{Sa}(200\\pi t)$，为保证无失真恢复，最大的允许抽样时间间隔 $T_{s,\\max}$ 为：",
    "options": [
      { "key": "A", "text": "$5\\text{ ms} = 0.005\\text{ s}$" },
      { "key": "B", "text": "$10\\text{ ms} = 0.01\\text{ s}$" },
      { "key": "C", "text": "$2.5\\text{ ms} = 0.0025\\text{ s}$" },
      { "key": "D", "text": "$1\\text{ ms}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：抽样函数频谱最高截止频率与最大采样间隔计算。

1. 抽样函数傅里叶变换对：
   $$\\text{Sa}(W t) \\stackrel{\\mathcal{F}}{\\longleftrightarrow} \\frac{\\pi}{W} \\text{rect}\\left(\\frac{\\omega}{2W}\\right)$$
2. 本题中 $W = 200\\pi$，因此信号的最高截止角频率为：
   $$\\omega_m = 200\\pi\\text{ rad/s} \\implies f_m = \\frac{\\omega_m}{2\\pi} = \\frac{200\\pi}{2\\pi} = 100\\text{ Hz}$$
3. 奈奎斯特最小抽样频率为：
   $$f_s \\ge 2 f_m = 200\\text{ Hz}$$
4. 对应最大的抽样时间间隔为：
   $$T_{s,\\max} = \\frac{1}{f_s} = \\frac{1}{200} = 0.005\\text{ s} = 5\\text{ ms}$$
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
      { "key": "A", "text": "作为抗混叠滤波器（Anti-aliasing Filter），滤除高于 $\\frac{f_s}{2}$ 的带外高频噪声与无用干扰" },
      { "key": "B", "text": "放大输入信号的幅度" },
      { "key": "C", "text": "将模拟信号转换为离散序列" },
      { "key": "D", "text": "消除低频直流漂移" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：抗混叠前置低通滤波器的工程原理。

1. 现实中的实际物理信号和环境噪声往往具有很宽的频谱，不是严格有限带限的；
2. 如果直接按采样率 $f_s$ 进行采样，高于奈奎斯特折叠频率 $\\frac{f_s}{2}$ 的所有高频分量和高频噪声都将折叠回基带内部，产生不可消除的混叠噪声；
3. 因此在采样之前，必须先经过一个截止频率为 $f_c \\le \\frac{f_s}{2}$ 的低通滤波器（称为抗混叠滤波器），强行消除带外高频分量，确保满足采样定理要求。
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
    "stem": "以周期为 $T_s$ 的理想冲激串 $p(t) = \\sum_{n=-\\infty}^\\infty \\delta(t - n T_s)$ 对连续信号 $f(t)$ 进行时域抽样，所得抽样信号 $f_s(t) = f(t)p(t)$ 的频谱表达式为：",
    "options": [
      { "key": "A", "text": "$F_s(j\\omega) = \\frac{1}{T_s} \\sum_{k=-\\infty}^\\infty F\\left(j(\\omega - k\\omega_s)\\right)$" },
      { "key": "B", "text": "$F_s(j\\omega) = \\sum_{k=-\\infty}^\\infty F\\left(j(\\omega - k\\omega_s)\\right)$" },
      { "key": "C", "text": "$F_s(j\\omega) = \\frac{1}{2\\pi} \\sum_{k=-\\infty}^\\infty F\\left(j(\\omega - k\\omega_s)\\right)$" },
      { "key": "D", "text": "$F_s(j\\omega) = F(j\\omega) * \\delta(\\omega - \\omega_s)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：时域周期冲激串抽样的频域严格推导。

1. 周期为 $T_s$ 的冲激序列的傅里叶级数展开式为：
   $$p(t) = \\sum_{n=-\\infty}^\\infty \\delta(t - nT_s) = \\frac{1}{T_s}\\sum_{k=-\\infty}^\\infty e^{jk\\omega_s t}, \\quad \\omega_s = \\frac{2\\pi}{T_s}$$
2. 时域抽样信号表示为：
   $$f_s(t) = f(t)p(t) = \\frac{1}{T_s}\\sum_{k=-\\infty}^\\infty f(t)e^{jk\\omega_s t}$$
3. 对两端取傅里叶变换，利用频移定理：
   $$F_s(j\\omega) = \\frac{1}{T_s}\\sum_{k=-\\infty}^\\infty F(j(\\omega - k\\omega_s))$$
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
    "stem": "对于频带范围在 $[f_L, f_H]$ 之间的高频窄带带通信号（带宽 $B = f_H - f_L \\ll f_H$），最低采样频率必须大于其最高频率的 2 倍（即 $f_s \\ge 2 f_H$）。",
    "options": [
      { "key": "A", "text": "正确（True）" },
      { "key": "B", "text": "错误（False）" }
    ],
    "answer": "B",
    "analysis": """【核心考点】：带通抽样定理（Bandpass Sampling Theorem）。

1. 奈奎斯特采样定理 $f_s \\ge 2 f_H$ 严格适用于**低通信号（频谱从 0 延伸到 $f_H$）**；
2. 对于高频窄带带通信号，其中间 $[0, f_L]$ 大段频谱为空，若依然按 $2f_H$ 采样会造成严重的计算量与硬件浪费；
3. **带通抽样定理**指出：只要合理选择采样频率 $f_s$，使得周期延拓后的各个带通谱带恰好插空落入空余频隙而不产生重叠，其采样率只需满足：
   $$f_s \\ge 2 B = 2(f_H - f_L)$$
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
    "stem": "对于单一频率正弦信号 $f(t) = \\sin(\\omega_0 t)$，若恰好按临界奈奎斯特采样角频率 $\\omega_s = 2\\omega_0$ 进行均匀抽样（采样时刻 $t_n = n T_s = n \\frac{\\pi}{\\omega_0}$），则采样得到的离散序列值 $f(n T_s)$ 将：",
    "options": [
      { "key": "A", "text": "全部恒等于 0（完全丢失信号信息）" },
      { "key": "B", "text": "完美恢复出正弦波" },
      { "key": "C", "text": "呈现交替正负 1 的方波" },
      { "key": "D", "text": "幅度变为原信号的 2 倍" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：单一正弦信号临界抽样 $\\omega_s = 2\\omega_0$ 的相位敏感陷阱（奈奎斯特准则的严格大于要求）。

1. 抽样间隔为 $T_s = \\frac{2\\pi}{\\omega_s} = \\frac{2\\pi}{2\\omega_0} = \\frac{\\pi}{\\omega_0}$；
2. 代入抽样时刻 $t_n = n T_s = n \\frac{\\pi}{\\omega_0}$：
   $$f(n T_s) = \\sin\\left(\\omega_0 \\cdot n \\frac{\\pi}{\\omega_0}\\right) = \\sin(n \\pi) = 0, \\quad (\\forall n \\in \\mathbb{Z})$$
3. 抽样点恰好每一次都精准落在了正弦波的**过零点**上，导致采到的所有离散样值恒为 0！
4. 这正是为什么抽样定理中严格要求 $\\omega_s > 2\\omega_m$（大于而不是等于），或者需要正交双通道采样的根本原因。
选 **A**。"""
  }
]

all_questions.extend(chapter7_questions)
print(f"Added Chapter 7: {len(chapter7_questions)} questions")
print(f"Total accumulated questions: {len(all_questions)}")
'''

with open('build_full_database.py', 'a', encoding='utf-8') as f:
    f.write(c6_c7_code)

print("Appended C6 and C7 successfully!")
