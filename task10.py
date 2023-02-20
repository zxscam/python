"""
В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
"""
a = list(map(int, input().split()))
min=a.index(min(a))
max=a.index(max(a))
a[min],a[max]=a[max],a[min]

print(*a)
