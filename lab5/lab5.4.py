import re
pattern = r"[A-Z][a-z]+"
test_string = "Test Another One OKAY FinalTest"
matches = re.findall(pattern, test_string)
print("Matches:", matches)
