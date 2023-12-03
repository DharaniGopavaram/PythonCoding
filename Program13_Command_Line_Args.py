"""
The below program explains about command line arguments

argv is the variable which will hold all the command line arguments
The type of the variable argv is list
The argv variable is available in sys module
The first value of the argv is the name of the filename where we write our code
If you want to make a command line argument with space as a single argument then enclose the
    command line argument with double quotes single quotes won't work in this case
"""

from sys import argv

print(f'The type of the variable argv is {type(argv)}')
print(f'argv: {argv}')  # will print the filename as first argument
print(f'argv[1:]: {argv[1:]}')  # will exclude the filename from the result

cmd_args_sum = 0
for x in argv[1:]:
    cmd_args_sum += int(x)

print(f'The sum of the command line arguments entered is: {cmd_args_sum}')
