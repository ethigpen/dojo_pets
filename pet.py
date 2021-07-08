class Pet:
    def __init__(self,name,animal_type,tricks):
        self.name = name
        self.animal_type = animal_type
        # tricks is a list of strings
        self.tricks = tricks
        self.energy = 0
        self.health = 0


    def sleep(self): 
        self.health += 25

    def eat(self): 
        self.energy += 5
        self.health += 10

    def play(self): 
        self.health += 5
        return self.health

    def noise(self): 
        return 'whine'