"""
Some theory about Python Programming Language :-
------------------------------------------------

When compared with other programming languages Python is very easy to learn
Python is a general purpose high level programming language
General purpose :- can be used to develop data analysis applications, web-application, desktop applications etc.,
Human understandable languages are high level programming languages

Python was developed by Guido Van Rossam in 1989 while working at National Research Institute in netherlands
Officially Python was made available to public in Feb 20th, 1991

C and Java are statically typed programming language (the variable type should be declared before using it)
Python is dynamically typed programming language (no need to declare type of variable before using it)
    Based on the value we assign to the variable the type of the variable will be determined

Features of Python :-
---------------------

1. Simple and easy to learn
2. Freeware(no need to pay anything to use the software) and open source(we can see the
source code of the functions and customise it if we want to)
3. Python is both procedure oriented and object-oriented programming language
4. Python is interpreted programming language
5. Python has rich library support which makes it easy to code complex logics

Python Versions :-
------------------

Python 1.0 introduced in Jan 1994
Python 2.0 introduced in October 2000
Python 3.0 introduced in December 2008 -- highly recommended to use

In General any new s/w version should provide support for old version programs
Python 3 doesn't provide backward compatibility to Python 2 programs

print "Hello" -- valid in Python 2 but invalid in Python 3
long data type is present in Python2 but not available in Python3

"""

import math  # math is called a module which is basically a group of functions, variables and classes
from random import *
import keyword

print('Hello World in Python')
a, b = 10, 20
print(f'Sum of {a} and {b} is: {a + b}')
a, b, c, d, e = 100, 200, 300, 400, 500
print(f'Sum of the variables declared in the same line is: {a + b + c + d + e}')
print(f'The type of the variable a is: {type(a)}')
a = True  # We can make variable a point to a different type of value as well which is perfectly fine in Python
print(f'The type of the variable a after modifying is: {type(a)}')

print(f'Square root of 10 is {math.sqrt(10)}')
print('Using randint function to generate a six digit random number')

# sep is used to pass our own delimiter between values in the print function
for i in range(10):
    print(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9),
          randint(0, 9), randint(0, 9), randint(0, 9), sep='')

'''
Identifiers :-
--------------
Any name in a Python program is called identifier.
It can be a variable name, function name, class name etc.,

Rules to define an identifier :-
--------------------------------

1. The only allowed symbols are Alphabets(both upper case an lower case), Digits(0-9) and underscore(_)
2. Identifiers should not start with digit
3. Python Identifiers are case sensitive. total and TOTAL are two different variables
4. We can not use keywords(reserved words) like if, def, class etc., as identifiers
5. There is no length limit for Python identifier

'''

total = 20
TOTAL = 200
print(f'total: {total}')
print(f'TOTAL: {TOTAL}')

# If the identifier starts with underscore symbol it indicates that it is private
# If the identifier starts with two underscore symbols then it is strongly private
# If the identifier starts and ends with two underscore symbols then it is language specific identifier

print(f'All the keywords in Python are: {keyword.kwlist}')
# In the current version of Python we are using there are 35 keywords

x = 10
print(f'The value of x before deletion is {x}')
del x  # deleting the variable x so that it is eligible for garbage collection
# print(f'The value of x after deletion is {x}')  # NameError: name 'x' is not defined
