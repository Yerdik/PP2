# count_lines.py

file_path = "example.txt"

with open(file_path, "r") as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))
