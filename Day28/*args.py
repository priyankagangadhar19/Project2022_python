def test1(*args):
    print(args)
    for i in args:
        print(i)

a = 10
b = 20
c = 30
test1(a, b, c)

def test2(a, b, c):
    print(a, b, c)

test2(1, 2, 3)

t = (10, 20, 30)
test2(t[0], t[1], t[2])
test2(*t)