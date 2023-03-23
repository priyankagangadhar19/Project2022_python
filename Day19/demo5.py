print('Start')

for i in range(10):
    pass

for i in range(10):#0 to 9
    print(i) #0
    break  #to exit from the for loop before completing the iteration

for i in range(10):
    print(i) # 0 1 2 3 4 5 6 7
    if i>6:
        break

for i in range(10):
    if i>6:
        break
    print(i) #0 1 2 3 4 5 6

print('End')