class Animal:  # parent class
    alive = True

    def sleep(self):
        print("This animal is sleeping")

    def eat(self):
        print("This animal is eating")


# child class
class Rabbit(Animal): # inherit happened
    def run(self):
        print("This rabbit can run")


class Fish(Animal):
    def swim(self):
        print("Fish can swim")


class Hawk(Animal):
    def fly(self):
        print("This hawk can fly")


# create object
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()
rabbit.run()
