import re
pattern = r"ab{2,3}"
test_string = "ab abb abbb abbbb a"
matches = re.findall(pattern, test_string)
print("Matches:", matches)
