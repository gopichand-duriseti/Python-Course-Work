import os
if os.path.exists("example.txt"):
    file = open("example.txt", "r")
    print("File opened successfully.")
else:
    print("File does not exist.")