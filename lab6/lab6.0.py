# write_list_to_file.py

my_list = ["apple", "banana", "cherry"]
with open("fruits.txt", "w") as f:
    for item in my_list:
        f.write(item + "\n")

print("List written to fruits.txt")
