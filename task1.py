<<<<<<< HEAD
def calculator(f_num,s_num,oper):
    if oper=='+':
        return f_num+s_num
    elif oper=='-':
        return f_num-s_num
    elif oper=='/':
        try:
            return f_num / s_num
        except:
            return 'Нельзя разделить на ноль'
    elif oper=='*':
        return f_num / s_num



print(calculator(5,0,'/')) #Нельзя разделить на ноль
print(calculator(20,20,'+')) #40

=======
"""
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа и выведите результат работы этой функции.
Если вы не знаете, как решить эту задачу, то вы, возможно, не изучали в школе теорему Пифагора. Попробуйте прочитать о ней на Википедии.
"""
from math import sqrt
def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

x1=float(input())
x2=float(input())
y1=float(input())
y2=float(input())
print(distance(x1,x2,y1,y2))
>>>>>>> def
