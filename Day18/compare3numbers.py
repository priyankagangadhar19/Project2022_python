#all 3 number are not same/ greatest num
a=int(input('Enter a: '))
b=int(input('Enter b:'))
c=int(input('Enter c:'))

if a>b and a>c :
    print(a,'a is greater')
elif b>a and b>c:
        print(b,'b is greater')
else:
    print(c,'c is greater')