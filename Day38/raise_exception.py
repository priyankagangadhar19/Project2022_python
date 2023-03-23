#generating an exceptio by us


def div_num(n1,n2):
    if n2==0:
        raise ZeroDivisionError('Bhanu div by zero')
    else:
        print(n1/n2)


div_num(10,2)
try:
    div_num(10,0)
except Exception as e:
    print(e)

print('Thank You')

# we create an object called ZeroDivisionError
# and store a message called ('Bhanu div by zero')
#ad in line 14 Exception class (parent) is accessing the ZeroDivisionErrorvalues:
# so it will print the message ('Bhanu div by zero')
