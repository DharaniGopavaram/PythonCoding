"""
The below program explains about pickling and unpickling of objects in Python.
In Python, pickling refers to the process of serializing objects into a byte stream,
and unpickling is the process of deserializing the byte stream back into objects.
This is useful for storing or transmitting data in a compact binary format.
The process of writing state of an object to a file is called pickling.
The process of reading state of an object from a file is called un-pickling.
"""

import pickle


class Employee:
    def __init__(self, eno, ename, esal, eaddr):  # this is a constructor
        self.emp_no = eno  # here we are defining class variables
        self.emp_name = ename
        self.emp_sal = esal
        self.emp_addr = eaddr

    def display(self):
        print('Employee number:',self.emp_no)
        print('Employee name:',self.emp_name)
        print('Employee salary:',self.emp_sal)
        print('Employee address:',self.emp_addr)


with open('emp.dat','wb') as f:
    e1 = Employee(100, 'Dharani', 10000, 'Hyd')
    pickle.dump(e1,f)  # dump method is used to perform pickling
    print('Pickling of emp object completed successfully')

with open('emp.dat','rb') as f:
    obj = pickle.load(f)  # load method is used to perform un-pickling
    print('Employee information after unpickling')
    print('Employee name using obj object is:',obj.emp_name)
    obj.display()
    # obj1 = pickle.load(f)  # EOFError: Ran out of input
    # If we try to unpickle the object again we get EOFError

