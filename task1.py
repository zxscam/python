def countdawn():
    ls= [i for i in range(10,-1,-1)]
    i = iter(ls)
    while True:
        print(next(i))

countdawn()