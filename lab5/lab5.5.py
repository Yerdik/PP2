import re
pattern = r"a.*b"
test_string = "acb a123b axxxb a b"
matches = re.findall(pattern, test_string)
print("Matches:", matches)