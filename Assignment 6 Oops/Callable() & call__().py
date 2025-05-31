class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return self.factor * number

# Step 1: Object banayein
m = Multiplier(5)

# Step 2: Object ko function ki tarah call karein
print(m(10))  # Output: 50

# Step 3: callable() check karein
print(callable(m))  # Output: True
