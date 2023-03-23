
print((lambda s:s in 'welcome to python')('python'))
print((lambda s:s in 'welcome to python')('cobra'))

print((lambda n:n+n)(15))

print((lambda s:s[0]=='c')('cat'))

print((lambda *args:sum(args))(10,20))
print((lambda *args:sum(args))(10,20,30,40))