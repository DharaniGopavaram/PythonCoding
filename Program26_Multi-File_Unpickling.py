import pickle

f = open('employee_info.dat','rb')

while True:
    try:
        obj = pickle.load(f)  # load function will everytime return one object at a time
        obj.display_emp_info()
    except EOFError:  # Once all the objects reading is completed we get EOFError
        print('All objects unpickling completed successfully')
        break

