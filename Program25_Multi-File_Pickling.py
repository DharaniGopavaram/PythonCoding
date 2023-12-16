import employee as e
import pickle

with open('employee_info.dat','wb') as f:
    e1 = e.EmployeeInfo(100,'Dharani',10000,'Hyd')
    pickle.dump(e1,f)
    e2 = e.EmployeeInfo(101,'John',20000,'Bangalore')
    pickle.dump(e2,f)
    e3 = e.EmployeeInfo(102,'Bharath',15000,'Delhi')
    pickle.dump(e3,f)
    e4 = e.EmployeeInfo(103,'Ravi',26000,'Kolkata')
    pickle.dump(e4,f)

print('All the objects are pickled successfully')
