row=3
for i in range(1,row+1):
    for j in range(row+1,i,-1):
        print(" ",end=" ")

    for k in range(i):
        print("* ",end=" ")
    print()