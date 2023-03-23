def main(m):
    print('this is main')
    return m
@main                    #fun1=main(fun1) #decorator
def fun1():     #receiving
    print('This is fun1')

fun1()  #sending

#go to higher order function
#decorator--> name should be higer order function

#sending andd receiving varibale name should be same for using decorator
#we cann  put variable  name same as function name. ex:fun1