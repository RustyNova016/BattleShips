# ----------------------------------------------
# Small python workout
# Inspired from this Vsauce video
# https://www.youtube.com/watch?v=LbALFZoRrw8
# ----------------------------------------------
# Feel free to use it :D
# " " = nothing
# "-" = water hit
# "+" = battleship hit
# ----------------------------------------------

#todo other gamemodes

from Battleships import *

menu_state = "title_screen"

ask_custom_ia = [
    {
        'type': 'input',
        'name': 'Custom AI name',
        'message': 'What\'s the name of the custom AI?',
    },
    {
        'type': 'list',
        'name': 'Hunting mode',
        'message': 'How the AI find the ships?',
        'choices': ['Random', 'Checkerboard'],
        'filter': lambda val: val.lower()
    }
]


def title_screen():
    global menu_state
    print("------------------------------")
    print("   Welcome to BattleShips !   ")
    print("")
    print("1) Play")
    print("2) Settings")
    print("0) Quit")

    awnser = input("")
    if awnser == "0":
        menu_state = "quit"
    elif awnser == "1":
        menu_state = "play"
    elif awnser == "2":
        menu_state = "settings"


def play():
    global menu_state
    print("------------------------------")
    print("            Gamemode ?        ")
    print("")
    print("1) 1v1 (Not Implemented yet)")
    print("2) Speedrun")
    print("3) Battle royal (Not Implemented yet)")
    print("0) Quit")

    awnser = input("")
    if awnser == "0":
        menu_state = "title_screen"
    elif awnser == "1":
        menu_state = "1v1_init"
    elif awnser == "2":
        menu_state = "speedrun_init"
    elif awnser == "3":
        menu_state = "battleroyal_init"


def speedrun_init():
    global menu_state
    print("------------------------------")
    print("   Speedrun mode   ")
    print("")
    print("Try to get the lowest score!")
    print("")

    settings["N_player"] = int(input("Number of players: "))
    settings["N_AI_Random"] = int(input("Number of AI (Type: Random): "))
    settings["N_AI_hunt_destroy"] = int(input("Number of AI (Type: Hunt & destroy): "))

    print("")
    print("Ready ?")
    print(" 1) Play")
    print(" 2) Change game settings")
    print(" 0) return")
    awnser = input("")
    if awnser == "0":
        menu_state = "play"
    elif awnser == "1":
        menu_state = "title_screen"
        SpeedrunMode()
    elif awnser == "2":
        menu_state = "speedrun_init"


while 1:
    print()
    if menu_state == "title_screen":
        title_screen()
    elif menu_state == "play":
        play()
    elif menu_state == "speedrun_init":
        speedrun_init()
    elif menu_state == "quit" or menu_state == "stop":
        break
    else:
        print("/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\\")
        print("|      Uhm something went wrong...   |  ")
        print("|                                    |  ")
        print("|  >>> Reverting to titlescreen...   |  ")
        print("\!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/  ")
        menu_state = "title_screen"
