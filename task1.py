class cat:
    def __init__(self, name, color,age):
        self.name = name
        self.color = color
        self.age = age

    def meow(self):
        print('meow')

    def mrr(self):
        print('mrr')

    def gav(self):
        print('gav')


silver = cat('silver','white','2')

silver.meow() # meow
silver.mrr() # mrr
silver.gav() # gav
print(silver.color) # white
print(silver.age) # 2
print(silver.name) # silver
