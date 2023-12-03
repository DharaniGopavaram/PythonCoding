"""

This program explains about data types in Python.

Data types represent the type of value present inside a variable
int, float, complex, bool, str, bytes, bytearray, range, list, tuple, set, frozenset, dict, None

In Python everything is an object

"""

# int datatype is used to represent integral values

a = 10
print(f'The type of variable a is: {type(a)}')
print(f'The variable a is stored in {id(a)} memory location')

# int datatype can hold huge values as well
b = 1234567891294649163946513465130463151046206401364019304
print(f'The type of variable b is {type(b)}')

'''

int datatype can be represented in four ways

1. Decimal form(base10 -- allowed digits are 0 to 9)
2. Binary form(base2 -- allowed digits are 0 and 1)  
3. Octal form(base8 -- allowed digits are 0 to 7)
4. Hexa decimal form(base16 -- allowed characters are 0-9,a,b,c,d,e,f(both upper case and lower case)

'''

# Binary number representation starts with either 0b or 0B
binary_num1 = 0b1111
binary_num2 = 0B1010
print(f'binary_num1: {binary_num1}')
print(f'binary_num2: {binary_num2}')

# Octal number representation starts with either 0o or 0O
octal_num1 = 0o777
octal_num2 = 0O123
print(f'octal_num1: {octal_num1}')
print(f'octal_num2: {octal_num2}')

# Hexadecimal representation starts with either 0x or 0X
hexadecimal_num1 = 0xFACE
hexadecimal_num2 = 0X123ABC
print(f'hexadecimal_num1: {hexadecimal_num1}')
print(f'hexadecimal_num2: {hexadecimal_num2}')

# Base conversion functions
# bin() -- convert any base to binary
# oct() -- convert any base to octal
# hex() -- convert any base to hexadecimal

print(f'converting decimal to binary: {bin(15)}')
print(f'converting octal to binary: {bin(0o10)}')
print(f'converting hexadecimal to binary: {bin(0x10)}')

print(f'converting decimal to octal: {oct(15)}')
print(f'converting binary to octal: {oct(0b1111)}')
print(f'converting hexadecimal to octal: {oct(0x10)}')

print(f'converting decimal to hexadecimal: {hex(15)}')
print(f'converting binary to hexadecimal: {hex(0b1111)}')
print(f'converting octal to hexadecimal: {hex(0o1234)}')

# float data type is used to represent floating point values

f1 = 123.456
print(f'The type of the variable f1 is: {type(f1)}')

f2 = 3.5e4  # different way to represent floating point numbers
print(f'The value of the variable f2 is {f2} and it\'s type is {type(f2)}')

# complex number are represented in the format of a + bj where 'a' is called real part and 'b' is called Imaginary part
# The value of j is sqrt(-1) which means j^2 = -1

complex_num1 = 10 + 20j
print(f'The value of the variable complex_num1 is {complex_num1} and it\'s type is {type(complex_num1)}')

# Extracting real and imaginary part of a complex number
# Internally both real and imag functions will return the output in floating point number only
print(f'The value of real part of complex number {complex_num1} is {complex_num1.real}')
print(f'The value of imaginary part of complex number {complex_num1} is {complex_num1.imag}')

# The real part and imaginary part can be either int or floating point literals
complex_num2 = 10.5 + 30.6j
print(f'The value of the variable complex_num2 is {complex_num2} and it\'s type is {type(complex_num2)}')

# We can specify the real part in either decimal, binary, octal or hexadecimal form
# The imaginary part should be specified only in decimal form

complex_num3 = 0b1111 + 35.6j
print(f'The value of the variable complex_num3 is {complex_num3} and it\'s type is {type(complex_num3)}')

# Operations on complex numbers -- used very rare just have an idea that's all
print(f'Addition of complex numbers: {complex_num1 + complex_num2}')
print(f'Subtraction of complex numbers: {complex_num2 - complex_num1}')
print(f'Multiplication of complex numbers: {complex_num2 * complex_num1}')

# The only allowed values for bool data type are True and False

bool_num1 = True
print(f'The value of the variable bool_num1 is {bool_num1} and it\'s type if {type(bool_num1)}')

# Internally True and False are represented as 1 and 0 respectively hence we can perform some arithmetic operations
print(f'True + True = {True + True}')
print(f'True + False = {True + False}')
print(f'False + False = {False + False}')
print(f'True * False = {True * False}')
# print(f'True / False = {True / False}')  # ZeroDivisionError: division by zero

# str data type is used to represent any sequence of characters
# We can represent single-line string literals using single quotes or double quotes
# We can represent multi-line string literals using triple single quotes or triple double quotes

s1 = 'dharani'
print(f'The value of the variable s1 is: {s1} and it\'s type is {type(s1)}')
print(f'The repetition operator on string s1: {s1} -- s1 * 4 = {s1 * 4}')
print(f'Length of the string s1 using len method is: {len(s1)}')  # len method will give us the length of the string

s2 = '''dharani
kumar gopavaram'''
print(f'The value of the variable s2 is: {s2}')

# int, float, bool, complex and str are known as fundamental data types

'''
Type Casting :- converting from one data type to another is called type casting
int(), float(), complex(), bool(), str()
'''

# int() function can be used to convert any other data type value to int data type
print(f'int(123.456) = {int(123.456)}')  # float to int conversion

