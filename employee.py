class EmployeeInfo:
    def __init__(self, eno, ename, esal, eaddr):
        self.emp_no = eno
        self.emp_name = ename
        self.emp_sal = esal
        self.emp_addr = eaddr

    def display_emp_info(self):
        print('Employee number:',self.emp_no)
        print('Employee name:',self.emp_name)
        print('Employee salary:',self.emp_sal)
        print('Employee address:',self.emp_addr)