# Create an ElectricCar class that inherits from the Car class and has an additional attribute battrey size.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class ElectricCar(Car):
    def __init__(self, brand, model ,battrey_size):
        super().__init__(brand, model)
        self.battrey_size = battrey_size

new_car = ElectricCar("Tesls", "S4", "80 kWh")

print(f"{new_car.brand} {new_car.model} {new_car.battrey_size}")
