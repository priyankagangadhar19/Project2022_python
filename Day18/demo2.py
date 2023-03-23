user=input('Enter User name: ')
pwd=input('Enter the Password: ')
if user.lower()== 'akshara':
    if pwd=='python':
        print('Login successful')
    else:
        print('Password is invalid')
else:
    print('User name is incorrect')