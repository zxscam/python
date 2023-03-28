def count(i,n):
    print(i)
    i += 1
    if(n==0):
        return 0
    return count(i,n-1)
count(0,10)