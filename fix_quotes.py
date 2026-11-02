import re

with open('src/data/signalsQuestions.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix delta'(x) inside single quotes
content = content.replace("stem: '计算广义积分 $\\int_{-\\infty}^\\infty (1 - x)\\delta'(x) \\, dx$ 的值为：'",
                          'stem: "计算广义积分 $\\\\int_{-\\\\infty}^\\\\infty (1 - x)\\\\delta\'(x) \\\\, dx$ 的值为："')

# Check other delta'
content = re.sub(r"stem: '([^']*?\\delta'[^']*?)'", r'stem: "\1"', content)

with open('src/data/signalsQuestions.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replacement done.")
