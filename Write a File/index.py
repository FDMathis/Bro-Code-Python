
#Write the text
text = "Yooooooooooooo\nThis is some text\nHave a good one!\n"

#'a' appends, 'w' writes
with open('/users/fredmathis/Bro Code/testfile.txt','a') as file: 
    file.write(text)

#Read file to check
try:
    with open('/users/fredmathis/Bro Code/testfile.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found.")       

#NOTE: Text was already written once and appended to write a second time