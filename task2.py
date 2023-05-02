class Queue:
    def __init__(self):
        self.inside = []

    def add(self, name):
        self.inside.append(name)

    def take_out(self):
        if len(self.inside) > 0:
            self.inside.pop(0)
        else:
            print("Очередь уже пуста")

    def __str__(self):
        return "=>".join(self.inside)

    def __add__(self, name):
        self.add(name)
        return self

    def __sub__(self, name):
        self.take_out()
        return self

    def __iadd__(self, name):
        self.add(name)
        return self

    def __isub__(self, name):
        self.take_out()
        return self


q = Queue()
q.add("Камиль")
q.add("Адель")
q.add("Ильнар")
q.take_out()
print(q) # Адель=>Ильнар
q += "Амир"
print(q) # Адель=>Ильнар=>Амир
q -= 'Адель'
print(q) # Ильнар=>Амир
