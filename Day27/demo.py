def fact(n):
    f=1
    if n>0:
        f=n*fact(n-1)
    return f

print(fact(4))