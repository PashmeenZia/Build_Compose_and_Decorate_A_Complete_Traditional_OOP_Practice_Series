#1. Using self
#Assignment:
#Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    # Constructor
    def __init__(self, name, marks):
        self.name = name      # 'self.name' means this object's 'name'
        self.marks = marks    # 'self.marks' means this object's 'marks'

    # Method to display student details
    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

# Ab object banate hain
student1 = Student("Pashmeen", 95)

# Object ka method call karte hain
student1.display()