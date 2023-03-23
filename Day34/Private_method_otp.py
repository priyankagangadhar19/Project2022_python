import random

class Validate:
    __otp=0

    @classmethod
    def get_otp(cls):
        cls.__generate_otp()
        print( cls.__otp)
        return cls.__otp

    @classmethod
    def __generate_otp(cls):
        s = range(100, 999)
        v=random.sample(s, 1)  #  generate a random OTP and return a single value. [s,1]
        cls.__otp=v[0]  # v[0] - returns the 0th index value of the list. that is the OTP
# ex: [s,1]-->[250] single list value is returned > 250 is the 0th index value of the list

    @classmethod
    def veirfy_otp(cls,otp):
        if otp==cls.__otp:
            print('OTP is valid')
        else:
            print('OTP is not valid')


ph=Validate.get_otp()
Validate.veirfy_otp(ph)
Validate.veirfy_otp(123)

# private methods can be used for internal validations > like OTP generation