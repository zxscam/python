def factorial(n):
    total = n
    n-=1
    while n > 1:
        total*=(n)
        n-=1
    return total
print(factorial(6))
