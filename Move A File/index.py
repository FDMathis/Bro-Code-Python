
# Import the os module
import os

source = "testfile.txt"
destination = "/users/fredmathis/Bro Code/testfile.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there.")
    else:
        os.replace(source,destination)
        print(source+" was moved.")
except FileNotFoundError:
    print(source+" was not found.")
