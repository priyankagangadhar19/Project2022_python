#in python can we write a function inside another function? Yes -inner/nested function
#from where we can call the inner function - inside the outer function where inner function is present
def outer():
    print('this is outer function')

    def inner():
        print('this is inner function')

    inner()

outer()
