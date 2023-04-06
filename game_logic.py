from classes import *
from user_setup import user
import questionary

def gameLogic(user):
    print(f"Test for user transfer: {user.name}")

    user_action = questionary.select(
        f"Good day {user.name}. What would you like to do?",
        choices=[
        "Buy",
        "Sell",
        "Exit"
        ]
    ).ask()

    if user_action == 'Buy':
        user.buyStock()
    elif user_action == 'Sell':
        user.sellStock()

    return