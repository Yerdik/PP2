# delete_file_if_exists.py

import os

file_path = "delete_me.txt"

if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"{file_path} deleted.")
    else:
        print(f"No write access to {file_path}")
else:
    print(f"{file_path} does not exist")
