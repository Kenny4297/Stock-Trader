class User:
    def __init__(self, name=None, wallet=0):
        self.name = name
        self.wallet = wallet

    def get_name(self):
        if self.name is None:
            self.name = input("What is your name? ")

    # A testing method used to check the users name and wallet amount
    def __str__(self):
        return f"Name: {self.name}, Wallet Balance: {self.wallet}"
    

