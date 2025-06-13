import re
text = "HelloWorldThisIsPython"
parts = re.findall(r'[A-Z][^A-Z]*', text)
print("Split parts:", parts)
