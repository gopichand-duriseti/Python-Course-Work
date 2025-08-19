import os
file_path = os.path.join("folder", "example.txt")
with open(file_path, "r") as file:
    print(file.read())