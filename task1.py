class Battery:
    def __init__(self, capacity=[], max_charge=5):
        self.capacity = capacity
        self.max_charge = max_charge

    def charge(self):
        if len(self.capacity) < self.max_charge:
            self.capacity.append(')')
        else:
            print("Батарея уже заряжена")

    def discharge(self):
        if len(self.capacity) > 0:
            self.capacity.pop()
        else:
            print("Батарея уже разрежена")

    def __str__(self):
        return "[" + "".join(self.capacity) + "]"

b = Battery()
print(b) # []
b.charge()
print(b) # [)]
b.charge()
print(b) # [))]
b.charge()
print(b) # [)))]
b.discharge()
print(b) # [))]

for i in range(5):
    b.charge()
print(b) # [)))))] (Батарея уже заряжена)
