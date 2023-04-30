class Father:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Child(Father):
    def __init__(self,name, surname, patronim):
        super().__init__(name,surname)
        self.patronim = patronim


ch = Child('Kamil', 'Miftiev', 'Volkovich')
print(ch.name, ch.surname, ch.patronim)