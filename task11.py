"""
В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.

Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой. У родоначальника высота равна 0, у любого другого элемента высота на 1 больше, чем у его родителя.

Вам дано генеалогическое древо, определите высоту всех его элементов.

Программа получает на вход число элементов в генеалогическом древе N. Далее следует N−1 строка, задающие родителя для каждого элемента древа, кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.

Программа должна вывести список всех элементов древа в лексикографическом порядке. После вывода имени каждого элемента необходимо вывести его высоту.
"""
n = int(input())

tree = {}
heights = {}

for _ in range(1, n):
    descendant, ancestor = input().split()
    tree[descendant] = ancestor

all_man = set(tree.keys()) | set(tree.values())


def h(name):
    if name not in tree:
        heights[name] = 0
        return 0

    parent = tree[name]
    if parent in heights:
        value = heights[parent] + 1
    else:
        value = h(parent) + 1

    heights[name] = value
    return value


for name in all_man:
    h(name)

for name in sorted(heights):
    print(name, heights[name])
