"""
The below program explains about functions
Function is a group of statements which can be re-used
It is the best reusable component of a program
"""


def wish():  # we need to use def keyword to define a function
    print('Good evening')


wish()  # calling the wish function
wish()  # Once we define a function we can call the function any number of times


def wish(name):  # we can define a function which accepts parameters
    print(f'Hello {name}, Good evening')


wish('Dharani')  # calling a function by passing one argument
wish('Ravi')


def squareit(x):
    print(f'The square of x is {x * x}')


squareit(10)
print(squareit(100))  # The default value of a function is None


def add_numbers(a, b):  # defining a function with return keyword
    return a + b


print(f'add_numbers(100, 200) = {add_numbers(100, 200)}')
print(f'add_numbers(100, 300) = {add_numbers(100, 300)}')

# Write a function to find factorial of a given number


def num_factorial(n):
    result = 1
    while n >= 2:
        result *= n
        n -= 1
    return result


for i in range(1,11):
    print(f'Factorial of {i} is {num_factorial(i)}')


# In Python a function can 