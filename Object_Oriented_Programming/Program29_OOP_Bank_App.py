import sys


class Customer:
    """The customer class can be used to perform several bank operations"""
    bank_name = 'Dharmavaram Bank'

    def __init__(self,name,balance = 0.0):
        self.name = name
        self.balance = balance

    def deposit(self,amt):
        self.balance += amt
        print('The balance in the account after deposit is:',self.balance)

    def withdraw(self,amt):
        if amt > self.balance:
            print('Insufficient funds hence exiting')
            sys.exit()
        self.balance -= amt
        print('The balance in the account after withdrawal is:',self.balance)


print(f'Welcome to {Customer.bank_name}')
customer_name = input('Enter your name:')
customer_balance = float(input('Enter the initial amount you want to deposit:'))
c = Customer(customer_name,customer_balance)

while True:
    print('d-deposit \nw-withdraw \ne-exit')
    option = input('Please select your option:')
    if option == 'd' or option == 'D':
        amt = float(input('Enter the amount you want to deposit:'))
        c.deposit(amt)
    elif option == 'w' or option == 'W':
        amt = float(input('Enter the amount you want to withdraw:'))
        c.withdraw(amt)
    elif option == 'e' or option == 'E':
        print('Thanks for using our application')
        sys.exit()
    else:
        print('Please select valid option to continue further')
