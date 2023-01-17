import os
import sys
import subprocess

cmd_arg = sys.argv #list that stores command line arguments
path = "." #make the current directory the default path

#get the path entered on the command line
if(len(cmd_arg) == 2):
    path = cmd_arg[1]

file_dir_list = os.listdir(path) #get the list of files and directories

du_process = subprocess.run(["du", "-h", "--max-depth=1", path], capture_output=True, text=True)

print(type(du_process.stdout))

#os.chdir(path) #move to the entered directory.

# for item in file_dir_list:
#     #print(os.path.abspath(item))
#     if(os.path.isdir(item)):
#         print(item)
