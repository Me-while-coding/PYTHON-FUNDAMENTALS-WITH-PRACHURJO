from abc import ABC , abstractmethod

class Animal(ABC):
    def eat(self):
        print("eating...")
    @abstractmethod
    def sound(self):
        pass



# animal = Animal()
class Dog(Animal):
    def sound(self):
        print("bhow bhow")

class Cat(Animal):
    def sound(self):
        print("meowwww")

class Lion(Animal):
    def sound(self):
        print("roar")
    pass


class Goat(Animal):
    def sound(self):
        print("Mehhhhhhhhhhhhhhhhhhhhhh")


class Mouse(Animal):
    def sound(self):
        print("squeeek")


animals = [Goat(),Dog(),Lion(),Cat(),Mouse()]

for animal in animals:
    animal.sound()
    animal.eat()



