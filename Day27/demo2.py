def test(n):
    if n>0:
        test(n-2)
        print(n)
    else:
        print('End')
test(10)

#prinnt alternatoive numbers using recursive function - 1 to 10

def test(n):
    if n>0:
        print(n)
        test(n-2)

    else:
        print('End')
test(10)