age=int(input('Enter your true age'))
gender=input('Enter your Gender M/F')

if gender=='M':
    if age>=21:
        print('you are eligible to get married')
    else:
        print('you cannot marry man')

elif gender=='F':
    if age>=18:
        print('you are eligible to get married lady')
    else:
        print('Please dont marry lady')
