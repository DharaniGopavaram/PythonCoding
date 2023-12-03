"""
The below program explains about range data type
range data type represents a sequence of values which are always immutable
"""

r = range(10)  # it represents values from 0 to 9
print(f'The type of the variable r is {type(r)} and it\'s value is {r}')
print(f'Accessing the range elements using index: {r[4]}')
sliced_range = r[0:5]  # will take values from 0 to 4
print(f'sliced_range = {sliced_range}')

# r[0] = 10  # TypeError: 'range' object does not support item assignment

for i in r:
    print(i, end=' ')  # If we specify end like this it won't go to next line

print()

# If we want to print values from a specific start and end then we should pass two arguments to range function
print(f'second form of range function')

r1 = range(100, 130)
for i in r1:
    print(i, end=' ')

print()

print(f'third form of range function')

r2 = range(10, 100, 5)  # print every 5th value from the range we specify
for i in r2:
    print(i, end=' ')

print()

r3 = range(10, 1, -1)  # If we pass negative values to step it will print the value in reverse order
for i in r3:
    print(i, end=' ')

print()

# r4 = range(10.1, 20.2)  # TypeError: 'float' object cannot be interpreted as an integer
