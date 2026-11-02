with open('build_full_database.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace any unescaped \underline with \\underline
fixed = content.replace(r'\underline', r'\\underline')
# Also check \u( or other \u not followed by 4 hex digits
import re
# If \u is followed by non-hex, escape it to \\u
# But don't break genuine \uXXXX
# Actually in python code, if the string isn't raw, \u followed by non-hex causes SyntaxError: truncated \uXXXX escape.
# Let's replace any \u that is NOT followed by 4 hex digits with \\u
def fix_u(match):
    s = match.group(0)
    # if it's \u[0-9a-fA-F]{4}, keep it
    if re.match(r'^\\u[0-9a-fA-F]{4}', s):
        return s
    return '\\\\' + s[1:]

fixed = re.sub(r'\\u[^{0-9a-fA-F]|\\[uU](?![0-9a-fA-F]{4})', fix_u, fixed)

with open('build_full_database.py', 'w', encoding='utf-8') as f:
    f.write(fixed)

print("Fixed build_full_database.py escapes!")
