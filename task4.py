def cesar(s):
    lis = []
    str = []
    for i in s:
        for j in i:
            num = ord(i)
            num+=3
            num = chr(num)
            str.append(num)
        lis.append(str)
    return lis
s = 'лох'
print(cesar(s)) #[['о', 'с', 'ш'], ['о', 'с', 'ш'], ['о', 'с', 'ш']]
