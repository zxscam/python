"""
Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.
"""
nums = list(map(int, input().split()))
result = set()
for num in nums:
    if num not in result:
        result.add(num)
        print('NO')
    else:
        print('YES')
