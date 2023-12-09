"""
The below program explains about exception handling in Python.
Preventing the abnormal termination of a program is called exception handling.
There are two types of errors.
    1. syntax error
    2. Runtime error also known as exceptions
Some unwanted, unexpected event which disturbs the normal flow of the program is called Exception.
The purpose of exception handling is graceful termination of the program.
Defining an alternate way to continue the rest of the program normally is the meaning for exception handling.
Every exception in Python is a class
All exception classes are child class of BaseException directly or indirectly
"""

import os

print('Hello')
try:
    print(10/0)  # we need to place the risky code in try block
    # risky code is nothing but the code which may rise exception
except ZeroDivisionError:
    print('Stupid fellow! how can u divide with zero')
print('Hi')

# printing the exception information
try:
    print(10/0)
except ZeroDivisionError as msg:
    print('Exception is raised and its description is',msg)

# try with multiple except blocks
try:
    print(10/2)
    x = int("ten")
except ZeroDivisionError:
    print('ZeroDivisionError occurred')
except ValueError:
    print('ValueError occurred')

# when we have multiple except blocks the execution order will be from top to bottom
# It means if we specify parent exception class first the bottom child class won't get executed

try:
    print(10/2)
    x = int("ten")
except Exception:
    print('Some exception occurred')
except ZeroDivisionError:
    print('zero division error occurred')

# the above code snippet will every time go into Exception class as it is the parent class for both
# ZeroDivisionError and ValueError

# single except block can handle multiple exceptions
try:
    print(10/1)
    x = int("ten")
except (ZeroDivisionError, ValueError) as msg:
    print(msg,'error occurred')

# default except block
try:
    print(5/1)
    x = int("ten")
except ZeroDivisionError:
    print('zero division error occurred')
except:  # this is default except block then can handle any exception
    print('Some exception occurred')

# The default except block must be last otherwise we will get syntax error

# finally block
# If you want to execute some statement whether exception is occurred or not finally block is best.
# Even when the exception is not handled finally block will ge executed

try:
    try:
        x = 10 + 'ten'
    except ZeroDivisionError as msg:
        print(msg,'error occurred')
    finally:  # In this scenario where exception is not handled as well finally block will get executed
        print('successfully completed the execution of code snippet')
except TypeError:
    print('Nested try catch')

# situation where finally block won't get executed is when the python interpreter shuts down

try:
    print('try')
    os._exit(0)  # this statement will shut down python interpreter hence finally block won't get executed
except ValueError:
    print('except')
finally:
    print('finally')
