"""
Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке. Если наибольших элементов несколько, выведите индекс первого из них.
"""
a = input().split()
max = a[0]
for i in range(len(a)):
    if int(a[i]) > int(max):
        max=a[i]
print(max, a.index(max))
