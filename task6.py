"""
Определите сумму всех элементов последовательности, завершающейся числом 0. В этой и во всех следующих задачах числа, следующие за первым нулем, учитывать не нужно.
"""
sum = 0
a = 1
while a != 0:
    a = int(input())
    sum += a

print(sum)
