def count(chet,ne_chet,n):
    if n % 2 == 0:
        chet += 1
    else:
        ne_chet += 1
    if(n==0):
        print(f"кол-во четных: ", chet)
        print("кол-во нечетных:", ne_chet)
        return 0
    return count(chet,ne_chet,n-1)
count(0,0,10)
