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

import questionary, time, json

class User:
    def __init__(self, name=None, wallet=0):
        self.name = name
        self.wallet = wallet

    def get_name(self):
        if self.name is None:
            self.name = input("What is your name? ")

    # A testing method used to check the users name and wallet ammout
    def __str__(self):
        return f"Name: {self.name}, Wallet Balance: {self.wallet}"

# Game starts:
print("Hi there!")
time.sleep(1)

# Ask the user with 'questionary' list format
played_before = questionary.select(
    "Have you played before?",
    choices=[
        "Yes",
        "No"
    ]).ask()

# Testing
print(f"You have answered {played_before}.")

if played_before == "No":
    #If the user has not played before, their user object will be stored in the json file

    # Setting the new user to an instance of that object
    user = User(name=None, wallet=0)

    # Asking the user for their name and saving it to the 'name' parameter
    user.get_name()

    # Add the user name to the 'users.json' file

    user = [{"name": user.name, "wallet": 0}]

    # saving the user information to the database
    with open("users.json", 'w') as file:
        json.dump(user, file)

    print(f"Welcome, {user.name}! Your wallet balance is {user.wallet}.")

    #This prints the '__str__' method below for testing purposes
    print(user)
else:
    with open('users.json', 'r') as file:
        users = json.load(file)

    user_names = [user["name"] for user in users]

    selectName = questionary.select(
        "Select your name:",
        choices=user_names
    ).ask()

     # loop through the users in the database and find the matching name, and save that data as a user instance
    selected_user = None
    for user in users:
        if user["name"] == selectName:
            #assigning the data to an object instance we can now use in the rest of the application
            selected_user = User(name=user['name'], wallet=user['wallet'])
            break
    user = selected_user
    
    print(f"The user selected data: {user}")











def Main():
    pass


if __name__ == '_main_':
    Main()