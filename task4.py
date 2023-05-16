from task3 import Box

class Truck:
    def __init__(self, capacity, driver, from_city, target_city):
        self.capacity = capacity
        self.driver = driver
        self.from_city = from_city
        self.target_city = target_city
        self.boxes = []

    def __str__(self):
        return f"Грузовик {self.driver}, емкость {self.capacity}, из {self.from_city} в {self.target_city}"

    def add(self, box):
        if len(self.boxes) < self.capacity:
            self.boxes.append(box)
            print(f"Коробка {box.get_name()} добавлена в грузовик")
        else:
            print("Недостаточно места в грузовике")

    def sub(self, box_name):
        for box in self.boxes:
            if box.get_name() == box_name:
                self.boxes.remove(box)
                print(f"Коробка {box_name} удалена из грузовика")
                return
        print(f"Коробки {box_name} нет в грузовике")


box1 = Box(142180, "Коробка 1", "Москва", "Санкт-Петербург")
box2 = Box(142181, "Коробка 2", "Москва", "Санкт-Петербург")
box3 = Box(142182, "Коробка 3", "Москва", "Санкт-Петербург")


print("Номер отправления:", box1.get_postcode()) # Номер отправления: 142180
print("Название:", box1.get_name()) # Название: Коробка 1
print("Отправлено из города:", box1.get_from_city()) # Отправлено из города: Москва
print("Целевой город:", box1.get_target_city()) # Целевой город: Санкт-Петербург


truck1 = Truck(2, "Водитель 1", "Москва", "Санкт-Петербург")


truck1.add(box1) # Коробка Коробка 1 добавлена в грузовик
truck1.add(box2) # Коробка Коробка 2 добавлена в грузовик
truck1.add(box3) # Недостаточно места в грузовике

truck1.sub("Коробка 2") # Коробка 2 удалена из грузовика

print(truck1) # Грузовик Водитель 1, емкость 2, из Москва в Санкт-Петербург