# list_dirs_and_files.py

import os

path = "."  # Current directory

# List only directories
print("Directories:")
print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])

# List only files
print("\nFiles:")
print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

# List all
print("\nAll (dirs and files):")
print(os.listdir(path))
