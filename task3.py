def sieve(list):
    uniq = []
    for i in list:
        if not (i in uniq):
            uniq=[i]+uniq
    return tuple(uniq)

a = [6,4,7,2,3,1]

print(sieve(a)) #(1, 3, 2, 7, 4, 6)

