class Car:
    def __init__(self, wheels, paint, motor, suspension, brakes):
        self.wheels = wheels
        self.paint = paint
        self.motor = motor
        self.suspension = suspension
        self.brakes = brakes

    def accelarate(self):
        self.wheels = "moving"
        self.motor = True
        self.suspension = True

    def stop(self):
        self.wheels = "stopped"
        self.brakes = True
        self.motor = False
        self.suspension = True


    def drive(self):
        self.wheels = "moving"
        self.motor = True
        self.suspension = True


    def steer(self):
        self.wheels = "angle"

    def print(self):
        print("I'm just a Car")

    def make_noise(self):
        pass

class Chevy(Car):
    def __init__(self, wheels, paint, motor, suspension, brakes, headlights):
        Car.__init__(self, wheels, paint, motor, suspension, brakes)
        self.headlights = headlights

    def print(self):
        print("I'm a chevy")

    def make_noise(self):
        print("SO LOUD!")




class Ford(Car):
    def __init__(self, wheels, paint, motor, suspension, brakes):
        Car.__init__(self, wheels, paint, motor, suspension, brakes)

    def make_noise(self):
        print("so smoooooth....")


def listen_to_car(carType : Car):
    return carType.make_noise()


justACar = Car(wheels="stop", paint="red", motor=False, suspension=True, brakes=True)
# ford = Car(wheels="stop", paint="blue", motor=False, suspension=True, brakes=True)

chevy = Chevy(wheels="stop", paint="red", motor=False, suspension=True, brakes=True, headlights="blue")
ford = Ford(wheels="stop", paint="red", motor=False, suspension=True, brakes=True)

# print(chevy.wheels)
# print(ford)
chevy.print()
ford.print()

listen_to_car(chevy)
listen_to_car(ford)

# print(f"{chevy}, {ford}, {astra}")