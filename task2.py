<<<<<<< HEAD
def reverse(variable):
    res=''
    for i in range(len(variable)-1,-1,-1):
        res+=variable[i]
    return res

print(reverse("привет как дела")) #алед как тевирп
=======
"""
Дано действительное положительное число a и целоe число n.

Вычислите an. Решение оформите в виде функции power(a, n).

Стандартной функцией возведения в степень пользоваться нельзя.
"""
def power(a,n):
    return a**n

a=float(input())
n=float(input())
print(power(a,n))
>>>>>>> def
