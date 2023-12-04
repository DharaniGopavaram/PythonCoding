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


def squareit(num):  # Here x is called formal parameter of a function
    print(f'The square of x is {num * num}')


squareit(10)  # Here 10 is called actual argument to a function
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


# In Python a function can return multiple values


def sum_sub(a, b):  # defining a function which returns multiple values
    return a + b, a - b


x, y = sum_sub(100,50)
print(f'The sum of the numbers is: {x}')
print(f'The difference of the numbers is: {y}')


def calculator(n1, n2):  # defining a function which returns more than 2 values
    num_sum = n1 + n2
    num_sub = n1 - n2
    num_mul = n1 * n2
    num_div = n1 / n2
    return num_sum, num_sub, num_mul, num_div


t = calculator(100, 50)  # The return values of the function are stored in tuple
print(f'The return type of the variable t is: {type(t)}')

for x in t:
    print(x)

'''
Types of arguments to a function :-
-----------------------------------

1. Positional arguments -- default arguments where order is important
2. Keyword arguments -- here order is not important
3. Default arguments
4. Variable length arguments
5. Keyword variable length arguments

'''


def wish(name, msg='Hi'):  # defining a function which have default argument
    print(f'{msg}, {name}')


wish('Dharani', 'Hello')  # Positional arguments
wish(msg='Hi', name='Dharani')  # keyword arguments order is not important
wish('Dharani', msg='Bye')  # we can add both positional and keyword arguments at the same time
# If we are taking both positional and keyword arguments then positional arguments should come first
# wish(name = 'Dharani', 'Bye')  # SyntaxError: positional argument follows keyword argument
# wish('Dharani', name = 'Dharani')  # TypeError: wish() got multiple values for argument 'name'


def sum_num(n1, n2=0, n3=0):  # we need to define default arguments at the end of the function only
    return n1 + n2 + n3


print(f'{sum_num(10,20,30)}')
print(f'{sum_num(n1=10, n3=20)}')
print(f'{sum_num(100,n3=30)}')

# Variable length arguments


def sum_multiple_num(*a):  # defining a function with variable length arguments
    print(type(a))  # var-args variable is a tuple
    return sum(a)


print(sum_multiple_num())
print(sum_multiple_num(10, 20))
print(sum_multiple_num(10, 20, 30, 40))


def student_sum(*nums, name):
    print(f'The sum of {name} is {sum(nums)}')


student_sum(10,20,30,name='Dharani')
student_sum(10,20,30,40,50,name='John')

# keyword variable length arguments


def display(**kwargs):
    print(type(kwargs))  # the kwargs is dict type
    for k,v in kwargs.items():
        print(f'{k} -> {v}')


display(name='Dharani', marks=20, age=30, height=6.1)  # we can call the function with any keyword arguments we want
display(name='Ravi', wife1='wife1', wife2='wife2')
