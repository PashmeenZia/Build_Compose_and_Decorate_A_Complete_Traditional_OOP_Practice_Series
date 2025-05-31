# Step 1: Class Decorator function
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet  # class me method add kar diya
    return cls

# Step 2: Apply decorator on class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Step 3: Use new method
p = Person("Izhaan")
print(p.greet())  # Greet method decorator ne add ki
