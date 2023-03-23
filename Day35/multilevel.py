class A:
    i = 20

    def __init__(self):
        self.j = 30


class B(A):
    x= 40

    def __init__(self):
        super().__init__()
        self.y =50

class C(B):
    p= 90

    def __init__(self):
        super().__init__()
        self.q =80
print(C.i)
print(C.x)
print(C.p)

obj = C()
print(obj.j)
print(obj.y)
print(obj.q)

# class A:
#     i=10
# ​
#     def __init__(self):
#         self.j=20
# ​
# class B(A):
#     x=30
#     def __init__(self):
#         self.y=40
#         super().__init__()
# ​
# ​
# class C(B):
#     p=50
#     def __init__(self):
#         self.q=60
#         super().__init__()
# ​
# ​
# print(C.i)
# print(C.x)
# print(C.p)
# ​
# obj=C()
# print(obj.j)
# print(obj.y)
# print(obj.q)
