user=input('Enter User name: ')
pwd=input('Enter the Password: ')
if user.lower()== 'sudheer':
    pwd=input('Enter the Password: ')
    if pwd=='python':
        print('Login successful')
    else:
        print('password is invalid')
else:
    print('Login Unsuccessful')

   