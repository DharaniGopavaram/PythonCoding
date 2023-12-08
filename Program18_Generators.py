"""
The below program explains about generators.
Generators in Python are a powerful tool for creating iterators.
They allow you to iterate over a potentially large sequence of data
    without creating the entire sequence in memory at once.
This can be more memory-efficient and faster compared to traditional approaches,
    especially when dealing with large datasets.
"""

# The below code will cause memory errors
# sample_list = [x * x for x in range(10000000000000000000000)]  # The entire data set will get saved in memory

sample_generator = (x * x for x in range(10000000000000000000000))  # does not cause memory issues
# The values are generated on the fly without using much memory
print(f'The type of the variable sample_generator is {type(sample_generator)}')

# yield keyword is used to return a generator


def sample_function():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'


gen = sample_function()
print(f'The type of the variable gen is {type(gen)}')

print(f'The next value in the generator variable is: {next(gen)}')  # next method can be used to retrieve next value

for x in gen:  # we can use for loop to retrieve the values one at a time
    print(f'The next value in the generator is: {x}')


def count_down(num):
    while num > 0:
        yield num
        num -= 1


values = count_down(10)
print(f'The type of the variable values is: {type(values)}')
print("All the values returned by the function are:")
for x in values:
    print(x)
print("Printing the values one more time")
for x in values:  # A generator is lost once it is consumed
    print(x)  # nothing is printed here


# Program to print first 100 fibonacci numbers using generator
def fibonacci_func(num):
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print(f'Printing the fibonacci series')
for x in fibonacci_func(100):
    if x > 10000000000000000000000000000000000000000:
        break
    print(x)


