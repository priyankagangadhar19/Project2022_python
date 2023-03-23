# create a class- Bank Customer
# AccountNumber CustomerName Balace
# deposit & withdrawal & check balance
class BankCustomer:

    def __init__(self, new_acc_num, customer_name,new_balance):
        self.account_number = new_acc_num
        self.customer_name = customer_name
        self.balance = new_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            self.check_balance()
        else:
            print('Invalid amount')

    def withdrawal(self, amount):
        if amount < 0:
            print("Invalid amount")
        elif amount > self.balance:
            print("insufficient balance")
        else:
            self.balance = self.balance - amount
            self.check_balance()

    def check_balance(self):
        print('Account Balance is:', self.balance)

print('hi')
a1 = BankCustomer(123, 'Arun')
a1.check_balance()
a1.deposit(1000)
a1.check_balance()
a1.withdrawal(700)
a1.check_balance()

a1.deposit(-500)
a1.withdrawal(-500)
a1.withdrawal(5000)

