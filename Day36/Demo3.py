class A:
   i=10

class B:
   i=20

class C(A,B): # takes the first class variables. if it is (B,A) then output takes B variable
   pass

print(C.i)