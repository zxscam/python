class Person:
    def __init__(self, name, age, surname):
        self.__name = name
        self.__age = age
        self.__surname = surname

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_surname(self):
        return self.__surname

    def set_age(self, new_age):
        self.__age = new_age


person = Person("Blad", 99, "Putin")
print(person.get_name())  # Blad
print(person.get_age())  # 99
print(person.get_surname())  # Putin

person.set_age(69)
print(person.get_age())  # 69