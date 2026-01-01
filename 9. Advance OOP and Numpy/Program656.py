"""

Find the MRO of class Z of below program:

"""

class A:
    pass
class B:
    pass
class C:
    pass
class D:
    pass
class E:
    pass
class K1(C,A,B):
    pass
class K3(A,D):
    pass
class K2(B,D,E):
    pass
class Z(K1,K3,K2):
    pass


print(Z.mro())

"""

[<class '__main__.Z'>, <class '__main__.K1'>, <class '__main__.C'>, <class '__main__.K3'>,
<class '__main__.A'>, <class '__main__.K2'>, <class '__main__.B'>, <class '__main__.D'>,
<class '__main__.E'>, <class 'object'>]

"""