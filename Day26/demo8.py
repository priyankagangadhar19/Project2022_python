def prime(n):
    msg = 'prime'
    if n > 0:
        if n == 1:
            msg = 'Not a prime'
        elif n == 2:
            msg = 'prime'
        else:
            for i in range(2, n):
                if n % i == 0:
                    msg = 'Not a prime'
                    break

        print(n,"is", msg)
    else:
        print('invalid input')

for i in range(0,9):
    prime(i)



# #create a function to check if the given number is prime or not
# def is_prime(n):
#     if  n<=0 :
#         print(n,' is Invalid input')
#         return
#     msg="Prime"
#     if n==1:
#         msg="Not a Prime"
#     elif n==2:
#         msg="Prime"
#     else:
#         for i in range(2,n):
#             if n % i==0:
#                 msg="Not a Prime"
#                 break
#     print(n,"is",msg)
# is_prime(1)
#









