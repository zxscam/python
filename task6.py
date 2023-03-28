<<<<<<< HEAD
def factorial(n):
    total = n
    n-=1
    while n > 1:
        total*=(n)
        n-=1
    return total
print(factorial(6))
=======
"""
Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. В этой задаче нельзя использовать циклы — используйте рекурсию.
"""
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(int(input())))
>>>>>>> def
