class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):  # Diamond Inheritance
    pass

# Object of D
d = D()
d.show()

# Check MRO
print(D.__mro__)
