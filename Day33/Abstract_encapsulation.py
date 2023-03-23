class BankCustomer:

    def __init__(self, new_acc_num):
        self.__account_number = new_acc_num       #public
        self.__balance = 0            #private
        print('Account is created:AN is', self.__account_number)

    def check_balance(self):
        pin=int(input('Plz enter the pin to know the balance'))
        if pin==123:
            print('Account Balance is:', self.__balance)
        else:
            print('Sorry we cant tell u')

    def deposit(self):
        new_amount = int(input('Plz enter the amount to deposit'))
        if new_amount>0:
            self.__balance=self.__balance+new_amount
            print('Deposit successful')
        else:
            print('Invalid Deposit amount')

    def withdraw(self):
        pin = int(input('Plz enter the pin to withdraw:'))
        if pin == 123:
            amount = int(input('Plz enter the amount to withdraw'))
            if amount>0 and amount<=self.__balance:
               self.__balance = self.__balance-amount;
               print('Please collect amount: ',amount)
            else:
                print('invalid amount to withdraw')
        else:
            print('Sorry u cant withdraw')

bhanu_account=BankCustomer(123)
bhanu_account.check_balance()
bhanu_account.deposit()
bhanu_account.check_balance()
bhanu_account.withdraw()
bhanu_account.check_balance()