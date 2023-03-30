import questionary, time, json, os

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

    # Setting the new user to an instance of the user class
    user = User(name=None, wallet=0)

    # Asking the user for their name and saving it to the 'name' parameter
    user.get_name()

    # Add the user object to the list of users
        # We want to add the data in the form of an array so we can simply append it in the future
    users = [{"name": user.name, "wallet": 0}]

    # Checking to see if the file exists
        # This gets skipped if a file does exist
    if not os.path.exists("users.json"):
        with open("users.json", "w") as file:
            # Just like earlier, we want to add an array so we can add to it easily
            json.dump([], file)

    # Adding the new user to the existing list of users
    with open("users.json", 'r') as file:
        # Loads the JSON object is a Python dictionary 
        users_data = json.load(file)
    users_data.append({"name": user.name, "wallet": 0})

    # Writing the data back into the json file
    with open("users.json", 'w') as file:
        json.dump(users_data, file)

    print(f"Welcome, {user.name}! Your wallet balance is {user.wallet}.")

    #This prints the '__str__' method below for testing purposes
    print(user)
else:
    with open('users.json', 'r') as file:
        users = json.load(file)

    # Initialize an empty list of user names
    user_names = []

    # Loop through the list of users and create a list of their names
    for user in users:
        user_names.append(user["name"])

    selectName = questionary.select(
        "Select your name:",
        choices=user_names
    ).ask()

    # Loop through the users in the database and find the matching name, and save that data as a user instance
    selected_user = None
    for user in users:
        if user["name"] == selectName:
            # Assigning the data to an object instance we can now use in the rest of the application
            selected_user = User(name=user['name'], wallet=user['wallet'])
            break
    user = selected_user
    
    print(f"The user selected data: {user}")





def Main():
    pass


if __name__ == '_main_':
    Main()
