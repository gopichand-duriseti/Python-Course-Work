'''
'r' Read (default mode)
'w' Write (overwrites existing content)
'a' Append (adds to the end of the file)
'b' Binary mode (e.g., for images, PDFs)
'+' Read and Write
'''

import os
'''OPENING A FILE'''
#Python uses the open() function to open a file in different modes.
file = open("example.txt", "r") # Opens file in read mode

'''CHECKING IF A FILE EXISTS BEFORE OPENING'''
#Use os.path.exists() to check if a file exists.
if os.path.exists("example.txt"):
    file = open("example.txt", "r")
    print("File opened successfully.")
else:
    print("File does not exist.")

'''READING A FILE'''
file = open("example.txt", "r")
content = file.read() # Reads the entire content
lines = file.readlines() # Reads all lines into a list
line = file.readline() # Reads a single line
print(content)
file.close()

#Best Practice: Use the with statement to automatically close the file.
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

'''WRITING TO A FILE'''
#Note: 'w' mode erases previous content.
with open("example.txt", "w") as file:
    file.write("Hello, World!") # Overwrites existing content

'''APPENDING TO A FILE'''
with open("example.txt", "a") as file:
    file.write("\nNew Line Added.") # Adds new content at the end

'''FILE PATH OPERATIONS'''
#Using os.path.join() for Cross-Platform Compatibility
#Use os.path.join() to construct file paths that work across different operating systems.
import os
file_path = os.path.join("folder", "example.txt")
with open(file_path, "r") as file:
    print(file.read())

'''GETTING FILE INFORMATION'''
import os
file_path = "example.txt"
if os.path.exists(file_path):
    print("File Size:", os.path.getsize(file_path), "bytes")
    print("Absolute Path:", os.path.abspath(file_path))
else:
    print("File does not exist")
