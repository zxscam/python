def login(dict):
    print("введите логин и пароль через пробел!")
    log,pas = map(str,input().split())
    for log,pas in dict.items():
        if True:
            print("Доступ разрешен!")
            break
    else:
        print("Регистрация прошла успешно!")
        dict[log] = pas
dict = {}
login(dict)
login(dict)