import re
pattern = r"ab*"
test_string = "abbb abb a ac"
matches = re.findall(pattern, test_string)
print("Matches:", matches)
