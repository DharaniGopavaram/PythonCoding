"""
The below program explains different ways of reading input from user

Python2 :-

    1. raw_input() -- input is treated as string we require to do type casting
    2. input() -- input is treated as whatever type we provide no type casting is needed

Python3 :-

    1. input() -- input is always treated as string

"""

from math import pi

a = int(input('Enter first number: '))  # we need to do explicit type casting
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))
maximum_value = a if a > b and a > c else b if b > c else c  # Nesting of Ternary operator is possible
print(f'The maximum value is: {maximum_value}')

r = int(input('Enter the radius of the circle: '))
print(f'Area of the circle is: {pi * (r ** 2)}')

# Reading multiple values from the user in a single line

x, y = (int(x) for x in input('Enter two numbers separated by space to perform product :').split())
print(f'The product of the entered numbers is: {x * y}')

# split method by default consider the delimiter as space
# If we want different delimiter we can pass it explicitly

x, y = (float(x) for x in input('Enter two float numbers separated by comma: ').split(','))
print(f'The sum of the two float numbers entered is: {x + y}')

# eval function is used to evaluate an expression dynamically

result = eval("10 + 20 + 30")
print(f'The result after evaluating the expression is: {result}')

data = eval(input('Enter some data : '))  # will dynamically evaluate the type of data we enter
print(f'The type of the variable data is: {type(data)}')

