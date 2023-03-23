age=int(input('Enter your true age'))
gender=input('Enter your Gender M/F')

if gender=='M' and age>=21:
    print('you are eligible to get married')
elif gender=='F' and age>=18:
    print('you are eligible to get married')
else:
    print('Please dont marry')
