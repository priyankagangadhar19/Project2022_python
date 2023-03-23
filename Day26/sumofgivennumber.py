def fact(n):
    fact=0
    for i in  range(n,0,-1):
        fact= fact+i
        if i==1:
            print(i,end="=")
        else:
            print(i,end=" ")

    return fact

print(fact(5))