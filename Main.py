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

print()
print("Loading...")
print()

from Battleships import *

menu_state = "title_screen"


def title_screen():
    global menu_state
    print("------------------------------")
    print("   Welcome to BattleShips !   ")
    print("")
    questions = [
        {
            'type': 'list',
            'name': 'main',
            'message': '',
            'choices': ['Play', 'Settings', 'Quit'],
            'filter': lambda val: val.lower()
        }
    ]
    menu_state = prompt(questions, style=style)["main"]


def play():
    global menu_state
    print("------------------------------")
    print("")
    questions = [
        {
            'type': 'list',
            'name': 'main',
            'message': 'Gamemode ?',
            'choices': ['Speedrun', 'Return'],
            'filter': lambda val: val.lower() + "_init"
        }
    ]
    menu_state = prompt(questions, style=style)["main"]
    if menu_state == "return_init":
        menu_state = "title_screen"


def speedrun_init():
    global menu_state
    print("------------------------------")
    print("   Speedrun mode   ")
    print("")
    print("Try to get the lowest score!")
    print("")

    questions = [
        {
            'type': 'input',
            'name': 'N_player',
            'message': 'Number of players: ',
            'validate': NumberValidator,
            'filter': lambda val: int(val)
        },
        {
            'type': 'input',
            'name': 'N_AI_Random',
            'message': 'Number of AI (Type: Random): ',
            'validate': NumberValidator,
            'filter': lambda val: int(val)
        },
        {
            'type': 'input',
            'name': 'N_AI_hunt_destroy',
            'message': 'Number of AI (Type: Hunt & destroy): ',
            'validate': NumberValidator,
            'filter': lambda val: int(val)
        },
        {
            'type': 'list',
            'name': 'ready',
            'message': 'Gamemode ?',
            'choices': ['Start', 'Return'],
            'filter': lambda val: val.lower()
        }
    ]

    awn = prompt(questions, style=style)
    if awn["ready"] == "return":
        menu_state = "play"
    else:
        settings["N_Players"] = awn["N_player"]
        settings["N_AI_Random"] = awn["N_AI_Random"]
        settings["N_AI_hunt_destroy"] = awn["N_AI_hunt_destroy"]
        menu_state = "title_screen"
        SpeedrunMode()

def setting():
    global menu_state
    questions = [
        {
            'type': 'checkbox',
            'message': 'Select settings',
            'name': 'setting',
            'choices': [
                {
                    'name': 'Music',
                    'checked': settings["music"]
                },
                {
                    'name': 'Show AI grid',
                    'checked': settings["show ai grid"]
                }
            ],
        }
    ]

    answers = prompt(questions, style=style)
    ans = []
    for ele in questions[0]["choices"]:
        settings[ele["name"].lower()] = False
    if not answers["setting"] == []:
        for ele in answers["setting"]:
            settings[ele.lower()] = True
    menu_state = "title_screen"

while 1:
    print()
    if menu_state == "title_screen":
        title_screen()
    elif menu_state == "settings":
        setting()
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

        print(menu_state)

        menu_state = "title_screen"
