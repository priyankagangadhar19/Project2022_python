#arbitary parameter---> add a * before parameter
def test(*a):
   print('No of arg:',len(a))
   for i in a:
      print(i)


test()
test(1)
test('bhanu','prakash')
test('bhanu',2,True)
