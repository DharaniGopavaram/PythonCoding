"""
The below program explains about different types of methods in a class
    1. instance methods -- object related methods
        Inside method body if we are accessing instance variables then that method talks about a particular object
        such type of methods are called instance methods.
        Instance methods should be called by using object reference.
        Getter and Setter methods are also instance methods which are helpful in setting and getting value of
            instance variables
        Normally we should not access variables outside class instead we should use getter and setter methods
            to set and get the instance variables.
        Getter methods also known as accessor methods.
        Setter methods also known as mutator methods.
    2. class methods  -- these methods are very rarely used
        Inside method body if we are using only static variables then that method is called class method
    3. static methods
        If we are not using any instance or static variables then that methods are called static methods.
        These methods just take a set of parameters and perform soe business logic on it.
        These methods are also known as general utility methods
"""


class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):  # This is an instance method
        print('Hi',self.name)
        print('Your marks are',self.marks)

    def grade(self):
        if self.marks >= 65:
            print('You got first grade')
        elif self.marks >= 50:
            print('You got second grade')
        elif self.marks >= 35:
            print('You got third grade')
        else:
            print('You are failed')


s1 = Student('Dharani',36)
s2 = Student('Bharath',90)
s1.display()
s2.display()
s1.grade()
s2.grade()


# Instead of using constructor we can use getter and setter methods to access and create instance methods.
# The below program shows the usual way of using getter and setter methods in out python program.
class Police:
    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def set_cader(self,cader):
        self.cader = cader

    def get_cader(self):
        return self.cader


p1 = Police()
p1.set_name('Dharani')
print(p1.get_name())
p1.set_cader('CI')
print(p1.get_cader())
print(p1.__dict__)


class Animal:
    legs = 4

    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs'.format(name,cls.legs))


Animal.walk('Dog')
Animal.walk('Cat')

# Program to know the number of objects created for a class


class Village:
    count = 0

    def __init__(self):
        Village.count += 1

    @classmethod
    def no_of_objects(cls):
        print(f'The total number of objects created for the class Village is: {cls.count}')
        print(f'The total number of objects created for the class Village is: {Village.count}')


v1 = Village()
v2 = Village()
Village.no_of_objects()


class DurgaMath:
    @staticmethod
    def add_num(x,y):  # This is a static method
        print(f'The sum is {x+y}')

    @staticmethod
    def product_num(x,y):  # we are not using any static or instance variable inside the body of this method
        print(f'The product is {x * y}')


DurgaMath.add_num(10,20)
DurgaMath.product_num(30,40)

# Passing members of one class to another class


class Employee:

    def __init__(self,eno,ename,esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal

    def display(self):
        print(f'Employee number: {self.eno}')
        print(f'Employee name: {self.ename}')
        print(f'Employee salary: {self.esal}')


class Manager:
    @staticmethod
    def modify_employee(emp):  # this method is taking parameter as an employee object and calling its methods
        emp.esal += 1000  # Incrementing the salary of the employee by 1000
        emp.display()  # calling the display method of the Employee class


e = Employee(100,'Dharani',10000)
Manager.modify_employee(e)  # passing the employee object to modify_employee method

# Inner classes :- An object can not be created without the existence of another object in these cases we should
#    go for inner classes.
# Inner classes help in managing namespaces by keeping related classes together,
# avoiding potential naming conflicts with classes in other parts of the program


class Outer:
    def m1(self):
        print('Outer class method')

    class Inner:
        def m2(self):
            print('Inner class method')


o = Outer()  # creating an object of outer class
o.m1()  # calling the outer class method
i = o.Inner()  # To create an object of Inner class we definitely need to create object of outer class
i.m2()  # calling the inner class method
Outer().Inner().m2()  # calling the inner class m2 method directly


class Person:
    def __init__(self):
        print('Person class constructor started')
        self.name = 'Dharani'
        self.dob = self.DOB()  # creating the DOB class object
        print('Person class constructor completed')

    def display(self):
        print(f'Name of the person: {self.name}')

    class DOB:
        def __init__(self):
            print('DOB class constructor started')
            self.dd = 19
            self.mm = 12
            self.yy = 1997
            print('DOB class constructor completed')

        def display(self):
            print('DOB = {}/{}/{}'.format(self.dd,self.mm,self.yy))


p = Person()  # This call will execute both the constructors
p.display()
p.dob.display()



