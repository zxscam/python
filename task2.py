"""
Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
"""
a = set(map(int,input().split()))
b = set(map(int,input().split()))
total = a & b
print(len(total))
