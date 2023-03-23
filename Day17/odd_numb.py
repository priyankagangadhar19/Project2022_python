# num=input('Enter the number:')
# num=int(num)
# if num%2:  #if not(num%2):
#     print(num,'The number is odd')
#
# else:
#     print(num,'The number is even')


#accept a number from user and check if it is odd number or even number
# 2 4 6 8      , 1 3 5...odd  --> False 0 '' None [] (){} -everything else True
num=int(input('Plz enter a number'))

if num % 2 != 0:
    print(num, ' is odd number')
else:
    print(num,' is even number')

if num % 2:
    print(num, ' is odd number')
else:
    print(num, ' is even number')