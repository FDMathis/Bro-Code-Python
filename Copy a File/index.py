
# copyfile() = copies contents of a file
# copy()     = copyfile() + permission mode + destination can be a directory
# copy2()    = copy() + copies metadata (file's creation and modification times)

#First, import the shutil module
import shutil

#Next, call shutil and copy method with source and destination
shutil.copyfile('/users/fredmathis/Bro Code/testfile.txt','testfilecopy.txt')