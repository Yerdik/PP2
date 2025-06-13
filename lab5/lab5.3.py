import re
pattern = r"[a-z]+_[a-z]+"
test_string = "this_is a_test string_example with_more_data"
matches = re.findall(pattern, test_string)
print("Matches:", matches)
