"""
The below program explains about different types of variables in class.
    1. instance variables -- If the value of a variable varies from object to object such type of variables are
            called instance variables or object related variables.
            For every object a separate copy of instance variables will be created.
            In general instance variables are declared inside constructor by using self
            Within the class we can access instance variables using self but outside the class we can access using
                reference variable
            Instance variables can be declared inside an instance method as well using self
            Instance variables can be declared outside the class using reference variable

    2. static variable -- If the value of the variable doesn't vary from object to object then we should declare
            that variable as a static variable
            Only one copy of the static variable will be created for all the objects
            We can access static variable by using  Class name or object reference but highly recommended
            to use class name
            We can declare static variable inside constructor using class name
            We can declare static variable inside instance method by using class name
            We can declare static variable inside class method by using cls variable or class name
            We can declare static variable inside static method by using class name
            We can declare static variable outside class by using class name.
            We can modify static variable either by using classname or by cls variable if it is class method
            If we are trying to modify static variable value by using object reference then static variable
                value won't be modified instead it will create a new instance variable
            We can delete static variable using del class_name.variable_name or cls.variable_name if we try to
                delete using object reference or self se get error

    3. Local variables -- Local variables are variables which we declare for temporary purpose inside a method
            The scope of the local variable will be gone once the method execution is complete
"""


class Student:

    student_college = 'Degree College'  # This is a statics variable

    def __init__(self,sno,sname,smarks):
        self.student_no = sno  # declaring a instance variable
        self.student_name = sname
        self.student_marks = smarks

    def display(self):
        print(f'Student sno: {self.student_no}')  # accessing instance variable inside class
        print(f'Student name: {self.student_name}')
        print(f'Student marks: {self.student_marks}')
        print()

    def m1(self,sage,sheight):  # Declaring instance variables inside an instance method
        self.student_age = sage
        self.student_height = sheight
        del self.student_name  # inside class deleting a instance variable


s1 = Student(100,'Dharani',90)

print('Accessing instance variables using reference variable')
print(f'Student name: {s1.student_name}')  # accessing instance variable outside class

print('All the instance variables for the s1 object')
print(s1.__dict__)  # __dict__ shows all the variables an object has and the values associated with it

print('calling the display method to display all the instance variables present in the object')
s1.display()

s1.student_no = 103  # Modifying the value of an instance variable
print('The values in s1 object after modification')
s1.display()

s1.student_addr = 'Hyd'  # creating one more instance variable outside class using reference variable
s1.m1(45,5.7)  # After calling this method we will have 2 more instance variables for the s1 object
print(s1.__dict__)  # printing all the instance variables available for s1 object

del s1.student_no  # deleting an instance variable outside class using reference variable
print(s1.__dict__)

print(f'Accessing static variable using class name: {Student.student_college}')
Student.student_college = 'Waste college'  # Modifying the value of the static variable
print(f'Accessing static variable using object reference: {s1.student_college}')

s2 = Student(101,'Bharath',98)
print('s2:',s2.__dict__)
print('s2.student_college',s2.student_college)

s2.student_name = 'Ram'  # If the instance variable already exists it will override the value
# In the above statement if student_name variable doesn't exist then it will create new instance variable
print('s2:',s2.__dict__)
print('s2.student_college',s2.student_college)

# Some more examples of static variable


class Test:
    a = 10  # This is a static variable

    def __init__(self):  # Inside a constructor we can access static variables using self and class name
        self.b = 20
        Test.c = 30  # This declares a static variable
        print(f'self.a = {self.a}')
        print(f'Test.a = {Test.a}')

    def m1(self):  # Inside an instance method we can access static variables using self and class name
        self.d = 40  # This will create an instance variable
        Test.e = 50  # This will create a static variable
        print(f'self.a = {self.a}')
        print(f'Test.a = {Test.a}')

    @classmethod
    def m2(cls):  # This is a class method
        cls.f = 60
        Test.g = 70
        # Inside a class method we can access static variables using cls and class name
        print(f'cls.a = {cls.a}')
        print(f'Test.a = {Test.a}')

    @staticmethod
    def m3():  # This is a static method no self argument here
        Test.h = 80
        # Inside a static method we can access static variables using class name
        print(f'Test.a = {Test.a}')


t1 = Test()
t2 = Test()
t1.m1()  # This method call will create one more static variable
t2.m1()
Test.m2()  # This method call will create two more static variables
Test.m3()  # Here we are calling the static method using class name
# We can call class method and static method using reference variable as well but highly recommended to use class name
Test.i = 90
print('t1:',t1.a,t1.b,t1.c,t1.d,t1.e,t1.f,t1.g,t1.h,t1.i)  # 10 20
print('t2:',t2.a,t2.b,t2.c,t2.d,t2.e,t2.f,t2.g,t2.h,t2.i)  # 10 20
Test.a = 888  # Modifying the static variable using class name
Test.e = 200
t1.b = 999  # Here we are modifying the instance variable
print('t1:',t1.a,t1.b,t1.c,t1.d,t1.e,t1.f,t1.g,t1.h,t1.i)  # 888 999
print('t2:',t2.a,t2.b,t2.c,t2.d,t2.e,t2.f,t2.g,t2.h,t2.i)  # 888 20
print(Test.__dict__)  # We can view all the static variables and the methods in the class using the __dict__


class Check:
    a = 10

    def __init__(self):
        self.b = 20


c1 = Check()
c2 = Check()
c1.a = 888  # We can not modify static variable value using object reference
# In the above statement we are creating a new instance variable for c1 object
c1.b = 999
print('c1:',c1.a,c1.b)  # 888 999
print('c2:',c2.a,c2.b)  # 10 20
print(c1.__dict__)  # {'b': 999, 'a': 888} Here the variable 'a' is instance variable
print(c2.__dict__)  # {'b': 20}

# Some examples related to instance and static variables


class Check1:
    a = 10

    def __init__(self):
        self.a = 888


c = Check1()
print(Check1.a)
print(c.a)


class Check2:
    a = 10

    def __init__(self):
        self.b = 20
        print(self)  # self always points to current object

    @classmethod
    def m1(cls):
        cls.a = 888
        cls.b = 999
        print(cls)  # cls always points to current class


c1 = Check2()
c2 = Check2()
c1.m1()
print('c1',c1.a,c1.b)
print('c2',c2.a,c2.b)
print('Check2',Check2.a,Check2.b)