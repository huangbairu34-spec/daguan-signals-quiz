# -*- coding: utf-8 -*-
import json

c4_c5_code = '''
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
    "stem": "计算假分式象函数 $F(s) = \\frac{s^2 + 4s + 5}{s^2 + 3s + 2}$（收敛域 $\\text{Re}(s) > -1$）的拉普拉斯逆变换 $f(t)$：",
    "options": [
      { "key": "A", "text": "$\\delta(t) + (2e^{-t} - e^{-2t})\\varepsilon(t)$" },
      { "key": "B", "text": "$\\delta(t) + (e^{-t} - 2e^{-2t})\\varepsilon(t)$" },
      { "key": "C", "text": "$(2e^{-t} - e^{-2t})\\varepsilon(t)$" },
      { "key": "D", "text": "$\\delta(t) + (2e^{-t} + e^{-2t})\\varepsilon(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：分子与分母同阶的假分式部分分式展开法。

1. **分离多项式多项式整式**：
   分子除以分母分离商数 1：
   $$F(s) = \\frac{(s^2 + 3s + 2) + (s + 3)}{s^2 + 3s + 2} = 1 + \\frac{s + 3}{(s + 1)(s + 2)}$$
2. **真分式留数法展开**：
   设 $\\frac{s + 3}{(s + 1)(s + 2)} = \\frac{A}{s + 1} + \\frac{B}{s + 2}$：
   - $A = \\left[ \\frac{s + 3}{s + 2} \\right]_{s = -1} = \\frac{-1 + 3}{-1 + 2} = 2$；
   - $B = \\left[ \\frac{s + 3}{s + 1} \\right]_{s = -2} = \\frac{-2 + 3}{-2 + 1} = -1$；
   因此：
   $$F(s) = 1 + \\frac{2}{s + 1} - \\frac{1}{s + 2}$$
3. **查常用拉普拉斯逆变换对**（收敛域为最右极点右侧因果信号）：
   - $1 \\stackrel{\\mathcal{L}^{-1}}{\\longleftrightarrow} \\delta(t)$；
   - $\\frac{1}{s + 1} \\stackrel{\\mathcal{L}^{-1}}{\\longleftrightarrow} e^{-t}\\varepsilon(t)$；
   - $\\frac{1}{s + 2} \\stackrel{\\mathcal{L}^{-1}}{\\longleftrightarrow} e^{-2t}\\varepsilon(t)$；
4. 综合得到：
   $$f(t) = \\delta(t) + (2e^{-t} - e^{-2t})\\varepsilon(t)$$
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
    "stem": "某稳定连续因果系统的系统函数为 $H(s) = \\frac{s - 2}{s + 2}$，则该系统属于：",
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
2. **频响幅值计算**：令 $s = j\\omega$：
   $$|H(j\\omega)| = \\left| \\frac{j\\omega - 2}{j\\omega + 2} \\right| = \\frac{\\sqrt{\\omega^2 + (-2)^2}}{\\sqrt{\\omega^2 + 2^2}} = \\frac{\\sqrt{\\omega^2 + 4}}{\\sqrt{\\omega^2 + 4}} = 1$$
3. 在全部频率 $-\\infty < \\omega < +\\infty$ 上，幅频增益恒等于常数 1，仅对相位产生色散滞后；
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
    "stem": "已知象函数 $F(s) = \\frac{s + 1}{s^2 + 2s + 10}$（收敛域 $\\text{Re}(s) > -1$），其对应的时域原函数 $f(t)$ 为：",
    "options": [
      { "key": "A", "text": "$e^{-t}\\cos(3t)\\varepsilon(t)$" },
      { "key": "B", "text": "$e^{-t}\\sin(3t)\\varepsilon(t)$" },
      { "key": "C", "text": "$\\cos(3t)\\varepsilon(t)$" },
      { "key": "D", "text": "$e^{-2t}\\cos(3t)\\varepsilon(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：分母含共轭复极点的拉普拉斯配方逆变换。

1. **分母配平方**：
   $$s^2 + 2s + 10 = (s + 1)^2 + 9 = (s + 1)^2 + 3^2$$
2. **分子配凑对应项**：
   分子本身恰好为 $s + 1$：
   $$F(s) = \\frac{s + 1}{(s + 1)^2 + 3^2}$$
3. **查经典衰减余弦变换对**：
   $$e^{-a t}\\cos(\\omega_0 t)\\varepsilon(t) \\stackrel{\\mathcal{L}}{\\longleftrightarrow} \\frac{s + a}{(s + a)^2 + \\omega_0^2}$$
4. 对比参数可知：$a = 1, \\, \\omega_0 = 3$：
   $$f(t) = e^{-t}\\cos(3t)\\varepsilon(t)$$
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
    "stem": "已知象函数 $F(s) = \\frac{2s + 3}{s^2 + 5s + 6}$（$\\text{Re}(s) > -2$），则其时域初值 $f(0_+)$ 与终值 $f(\\infty)$ 分别为：",
    "options": [
      { "key": "A", "text": "$f(0_+) = 2, \\, f(\\infty) = 0$" },
      { "key": "B", "text": "$f(0_+) = 0, \\, f(\\infty) = 2$" },
      { "key": "C", "text": "$f(0_+) = 2, \\, f(\\infty) = 0.5$" },
      { "key": "D", "text": "$f(0_+) = 3, \\, f(\\infty) = 0$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：单边拉普拉斯变换的初值定理与终值定理。

1. **初值定理计算**：
   $$f(0_+) = \\lim_{s \\to \\infty} s F(s) = \\lim_{s \\to \\infty} \\frac{s(2s + 3)}{s^2 + 5s + 6} = \\lim_{s \\to \\infty} \\frac{2s^2 + 3s}{s^2 + 5s + 6} = 2$$
2. **终值定理计算**：
   - 检验极点：分母 $s^2 + 5s + 6 = (s + 2)(s + 3) = 0 \\implies s_1 = -2, s_2 = -3$；
   - 两个极点均严格位于左半开平面，信号时域必渐近收敛，满足终值定理适用条件；
   $$f(\\infty) = \\lim_{s \\to 0} s F(s) = \\lim_{s \\to 0} \\frac{s(2s + 3)}{s^2 + 5s + 6} = \\frac{0 \\times 3}{6} = 0$$
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
    "stem": "某 LTI 系统的系统函数为 $H(s) = \\frac{s + 3}{(s + 1)(s + 2)}$。若已知该系统既是因果系统又是稳定系统，则其拉普拉斯收敛域（ROC）必须是：",
    "options": [
      { "key": "A", "text": "$\\text{Re}(s) > -1$" },
      { "key": "B", "text": "$-2 < \\text{Re}(s) < -1$" },
      { "key": "C", "text": "$\\text{Re}(s) < -2$" },
      { "key": "D", "text": "整个复 $s$ 平面" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：连续系统因果性与 BIBO 稳定性对收敛域 ROC 的双重要求。

1. **极点位置**：系统极点为 $s_1 = -1$ 和 $s_2 = -2$；
2. **因果性要求**：因果系统的冲激响应为右边信号，其收敛域必须位于**最右边极点的右侧右半平面**：
   $$\\text{ROC}: \\text{Re}(s) > \\max(-1, -2) = -1$$
3. **稳定性要求**：BIBO 稳定系统的充要条件是冲激响应绝对可积，对应收敛域**必须包含虚轴 $j\\omega$（即包含 $\\text{Re}(s) = 0$）**；
4. 当 $\\text{ROC}: \\text{Re}(s) > -1$ 时，原点及虚轴 $\\text{Re}(s) = 0 > -1$ 包含在收敛域内，因此同时满足因果性与稳定性！
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
    "stem": "计算时域信号 $f(t) = t \\varepsilon(t - 1)$ 的单边拉普拉斯变换 $F(s)$ 为：",
    "options": [
      { "key": "A", "text": "$\\frac{s + 1}{s^2}e^{-s}$" },
      { "key": "B", "text": "$\\frac{1}{s^2}e^{-s}$" },
      { "key": "C", "text": "$\\frac{s - 1}{s^2}e^{-s}$" },
      { "key": "D", "text": "$\\frac{1}{s}e^{-s}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：自变量时移与阶跃函数的拉氏变换处理。

1. **配凑时移变量 $t - 1$**：
   $$f(t) = t \\varepsilon(t - 1) = (t - 1 + 1)\\varepsilon(t - 1) = (t - 1)\\varepsilon(t - 1) + \\varepsilon(t - 1)$$
2. **分别查经典变换对并应用时移性质**：
   - 斜坡项：$t \\varepsilon(t) \\leftrightarrow \\frac{1}{s^2} \\implies (t - 1)\\varepsilon(t - 1) \\leftrightarrow \\frac{1}{s^2}e^{-s}$；
   - 阶跃项：$\\varepsilon(t) \\leftrightarrow \\frac{1}{s} \\implies \\varepsilon(t - 1) \\leftrightarrow \\frac{1}{s}e^{-s}$；
3. **通分合并**：
   $$F(s) = \\left( \\frac{1}{s^2} + \\frac{1}{s} \\right) e^{-s} = \\frac{s + 1}{s^2}e^{-s}$$
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
    "stem": "信号 $f(t) = e^{-a t}\\sin(\\omega_0 t)\\varepsilon(t)$ 的单边拉普拉斯变换 $F(s)$ 及其收敛域为：",
    "options": [
      { "key": "A", "text": "$\\frac{\\omega_0}{(s + a)^2 + \\omega_0^2}, \\quad \\text{Re}(s) > -a$" },
      { "key": "B", "text": "$\\frac{s + a}{(s + a)^2 + \\omega_0^2}, \\quad \\text{Re}(s) > -a$" },
      { "key": "C", "text": "$\\frac{\\omega_0}{s^2 + \\omega_0^2}, \\quad \\text{Re}(s) > 0$" },
      { "key": "D", "text": "$\\frac{1}{(s + a)^2 + \\omega_0^2}, \\quad \\text{Re}(s) > a$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：单边拉普拉斯变换频移定理与正弦变换对。

1. 基本正弦信号的单边拉普拉斯变换：
   $$\\sin(\\omega_0 t)\\varepsilon(t) \\stackrel{\\mathcal{L}}{\\longleftrightarrow} \\frac{\\omega_0}{s^2 + \\omega_0^2}, \\quad \\text{Re}(s) > 0$$
2. 根据复频移性质 $e^{-a t} f(t) \\leftrightarrow F(s + a)$：
   将 $s$ 整体替换为 $s + a$：
   $$F(s) = \\frac{\\omega_0}{(s + a)^2 + \\omega_0^2}$$
3. 收敛域平移：$\\text{Re}(s + a) > 0 \\implies \\text{Re}(s) > -a$。
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
    "stem": "已知某系统的系统函数为 $H(s) = \\frac{10(s + 2)}{s(s + 5)}$，其单位冲激响应 $h(t)$ 的初值 $h(0_+)$ 与终值 $h(\\infty)$ 分别为：",
    "options": [
      { "key": "A", "text": "$h(0_+) = 10, \\, h(\\infty) = 4$" },
      { "key": "B", "text": "$h(0_+) = 4, \\, h(\\infty) = 10$" },
      { "key": "C", "text": "$h(0_+) = 10, \\, h(\\infty) = 0$" },
      { "key": "D", "text": "$h(0_+) = 0, \\, h(\\infty) = 4$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：初值定理与终值定理在系统响应中的标准求解。

1. **计算初值 $h(0_+)$**：
   $$h(0_+) = \\lim_{s \\to \\infty} s H(s) = \\lim_{s \\to \\infty} s \\cdot \\frac{10(s + 2)}{s(s + 5)} = \\lim_{s \\to \\infty} \\frac{10(s + 2)}{s + 5} = 10$$
2. **计算终值 $h(\\infty)$**：
   - 极点分析：$s(s + 5) = 0 \\implies s_1 = 0, \\, s_2 = -5$；极点除原点单极点外均在左半平面，满足终值定理适用条件；
   $$h(\\infty) = \\lim_{s \\to 0} s H(s) = \\lim_{s \\to 0} s \\cdot \\frac{10(s + 2)}{s(s + 5)} = \\lim_{s \\to 0} \\frac{10(s + 2)}{s + 5} = \\frac{10 \\times 2}{5} = 4$$
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

1. 因果连续系统稳定的充分必要条件是：**系统函数 $H(s)$ 的所有极点都必须位于左半开平面**（$\\text{Re}(p_k) < 0$），收敛域包含虚轴；
2. **零点的位置完全不受限制**：零点可以位于左半平面、虚轴，也可以位于右半平面！
   - 例如全通滤波器 $H(s) = \\frac{s - 2}{s + 2}$，其零点为 $s = +2$（位于右半平面），但极点为 $s = -2$（在左半平面），系统完全是 BIBO 稳定的！
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
    "stem": "求象函数 $F(s) = \\frac{e^{-3s}}{s^2 + 3s + 2}$ 的单边拉普拉斯逆变换 $f(t)$：",
    "options": [
      { "key": "A", "text": "$[e^{-(t - 3)} - e^{-2(t - 3)}]\\varepsilon(t - 3)$" },
      { "key": "B", "text": "$(e^{-t} - e^{-2t})\\varepsilon(t - 3)$" },
      { "key": "C", "text": "$[e^{-(t - 3)} + e^{-2(t - 3)}]\\varepsilon(t - 3)$" },
      { "key": "D", "text": "$[2e^{-(t - 3)} - e^{-2(t - 3)}]\\varepsilon(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：部分分式展开与时移性质的结合。

1. 先对不含时延因子的母函数展开：
   $$F_0(s) = \\frac{1}{s^2 + 3s + 2} = \\frac{1}{(s + 1)(s + 2)} = \\frac{1}{s + 1} - \\frac{1}{s + 2}$$
2. 求母函数的时域原函数：
   $$f_0(t) = (e^{-t} - e^{-2t})\\varepsilon(t)$$
3. 乘以时延因子 $e^{-3s}$ 对应时域整体右移 3 个单位（延时 3）：
   $$f(t) = f_0(t - 3) = [e^{-(t - 3)} - e^{-2(t - 3)}]\\varepsilon(t - 3)$$
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
    "stem": "某连续时间系统的零输入响应为 $y_{zi}(t) = (e^{-t} - 2e^{-2t} + e^{-3t})\\varepsilon(t)$，则该系统的极点必定包含：",
    "options": [
      { "key": "A", "text": "$-1, \\, -2, \\, -3$" },
      { "key": "B", "text": "$1, \\, 2, \\, 3$" },
      { "key": "C", "text": "$-1, \\, -2$" },
      { "key": "D", "text": "$-1, \\, 2, \\, -3$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：零输入响应的模态形式与系统极点的严格对应。

1. 零输入响应 $y_{zi}(t)$ 是系统在没有外加输入激励的情况下，仅由初始状态所激发的自然响应；
2. 零输入响应的时域基底函数 $e^{\\lambda_k t}$ 中的指数项系数 $\\lambda_k$，即为系统特征方程的根（也是系统函数的固有极点）；
3. 观察题干表达式中的三项指数分量：
   - $e^{-t} \\implies \\lambda_1 = -1$；
   - $e^{-2t} \\implies \\lambda_2 = -2$；
   - $e^{-3t} \\implies \\lambda_3 = -3$；
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
    "stem": "已知某连续稳定系统的系统函数为 $H(s) = \\frac{s}{s + 3}$，则该滤波器属于：",
    "options": [
      { "key": "A", "text": "高通滤波器（High-pass Filter）" },
      { "key": "B", "text": "低通滤波器（Low-pass Filter）" },
      { "key": "C", "text": "带通滤波器" },
      { "key": "D", "text": "带阻滤波器" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：频率响应在零频与高频极限下的增益特性。

1. 令 $s = j\\omega$，系统的频响为：
   $$H(j\\omega) = \\frac{j\\omega}{j\\omega + 3}$$
2. 计算直流（零频 $\\omega = 0$）处的增益：
   $$|H(j 0)| = \\frac{0}{0 + 3} = 0$$
   （低频完全被阻断）；
3. 计算高频（$\\omega \\to \\infty$）处的增益：
   $$\\lim_{\\omega \\to \\infty} |H(j\\omega)| = \\lim_{\\omega \\to \\infty} \\frac{\\omega}{\\sqrt{\\omega^2 + 9}} = 1$$
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
    "stem": "微分方程 $r''(t) + 6r'(t) + 5r(t) = e'(t) + 2e(t)$，初始条件 $r(0_-) = 1, \\, r'(0_-) = 0$。则其零输入响应的拉普拉斯变换 $R_{zi}(s)$ 为：",
    "options": [
      { "key": "A", "text": "$\\frac{s + 6}{s^2 + 6s + 5}$" },
      { "key": "B", "text": "$\\frac{s + 2}{s^2 + 6s + 5}$" },
      { "key": "C", "text": "$\\frac{1}{s^2 + 6s + 5}$" },
      { "key": "D", "text": "$\\frac{s}{s^2 + 6s + 5}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：单边拉普拉斯变换时域微分定理（含 $0_-$ 状态模型）。

1. 二阶微分的单边拉普拉斯变换时域微分定理：
   $$\\mathcal{L}\\{r''(t)\\} = s^2 R(s) - s r(0_-) - r'(0_-)$$
   $$\\mathcal{L}\\{r'(t)\\} = s R(s) - r(0_-)$$
2. 求解零输入响应时，令外加激励 $e(t) = 0$：
   $$[s^2 R_{zi}(s) - s r(0_-) - r'(0_-)] + 6[s R_{zi}(s) - r(0_-)] + 5 R_{zi}(s) = 0$$
3. 代入初始状态 $r(0_-) = 1, \\, r'(0_-) = 0$：
   $$(s^2 + 6s + 5)R_{zi}(s) - s(1) - 0 - 6(1) = 0$$
   $$(s^2 + 6s + 5)R_{zi}(s) = s + 6$$
4. 解得：
   $$R_{zi}(s) = \\frac{s + 6}{s^2 + 6s + 5}$$
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
    "stem": "系统函数为 $H(s) = \\frac{s + 2}{s^2 + 6s + 5}$（因果系统），则单位冲激响应 $h(t)$ 为：",
    "options": [
      { "key": "A", "text": "$[\\frac{1}{4}e^{-t} + \\frac{3}{4}e^{-5t}]\\varepsilon(t)$" },
      { "key": "B", "text": "$[\\frac{3}{4}e^{-t} + \\frac{1}{4}e^{-5t}]\\varepsilon(t)$" },
      { "key": "C", "text": "$(e^{-t} - e^{-5t})\\varepsilon(t)$" },
      { "key": "D", "text": "$[\\frac{1}{2}e^{-t} + \\frac{1}{2}e^{-5t}]\\varepsilon(t)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：部分分式展开法求因果系统单位冲激响应。

1. 分解分母多项式：
   $$s^2 + 6s + 5 = (s + 1)(s + 5)$$
2. 设部分分式：
   $$H(s) = \\frac{s + 2}{(s + 1)(s + 5)} = \\frac{A}{s + 1} + \\frac{B}{s + 5}$$
3. 计算留数系数：
   - $A = \\left[ \\frac{s + 2}{s + 5} \\right]_{s = -1} = \\frac{-1 + 2}{-1 + 5} = \\frac{1}{4}$；
   - $B = \\left[ \\frac{s + 2}{s + 1} \\right]_{s = -5} = \\frac{-5 + 2}{-5 + 1} = \\frac{-3}{-4} = \\frac{3}{4}$；
4. 取单边拉普拉斯逆变换：
   $$h(t) = \\left( \\frac{1}{4}e^{-t} + \\frac{3}{4}e^{-5t} \\right)\\varepsilon(t)$$
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
      { "key": "A", "text": "$\\frac{1}{s + 1}$" },
      { "key": "B", "text": "$\\frac{s + 5}{(s + 1)(s + 5)}$" },
      { "key": "C", "text": "$\\frac{1}{s + 5}$" },
      { "key": "D", "text": "$\\frac{s + 1}{s + 5}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：系统函数的零极点相消与一阶退化。

1. 对微分方程两端取拉普拉斯变换（零状态）：
   $$(s^2 + 6s + 5)Y(s) = (s + 5)F(s)$$
2. 得到系统函数：
   $$H(s) = \\frac{Y(s)}{F(s)} = \\frac{s + 5}{s^2 + 6s + 5} = \\frac{s + 5}{(s + 1)(s + 5)}$$
3. 因子相消：零点 $s = -5$ 与极点 $s = -5$ 重合对消：
   $$H(s) = \\frac{1}{s + 1}$$
4. 系统退化为一阶因果低通系统，单位冲激响应为 $h(t) = e^{-t}\\varepsilon(t)$。
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
    "stem": "信号 $f(t) = t e^{-2t}\\varepsilon(t)$ 的拉普拉斯变换 $F(s)$ 及其收敛域为：",
    "options": [
      { "key": "A", "text": "$\\frac{1}{(s + 2)^2}, \\quad \\text{Re}(s) > -2$" },
      { "key": "B", "text": "$\\frac{1}{(s + 2)^2}, \\quad \\text{Re}(s) > 2$" },
      { "key": "C", "text": "$\\frac{1}{s + 2}, \\quad \\text{Re}(s) > -2$" },
      { "key": "D", "text": "$\\frac{2}{(s + 2)^2}, \\quad \\text{Re}(s) > -2$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：频域微分性质在拉普拉斯变换中的应用。

1. 基本衰减指数信号变换：
   $$e^{-2t}\\varepsilon(t) \\stackrel{\\mathcal{L}}{\\longleftrightarrow} \\frac{1}{s + 2}, \\quad \\text{Re}(s) > -2$$
2. 利用复频域微分性质 $t f(t) \\leftrightarrow -\\frac{dF(s)}{ds}$：
   $$F(s) = -\\frac{d}{ds}\\left( \\frac{1}{s + 2} \\right) = -\\left( -\\frac{1}{(s + 2)^2} \\right) = \\frac{1}{(s + 2)^2}$$
3. 因果信号收敛域为极点右侧：$\\text{Re}(s) > -2$。
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
2. **逆系统因果稳定**：逆系统的系统函数为 $H_{inv}(s) = \\frac{1}{H(s)}$，其极点正是原系统的**零点**！
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
      { "key": "A", "text": "容抗阻抗 $\\frac{1}{sC}$ 串联电压源 $\\frac{u_C(0_-)}{s}$" },
      { "key": "B", "text": "容抗阻抗 $sC$ 串联电压源 $u_C(0_-)$" },
      { "key": "C", "text": "容抗阻抗 $\\frac{1}{sC}$ 并联电流源 $C u_C(0_-)$" },
      { "key": "D", "text": "容抗阻抗 $\\frac{1}{sC}$ 串联电压源 $C u_C(0_-)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：储能元件的复频域戴维宁与诺顿等效模型。

1. 电容时域伏安方程：$i_C(t) = C \\frac{du_C(t)}{dt}$；
2. 积分形式：$u_C(t) = u_C(0_-) + \\frac{1}{C}\\int_{0_-}^t i_C(\\tau)d\\tau$；
3. 取单边拉普拉斯变换：
   $$U_C(s) = \\frac{u_C(0_-)}{s} + \\frac{1}{sC} I_C(s)$$
4. 该式直接对应一个等效阻抗为 $Z_C(s) = \\frac{1}{sC}$，与一个大小为 $\\frac{u_C(0_-)}{s}$ 的冲激步阶电压源相串联。
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
    "stem": "已知某离散时间 LTI 系统的系统函数为 $H(z) = \\frac{z^2 + 2}{z^2 - 1.5z - 1}$。若已知该系统是稳定系统（BIBO Stable），则其收敛域 ROC 必须是：",
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
2. **极点模长**：$|z_2| = 0.5$，\\, $|z_1| = 2$；
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
    "stem": "离散梳状滤波器的系统函数为 $H(z) = 1 - z^{-6} = \\frac{z^6 - 1}{z^6}$，则该滤波器在区间 $[0, \\pi]$ 内幅频响应 $|H(e^{j\\Omega})|$ 的零点（陷波点）个数为：",
    "options": [
      { "key": "A", "text": "4 个（含 0 和 $\\pi$）" },
      { "key": "B", "text": "3 个" },
      { "key": "C", "text": "6 个" },
      { "key": "D", "text": "2 个" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：梳状滤波器（Comb Filter）的单位圆零点分布与幅频陷波点。

1. **求系统的传输零点**：
   分子多项式令为零：$z^6 - 1 = 0 \\implies z_k = e^{j \\frac{2\\pi k}{6}} = e^{j \\frac{k\\pi}{3}}, \\quad (k = 0, 1, 2, 3, 4, 5)$；
2. 六个零点严格均匀分布在单位圆 $|z| = 1$ 上；
3. **统计区间 $[0, \\pi]$ 内的零点**：
   - $k = 0$: $\\Omega_0 = 0$
   - $k = 1$: $\\Omega_1 = \\frac{\\pi}{3}$
   - $k = 2$: $\\Omega_2 = \\frac{2\\pi}{3}$
   - $k = 3$: $\\Omega_3 = \\pi$
4. 在 $[0, \\pi]$ 区间内共有 4 个零点，在这些数字角频率上系统的幅频响应严格为 0（陷波），形成周期梳状凹陷。
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
    "stem": "指数序列 $f(k) = a^k \\varepsilon(k)$（其中 $|a| < 1$）的 Z 变换 $F(z)$ 及其收敛域为：",
    "options": [
      { "key": "A", "text": "$\\frac{z}{z - a}, \\quad |z| > |a|$" },
      { "key": "B", "text": "$\\frac{1}{z - a}, \\quad |z| > |a|$" },
      { "key": "C", "text": "$\\frac{z}{z - a}, \\quad |z| < |a|$" },
      { "key": "D", "text": "$\\frac{z}{z + a}, \\quad |z| > |a|$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：单边因果指数序列的 Z 变换级数求和与收敛域定义。

1. 由单边 Z 变换定义式：
   $$F(z) = \\sum_{k=0}^\\infty a^k z^{-k} = \\sum_{k=0}^\\infty (a z^{-1})^k$$
2. 利用等比无穷级数求和公式（当公比 $|a z^{-1}| < 1 \\implies |z| > |a|$ 时收敛）：
   $$F(z) = \\frac{1}{1 - a z^{-1}} = \\frac{z}{z - a}$$
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
    "stem": "交替阶跃序列 $f(k) = (-1)^k \\varepsilon(k)$ 的 Z 变换为：",
    "options": [
      { "key": "A", "text": "$\\frac{z}{z + 1}, \\quad |z| > 1$" },
      { "key": "B", "text": "$\\frac{z}{z - 1}, \\quad |z| > 1$" },
      { "key": "C", "text": "$\\frac{1}{z + 1}, \\quad |z| > 1$" },
      { "key": "D", "text": "$\\frac{z}{z + 1}, \\quad |z| < 1$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：单边指数序列的 $a = -1$ 特例计算。

1. 代入标准公式 $a^k \\varepsilon[k] \\leftrightarrow \\frac{z}{z - a}$；
2. 取 $a = -1$：
   $$F(z) = \\frac{z}{z - (-1)} = \\frac{z}{z + 1}$$
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
      { "key": "A", "text": "$H(z) = \\frac{z}{z^2 - 0.3z - 0.4}$，系统稳定" },
      { "key": "B", "text": "$H(z) = \\frac{1}{z^2 - 0.3z - 0.4}$，系统不稳定" },
      { "key": "C", "text": "$H(z) = \\frac{z^2}{z^2 - 0.3z - 0.4}$，系统处于临界稳定" },
      { "key": "D", "text": "$H(z) = \\frac{z - 1}{z^2 - 0.3z - 0.4}$，系统不稳定" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散系统差分方程的 Z 域转换与单位圆极点判据。

1. **求系统函数 $H(z)$**：
   两边取 Z 变换：
   $$Y(z)(1 - 0.3z^{-1} - 0.4z^{-2}) = X(z)z^{-1}$$
   $$H(z) = \\frac{Y(z)}{X(z)} = \\frac{z^{-1}}{1 - 0.3z^{-1} - 0.4z^{-2}} = \\frac{z}{z^2 - 0.3z - 0.4}$$
2. **求解系统极点**：
   分母因式分解：
   $$z^2 - 0.3z - 0.4 = (z - 0.8)(z + 0.5) = 0$$
   极点为 $z_1 = 0.8, \\, z_2 = -0.5$；
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
      { "key": "A", "text": "$\\frac{a z}{(z - a)^2}, \\quad |z| > |a|$" },
      { "key": "B", "text": "$\\frac{z}{(z - a)^2}, \\quad |z| > |a|$" },
      { "key": "C", "text": "$\\frac{a z}{z - a}, \\quad |z| > |a|$" },
      { "key": "D", "text": "$\\frac{a}{(z - a)^2}, \\quad |z| > |a|$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：Z 变换的 Z 域微分性质（乘以时域序列序号 $n$）。

1. 基础单边指数序列：
   $$a^n u(n) \\stackrel{\\mathcal{Z}}{\\longleftrightarrow} \\frac{z}{z - a} = \\frac{1}{1 - a z^{-1}}, \\quad |z| > |a|$$
2. 利用 Z 域微分性质：$n x(n) \\leftrightarrow -z \\frac{d X(z)}{dz}$：
   $$\\frac{d}{dz}\\left( \\frac{z}{z - a} \\right) = \\frac{(z - a) - z}{(z - a)^2} = -\\frac{a}{(z - a)^2}$$
3. 代入性质公式乘以 $-z$：
   $$X(z) = -z \\left( -\\frac{a}{(z - a)^2} \\right) = \\frac{a z}{(z - a)^2} = \\frac{a z^{-1}}{(1 - a z^{-1})^2}$$
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
      { "key": "A", "text": "$X(z) = -\\frac{z}{z - 3} + \\frac{2z}{z - 2}, \\quad 2 < |z| < 3$" },
      { "key": "B", "text": "$X(z) = \\frac{z}{z - 3} + \\frac{2z}{z - 2}, \\quad |z| > 3$" },
      { "key": "C", "text": "$X(z) = -\\frac{z}{z - 3} + \\frac{z}{z - 2}, \\quad |z| < 2$" },
      { "key": "D", "text": "收敛域为空集，Z 变换不存在" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：左边反因果序列与右边因果序列叠加的环状收敛域。

1. **第一项（反因果左边序列）**：
   由标准反因果公式 $-a^n u(-n - 1) \\leftrightarrow \\frac{z}{z - a}, \\, |z| < |a|$；
   因此 $3^n u(-n - 1) = -[-3^n u(-n - 1)] \\leftrightarrow -\\frac{z}{z - 3}$，其收敛域为内圆：$|z| < 3$；
2. **第二项（因果右边序列）**：
   $2^{n+1}u(n) = 2 \\cdot [2^n u(n)] \\leftrightarrow 2 \\cdot \\frac{z}{z - 2} = \\frac{2z}{z - 2}$，其收敛域为外圆：$|z| > 2$；
3. **求总收敛域交集**：
   $$\\text{ROC} = \\{|z| < 3\\} \\cap \\{|z| > 2\\} = 2 < |z| < 3$$
4. 两圆环相交不为空，因此变换存在，解析式为：
   $$X(z) = -\\frac{z}{z - 3} + \\frac{2z}{z - 2}, \\quad 2 < |z| < 3$$
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
      { "key": "A", "text": "$-\\frac{z}{z + 3}, \\quad |z| < 3$" },
      { "key": "B", "text": "$\\frac{z}{z + 3}, \\quad |z| > 3$" },
      { "key": "C", "text": "$\\frac{z}{z - 3}, \\quad |z| < 3$" },
      { "key": "D", "text": "$-\\frac{z}{z - 3}, \\quad |z| > 3$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：反因果左边序列的 Z 变换求解与收敛域判别。

1. 标准反因果左边序列变换公式：
   $$-a^k u(-k - 1) \\stackrel{\\mathcal{Z}}{\\longleftrightarrow} \\frac{z}{z - a}, \\quad |z| < |a|$$
2. 取 $a = -3$：
   $$-(-3)^k u(-k - 1) \\stackrel{\\mathcal{Z}}{\\longleftrightarrow} \\frac{z}{z - (-3)} = \\frac{z}{z + 3}, \\quad |z| < |-3| = 3$$
3. 两端同乘以 $-1$：
   $$(-3)^k u(-k - 1) \\stackrel{\\mathcal{Z}}{\\longleftrightarrow} -\\frac{z}{z + 3}, \\quad |z| < 3$$
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
      { "key": "C", "text": "$h(k) = \\sum_{m=-\\infty}^k g(m)$" },
      { "key": "D", "text": "$h(k) = \\frac{d g(k)}{dk}$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散单位冲激响应与阶跃响应的一阶后向差分关系。

1. 连续系统中冲激响应是阶跃响应的一阶导数：$h(t) = \\frac{dg(t)}{dt}$；
2. 离散系统中微分由**一阶后向差分**取代：
   $$\\delta(k) = \\varepsilon(k) - \\varepsilon(k - 1)$$
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
    "stem": "任意离散时间序列 $x(n)$ 的离散时间傅里叶变换（DTFT）$X(e^{j\\Omega}) = \\sum_{n=-\\infty}^\\infty x(n)e^{-j\\Omega n}$，必定是：",
    "options": [
      { "key": "A", "text": "以 $2\\pi$ 为周期的连续周期函数" },
      { "key": "B", "text": "非周期的连续函数" },
      { "key": "C", "text": "以 $\\pi$ 为周期的离散函数" },
      { "key": "D", "text": "非周期的离散序列" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散时间傅里叶变换（DTFT）的天然周期性。

1. 考察数字角频率平移 $2\\pi$：
   $$X(e^{j(\\Omega + 2\\pi)}) = \\sum_{n=-\\infty}^\\infty x(n) e^{-j(\\Omega + 2\\pi)n} = \\sum_{n=-\\infty}^\\infty x(n) e^{-j\\Omega n} \\cdot e^{-j 2\\pi n}$$
2. 因为对于任意整数 $n$，$e^{-j 2\\pi n} = \\cos(2\\pi n) - j\\sin(2\\pi n) = 1$；
3. 所以恒有：
   $$X(e^{j(\\Omega + 2\\pi)}) = X(e^{j\\Omega})$$
4. 因此 DTFT 的频谱必然是**以 $2\\pi$ 为周期的连续频域函数**。
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
    "stem": "因果序列 $f(k)$ 的 Z 变换为 $F(z) = \\frac{z^2 + 2z}{z^2 - 1.2z + 0.32}$，则序列初始值 $f(0)$ 为：",
    "options": [
      { "key": "A", "text": "1" },
      { "key": "B", "text": "2" },
      { "key": "C", "text": "0" },
      { "key": "D", "text": "3.2" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：单边 Z 变换初值定理的计算。

1. 单边因果序列初值定理公式：
   $$f(0) = \\lim_{z \\to \\infty} F(z)$$
2. 代入分式求极限：
   $$f(0) = \\lim_{z \\to \\infty} \\frac{z^2 + 2z}{z^2 - 1.2z + 0.32} = \\lim_{z \\to \\infty} \\frac{1 + \\frac{2}{z}}{1 - \\frac{1.2}{z} + \\frac{0.32}{z^2}} = \\frac{1}{1} = 1$$
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
    "stem": "离散因果稳定全通系统（All-pass Filter）如果存在一个位于单位圆内的极点 $z_p = r e^{j\\theta}\\,(r < 1)$，则其对应的传输零点必定位于单位圆外共轭镜像倒数位置 $z_0 = \\frac{1}{z_p^*} = \\frac{1}{r}e^{j\\theta}$ 处。",
    "options": [
      { "key": "A", "text": "正确（True）" },
      { "key": "B", "text": "错误（False）" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散全通系统零极点在单位圆内外的几何倒数对称性。

1. 一阶离散全通滤波器的标准形式为：
   $$H_{ap}(z) = \\frac{z^{-1} - z_p^*}{1 - z_p z^{-1}} = \\frac{1 - z_p^* z}{z - z_p}$$
2. 求其极点与零点：
   - 极点由分母决定：$z = z_p$（位于单位圆内）；
   - 零点由分子决定：$1 - z_p^* z = 0 \\implies z = \\frac{1}{z_p^*}$；
3. 若极点为 $r e^{j\\theta}$，则零点为 $\\frac{1}{r e^{-j\\theta}} = \\frac{1}{r}e^{j\\theta}$，模长为 $\\frac{1}{r} > 1$，严格位于单位圆外部的共轭径向射线延长线上；
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
    "stem": "求象函数 $F(z) = \\frac{z}{(z - 1)(z - 2)}$（因果收敛域 $|z| > 2$）的逆 Z 变换 $f(k)$：",
    "options": [
      { "key": "A", "text": "$[2^k - 1]\\varepsilon(k)$" },
      { "key": "B", "text": "$[1 - 2^k]\\varepsilon(k)$" },
      { "key": "C", "text": "$[2^{k+1} - 1]\\varepsilon(k)$" },
      { "key": "D", "text": "$[2^k + 1]\\varepsilon(k)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散 Z 变换的“除以 $z$ 部分分式展开法”。

1. 先将两边除以 $z$：
   $$\\frac{F(z)}{z} = \\frac{1}{(z - 1)(z - 2)} = \\frac{A}{z - 1} + \\frac{B}{z - 2}$$
2. 留数法求系数：
   - $A = \\left[ \\frac{1}{z - 2} \\right]_{z = 1} = \\frac{1}{1 - 2} = -1$；
   - $B = \\left[ \\frac{1}{z - 1} \\right]_{z = 2} = \\frac{1}{2 - 1} = 1$；
3. 将 $z$ 乘回分子：
   $$F(z) = -\\frac{z}{z - 1} + \\frac{z}{z - 2}$$
4. 查标准因果逆变换对：
   - $\\frac{z}{z - 1} \\leftrightarrow \\varepsilon(k)$；
   - $\\frac{z}{z - 2} \\leftrightarrow 2^k \\varepsilon(k)$；
5. 合并得：
   $$f(k) = (2^k - 1)\\varepsilon(k)$$
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
   $$h(k) = (z_p)^k \\varepsilon(k) = (-0.6)^k \\varepsilon(k)$$
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

1. 若在单位圆 $z = 1$ 上有单极点，时域对应阶跃信号 $\\varepsilon(k)$（等幅有界，为临界稳定）；
2. 但若在单位圆上有 $m$ 阶（$m \\ge 2$）重极点，根据 Z 域微分性质，部分分式逆变换后将激发出自变量正比例项：
   $$\\frac{z}{(z - 1)^2} \\stackrel{\\mathcal{Z}^{-1}}{\\longleftrightarrow} k \\varepsilon(k)$$
3. 随着时间 $k \\to \\infty$，项 $k$ 将线性无限增大发散；
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
      { "key": "A", "text": "$X_1(z) X_2(z)$，收敛域至少为 $R_1 \\cap R_2$" },
      { "key": "B", "text": "$X_1(z) + X_2(z)$，收敛域为 $R_1 \\cup R_2$" },
      { "key": "C", "text": "$\\frac{1}{2\\pi j}\\oint X_1(v) X_2(z/v) v^{-1} dv$" },
      { "key": "D", "text": "$X_1(z) * X_2(z)$" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：时域卷积对应 Z 域代数乘积定理及收敛域交集。

1. 时域卷积定理：
   $$\\mathcal{Z}\\{x_1(k) * x_2(k)\\} = X_1(z) \\cdot X_2(z)$$
2. 收敛域规则：两信号乘积的收敛域至少包含各自收敛域的交集（即 $R_1 \\cap R_2$），若乘积中存在零极点对消，收敛域还可能进一步扩大。
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
    "stem": "在复 $z$ 平面上采用几何矢量法确定离散系统在频率 $\\Omega$ 处的幅频响应时，若在单位圆上的测试点 $e^{j\\Omega}$ 极度靠近系统的某个极点 $z_p$，则该频率处的幅频增益响应将：",
    "options": [
      { "key": "A", "text": "出现尖锐峰值（增益极大）" },
      { "key": "B", "text": "出现深坑下陷（增益衰减为零）" },
      { "key": "C", "text": "保持为 1 不变" },
      { "key": "D", "text": "发生 $180^\\circ$ 相位反转且增益不变" }
    ],
    "answer": "A",
    "analysis": """【核心考点】：离散系统频率响应的零极点几何矢量法。

1. 几何确定法幅频公式：
   $$|H(e^{j\\Omega})| = \\frac{\\prod_{m} |e^{j\\Omega} - z_{0m}|}{\\prod_{n} |e^{j\\Omega} - z_{pn}|} = \\frac{\\text{各零点矢量的长度之积}}{\\text{各极点矢量的长度之积}}$$
2. 当测试点 $e^{j\\Omega}$ 沿单位圆逆时针移动到某个靠近单位圆的极点 $z_p$ 附近时，对应的分母极点矢量长度 $|e^{j\\Omega} - z_p|$ 变得极小；
3. 分母极小导致整个商数急剧增大，从而在幅频特性曲线上形成尖锐的**增益峰值（共振峰）**。
（反之，若靠近零点则由于分子极小而形成深坑陷波）。
选 **A**。"""
  }
]

all_questions.extend(chapter5_questions)
print(f"Added Chapter 5: {len(chapter5_questions)} questions")
'''

with open('build_full_database.py', 'a', encoding='utf-8') as f:
    f.write(c4_c5_code)

print("Appended C4 and C5 successfully!")
