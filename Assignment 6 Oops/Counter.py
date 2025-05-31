#2. Using cls
#Assignment:
#Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    # Class variable
    object_count = 0

    def __init__(self):
        # Jab bhi object banega, count barhega
        Counter.object_count += 1

    # Class method to display count
    @classmethod
    def display_count(cls):
        print(f"My total objects created are: {cls.object_count}")

# Objects banaate hain
c1 = Counter()
c2 = Counter()
c3 = Counter()
c4 = Counter()

# Class method call karte hain
Counter.display_count()
