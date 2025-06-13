import re
text = "Python is fun, easy. Simple!"
replaced = re.sub(r"[ ,.]", ":", text)
print("Replaced string:", replaced)
