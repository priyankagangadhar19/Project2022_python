def outer(m):
    def inner():
        print('Inner function start')
        m()
        print('Inner function end')

    return inner

def fun1():
    print('this is func1')


fun2=outer(fun1)
fun2()
