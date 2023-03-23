def test(n):
    if n>0:
        test(n-1)
        print(n)
    # else:
    #     print('End')
test(3)