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
    print('Nested try except')

# situation where finally block won't get executed is when the python interpreter shuts down

try:
    print('try')
    # os._exit(0)  # this statement will shut down python interpreter hence finally block won't get executed
except ValueError:
    print('except')
finally:
    print('finally')

# Nested try except block

try:
    print('stmt 1')
    print('stmt 2' + 10)
    print('stmt 3')
    try:
        print('stmt 4')
        print('stmt 5')
        print('stmt 6')
    except ZeroDivisionError:
        print('stmt 7')
    finally:
        print('stmt 8')
    print('stmt 9')
except TypeError:
    print('stmt 10')
finally:
    print('stmt 11')
print('stmt 12')

'''
case 1: If there is no exception -- 1,2,3,4,5,6,8,9,11,12 will get executed with normal termination
case 2: If exception raised at stmt 2 and corresponding except block matched 
        then statements 1,10,11,12 with normal termination
case 3: If exception raised at stmt 2 and corresponding except block not matched
        then statements 1,11 with abnormal termination
case 4: If exception raised at stmt 5 and corresponding inner except block matched 
        then statements 1,2,3,4,7,8,9,11,12 with normal termination
case 5: If exception raised at stmt 5 and corresponding inner except block not matched but outer except
        block matched then statements 1,2,3,4,8,10,11,12 with normal termination
case 6: If exception raised at stmt 5 and both inner and outer except blocks not matched then
        statements 1,2,3,4,8,11 with abnormal termination
case 7: If exception raised at statement 7 and corresponding outer except block matched then
        statements 1,2,3,4,8,10,11,12 with normal termination
case 8: If exception raised at statement 7 and corresponding except block not matched then
        statements 1,2,3,4,8,11 with abnormal termination
case 9: If exception raised at statement 8 and corresponding except block matched then
        statements 1,2,3,4,5,6,10,11,12 with normal termination
case 10: If exception raised at statement 8 and corresponding except block not matched then
         statements 1,2,3,4,5,6 with abnormal termination
case 11: If exception raised at statement 9 and the corresponding except block matched then
         statements 1,2,3,4,5,6,8,10,11,12 with normal termination
case 12: If exception raised at statement 9 and the corresponding except block not matched then
         statements 1,2,3,4,5,6,8,11 with abnormal termination
case 13: If exception raised at statement 10 then the statements 1,11 will get executed with
         abnormal termination
'''

# else block with try-except-finally
# else block will get executed when there is no exception
# finally block will get executed when there is no exception occurred or didn't occur handled or not handled

try:
    print('try')
    print(10/1)
except ZeroDivisionError:  # If there is exception except block will get executed
    print('except')
else:
    print('else')  # If there is no exception then else block will get executed
finally:
    print('finally')

print('various combinations of try/except/else/finally blocks')

'''
various possible combinations of try-except-else-finally blocks :-

    1. try without except or finally block is always invalid
    2. without try only except block is always invalid
    3. only else block is always invalid
    4. only finally block is always invalid
    5. try-except is always valid
    6. try-finally is always valid
    7. try-except-else is always valid
    8. try-else is always invalid. We can not have else block without except
    9. try-else-finally is always invalid
   10. try with multiple except blocks is always valid
   11. try-except-else-else is always invalid. We can have only one else block
   12. try-except-finally-finally is always invalid. We can have only one finally block
   
    
'''

'''
There are two types of exceptions in Python:
    1. Predefined exceptions or inbuilt exceptions. -- The exceptions raised by python automatically
    2. User defined exceptions.
'''

# Defining user defined exceptions


class TooYoungException(Exception):  # We are defining TooYoungException class as child class of Exception
    def __int__(self,arg):  # This is a constructor
        self.msg = arg


class TooOldException(Exception):
    def __int__(self,arg):
        self.msg = arg


age = int(input('Enter your age:'))
if age > 60:
    raise TooOldException('You crossed your age to get married')
elif age < 18:
    raise TooYoungException('You are very young to get married')
else:
    print('Your age is correct..all the best')
