#4. Class Variables and Class Methods
#Assignment:
#Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Soneri Bank"  # class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # class variable ko update karna

    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank: {Bank.bank_name}")

# Do accounts banate hain
acc1 = Bank("Umaima")
acc2 = Bank("Izhaan")

# Dono ka current bank name dekhein
acc1.display()  # State Bank
acc2.display()  # State Bank

# Bank name change karte hain
Bank.change_bank_name("Meezan Bank")

# Dubara display karte hain
acc1.display()  # National Bank
acc2.display()  # National Bank
