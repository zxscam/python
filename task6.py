import string
def alphabet():
    alpha = list(string.ascii_lowercase)
    dic = {}
    for i in range(len(alpha)):
        dic[i+1] = alpha[i]
    print(dic)
alphabet()