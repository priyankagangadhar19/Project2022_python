for i in range(1,10):
    if i<5:
        continue   #skip remaing code and goto next iteration
    print(i)

for i in range(1,10):

    if i>3 and i<7:
        continue
    print(i,end=' ')

print('-----')
for i in range(1,10):
    if i>3 and i<7:
        break
    print(i,end=' ')

