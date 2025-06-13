import re
text = "InsertSpaceBeforeCapitalsInThisSentence"
spaced = re.sub(r'(?=[A-Z])', ' ', text).strip()
print("Spaced string:", spaced)
