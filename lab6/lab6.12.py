# copy_file.py

import shutil

source = "source.txt"
destination = "destination.txt"

shutil.copyfile(source, destination)
print(f"Copied contents from {source} to {destination}")
