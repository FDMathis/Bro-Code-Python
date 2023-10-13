# Module = A file containing Python code.  May contain functions, classes, etc...
#          Used with modular programming, which is to separate a program into parts



#import messages file and call functions
import messages

messages.hello()
messages.bye()


#Import messages file as a nickname and call functions
#import messages as msg
#msg.hello
#msg.bye


# Import specific functions from messages file and call them directly
# from messages import hello,bye
#hello()
#bye()



# from messages import * (asterisk means "import all" this one is dangerous)
# It can be problematic if importing a large file - AVOID!!


#To see a list of prewritten modules
#help("modules")