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