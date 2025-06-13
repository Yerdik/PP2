# create_A_to_Z_files.py

import string

for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    with open(filename, "w") as f:
        f.write(f"This is file {filename}\n")

print("Files A.txt to Z.txt created.")
