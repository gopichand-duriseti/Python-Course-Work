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