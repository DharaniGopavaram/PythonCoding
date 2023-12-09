"""
This file is used as a module
"""

print(f'This is an user defined module')

x = 777
y = 999


def add_num(a, b):
    print(f'The sum of {a} and {b} is {a + b}')
    print(f'Completed sum')


def product_num(a, b):
    print(f'The product of {a} and {b} is {a * b}')


def f1():
    if __name__ == '__main__':
        print('The code executed directly as a program')
        print(f'The value of the variable __name__ is: {__name__}')
    else:
        print('The code executed indirectly as a module from some other program')
        print(f'The value of the variable __name__ is: {__name__}')


f1()
