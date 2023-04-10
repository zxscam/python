from random import sample
def countdawn(lis):
    lis = sorted(lis)
    lis = reversed(lis)
    lis = [str(i) for i in lis]
    lis.append('Пуск!')
    return lis
s=sample(range(0, 10), 10)
print(*countdawn(s))