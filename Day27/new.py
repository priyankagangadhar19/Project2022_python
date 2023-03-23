def test(n):
    if n>0:
        print(n)
        test(n-2)

    else:
        print('End')
test(11)