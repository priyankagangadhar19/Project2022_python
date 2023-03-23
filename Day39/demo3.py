class MultiplyByZeroErr(Exception):

    def __init__(self,msg,details):
        super().__init__(msg)
        self.details=details

    def log_details(self):
        print( self.details)


def multiply(n,m):
    if n==0 or m==0:
        raise MultiplyByZeroErr('input is zero','n is :'+str(n)+" and m is "+str(m))
    else:
        return n*m


print(multiply(2,4))

try:
    print(multiply(2,0))
except MultiplyByZeroErr as zero_err_obj:
    print(zero_err_obj)
    zero_err_obj.log_details()
