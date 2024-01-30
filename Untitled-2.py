class X:
    pass
class Y:
    pass
class Z:
    pass
class A(X,Y):
    pass
class B(X,Z):
    pass
class M(B,A,Z):
    pass
print (M.mro())