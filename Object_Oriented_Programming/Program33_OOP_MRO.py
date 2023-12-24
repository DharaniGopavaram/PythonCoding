"""The below program explains about MRO(Method Resolution Order)
Python uses C3 linearization algorithm designed by Samuel Pedroni.
If Python requires any method
 1. First priority is always for child class
 2. If child class does not contain then only parent class method will be executed
 3. If multiple parents are available then Python will consider from left to right of declaration.
 4. In MRO Python will visit any class only once.

Linearization(Class) = Class + merge(Linearization(ParentClass1),Linearization(ParentClass2)...,ParentList)

"""


class P1: pass
class P2: pass

class P3(P1,P2):pass
print(P3.mro())

"""
Linearization for class P3 is like below.
L(P3) = P3 + merge(L(P1),L(P2),P1P2) - Here P1P2 is parent list

L(P1) = P1 + merge(L(O)+O)
      = P1 + merge(O+O)
      = P1 + O

just like above the L(P2) will be P2 + O

L(P3) = P3 + merge(P1 + O,P2 + O,P1 + P2)
The first element in the merge is (P1 + O) and the first value is P1 which is called head
If the head element is not in the tail part of the another merge elements then we can consider head

L(P3) = P3 + P1 + merge(O,P2 + O,P2) -- after finalising P1
Since the next head element is O and O is available in tail part P2 + O we should not consider it
Moving on to the next head P2 and P2 is not available as tail part for any other elements we should consider P2

L(P3) = P3 + P1 + P2 + merge(O,O) -- after finalising and removing P2
L(P3) = P3 + P1 + P2 + O -- this is the final MRO
"""

class D:pass
class E:pass
class F:pass
class B(D,E):pass
class C(E,F):pass
class A(B,C):pass
print(A.mro())

'''
L(A) = A + merge(L(B),L(C),BC)

L(B) = B + merge(L(D),L(E),DE)
     = B + merge(D + O,E + O,DE)
     = B + D + merge(O,E + O,E)
     = B + D + E + merge(O,O)
     = B + D + E + O

L(C) = C + merge(L(E),L(F),EF)
     = C + merge(E + O,F + O,EF)
     = C + E + merge(O,F + O,F)
     = C + E + F + O

L(A) = A + merge(BDEO,CEFO,BC)
     = A + B + merge(DEO+CEFO+C)
     = A + B + D + merge(EO+CEFO+C) -- we can not remove E here because it is tail part
     = A + B + D + C + merge(EO + EFO)
     = A + B + D + C + E + merge(O + FO)
     = A + B + D + C + E + F + O
     = ABDCEFO
'''