# print(int(10+20j))  # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
# The above statement will give an error because we can not convert complex data type to int

print(f'int(True) = {int(True)}')  # bool to int conversion
print(f'int(False) = {int(False)}')

print(f"int('10') = {int('10')}")  # string to int conversion
# print(f"int('10.5') = {int('10.5')}")  # ValueError: invalid literal for int() with base 10: '10.5'®
# If we want to convert string to int the string value should be of base 10(decimal form) only
# print(f"int('dharani') = {int('dharani')}")  # ValueError: invalid literal for int() with base 10: 'dharani'

# Different way of converting binary, octal and hexadecimal to string
print(f"int('0b1111', 2) = {int('0b1111', 2)}")
print(f"int('0o20', 8) = {int('0o20', 8)}")
print(f"int('0x30', 16) = {int('0x30', 16)}")

# float() function can be used to convert other data type to float

print(f'float(10) = {float(10)}')  # int to float conversion
# print(f"float(10+20j) = {float(10+20j)}")
# TypeError: float() argument must be a string or a real number, not 'complex'

print(f'float(True) = {float(True)}')  # bool to float conversion
print(f'float(False) = {float(False)}')
print(f"float('10') = {float('10')}")
print(f"float('10.5') = {float('10.5')}")
# print(f"float('dharani') = {float('dharani')}")  # ValueError: could not convert string to float: 'dharani'

# complex() function can be used to convert other data type to complex
# It is an overloaded function which has two forms to it
# complex(x) -- x + 0j
# complex(x,y) -- x + yj

print(f'complex(10) = {complex(10)}')
print(f'complex(10.5) = {complex(10.5)}')
print(f'complex(True) = {complex(True)}')
print(f'complex(False) = {complex(False)}')
print(f"complex('10') = {complex('10')}")
print(f"complex('10.5') = {complex('10.5')}")
# print(f"complex('ten') = {complex('ten')}")  # ValueError: complex() arg is a malformed string

print(f'complex(10, 20) = {complex(10, 20)}')
print(f'complex(True, False) = {complex(True, False)}')
print(f'complex(10.5, 20.6) = {complex(10.5, 20.6)}')
# print(f"complex('10', 20') = {complex('10', '20')}")
# TypeError: complex() can't take second arg if first is a string

# bool function can be used to convert other data type to bool
print(f'bool(0) = {bool(0)}')  # for int if the value is zero bool returns False otherwise True
print(f'bool(10) = {bool(10)}')
print(f'bool(-10) = {bool(-10)}')

print(f'bool(0.01) = {bool(0.01)}')  # If the final value of float is 0 then bool returns False else True
print(f'bool(0.0) = {bool(0.0)}')

print(f'bool(10+0j) = {bool(10 + 0j)}')
print(f'bool(0+0j) = {bool(0 + 0j)}')  # If both real and imaginary part are 0 bool returns False else True

print(f"bool('dharani') = {bool('dharani')}")
print(f"bool('') = {bool('')}")  # If the string is empty bool returns False else True

# str() function is used to convert any data type to string
print(f'str(10) = {str(10)}')
print(f'str(10.5) = {str(10.5)}')
print(f'str(10+20j) = {str(10 + 20j)}')
print(f'str(True) = {str(True)}')
print(f'str(False) = {str(False)}')

# Escape characters in string

s = "dharani\ngopavaram"  # new line character
print(f'The value of variable s is {s}')

s = "dharani\tgopavaram"  # tab separated output
print(f'The value of variable s is {s}')

s = "Learning \"Python\" is good"  # escaping double quotes
print(f'The value of variable s is {s}')

# int, float, bool, str, complex are immutable data types
# Once we create an object we can not perform any change on this object
# If we try to perform change then by default a new object will be created with the required changes
# Immutability mainly provides object re-usability

# bytes data type is used to represent a group of byte numbers just like an array
# bytes data type is immutable we can not modify once we create

x = [10, 20, 30, 40]
b = bytes(x)
print(f'The type of the variable b is: {type(b)}')
print(f'Accessing 1st element from bytes data type: {b[0]}')
print(f'Accessing last element from bytes data type using negative index: {b[-1]} ')
print(f'Using slice operator on bytes data type: {b[0:3]}')

print(f'Printing values in bytes data type using for loop')
for x in b:
    print(x)

# b[0] = 30 # TypeError: 'bytes' object does not support item assignment

y = [100, 200, 256]  # The value 256 is also not allowed
# b1 = bytes(y)  # ValueError: bytes must be in range(0, 256)

# bytearray is same like bytes the only difference is bytearray is mutable
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = bytearray(x)
print(f'The type of the variable b is: {type(b)}')

print(f'Printing values of bytearray using for loop')
for x in b:
    print(x)

print(f'Modifying the first element of bytearray')
b[0] = 100  # this is possible because bytearray is mutable
print(f'Elements in bytearray after modifying')

for x in b:
    print(x)


# None data type is used to represent the absence of a value or a null value
# It is often used to signify that variable or a function does not have a meaningful value or result

def f1():
    pass  # we are not willing to define function body at this time


# pass keyword is mainly used to define the function which does not do anything
print(f'The return value from f1 function is: {f1()}')

# There are no constants in Python
