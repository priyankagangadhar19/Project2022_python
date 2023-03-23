try:
    n1=int(input('Please enter  the number: '))
    n2=int(input('Please enter  the number: '))
    result= n1/n2
    print('Result of n1/n2 is: ', result)

except Exception as obj:
    print(obj)

print('The end')

#We are creating an object obj=Exception()
