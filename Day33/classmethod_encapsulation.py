#encapsulation w.r.t class variable
class Bank:
    __name='SBI'
    @classmethod
    def get_bank_name(cls):
        print(cls.__name)


Bank.get_bank_name()