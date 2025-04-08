class Vehicle:
    def move(self):
        print("This vehicle moves in some way.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water.")

car = Car()
plane = Plane()
boat = Boat()

car.move()     
plane.move()   
boat.move()    
