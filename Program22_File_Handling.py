"""
The below program explains about file handling techniques in Python.
When we have less information, and we want to store that information for future purpose then we should go for files.

Files are a permanent way of storing our data.
Types of files:
    1. text files -- used to store text data
    2. binary files -- used to store image, video files

If we want to perform any operation with files you have to open the file.
While opening the file we need to specify for which purpose we are opening the file.

To open the file we need to python in-built open() function
    f = open(filename,mode)

The allowed modes in Python are:-
---------------------------------

    1. r ==> open an existing file for read operation. If the file is not present we get FileNotFoundError.
    2. w ==> open a file for write operation. If the file already exists the data will be overwritten otherwise
             it will create a new file
    3. a ==> open a file for append operation. If the file already exists it will start appending the data.
            If the file doesn't exist it will create a new file
    4. r+ ==> To read and write data to the file. The previous data in the file won't be deleted.
              The file pointer always point to the beginning of the file
    5. w+ ==> To perform write and read operation. In this case the file data will be overwritten.
    6. a+ ==> To perform append and read operation. The file data won't be overwritten.
    7. x ==> To open a file in exclusive creation mode for write operation. If the file is already available
             while writing it will return FileExistsError

All these modes are applicable only for text files.
If we want to work on binary files for all these modes we need to suffix with b.
rb, wb, ab, r+b, w+b, a+b, xb

After performing all the required operations we are required to close the file.
    f.close()

Various properties of the file object:-
---------------------------------------

    1. f.name --> To know the name of the file
    2. f.mode --> In which mode did we open the file
    3. f.closed --> returns the boolean value whether the file is closed or not
    4. f.readable() --> Is it a readable file or not
    5. f.writable() --> Is it a writable file or not

Reading data from the file:-
----------------------------

read() -- To read total data from the file
read(n) -- To read n characters from the file
readline() -- To read only one line
readlines() -- To read all the lines in the file into a list

"""

import os.path
import os
import csv
import random
from zipfile import *


file1 = open('abc.txt','w')  # The file will be created in the current working directory
print(f'File name: {file1.name}')
print(f'File mode: {file1.mode}')
print(f'Is file readable: {file1.readable()}')
print(f'Is file writable: {file1.writable()}')
print(f'File closed: {file1.closed}')
file1.write('Dharani\n')  # writing the data to the file
file1.write('Kumar\n')
file1.write('Gopavaram\n')
print('Data successfully written to the file')
file1.close()
print(f'File closed: {file1.closed}')

file2 = None
try:
    file2 = open('dharani.txt','r')
except FileNotFoundError:
    print('The specified is not available for read')
finally:
    if file2 is not None:
        file2.close()

file3 = None
try:
    file3 = open('dharani.txt','x')
    print(f'File name: {file3.name}')
    print(f'File mode: {file3.mode}')
    print(f'Is file readable: {file3.readable()}')
    print(f'Is file writable: {file3.writable()}')
    print(f'File closed: {file3.closed}')
    print(f'File closed: {file3.closed}')
except FileExistsError:
    print("Exclusive mode doesn't accept a file which already exists")
finally:
    if file3 is not None:
        print('Successfully closing the file')
        file3.close()

file4 = open('abc.txt','a')  # append method won't overwrite the file
file4.write('Dharani\n')  # If we want to write one line at a time we can use the write method
file4.write('Kumar\n')  # If we don't specify \n then it will get appended in the same line itself
file4.write('Gopavaram\n')
file4.write('Kavya\n')
sample_list = ['Sunny\n','Bunny\n','Dharani\n','Kumar\n']
file4.writelines(sample_list)  # To write multiple lines to a file at the same time
# The writelines method accepts only
file4.close()
print('Data successfully appended to the file')

# reading data from the file

# read method

file5 = open('abc.txt','r')
data = file5.read()  # This will convert the entire file data to string
print(f'The type of the variable data is {type(data)}')
print('The data in the file abc.txt is')
print(data)
file5.close()

# read(n) -- reading characters method

file6 = open('abc.txt','r')
first_10_char = file6.read(10)
print('The first 10 characters in the file abc.txt is')
print(first_10_char)
file6.close()

# reading line by line

print('The first 3 lines in the file abc.txt are')
file7 = open('abc.txt','r')
print(file7.readline(),end='')
print(file7.readline(),end='')
print(file7.readline())
file7.close()

