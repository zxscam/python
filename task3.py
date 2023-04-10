def honest(ls):
    b = []
    for i in range(len(ls)):
        if ls[i] % 2 == 0:
            b.append(ls[i])
    return b

a = []
for i in range(20):
    a.append(i)

print(honest(a)) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]