"""
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
"""
a = input().split()
ln = len(a)
for i in range(ln):
    a[i]=int(a[i])
    if (i == ln - 1):
        break
    b = int(a[i + 1])
    if b>a[i]:
        print(b)
