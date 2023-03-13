"""
Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.
"""
a = {}
for _ in range(int(input())):
    s = input().split()
    country, cityes = s[0], s[1:]
    for city in cityes:
        a[city] = country
for i in range(int(input())):
    print(a[input()])
