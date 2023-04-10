def is_alpha(s):
    return s.isalpha()

def capit(s):
    lis = []
    lis.append(s.capitalize())
    return lis

s = ['анТОн', 'НАТАЛЬЯ', 'никита', 'МаРиЯ', '!СЕРГЕЙ!', 'Владимир747', 'Павел+100500']
for i in range(len(s)):
    print(capit("".join(filter(is_alpha, s[i]))))