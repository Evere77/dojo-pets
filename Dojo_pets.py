class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    

    def walk(self):
        self.pet.play()
        return self
        

    def feed(self):
        self.pet.eat()
        return self
        

    def bathe(self):
        self.pet.noise()
        return self
        


class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.sound = noise

    def sleep(self):
        self.energy += 25
        self.health += 5
        print(f"Sleep always helps with health and energy")
        print(self.energy)
        print(self.health)
        return self
        

    def eat(self):
        self.energy += 5
        print(f"Logan has just leveled up energy")
        self.health += 10
        print(self.energy)
        print(self.health)
        return self
        

    def play (self):
        self.health += 5
        print(f"Logan feels happier")
        self.energy -= 3
        print(f"Logan now needs more energy")
        print(self.health)
        print(self.energy)
        return self
        

    def noise(self):
        print(self.sound)


my_treats = ["Bacon favored", "Chicken favored", "Beef favored"]
my_pet_food = ["Dry food", "Wet food", "Human food"]

logan = Pet("Logan", "Dog", ["Sit", "Shake", "Roll over"], "Woof Woof!")

everett = Ninja("Everett", "Martinez", my_treats, my_pet_food, logan)


everett.bathe()
# everett.walk()
# logan.sleep()

logan