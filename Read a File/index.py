
try:
    with open('/users/fredmathis/Bro Code/testfile.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found.")       