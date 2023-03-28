def hello(str,lis):
    if str in lis:
        print("Привет, " + str +"!")
        return lis
    else:
        print("Привет, " + str + "! Рад знакомству!")
        lis.append(str)
        return lis
lis = []
str = "Камиль"
hello(str,lis)
hello(str,lis)
