# multi-level inheritance -> when a derived (child) class inherits another derived (child) class
class Organism:  # parent class
    alive = True


class Animal(Organism):  # Animal is the child class of Organism
    def eat(self):
        print("This animal is eating")


class Dog(Animal):  # Dog is the child class of Animal
    def bark(self):
        print("This dog is barking")


dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()
