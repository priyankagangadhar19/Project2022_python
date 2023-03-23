class A:
    i=10

    def __init__(self):
        self.j=20

class B(A):

    def __init__(self):

obj=B()
print(obj.j)

print(B.i)