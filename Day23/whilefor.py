i=1
while i<=3:
    pin= input('enter  the pin: ')
    if pin == '1234':
        print('Welcome')
        break
    elif i == 3:
        print('Card is blocked')
    else:
        print('Invalid, try again')
    i=i+1
