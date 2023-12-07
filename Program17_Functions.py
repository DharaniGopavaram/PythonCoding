"""
The below program explains about functions
Function is a group of statements which can be re-used
It is the best reusable component of a program
Even functions are objects are in Python
"""

from functools import reduce


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
    factorial_result = 1
    while n >= 2:
        factorial_result *= n
        n -= 1
    return factorial_result


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

'''
Modules :- A group of functions and variables saved to a file is called module
Package :- A group of modules saved inside a folder is called Package
Library :- A group of packages is called library

Types of variables :-

1. Global variables :- A variable defined outside function is called global variable
        Global variable is accessible to all the functions in the module
2. Local variables :- Variables defined inside function is called local variable
        We can not access local variable defined in one function outside of the function
'''

global_var = 10


def f1():
    global global_var  # If we specify like this from now on it will be a global variable
    # We are not required to have a global variable defined while using global keyword
    global_var = 777  # changing the value of the global variable
    print(f'The global variable value is: {global_var}')  # by, default it always takes local variable


def f2():
    global_var = 100  # this is local variable
    print(f'The local variable value global_var is: {global_var}')
    print(f"The global variable value global_var is: {globals()['global_var']}")
    # In the above line we are accessing global variable using globals() dictionary


f2()
f1()
f2()


# Recursive functions -- A function calling itself is called recursive function
# The length of the code and the readability of the code will be improved if we use recursion

def factorial(n):
    if n == 0:
        fact_result = 1
    else:
        fact_result = n * factorial(n - 1)
    return fact_result


print(f'Factorial of 3 is: {factorial(3)}')
print(f'Factorial of 5 is: {factorial(5)}')

'''
Anonymous functions:-
---------------------

Some times we can define functions without name such type of nameless functions are called Anonymous functions
Syntax :- lambda input-argument-list:expression
lambda functions are useful when we want to pass function as argument to a function
Some example of functions which accept functions are arguments are filter(), map(), reduce() etc.,

filter() syntax -- filter(lambda function, sequence)
'''

s = lambda n:n*n
print(f'Calling the anonymous function to get square: {s(4)}')
print(f'Calling the anonymous function to get square: {s(40)}')

s = lambda num1, num2: num1 + num2
print(f'Calling the anonymous function to get sum: {s(10, 20)}')
print(f'Calling the anonymous function to get sum: {s(100, 200)}')

s = lambda a, b: a if a > b else b
print(f'Calling the anonymous function to know the bigger value: {s(10, 20)}')
print(f'Calling the anonymous function to know the bigger value: {s(9, -3)}')


def iseven(n):
    if n % 2 == 0:
        return True
    else:
        return False


# filter function using normal function
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Filtering out the even values in sequence: {list(filter(iseven,sample_list))}')

# filter function using anonymous function
final_output_list1 = list(filter(lambda num:num % 2 == 0,sample_list))
print(f'Filtering out the even values in sequence: {final_output_list1}')

final_output_list2 = list(map(lambda n1: n1 * 2,sample_list))
print(f'Doubling the values in sequence using map function: {final_output_list2}')

sample_words_list = ['dharani', 'durga', 'kavya', 'bharath']
final_output_list3 = list(map(lambda n1: (n1,len(n1)),sample_words_list))
print(f'Returning a tuple from the map function: {final_output_list3}')

# we can apply map function on multiple sequences
# map function will automatically terminate when all the values in any sequence are completed
another_set = {10, 20, 30, 40, 50}
final_output_list4 = list(map(lambda a1,a2: a1 * a2,sample_list,another_set))
print(f'map function on multiple sequences: {final_output_list4} ')


# reduce function
result = reduce(lambda num1,num2:num1 + num2, sample_list)
print(f'The result of the reduce function using lambda is: {result}')


def add_num(num_1, num_2):
    return num_1 + num_2


final_result = reduce(add_num,sample_list)  # calling reduce function using normal function
print(f'The result of the reduce function using normal function is: {final_result}')

# Function aliasing


def original_func(name):
    print("Good Morning", name)


duplicate_func = original_func

print(f'The address of the variable duplicate_func is {id(duplicate_func)}')
print(f'The address of the variable original_func is {id(original_func)}')
print(f'Calling the duplicate_func:')
duplicate_func('Dharani')

# If the object has any variable pointing to it and even if we delete the variable the object will still be there
del original_func  # deleting the original function
duplicate_func('Dharani')

# Nested functions
# Function inside function is known as nested function


def outer():
    print('outer function execution started')

    def inner(num1, num2):
        print('inner function execution started')
        print(f'The sum is: {num1 + num2}')
        print(f'The average is: {(num1 + num2)/2}')

    inner(10,20)
    inner(100,200)
    inner(30,40)

    print('outer function execution completed')


outer()  # calling the outer function


# A function can return another function as well

def outer_func():
    print("outer function execution started")

    def inner_func():
        print("inner function executed")

    print("outer function returning inner function")
    return inner_func


return_func = outer_func()  # calling the outer_func function
return_func()  # this will call the inner_func function

# Function Decorators -- used to extend the functionality of existing function
# without changing the function logic if u want to play with function parameters then we can use decorators.
# Decorators provide a clean and reusable way to extend the functionality of
#   functions without modifying their code directly.
# Let's say for the below greeting_function if Sunny as received as parameter we should print different output


# Implicitly calling decorator of greeting_function

def greeting_decor_func(input_function):

    def inner_decor_func(input_function_param):
        if input_function_param == 'Sunny':
            print('Hello Sunny bad morning')
        else:
            input_function(input_function_param)

    return inner_decor_func


@greeting_decor_func
def greeting_function(name):
    print(f'Hello {name} Good morning')


greeting_function("Dharani")
greeting_function("Bunny")
greeting_function("Sunny")

# Explicitly calling the decorator function


def sum_of_two_numbers_decor(input_function):
    def inner_decor_func(x1, x2):
        if x1 > 100:
            return -100
        else:
            input_function(x1, x2)

    return inner_decor_func


def sum_of_two_numbers(a, b):
    return a + b


decor_func = sum_of_two_numbers_decor(sum_of_two_numbers)
print(f'Normal function without decorator: {sum_of_two_numbers(200, 300)}')
print(f'With decorator: {decor_func(200, 300)}')


# one more example of using decorators


def smart_division(input_func):

    def inner(a, b):
        if b == 0:
            print('Hello Stupid how can u divide with zero')
            return
        else:
            return input_func(a, b)
    return inner


@smart_division
def division(a, b):
    return a / b


print(f'Division result: {division(10, 20)}')
division(10, 0)

# We can have multiple decorators for a single function this is called decorator chaining


def sample_function_decor_1(input_func):
    def inner_decor_1(name):
        print(f'sample_function_decor_1 function started')
        input_func(name)
        print(f'sample_function_decor_1 function completed')
    return inner_decor_1


def sample_function_decor_2(input_func):
    def inner_decor_2(name):
        print(f'sample_function_decor_2 function started')
        input_func(name)
        print(f'sample_function_decor_2 function completed')
    return inner_decor_2


@sample_function_decor_2  # This will get executed at last
@sample_function_decor_1  # This decorator will get executed first and the result is passed to output decorator
def sample_function(name):
    print(f'Hello {name} Good morning')


sample_function('Dharani')
# The execution of multiple decorators is like this: sample_function_decor_2(sample_function_decor_1(sample_function))
