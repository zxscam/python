from abc import ABC, abstractmethod
class Stationery(ABC):
    def __init__(self, title):
        self.title = title
    @abstractmethod
    def draw(self):
        pass

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

