"""
The below program explains about the important functions present in os module
"""

import os
import datetime

print(os.getcwd())  # print the current working directory
print(os.listdir())  # print the contents present in the current working directory
print(os.listdir('/Users/dharani-kumar/Desktop'))  # We can explicitly specify the directory if we want

try:
    os.mkdir('Dharani/')  # To create a single directory
    print('Directory Dharani got created successfully')
except FileExistsError:
    print('The directory with name Dharani already exists')

try:
    os.makedirs('Dharani/Kumar/Kavya/')  # to create multiple directories at the same time we need to use makedirs
    print('Multiple directories Dharani/Kumar/Kavya got created successfully')
except FileExistsError:
    print('The directory with name Dharani/Kumar/Kavya already exists')

os.rename('Dharani/Kumar/Kavya','Dharani/Kumar/Gopavaram')  # renaming the directory
print('Successfully renamed the directory')

os.rmdir('Dharani/Kumar/Gopavaram/')  # To remove one single directory we need to use rmdir
# The directory should be empty if we want run rmdir command
print('Successfully removed the last sub-folder')

os.removedirs('Dharani/Kumar')  # Remove multiple directories at the same time
print('Successfully removed all the folders')

file_stats = os.stat('employee_data.csv')  # To get statistics of a file
# The times returned by the stat method is the number of milliseconds that happened since Jan 1st, 1970 12:00
print('File size:',file_stats.st_size)
print('Last accessed time in date format:',datetime.datetime.fromtimestamp(file_stats.st_atime))
print('Last modified time in date format:',datetime.datetime.fromtimestamp(file_stats.st_mtime))

for dir_path, dir_names, filenames in os.walk('.'):
    print('Current working directory:',dir_path)
    print('Directories in the current directory:',dir_names)
    print('Files in the current directory:',filenames)
    print()

# Running shell commands from Python program
# we can use the system function present in os module to run the shell commands from Python program

os.system('ls -l *.py')
os.system('cat *.py | grep -i files')




