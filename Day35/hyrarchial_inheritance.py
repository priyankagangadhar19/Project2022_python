class A:
    i = 10

    def __init__(self,k):
        self.j = k


class B(A):
    def __init__(self):
        super().__init__(100)


class C(A):
    def __init__(self,l):
        super().__init__(l)


print(B.i)  #10
print(C.i)  #10

obj1 = B()
print(obj1.j) #100

obj2 = C(200)
print(obj2.j)   #200