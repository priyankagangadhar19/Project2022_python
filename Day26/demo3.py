
#**a is arbitary keyword---> Tuple >> output will be dictonary

def test1(**a):
    print(a)
test1()
test1(name='Priya')
test1(name='Priya',city='Pune')
test1(name='Priya',city=1)



#*a-->arbitrary  - tuple
def test3(*a):
    print(a)

test3()
test3('bhanu')
test3('bhanu',1)

#**a -->arbitrary + keyword --> dict
def test2(**a):
    print(a)

test2()
test2(name='bhanu')
test2(name='bhanu',city='Pune')