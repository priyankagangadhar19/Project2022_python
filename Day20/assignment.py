n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=' ')
    print()
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i+1):
        print("*", end=' ')
    print()



# for i in range(0,6):
#     for j in range(i):
#         print(' ',end=' ')
#     for j in range(i):
#         print('*',end=' ')
#     for j in range(i+1):
#         print("*", end=' ')
#     print()
# for i in range(0,6):
#     for j in range(i+1):
#         print(' ',end=' ')
#     for j in range(i,-1):
#         print('*',end=' ')
#     for j in range(i):
#         print("*", end=' ')
#     print()
