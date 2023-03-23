#print 1 to 10
# a=[1,2,3,4,5,6,7,8,9,10]
# for i in a:
#     print(i)

for i in range(10): #automatically generates number from 0 to n-1, default step count is 1
    print(i,end=' ')

print()
print('----')

for i in range(0,10): #include 0 , exclude 10 (0--9)
    print(i,end=' ')

print()
print('----')

for i in range(1,11):
    print(i, end=' ')

print()
print('----')

for i in range(1,11,1):
    print(i, end=' ')

print()
print('----')

for i in range(1,11,2):
    print(i, end=' ')

print()
print('----')

for i in range(0,11,2):
    print(i, end=' ')

print()
print('----')
for i in range(10,0,-1):
    print(i, end=' ')

print()
print('----')
for i in range(10,0,-2):
    print(i, end=' ')