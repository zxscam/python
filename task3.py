class Box:
    def __init__(self, postcode, name, from_city, target_city):
        self.__postcode = postcode
        self.__name = name
        self.__from_city = from_city
        self.__target_city = target_city

    def get_postcode(self):
        return self.__postcode

    def get_name(self):
        return self.__name

    def get_from_city(self):
        return self.__from_city

    def get_target_city(self):
        return self.__target_city

    def set_target_city(self, new_target_city):
        self.__target_city = new_target_city

box = Box(2913150, "Коробка 1", "Москва", "Санкт-Петербург")

print("Номер отправления:", box.get_postcode()) # Номер отправления: 2913150
print("Название:", box.get_name()) # Название: Коробка 1
print("Отправлено из города:", box.get_from_city()) # Отправлено из города: Москва
print("Целевой город:", box.get_target_city()) # Целевой город: Санкт-Петербург


box.set_target_city("Казань")
print("Новый целевой город:", box.get_target_city()) # Новый целевой город: Казань