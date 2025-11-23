# Polymorphism

class Vehical:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

class Car(Vehical):
    def move(self):
        print("Move!")

class Boat(Vehical):
    def move(self):
        print("Sail!")

class Plane(Vehical):
    def move(self):
        print("Fly!")

car = Car("BMW", "M4")
boat = Boat("Ibiza", "Touring")
plane = Plane("Tejas", "747")

for x in (car, boat, plane):
    print(f"{x.brand} {x.model}")
    x.move()