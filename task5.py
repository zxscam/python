<<<<<<< HEAD
def fib(n):
    total = 0
    fib = 1
    while(True):
        total = 0
        fib_tot = n + fib
        n = fib
        fib = fib_tot
        total += fib_tot
        if (total > 100):
            break
        print(fib_tot, end=' ')
fib(0)
=======
"""
Дана последовательность целых чисел, заканчивающаяся числом 0. Выведите эту последовательность в обратном порядке.
При решении этой задачи нельзя пользоваться массивами и прочими динамическими структурами данных. Рекурсия вам поможет.
"""
def reverse():
    x = int(input())
    if x != 0:
        reverse()
    print(x)

reverse()
>>>>>>> def
