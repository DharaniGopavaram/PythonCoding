"""
The below program explains about Composition and Inheritance

How can we use members of one class inside another class:
1. By using composition(Has-A relationship)
2. By using inheritance(Is-A relationship)
"""

# Composition example 1 :-


class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color

    def get_car_info(self):
        print(f'Car name: {self.name}, Car model: {self.model}, Car color: {self.color}')


class Employee:
    def __init__(self,eno,ename,car):
        self.eno = eno
        self.ename = ename
        self.car = car  # here the instance variable points to Car class object

    def get_emp_info(self):
        print(f'Employee name: {self.ename}')
        print(f'Employee number: {self.eno}')
        print('Car information of employee')
        self.car.get_car_info()


c = Car('Benz', '2.5z', 'Grey')
e = Employee(101, 'Dharani', c)
e.get_emp_info()

# In the above example Employee has Car object created which will give us the functionality to use car features

# Inheritance example 1:-


class X:
    a = 10

    def m1(self):
        print('Parent class instance method')

    @classmethod
    def m2(cls):
        print('class method of Parent class ')

    @staticmethod
    def m3():
        print('static method of Parent class ')

    def __init__(self):
        self.b = 8888
        print('parent class constructor')


class Y(X):  # This is called inheritance
    pass


# Once we create a child class using inheritance all the methods, variables and constructors also
# will be available for child class
y = Y()  # If no constructor defined in child class this will call parent class constructor
# If constructor defined in child class then that constructor is called
print(y.a)  # Access the variable 'a' of parent class using child class object y
y.m1()  # Calling the m1 method of parent class using child class object
y.m2()  # Calling class method of parent class
y.m3()  # Calling static method of parent class
print('Instance variable of parent class:',y.b)


class Parent:
    a = 10

    def __init__(self):
        print('Parent class constructor')

    def m1(self):
        print('Parent class instance method')


class Child(Parent):
    a = 100

    def __init__(self):
        super().__init__()  # calling the parent class constructor
        print('Child class constructor')
        print(f'The value of the variable a in parent class is {super().a}')

    def m1(self):
        super().m1()  # calling the parent class m1 method
        print('child class instance method')


c = Child()
print(f'The value of the variable a is {c.a}')  # Here we will get 100
c.m1()  # If the child class doesn't contain m1 method then parent class m1 will be called
# If the child class contains the same variable as parent class always the child class variable is given the
# highest preference
# If the child class has a constructor then it is called otherwise parent class constructor wil get called
# same thing gets applied for destructor as well


class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat_and_drink(self):
        print('Biryani eating and beer drinking')


class SoftwareEngineer(Human):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno = eno
        self.esal = esal

    def work(self):
        print('Python coding is a cakewalk')


s = SoftwareEngineer('Dharani', 30, 100, 10000)
print(s.name, s.age, s.eno, s.esal)
s.eat_and_drink()  # using the child class we can call the parent class method
s.work()

# super() can not be used to get instance variable values to child class
# We need to use self to access parent class instance variables


class A:
    a = 8888
    def m1(self):
        self.a = 10

class B(A):
    def __init__(self):
        super().m1()
        print(super().a)  # This will access parent class static variable 'a'
        print(self.a)  # This will access parent class instance variable a


b = B()

'''
Types of Inheritance:-

    1. Single -- only one parent one child
    2. Multi-level -- A <- B <- C
    3. Multiple -- multiple parents single child
    4. Hierarchical -- Single parent multiple children
    5. Cyclic -- not allowed in Python 
    6. Hybrid -- combination of multiple, single, multi-level inheritance is called hybrid
'''

# Multi-level inheritance example

print('Multi level inheritance')
class GrandFather:
    def m1(self):
        print('Land')

class Father(GrandFather):
    def m2(self):
        print('Cash')

class Son(Father):
    def m3(self):
        print('Enjoy')


s = Son()
s.m1()
s.m2()
s.m3()

# Hierarchical inheritance example

print('Hierarchical inheritance')
class P:
    def m1(self):
        print('Parent')

class C1(P):
    def m2(self):
        print('Child1')

class C2(P):
    def m3(self):
        print('Child2')

c1 = C1()
c1.m1()
c1.m2()

c2 = C2()
c2.m1()
c2.m3()


# super() in depth
class P1:
    def __init__(self):
        print('Parent class constructor')
    def m1(self):
        print('instance method')

    @classmethod
    def m2(cls):
        print('class method')

    @staticmethod
    def m3():
        print('static method')


class Child1(P1):

    ''' # From child class constructor we can call all the methods present in parent class using super()
        def __init__(self):
            super().__init__()
            super().m1()
            super().m2()
            super().m3()
    '''

    ''' # From child class instance method we can call all the methods in parent class using super()
    def m1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
    '''

    '''
    # From child class 'class method' can not call the parent class constructor and instance method using super()
    @classmethod
    def m2(cls):
        #super().__init__()
        #super().m1()
        super().m2()
        super().m3()
    '''

    @staticmethod
    def m2():  # inside child class 'static method' we can't use super() at all
        #super().__init__()
        #super().m1()
        #super().m2()
        #super().m3()
        print('child class static method done')


c1 = Child1()
c1.m2()


# Multiple inheritance example
class Father1:
    def height(self):
        print('Height is 6 ft')

    def asset(self):
        print('Father\'s assets')


class Mother1:

    def color(self):
        print('brown color')

    def asset(self):
        print('Mother\'s assets')


class Baby1(Father1,Mother1):
    pass


b = Baby1()
print('The baby inherited the below properties from parents')
b.height()
b.color()
b.asset()  # Father's assets if we define class Baby1(Father1,Mother1)

# The order in which we inherit classes helps in removing the diamond problem in multiple inheritance


class Baby2(Mother1,Father1):
    pass


b2 = Baby2()
b2.asset()  # Mother's assets




