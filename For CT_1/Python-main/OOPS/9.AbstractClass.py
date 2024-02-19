from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass


class Car(Vehicle):
    def go(self):
        print("This car is driving")


class Motorcycle(Vehicle):
    def go(self):
        print("This motorcycle is driving")

# vehicle = Vehicle() # we can not make object of abstract class
# vehicle.go()


car = Car()
car.go()

motorcycle = Motorcycle()
