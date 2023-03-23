def outer(m):
    def inner():
        print('Inner function start')
        m()
        print('Inner function end')

    return inner

@outer
def fun1():
    print('this is func1')


#fun1=outer(fun1)
fun1()