# reading the entire content of the file to list
print('saving the entire file content to list')
file8 = open('abc.txt','r')
data_list = file8.readlines()
for line in data_list:
    print(f'current line is: {line}',end='')
file8.close()

# using with keyword to perform operations on file which will automatically close the file once we are done

with open('dharani.txt','w') as f:
    f.write('Ram\n')
    f.write('Robert\n')
    f.write('Rahim\n')
    print('Is file closed?',f.closed)
print('came out of the with block')
print('Is file closed?',f.closed)  # Once we come out of the block the file will be automatically closed

# tell() method is used to know the current position of the cursor

with open('dharani.txt','r') as f:
    print(f.tell())  # The current position of the file pointer will be always zero
    print(f.readline(),end='')
    print(f.tell())  # Once we read some data the file pointer position will automatically move
    print(f.read(4))
    print(f.tell())

# seek() method is used to move the file pointer to a specific position

data = 'All students are STUPIDS'
with open('file_practice.txt','w+') as f:
    f.write(data)  # writing the data to the file
    print('Data successfully written to the file')
    print('Reading the data from the file')
    print(f.read(),end='')
    print(f'The current cursor position is: {f.tell()}')
    f.seek(17)  # Moving the cursor position to the 17th position
    print(f'The current cursor position is: {f.tell()}')
    f.write('GEMS!!!')  # Overriding the data starting from 17th position
    f.seek(0)
    print('Data in the file after modification')
    print(f.read())

# Sample program to check whether a given file exists or not
# If it is available read the content and display the number of lines, characters and words present in the file

filename = input('Enter the filename:')
if os.path.exists(filename):  # We can use os module exists method to check whether a file exists or not
    with open(filename,'r') as f:
        line_count = word_count = character_count = 0
        for line in f:
            line_count += 1
            character_count += len(line)
            word_count += line.count(' ') + 1
        print(f'The number of lines present in the file is: {line_count}')
        print(f'The number of words present in the file is: {word_count}')
        print(f'The number of characters present in the file is: {character_count}')
else:
    print('The specified file does not exist')

# copy and paste an image file using python file handling concept
with open('/Users/dharani-kumar/Desktop/time_quote.jpg','rb') as f1:
    with open('/Users/dharani-kumar/Desktop/time_quote_copy.jpg','wb') as f2:
        image_data = f1.read()  # The binary data is stored in bytes datatype
        print(f'The type of the variable image_data is {type(image_data)}')
        f2.write(image_data)
        print('Image copied successfully')

# working with csv data we have an in-built module called csv module which will help us do it
# writing the data to the csv file

with open('employee_data.csv','w',newline='') as f:  # newline will prevent adding one extra line between the lines
    w = csv.writer(f)  # creating a csv writer object to write the data
    w.writerow(("Employee_number","Employee_Name","Employee_Sal","Employee_Addr"))
    # writerow method is used to write data to the csv file
    sample_name_list = ['Ram', 'Robert', 'Rahim', 'Ram']
    sample_addr_list = ['Hyd', 'Mumbai', 'Chennai', 'Kolkata']
    sample_sal_list = [10000, 9800, 9600, 9900, 8800]
    for i in range(1,100):
        emp_no = random.randint(1,1000000)
        emp_name = random.choice(sample_name_list)
        emp_sal = random.choice(sample_sal_list)
        emp_addr = random.choice(sample_addr_list)
        w.writerow([emp_no, emp_name, emp_sal, emp_addr])  # writerow function accepts an iterable

print('Total employee data returned to csv file successfully')

# reading the data from the csv file

with open('employee_data.csv','r') as f:
    r = csv.reader(f)
    csv_data = list(r)  # The data will be stored in list(list)
    for line in csv_data:
        for word in line:
            print(word,'\t',end='')
        print()


# Zipping and unzipping files

# zipping multiple files into one single zip file

with ZipFile('file.zip','w',ZIP_DEFLATED) as f:  # here we are creating ZipFile class object
    f.write('abc.txt')  # writing a file to the zip file
    f.write('employee_data.csv')
    f.write('log.txt')

print('files.zip file created successfully')


# unzipping the files

with ZipFile('file.zip','r',ZIP_STORED) as f:
    names = f.namelist()  # this will give us all the filenames present in the zip file
    for name in names:  # printing the data present in every file to console
        print('The content of the file',name,'is')
        with open(name,'r') as f1:
            for line in f1:
                print(line,end='')
            print()
