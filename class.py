class Vehicle:
    def Vehicle_info(self):
        print("Inside Vehicle class")

class Car(Vehicle):
    def car_info(self):
        print("inside car class")

car=Car()

car.Vehicle_info()
car.car_info()
