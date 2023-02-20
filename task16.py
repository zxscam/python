"""
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей. Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
"""
chess = []
for i in range(8):
    a = list(map(int, input().split()))
    chess.append(a)
check = 0

for i in range(8):
    if check == 1:
        print("YES")
        break
    for j in range(i + 1, 8):
        if (chess[i][0] == chess[j][0] or chess[i][1] == chess[j][1]):
            check = 1
            break
        elif (chess[i][1] - chess[i][0] == chess[j][1] - chess[j][0]):
            check = 1
            break
        elif (chess[i][1] + chess[i][0] == chess[j][1] + chess[j][0]):
            check = 1
            break

if (check == 0):
    print("NO")
