# class Account:
#     def __init__(self,ac_holder,balance):
#         self.ac_holder=ac_holder
#         self.balance=balance

#     def deposit(self,amount):
#         self.balance+=amount
#         print('Balance after deposit:\t',self.balance)

#     def withdraw(self,amount):
#         if(self.balance>=amount):
#             self.balance-=amount
#             print('Balance after withdraw:\t',self.balance)
#         else:
#             print('Insufficient amount in account')
#             print('Transaction Failed!')
    
#     def display(self):
#         print(f'Account Holder Name:{self.ac_holder} Account Balance: {self.balance}')

# # ac1=Account('Qaiyim',5000)
# # ac2=Account('Intan',3000)

# # ac1.display()
# # ac2.display()

# #withdraw example
# # ac1=Account('Qaiyim',5000)
# # ac1.display()
# # withdrawamount=float(input('Enter amount to withdraw:\t'))
# # ac1.withdraw(withdrawamount)

# #deposit example
# ac1=Account('Qaiyim',5000)
# ac1.display()
# depoamount=float(input('Enter deposit amount:\t'))
# ac1.deposit(depoamount)

#Example 3 (redo)
# class Account: 
#     def __init__(self,ac_holder,balance):
#         self.ac_holder=ac_holder
#         self.balance=balance

#     def get_balance(self)
#         return self.balance
    
#     acc = Account('Qaiyim',5500)
#     acc.balance=34000

#Example 4 to choose either depo or withdraw
class Account:
    def __init__(self,ac_holder,balance):
        self.ac_holder=ac_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print('Balance after deposit:\t',self.balance)

    def withdraw(self,amount):
        if(self.balance>=amount):
            self.balance-=amount
            print('Balance after withdraw:\t',self.balance)
        else:
            print('Insufficient amount in account')
            print('Transaction Failed!')
    
    def display(self):
        print(f'Account Holder Name:{self.ac_holder} Account Balance: {self.balance}')

ac=Account('Qaiyim',5500)
ac.display()
print('Please choose\n 1.Deposit 2.Withdraw 3.Balane info')
option=int(input('Please enter you option:\t'))

if (option==1):
    depoamount=float(input('Enter amount to deposit:\t'))
    ac.deposit(depoamount)
if(option==2):
    wdamount=float(input('Enter amount to withdraw:\t'))
    ac.withdraw(wdamount)
if(option==3):
    ac.display()
else:
    print('Invalid option')