"""
Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.
"""
a = input()
b = len(a)
for i in range(b):
    if i % 3==0:
        a=a.replace(a[i],"0", 1)
print(a.replace("0", ""))
