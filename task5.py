from time import time, localtime
class Clock:
    @staticmethod
    def Say_time():
        rez = localtime(time())
        print(f'{rez.tm_hour}:{rez.tm_min}:{rez.tm_sec}')

Clock.Say_time()