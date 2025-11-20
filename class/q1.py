# Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

if __name__ == "__main__":
    # This code only runs when q1.py is run directly
    my_new_car = Car("Toyota", "Carolla")
    print(my_new_car.brand)
    print(my_new_car.model)
