import re

pattern = re.compile('[A-Z]{1}[a-z]*')
message = """Mary is a friend of mine, she studied at Oxford and now works at Google"""

print(pattern.findall(message))

# ============================================

keywords = {'greet': ['hello', 'hi', 'hey'], 'goodbye': ['bye', 'farewell'], 'thankyou': ['thank', 'thx']}
patterns = {}

for intent, keys in keywords.items():
    patterns[intent] = '|'.join(keys)

print(patterns)

# ============================================


