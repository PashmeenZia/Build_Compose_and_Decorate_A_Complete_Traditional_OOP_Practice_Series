#5. Static Variables and Static Methods
#Assignment:
#Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Static method ko object ke bina bhi call kar sakte hain
result = MathUtils.add(5, 3)
print("Sum of my 2 numbers are:", result)
