class A:
    def __init__(self):
        i = 10


class B(A):
    def __init__(self):
        super().__init__()
        self.i = 20


class C(A):
    def __init__(self):
        super().__init__()
        self.i = 30


class D(B, C):

    def __init__(self):
        super().__init__()
        C.__init__(self)


obj = D()
print(obj.i)
