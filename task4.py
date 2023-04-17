def fibbonachi():
    a,b=0,1
    for i in range(0,10):
        yield a+b
        a,b=b,a+b
result=list(i for i in fibbonachi())

def iterator(ls):
    iterr=iter(ls)
    while True:
        print(next(iterr))

iterator(result)


