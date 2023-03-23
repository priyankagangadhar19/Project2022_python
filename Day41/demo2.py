def main(m):
    print('this is main')
    return m

def fun1():
    print('This is fun1')

fun2=main(fun1)
fun2()
