from random import randint
num = randint(0,100)
def play(col,nm):
    if col == 0:
        print(nm)
        return 0
    chis = int(input())
    if chis == nm:
        print("число отгадано!")
        return 0
    if chis > nm:
        print("загаданное число меньше")
    else:
        print("загаданное число больше")
    return play(col-1,nm)
play(10,num)
