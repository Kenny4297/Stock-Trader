from classes import *
from user_setup import *
from game_logic import *

def Main():
    global user
    user = userSetup()
    gameLogic(user)

if __name__ == '__main__':
    Main()

