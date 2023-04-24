from time import sleep
class trafficlight:
    def init(self, color="красный"):
        self.color = color

    def switching(self):
        self.color = "красный"
        print(f"{self.color} свет")
        sleep(1)
        self.color = "желтый"
        print(f"{self.color} свет")
        sleep(0.5)
        self.color = "зеленый"
        print(f"{self.color} свет")
        sleep(2)
traf = trafficlight()
traf.switching()
