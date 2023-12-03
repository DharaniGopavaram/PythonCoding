"""
The below program explains about operators in Python

Different types of operator in Python :-
    1. Arithmetic operator (+, -, /, *, %, //(floor division operator), **(exponential operator))
    2. Relational operator or Comparison operator (> ,<, >=, <=, ==, !=)
    3. Logical operators (and, or , not)
    4. Bitwise operators (&, |, ^, ~, <<, >>)
    5. Assignment operators (=, +=, -=, *= ...)
    6. Special operator (is, is not, in, not in)
"""

print(f'Normal division operator: 10 / 3 = {10 / 3}')  # will always return float result only
print(f'Floor division operator: 20 // 3 = {20 // 3}')  # will return int if both numbers are int
print(f'Floor division operator: 20 // 3.0 = {20 // 3.0}')  # will return float if any number is float literal
print(f'Exponential operator: 2 ** 4 = {2 ** 4}')  # 2 ^ 4 which will return 16

# + operator can be applied on strings as well when applied on strings it is called concatenation operator
# both the arguments to + should be strings only if any of the argument is not string we will get TypeError

print(f"String concatenation: 'dharani ' + 'gopavaram' = {'dharani ' + 'gopavaram'}")
# print('dharani' + 3)  # TypeError: can only concatenate str (not "int") to str

print(f"String repetition operator: 'dharani' * 3 = {'dharani' * 3}")

# we can apply relational operators on strings as well
# When we apply relational operators on string they work based on alphabetical order

a = 'dharani'
b = 'kavya'
print(f'{a} > {b} = {a > b}')
print(f'{a} >= {b} = {a >= b}')
print(f'{a} < {b} = {a < b}')
print(f'{a} <= {b} = {a <= b}')

# print(10 > 'dharani')  # TypeError: '>' not supported between instances of 'int' and 'str'

# Logical operators on non-boolean types
# 0 means False, non-zero means True, empty string is False

# x and y -- if x evaluates to False then result is x otherwise returns y

print(f'10 and 20 = {10 and 20}')
print(f'0 and 100 = {0 and 100}')

# x or y -- if x evaluates to True then result is x otherwise returns y

print(f'10 or 20 = {10 or 20}')
print(f'0 or 20 = {0 or 20}')
print(f'10 or 10/0 = {10 or 10/0}')
# Logical operators are short-circuited meaning if the 1st expression determines the result the 2nd one is not evaluated

print(f'not 10 = {not 10}')
print(f"not '' = {not ''}")

'''
Bitwise operators :-
--------------------
& -- If both the bits are 1 then 1 otherwise 0
| -- If one bit is 1 then 1 otherwise 0 
^ -- If both bits are different then 1 otherwise 0
<< -- bitwise left shift operator
>> -- bitwise right shift operator
'''

print(f'4 & 5 = {4 & 5}')
print(f'4 | 5 = {4 | 5}')
print(f'4 ^ 5 = {4 ^ 5}')
print(f'10 << 2 = {10 << 2}')
print(f'10 >> 2 = {10 >> 2}')

# There are no increment(x++, ++x) and decrement(x--, --x) operator in Python

# Ternary operator syntax in Python
# x = firstValue if condition else secondValue

x = 10 if 20 < 30 else 40
print(f'The value of x using ternary operator is: {x}')

y = 30 if 10 > 20 else 40
print(f'The value of y using ternary operator is: {y}')

# is operator is used to perform address comparison of two variables

a = (10, 20, 30)
b = (10, 20, 30)
print(f'The address of a is: {id(a)}')
print(f'The address of b is: {id(b)}')
print(f'Hence a is b: {a is b}')
print(f'Hence a is not b: {a is not b}')  # 'is not' operator is also available

# in operator is used to check whether an element is present in the collection or not

list1 = [10, 20, 30, 40]
print(f'10 in list1: {10 in list1}')
print(f'100 in list1: {100 in list1}')
print(f'100 not in list1: {100 not in list1}')
print(f"'s' in 'python': {'s' in 'python'}")
