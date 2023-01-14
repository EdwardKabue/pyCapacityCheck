import os
import sys

cmd_arg = sys.argv #list that stores command line arguments
path = "." #make the current directory the default path

#get the path entered on the command line
if(len(cmd_arg) == 2):
    path = cmd_arg[1]

file_dir_list = os.listdir(path) #get the list of files and directories

for item in file_dir_list:
    #print(os.path.abspath(item))
    if(os.path.isdir(os.path.abspath(item))):
        print(item)
    