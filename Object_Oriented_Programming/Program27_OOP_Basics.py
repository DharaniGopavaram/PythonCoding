"""
The below program explains about oop concepts
Class : blueprint or plan or design
Object : Physical existence of a class is an object
reference variable : The variable which is used to access or operate an object is called reference variable
Class can contain some attributes which are defined using variables
Class can contain some actions or behaviors which are defined using methods
"""


class Student:
    """This is student class which contains all the variables and methods to create student objects"""

    student_college = 'Sri Vidyanikethan Engineering College'
    # The above line declares a static variable which is available across all objects

    def __init__(self,sno,sname,smarks):  # This is called constructor which is used to initialise an object
        self.student_no = sno  # Here we are declaring an instance variable
        self.student_name = sname  # anything that starts with self is called instance variable
        self.student_marks = smarks

    # If we don't write any constructor then Python by default will generate a constructor.
    # constructor will be executed automatically whenever we are creating object.
    # constructor will be executed only once per object
    # constructor will be executed to declare and initialise instance variables of an object

    def display(self):  # self is reference variable to current object
        print(f'Student num:{self.student_no}, Student name:{self.student_name}, '
              f'Student marks: {self.student_marks}')

    # self can be used to access instance variables and instance methods
    # self is the first parameter in constructor and instance methods


s1 = Student(100,'Dharani',80)
s2 = Student(101,'Sunny',98)

print(f'The type of the variable s1 is {type(s1)}')
print(f'Student s1 name = {s1.student_name}')

# print(s1.student_no,s1.student_name,s1.student_marks)
# print(s2.student_no,s2.student_name,s2.student_marks)
# Instead of writing two print statements like above we can declare an instance method in class

s1.display()
s2.display()

print(Student.__doc__)  # We can print doc string like this
help(Student)  # to print high level information about the Student class

print(Student.student_college)  # we can use class name to access static variable
print(s1.student_college)  # we can use object reference as well to access static variable


class Test:
    def __init__(self,n='',m=0):  # this way of declaring constructor will help us to create objects in different ways
        self.var1 = n
        self.var2 = m

    def display(self):
        print('Hi',self.var1)
        print(f'You have {self.var2} score')


t1 = Test()  # calling constructor with no arguments
t1.display()

t2 = Test('Dharani')  # calling constructor with one argument
t2.display()

t3 = Test('Bharath',100)  # calling constructor with two arguments
t3.display()
