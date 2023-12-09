"""
The below program shows different ways of importing modules to our application
"""

import math
import os as o  # giving alias name to the imported module
import random
import dharani_math_module  # a module will be imported only once no matter how many times u import it
import time
# from imp import reload # imp module is deprecated from pytho 3.12

print(f'using sqrt function in math module math.sqrt(100) = {math.sqrt(100)}')
print(f'getting the pi value using math function math.pi = {math.pi}')
print(f"checking whether a file exists or not")
print(o.path.exists('/Users/dharani-kumar/Documents/Final_Interview_Preparation'))  # using alias name
print(f'Using randint function in random module directly: {random.randint(10, 100)}')  # directly using function
print(f'Using choices method in random module directly: {random.choices([10, 20, 30])}')

print(f'dharani_math_module.x = {dharani_math_module.x}')
print(f'dharani_math_module.y = {dharani_math_module.y}')

print('Program entering into sleep for 2 seconds')
time.sleep(2)  # sleep method will make the program sleep for 30 seconds
import dharani_math_module  # Here it won't get imported again
dharani_math_module.add_num(10, 20)
dharani_math_module.product_num(10, 20)

'''
This is the way we can reload the module if imp module is available:
--------------------------------------------------------------------

print('Program entering into sleep for 30 seconds')
time.sleep(30)
reload(dharani_math_module)  # Here the new version of the module will get imported
import dharani_math_module
dharani_math_module.add_num(10, 20)
dharani_math_module.product_num(10, 20)

'''

print(f'The members in the current module is {dir()}')  # will return the members in the current module
print(f'The members in the math module is {dir(math)}')  # will return the members of the module we passed
print(f'Detailed description of every method present in math module is {help(math)}')

# use of the special variable __name__
# __name__ variable will help us figure out how the function call got executed
# Is it directly as a file or indirectly as a module in some other python program

dharani_math_module.f1()


# some important functions in math module
print(f'math.sqrt(4) = {math.sqrt(4)}')  # returns floating point value
print(f'math.ceil(10.1) = {math.ceil(10.1)}')  # returns the next integer value
print(f'math.floor(10.1) = {math.floor(10.1)}')  # returns the previous integer value
print(f'math.fabs(-10.1) = {math.fabs(-10.1)}')  # returns the absolute value which will ignore the sign
print(f'math.fabs(10.1) = {math.fabs(10.1)}')  # fabs means float absolute value


# working with functions in random module.
# random module contains several functions which are useful to generate random numbers.

print(f'random.random() = {random.random()}')  # will generate random float number between 0 and 1(not inclusive)
print(f'random.randint(100,1000) = {random.randint(100, 1000)}')
# randint will generate random number between the numbers we pass(inclusive)
print(f'random.uniform(1,2) = {random.uniform(1,2)}')
# uniform function will return random float number between the numbers we pass(not inclusive)

print(f'random.randrange(10) = {random.randrange(10)}')  # will generate random number between 0 and 9
print(f'random.randrange(1,11) = {random.randrange(1,11)}')  # will generate random number between 1 and 10
print(f'random.randrange(1,11,2) = {random.randrange(1,11,2)}')
# The above line will generate random number picked from 1, 3, 5, 7, 9

sample_list = [10, 20, 30, 40, 'Dharani']
print(f'random element in the collection is: {random.choice(sample_list)}')
print(f'random element in the string is: {random.choice("dharani")}')
# we can not apply choice method on sets because sets are not indexed

# generate 6 digit random number
for i in range(10):
    print(random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),
          random.randint(0,9),random.randint(0,9),sep='')

# generate random password of length 6 where 1, 3, 5 are alphabet symbols and 2, 4, 6 are digits
for i in range(10):
    print(chr(random.randrange(65,90)),random.randint(0,9),chr(random.randrange(65,90)),random.randint(0,9),
          chr(random.randrange(65,90)),random.randint(0,9),sep='')
