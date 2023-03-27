# Create A stock trader application that follows the instructions in 'instructions.txt'. 

# What I will need:

# USER CLASS
    # Dictionary to store stocks
    # Wallet to keep track of Users cash
    # Buying and selling options
        # If buy, ask user how many stocks they want to buy


# STOCK CLASS 
    # Contain all the stocks that are available to buy using the 'stock list' array in 'list_of_companies'. 
    # Keeps track of each updated stock each day
        # Update the daily stock changes by 20% up or down. 

#! Next Steps: Create a user Class and add the necessary variable

#^ Example of a Python class
# class Cat:
#     def __init__(self, name, color, age):
#         self.name = name
#         self.color = color
#         self.age = age
    
#     def meow(self):
#         print("Meow! Meow!")
    
#     def get_name(self):
#         return self.name
    
#     def get_color(self):
#         return self.color
    
#     def get_age(self):
#         return self.age

import questionary, time, json

class User:
    def __init__(self, name, wallet):
        self.name = name
        # How much money the user will use to play in the stock market.
        self.wallet = wallet

    def get_name(self):
        self.name = input("What is your name?")

# # Game starts:
# print("Hi there!")
# time.sleep(1)

# playedBefore = questionary.select(
#     "Have you played before?",
#     choices=[
#     "Yes",
#     "No"
#     ]).ask()

# print(f"You have answered {playedBefore}")

# if (playedBefore != "Yes"):
#     userName = input("What is your name?")
#     # Create new instance with the users name here. Leave out the wallet information

class User:
    def __init__(self, name=None, wallet=0):
        self.name = name
        self.wallet = wallet

    def get_name(self):
        if self.name is None:
            self.name = input("What is your name? ")

    def __str__(self):
        return f"Name: {self.name}, Wallet Balance: {self.wallet}"

# Game starts:
print("Hi there!")
time.sleep(1)

played_before = questionary.select(
    "Have you played before?",
    choices=[
        "Yes",
        "No"
    ]).ask()

print(f"You have answered {played_before}.")

if played_before == "No":
    user_name = User(name=None, wallet=0)
    user_name.get_name()
    print(f"Welcome, {user_name.name}! Your wallet balance is {user_name.wallet}.")
    print(user_name)
else:
    selectName = questionary.select(
        
    )











def Main():
    pass


if __name__ == '_main_':
    Main()