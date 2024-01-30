class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class C(B, A, Z):
    pass

print(A.__subclasscheck__(X))
