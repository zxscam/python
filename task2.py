from abc import ABC, abstractmethod

class Cloth(ABC):
    def __init__(self, width):
        self.width = width

    def fabric_required(self):
        pass

class Coat(Cloth):
    reserved = 0

    def __init__(self, size):
        super().__init__(width=0)
        self.size = size

    def fabric_required(self):
        return self.size / 6.5 + 0.5

class Suit(Cloth):
    reserved = 0

    def __init__(self, height):
        super().__init__(width=0)
        self.height = height

    def fabric_required(self):
        return 2 * self.height + 0.3

coat1 = Coat(42)
coat2 = Coat(48)
suit1 = Suit(1.7)
suit2 = Suit(1.8)

print("Количество ткани для пальто 1:", coat1.fabric_required()) # Количество ткани для пальто 1: 6.961538461538462
print("Количество ткани для пальто 2:", coat2.fabric_required()) # Количество ткани для пальто 2: 7.884615384615385
print("Количество ткани для костюма 1:", suit1.fabric_required()) # Количество ткани для костюма 1: 3.6999999999999997
print("Количество ткани для костюма 2:", suit2.fabric_required()) # Количество ткани для костюма 2: 3.9

Coat.reserved += coat1.fabric_required()
Coat.reserved += coat2.fabric_required()
Suit.reserved += suit1.fabric_required()
Suit.reserved += suit2.fabric_required()

print("Общее количество зарезервированной ткани:", Coat.reserved + Suit.reserved) # Общее количество зарезервированной ткани: 22.446153846153848
print("Количество зарезервированной ткани для пальто:", Coat.reserved) # Количество зарезервированной ткани для пальто: 14.846153846153847
print("Количество зарезервированной ткани для костюмов:", Suit.reserved) # Количество зарезервированной ткани для костюмов: 7.6