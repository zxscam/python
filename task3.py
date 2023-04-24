class Car:
    def __init__(self, color, mark, body, type):
        self.color = color
        self.mark = mark
        self.body = body
        self.type = type

    def start(self):
        print('Speed = 10 km/h')
        self.speed = 10

    def stop(self):
        print('Speed = 0 km/h')
        self.speed = 0

    def turn(self):
        print('Машина повернула налево')

    def speed_up(self, i = 1):
        print(f'Speed = {self.speed + i} km/h')
        self.speed +=i

    def speed_down(self, i = 1):
        if self.speed == 0:
            print('Speed = 0 km/h')
        else:
            print(f'Speed = {self.speed - i } km/h')
            self.speed -= i


    def beep(self):
        print('beep**beep')

car = Car('yellow', 'Mercedes', 'sedan', 'authomatic')
car.start() # Speed = 10 km/h
car.speed_down(2) # Speed = 8 km/h
car.turn() # Машина повернула налево
car.speed_up(10) # Speed = 18 km/h
car.beep() #beep**beep
car.stop() # Speed = 0 km/h

print("\n")

truck = Car('blue', 'Gazel', 'truck', 'authomatic')
truck.start() # Speed = 10 km/h
truck.speed_down(2) # Speed = 8 km/h
truck.turn() # Машина повернула налево
truck.speed_up(10) # Speed = 18 km/h
truck.beep() #beep**beep
truck.stop() # Speed = 0 km/h
