#3. Public Variables and Methods
#Assignment:
#Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand  # public variable

    def start(self):       # public method
        print(f"{self.brand} is starting...")

# Object create karte hain
my_car = Car("Toyota")

# Public variable access karte hain
print(my_car.brand)  # Output: Toyota

# Public method call karte hain
my_car.start()       # Output: Toyota is starting...
