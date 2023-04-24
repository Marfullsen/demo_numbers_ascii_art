import art
import sys

output = ''

for font in art.FONT_NAMES:
    output += font + '\n===\n'
    output += art.text2art("1234567890", font=font)
    output += '\n\n\n'

original_stdout = sys.stdout
with open('output.txt', 'w', encoding="utf-8") as f:
    sys.stdout = f
    print(output)
    sys.stdout = original_stdout