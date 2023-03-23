#for loop

x=[1,2,3,4]
for i in x:
    print(i)
print('--------')

y=(1,2,3,4,)
for i in y:
    print(i)
print('--------')

#for loop - run a block of code multiple times
# for var in collection/group:
#    .......
#      ......

a=[4,27,31]
for i in a:
   print(i)
print('-------')
a=[1,'bhanu',True]
for v in a:
   print(v)
print('-------')
b=(1,'bhanu',True)
for i in b:
   print(i)
print('-------')
c={1,'bhanu',False,'bhanu'}
for i in c:
   print(i)
print('-------')
d={"name":"bhanu","sub":"pyhton"}
for i in d: #print the keys
   print(i)

print('-------')
for s in 'bhanu':
   print(s)