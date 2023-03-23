#function=lambda args:exp

def m1():
    return "this is m1"

f=lambda a:a()

print(f(m1))
