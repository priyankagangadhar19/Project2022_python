# class Bank_customer:
#     Bank_name='SBI'
#     IFSC_Code='SBI001'
#
#
# e1=Bank_customer()
# print(Bank_customer.Bank_name)
#create a class for a Bank customer- use class var or insta var to store below info
#Bank Name='SBI' & IFSC code=SBI001
#Customer Name='Bhanu',Account Number=001
#create 2 customer objects and print above info of each customer
class BankCustomer:
    bank_name='SBI'
    ifsc_code='SBI001'

    def __init__(self,c_name,a_num):
        self.customer_name=c_name
        self.account_number=a_num

    def print_customer_details(self):
        print('Bank Name:',self.bank_name)
        print('IFSC',self.ifsc_code)
        print('Name',self.customer_name)
        print('AC no.',self.account_number)
        print('_'*10)

customer1=BankCustomer('Sandeep','001')
customer2=BankCustomer('Shruthi','002')

customer1.print_customer_details()
customer2.print_customer_details()
