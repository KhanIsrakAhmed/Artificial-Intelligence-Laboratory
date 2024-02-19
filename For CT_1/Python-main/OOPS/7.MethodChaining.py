# method chaining -> calling multiple method sequentially
#                    each call perform an action on the same object and return self

class Car:
    def start(self):
        print("Turn on the engine")
        return self

    def drive(self):
        print("Drive the car")
        return self

    def Break(self):
        print("You step on the break")
        return self

    def stop(self):
        print("Turn off the engine")
        return self


car = Car()
# car.start().drive() # calling method sequentially

car.start()\
    .drive()\
    .Break()\
    .stop()

# we use '\' to line break
