"""
The below program explains about polymorphism concept in OOP.

If we consider the + operator sometimes it works as addition, and sometimes it works as string concatenation operator.
We can say + operator is overloaded
So the same operator is used for multiple purposes which is called polymorphism.
This specific polymorphism is called operator overloading

1. Duck Typing philosophy of Python
2. Overloading
    Operator overloading
    Method overloading -- When two methods are having different type of parameters but same name then we can say
        such type of methods are overloaded methods
        In Python since we can not separate two methods based on type method overloading is not possible
    Constructor overloading is also not possible
        If we declare multiple constructors with the same name and different number of arguments only the
            last constructor will be there others will be overridden
3. Overriding
    Method overriding
    Constructor overriding
"""

# Duck typing example


class Duck:
    def talk(self):
        print('Quack Quack')


class Dog:
    def bark(self):
        print('Bow Bow')


class Cat:
    def talk(self):
        print('Meow Meow')


l1 = [Duck(),Dog(),Cat()]
for obj in l1:
    if hasattr(obj,'talk'):  # hasattr method can be used to check the attributes of an object
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()
    else:
        print('No talk method and bark method is available for the specified object')

# Operator overloading
# For every operator there are some magic methods available. If we overwrite that magic method in our class
# then we can happily use operator overloading

'''
Magic methods of some operators:-

    1. + --> __add__(self,other)
    2. - --> __sub__()
    3. * --> __mul__()
    4. / --> __div__()
    5. // --> __floordiv__()
    6. % --> __mod__()
    6. ** --> __pow__()
    7. += --> __iadd__()
    8. -= --> __isub__()
    9. *= --> __imul__()
    10. < --> __lt__()
    11. <= --> __le__()
    12. > --> __gt__()
    13. >= --> __ge__()
    14. == --> __eq__()
    15. != --> __ne__()
    
'''


class Book:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self, other):  # magic method of + operator
        return self.pages + other.pages

    def __mul__(self, other):
        if hasattr(other,'pages'):
            return self.pages * other.pages
        return self.pages * other

    def __lt__(self, other):
        return self.pages < other.pages


b1 = Book(100)
b2 = Book(200)
print(f'The total number of pages is:{b1 + b2}')
print(f'The multiplication of number of pages is:{b1 * b2}')
print(f'The multiplication of number of pages is:{b1 * 10}')
print(f'b1 < b2:{b1 < b2}')
print(f'b2 < b1:{b2 < b1}')

# Operator overloading one more example


class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __mul__(self, other):
        if self.name == other.name:
            return self.salary * other.days
        else:
            print('The employee does\'t exist hence returning 0')
            return 0


class Timesheet:
    def __init__(self,name,days):
        self.name = name
        self.days = days


e = Employee('Dharani', 500)
t = Timesheet('Dharani1',25)
print(f'The total salary of the employee is: {e * t}')

# Method overloading


class Test:
    def m1(self):
        print('No arg method')

    def m1(self,a):  # The first m1 method will be overwritten
        print('One arg method')

    def m1(self,a,b):  # The second m1 method will be overwritten
        print('Two arg method')

    def sum(self,*num):
        total = 0
        for x in num:
            total += x
        return total


# In Test class we only have one m1 method which has overwritten the previously declared m1 methods
t = Test()
t.m1(10,20)
print(t.sum(10,20))
print(t.sum(10,20,30))
print(t.sum(10,20,30,40))

# If we want to use method overloading then we can declare the method using variable argument list

# constructor overloading

class Constructor:
    def __init__(self):
        print('no arg constructor')

    def __init__(self,a):
        print('one arg constructor')
    def __init__(self,a,b):  # This constructor will override the other two constructors
        print('Two arg constructor')


c = Constructor(1,2)

# Method overriding

class P:
    def property(self):
        print('cash+land+gold+power')
    def marry(self):
        print('Appalamma')

class C(P):
    def marry(self):  # Here we are overriding the parent class marry method
        print('Katrina Kaif')

c = C()
c.property()
c.marry()

# Same like method overriding we can perform constructor overriding

