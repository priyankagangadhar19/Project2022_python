#Create ATM class
class ATM:
    bank_name='SBI'
​
    def __init__(self,card_number,pin):
        self.card_number=card_number
        self.pin=pin
        self.balance=1000
        self.card_is_active=True
        self.ms=[]
​
    def login(self):
        for i in range(3):
            pin = int(input('Please enter the PIN for the card: '+self.card_number))
            if(self.pin==pin):
                print('Welcome to ',self.bank_name,'ATM ,Your Login is successfull')
                break
            elif i==2:
                self.card_is_active = False
                print('Card:',self.card_number,' is blocked')
            else:
                print('invalid pin please try again')
​
    def check_balance(self):
        if self.card_is_active:
            print('Balance is',self.balance)
            self.update_mini_statement('Balance is:'+str(self.balance))
        else:
            print('Sorry ,ur card is blocked','U cant check the balance')
​
    def withdrawal(self):
        if self.card_is_active:
            amount = int(input('Please enter the amount to withdraw'))
            if amount <= 0:
                print("Invalid amount")
            elif amount > self.balance:
                print("insufficient balance")
            else:
                self.balance = self.balance - amount
                print('withdraw is successful')
                self.update_mini_statement('withdraw of '+str(amount)+' is successful & balance is ' + str(self.balance))
        else:
            print('Sorry ,ur card is blocked','U cant withdrawal')
​
​
    def update_mini_statement(self,msg):
        if len(self.ms)==3:
            self.ms.pop(0)
​
        self.ms.append(msg)
​
    def print_mini_statement(self):
​
        print('Your last 3 transactions are')
        print('_'*10)
        for msg in self.ms:
            print(msg)
        print('_' * 10)
​
#--------------------------------------------------------------------------------------------------
#process of hiding details of internal implemention and providing access to only necessory functionality - abstraction
a1=ATM('C1',123)
a1.balance=500
​
# a1.login()
#
# a1.check_balance()
# # a1.print_mini_statement()
#
# a1.withdrawal()
# # a1.print_mini_statement()
#
# a1.withdrawal()
#
# a1.withdrawal()
#
# a1.print_mini_statement()
