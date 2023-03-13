"""
В генеалогическом древе определите для двух элементов их наименьшего общего предка (Lowest Common Ancestor). Наименьшим общим предком элементов A и B является такой элемент C, что С является предком A, C является предком B, при этом глубина C является наибольшей из возможных. При этом элемент считается своим собственным предком.
"""
bloodline = {}

for x in range(int(input())-1):
    child, parent = input().split()
    bloodline[child] = parent

for i in range(int(input())):
    A, B = set(), set()
    first, second = input().split()
    while A.intersection(B) == '':
        A.add(first)
        if first in bloodline:
            first = bloodline[first]
        B.add(second)
        if second in bloodline:
            second = bloodline[second]
    print(list(A.intersection(B))[0])
