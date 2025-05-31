# Engine class
class Engine:
    def start(self):
        print("Engine started!")

# Car class (composition: Engine is part of Car)
class Car:
    def __init__(self, engine):
        self.engine = engine  # Storing Engine object inside Car

    def start_car(self):
        print("Starting car...")
        self.engine.start()  # Accessing Engine method

# Pehle Engine ka object banayein
e = Engine()

# Engine object ko Car me pass karein
my_car = Car(e)

# Car ke zariye Engine ka method call karein
my_car.start_car()
