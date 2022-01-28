#To create a Bus child class that inherits from the Vehicle class.
class Vehicle:
    def __init__(self, distance, capacity):
        self.distance = distance
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        fare_bus = self.capacity * 100
        total_fare = fare_bus + (0.1 *fare_bus)
        return total_fare
Hamro_Bus = Bus(10, 25)
print("The total Bus fare is:", Hamro_Bus.fare())
