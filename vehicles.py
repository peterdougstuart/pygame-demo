

class Car:

    # define class level constant for top speed
    TOP_SPEED = 100.0
    INITIAL_FUEL_LEVEL = 50.0

    # class to represent a car
    # note: a class is like the cookie cutter

    def __init__(self, registration, wheels=4):

        # class constructore: this code is run when the object is created
        print("I've got a new car")

        # hold information to descripe properties of car which do not change
        self.registration = registration
        self.wheels = wheels

        # initialise properties of car that do change
        self.fuel_level = Car.INITIAL_FUEL_LEVEL

        self.speed = 0.0
        self.direction = 0.0  # compass orientation (0=north)

    def accelerate(self):

        self.speed += 1.0

        # enforce top speed
        if self.speed > Car.TOP_SPEED:
            self.speed = Car.TOP_SPEED

    def brake(self):

        self.speed -= 1.0

        # enforce minimum speed
        if self.speed < 0:
            self.speed = 0

    def steer_right(self):
        self.direction += 1.0

    def steer_left(self):
        self.direction -= 1.0

    def __str__(self):

        # string representation of object

        text = "CAR INFORMATION:\n"
        text += f"- Registration: {self.registration}\n"
        text += f"- Wheels: {self.wheels}\n"
        text += f"- Speed: {self.speed}\n"
        text += f"- Direction: {self.direction}\n"

        return text


if __name__ == "__main__":

    #note:
    # if this file is executed the __name__ varialbe will be "__main__"
    # if this file is important the __name__ variable will be "vehicles"

    # test code to demonstrate objects

    # ensure test code only runs when this file is run (not on import)

    # create a car object
    # note: an object is the cookie
    car = Car(registration="3 LZ")

    print(car)

    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()

    car.steer_right()
    car.steer_right()

    print(car)

    car.brake()
    car.brake()
    car.brake()
    car.brake()
    car.brake()
    car.brake()
    car.brake()
    car.brake()

    print(car)

    # create another car object
    # note: an object is the cookie
    #reliant_robin = Car(registration="DHV 938D", wheels=3)
    #print(reliant_robin)
    # access car properties
    #print(reliant_robin.registration)
    #print(reliant_robin.wheels)
