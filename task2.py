import string
def alpha():
    ls = list(string.ascii_lowercase)
    for i in ls:
        yield i

generator = alpha()

while True:
    print(next(generator))