from abc import ABC, abstractmethod
class Stationery(ABC):
    def __init__(self, title):
        self.title = title
    @abstractmethod
    def draw(self):
        pass
    @classmethod
    def set_color(cls, color):
        cls.color = color


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.color = 'blue'

    def draw(self):
        print(f'{self.title} {self.color} пишет')

class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} рисует')

class Handle(Stationery):
    def draw(self):
        print(f'{self.title} выделяет')

pen = Pen('Ручка')
penc = Pencil('Карандаш')
hand = Handle('Маркер')
pen.draw() # Ручка blue пишет
penc.draw() # Карандаш рисует
hand.draw() # Маркер выделяет
Stationery.set_color('Yellow')
print(Pen.color) # Yellow
print(Pencil.color) # Yellow
print(Handle.color) # Yellow
