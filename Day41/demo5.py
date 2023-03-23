def main(m):
    print('this is main1')
    return m

@main           # fun1=main(fun1)   #--decorator
def fun1():
    print('This is fun1')
fun1()

@main
def fun2():
    print('this is fun2')

fun2()