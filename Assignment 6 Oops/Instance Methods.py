class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking! Woof woof!")

# Object create karte hain
dog1 = Dog("Bruno", "Labrador")

# Instance method call
dog1.bark()
