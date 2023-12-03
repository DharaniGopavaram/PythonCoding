"""
The below program explains different forms of print statement in Python
"""

print("Hello\nDharani")  # we can use escape characters happily in the print function
print()  # just prints a new line character
print("Good\tMorning")
print('dharani' * 3)  # we can use repetition operator like this in print function

print('dharani' + 'kumar')  # the output doesn't have any space
print('dharani', 'kumar')  # here the output will have space

# by default if we pass multiple string arguments to print function they are separated by space

a, b, c = 10, 20, 30
print('The values of the variables are:', a, b, c)  # we can pass any number of arguments to print function
print(a, b, c, sep=',')  # sep can be used to pass our own delimiter to the print function

print("Hello", end=' ')  # by default print will add \n at the end of the string
print("Team", end=' ')  # if we use end we can change this behavior
print("Python is very easy")

print(10, 20, 30, 40, sep=':', end='...')
print(50, 60, 70, 80, sep='-')

# print with formatted string

print("The value of a is %i" % a)
print("The value of b is %d" % b)
print("The value of a, b, c is %d %d %d" % (a, b, c))

name = 'dharani'
list1 = [10, 20, 30, 40]
print("Hello %s the list values are %s" % (name, list1))

# print with replacement operator

salary = 10000
gf = 'Sunny'
print("Hello {0} your salary is {1} and your girlfriend {2} is waiting".format(name, salary, gf))
print("Hello {} your salary is {} and your girlfriend {} is waiting".format(name, salary, gf))
print("Hello {x} your salary is {y} and your girlfriend {z} is waiting".format(z=gf, x=name, y=salary))
