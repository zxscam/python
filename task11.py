"""
Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.
"""
a = input()
b = a.find('h')
c = a.rfind('h')
x = a[b + 1:c]
print(a[:b + 1] + x.replace('h', 'H') + a[c:])
