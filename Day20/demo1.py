#else block
for i in range(1,11):
    print(i)
else:
    print('The end')

for i in range(1,11):
    print(i)
    break
else:
    print('The end')

for i in range(1,11):
    print(i)
    continue
else:
    print('The end')