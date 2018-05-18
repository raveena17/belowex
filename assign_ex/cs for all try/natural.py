'''def selection():
    x=raw_input('enter the nice number:')
    return  float(x)'''
class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        print "withdraw"
        print a.balance
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print "deposit"
        return self.balance
'''a=BankAccount()
print a.deposit(10000)
print a.withdraw(5000)
a.withdraw(4000)'''
