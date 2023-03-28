def count(n):
    chet = 0
    ne_chet = 0
    while n > 0:
        if n % 2 == 0:
            chet += 1
        else:
            ne_chet += 1
        n -= 1
    print("кол-во четных: ", chet)
    print("кол-во нечетных: ", ne_chet)
count(10)
