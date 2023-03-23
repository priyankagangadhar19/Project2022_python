def loginlogout(m):
    def inner():
        print('login to app')
        m()
        print('logout from app')

    return inner

@loginlogout
def script1():
    print('create customer')

script1()

@loginlogout
def script2():
    print('delete customer')

script2()
