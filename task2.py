"""
Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
"""
a = int(input())
i = 1
b = 0
while (i <= a):
    if (a%i==0):
        if (i==1):
            i = i + 1
            continue
        else:
            b = i
            break
    i = i + 1
print(b)
