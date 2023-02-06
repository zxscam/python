"""
Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φn = A. Если А не является числом Фибоначчи, выведите число -1.
"""
A = int(input())
a = 0
b = 1
res = 0
count = 1
bool = 0
while(res<=A):
    res = a+b
    a = b
    b = res
    count+=1
    if(A == res):
        bool = 1
        break
if(bool == 1):
     print(count)
else:
    print(-1)
