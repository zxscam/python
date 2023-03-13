"""
Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.

Для слова из словаря, записанного в последней строке, определите его синоним.
"""
n = int(input())
dict = {}
for el in range(n):
    key, value = input().split()
    dict[key] = value
    key, value = value, key
    dict[key] = value
word = input()
print(dict[word])
