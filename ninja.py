from pet import Pet
class Ninja:
    def __init__(self , first_name , last_name , treats , pet_food , pet1, pet2):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet1 = pet1
        self.pet2 = pet2


    # walks the ninja's pet invoking the pet play() method
    def walk(self,num): 
        if num == 1:
            self.pet1.play()
        if num == 2:
            self.pet2.play()
        return self

    #feeds the ninja's pet invoking the pet eat() method
    def feed(self,num): 
        if num == 1:
            self.pet1.eat()
        if num == 2:
            self.pet2.eat()
        return self

    #cleans the ninja's pet invoking the pet noise() method
    def bathe(self, num): 
        if num == 1:
            return self.pet1.noise()
        if num == 2:
            return self.pet2.noise()