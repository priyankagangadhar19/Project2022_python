#check if the given number is prime or not
#1. it should be natural number -> 1 2 3 4
#2. should be divisble by exactly 2 numbers
#-2 1 4 6 8 9
#2 3 5 7 --> 2,3,4,5,6<n

n=7
msg='prime'
if n>0:
    if n==1:
        msg='Not a prime'
    elif n==2:
        msg='prime'
    else:
        for i in range(2,n):
            if n % i==0:
                msg='Not a prime'
                # break

    print(msg)
# else:
#     print('invalid input')



