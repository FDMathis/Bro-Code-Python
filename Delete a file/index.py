
import os
import shutil

path = 'delete me.txt'

try:
    os.remove(path) #delete a file
    #os.rmdir(path) #delete a file of empty folder (directory)
    #shutil.rmtree(path) #delete files and or folders
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("That folder contains no files")
else:
    print(path+" deletion was successful")
