"""
Каждый из некоторого множества школьников некоторой школы знает некоторое количество языков. Нужно определить сколько языков знают все школьники, и сколько языков знает хотя бы один из школьников.

В первой строке задано количество школьников. Для каждого из школьников сперва записано количество языков, которое он знает, а затем - названия языков, по одному в строке.

В первой строке выведите количество языков, которые знают все школьники. Начиная со второй строки - список таких языков. Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков. Языки нужно выводить в лексикографическом порядке, по одному на строке.
"""
n = int(input())
lis = []
mn = set()
for i in range(n):
    s = int(input())
    for j in range(s):
        lan = input()
        mn.add(lan)
    lis.append(mn)
    mn = set()
dop = set(lis[0])
for i in range(1,n):
    dop.intersection_update(lis[i])
print(len(dop),*sorted(dop),sep='\n')
dop = lis[0]
for i in range(1,n):
        dop |= lis[i]
print(len(dop),*sorted(dop),sep='\n')
