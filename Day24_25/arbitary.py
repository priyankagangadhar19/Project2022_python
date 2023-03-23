def test1(*a):
    print(a)

def test2(a,*b):
    print(a)
    print(b)

#how many argumets it accepts , how to call above function????
# test1- takes 0 or more
#test2- 1 or more
test1()
test1('bhanu')

test2('bhanu')
test2('bhanu','python')

# #invalid
# def test2(*a,b):
#     print(a)
#     print(b)










