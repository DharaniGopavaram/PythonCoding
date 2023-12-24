"""
The below program explains about abstract methods.
The methods which have only declaration but no proper definition are called abstract methods.
Partially implemented classes are called abstract classes
We can make a class abstract by making it the child class of ABC class.
We can not create an object for a class if class is extending ABC class and contains at-least one abstract method.
Abstract class can contain abstract method and normal methods.
Child classes are responsible to provide proper implementation of parent class abstract methods.
If abstract class contains only abstract methods it is considered as interface.
"""

# abc module stand for abstract base class
from abc import abstractmethod,ABC


class Vehicle(ABC):
    @abstractmethod
    def get_no_of_wheels(self):
        print('This is abstract method')
        pass


# v = Vehicle()  # This is possible if the class is not child class of ABC and does not contain any abstract method
# v.get_no_of_wheels()


class Bike(Vehicle):
    def get_no_of_wheels(self):
        return 2


b = Bike()
print('The number of wheels for bike is:', b.get_no_of_wheels())


class CollegeAutomation(ABC):
    @abstractmethod
    def m1(self):pass
    @abstractmethod
    def m2(self):pass
    @abstractmethod
    def m3(self):pass


class ImplCls(CollegeAutomation):  # this is again an abstract class since we didn't provide all implementation
    def m1(self):
        print('m1 implementation done')

    def m2(self):
        print('m2 implementation done')

# i = ImplCls()  This will result in an error since we didn't provide implementation for m3 method


class ConcreteCls(ImplCls):
    def m3(self):
        print('m3 implementation done')


c = ConcreteCls()
c.m1()
c.m2()
c.m3()

class DBInterface(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass


class Oracle(DBInterface):
    def connect(self):
        print('connecting to oracle database')
    def disconnect(self):
        print('disconnecting from oracle database')

class MySQL(DBInterface):
    def connect(self):
        print('connecting to MySQL database')
    def disconnect(self):
        print('disconnecting from MySQL database')

class Postgres(DBInterface):
    def connect(self):
        print('connecting to Postgres database')
    def disconnect(self):
        print('disconnecting from Postgres database')


dbname = input('Enter the database you want to connect:')
classname = globals()[dbname]  # This will convert string to class name
print(type(classname))
db = classname()
db.connect()
db.disconnect()


