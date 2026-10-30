import re

with open("test-repo/deliveries/jee-mechanics-handbook/index.html") as f:
    html = f.read()

# 1. Display math blocks
display_math = re.findall(r'\$\$(.*?)\$\$', html, re.DOTALL)
print(f"Total Display Math blocks: {len(display_math)}")

unbalanced_display = []
for idx, block in enumerate(display_math):
    open_b = block.count('{')
    close_b = block.count('}')
    if open_b != close_b:
        unbalanced_display.append((idx, block, open_b, close_b))

print(f"Unbalanced display math blocks: {len(unbalanced_display)}")
for idx, block, ob, cb in unbalanced_display:
    print(f"  Block #{idx}: open={ob}, close={cb}")
    print(f"  Content: {block.strip()[:100]}")

# 2. Inline math blocks
cleaned = re.sub(r'\$\$.*?\$\$', '', html, flags=re.DOTALL)
inline_tokens = cleaned.split('$')
# Even tokens are text, odd tokens are math
inline_math = inline_tokens[1::2]
print(f"Total Inline Math blocks: {len(inline_math)}")

unbalanced_inline = []
for idx, block in enumerate(inline_math):
    open_b = block.count('{')
    close_b = block.count('}')
    if open_b != close_b:
        unbalanced_inline.append((idx, block, open_b, close_b))

print(f"Unbalanced inline math blocks: {len(unbalanced_inline)}")
for idx, block, ob, cb in unbalanced_inline:
    print(f"  Inline #{idx}: open={ob}, close={cb}")
    print(f"  Content: {block.strip()}")
