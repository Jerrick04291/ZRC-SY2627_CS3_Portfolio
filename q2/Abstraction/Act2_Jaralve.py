# 1. A.) Duck typing is another way to acheive polymorphism. The object must have the 
#necessary attributes/methods. "If it looks like a duck, qucks like a duck, it must be a duck"

# 2.  B.) The car needed the speak method and the alive attribute

class Car:
    def move(self):
        print("The car drives on the road.")


class Boat:
    def move(self):
        print("The boat sails on water.")


class Drone:
    def move(self):
        print("The drone flies in the sky.")


def start_trip(vehicle):
    vehicle.move()


car = Car()
boat = Boat()
drone = Drone()

start_trip(car)
start_trip(boat)
start_trip(drone)