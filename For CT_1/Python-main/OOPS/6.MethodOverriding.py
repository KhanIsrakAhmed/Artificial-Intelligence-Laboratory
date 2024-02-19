class Animal:
    def eat(self):
        print("This animal is eating")


class Rabbit(Animal):
    def eat(self):  # override -> same function in child class
        print("Rabbit is eating")


animal = Animal()
animal.eat()

rabbit = Rabbit()
rabbit.eat()
    