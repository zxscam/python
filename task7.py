def hello(func):
    def wrapper(*a):
        n = func(*a)
        print(f"привет,{n}!")
        return n
    return wrapper()
@hello
def get_name( ):
    name = input('Введите имя')
    return name