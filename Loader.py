# from __future__ import print_function, unicode_literals
# from pprint import *
# from PyInquirer import *
from Methodes import *
from Ships import *
from random import *
from time import *
loading_errors = []

settings = {
    "music": True,
    "colors": False,
    "N_Players": 0,
    "N_AI_Random": 1,
    "N_AI_hunt_destroy": 1,
    "N_AI_chess": 0,
    "N_AI_heatmap": 0
}

# insert filler names
with open('names.txt', 'r') as f:
    AI_nicknames_list = [line.strip() for line in f]

# if settings["music"] == True:
#     from pygame import

a = 4
try:
    from terminaltables import *
except:
    loading_errors.append("Loader: Couldn't find terminaltable installed. Please install it in the cmd by writing: 'py -m pip install terminaltable'")

try:
    from PyInquirer import *
except:
    loading_errors.append("Loader: Couldn't find PyInquirer installed. Please install it in the cmd by writing: 'py -m pip install PyInquirer'")

if loading_errors != []:
    print("/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("|      Uhm something went wrong...     ")
    print("|                                      ")
    for error in loading_errors:
        print("|" + error)
        print("|                                      ")
    print("\!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  ")

    menu_state = "stop"
else:
    menu_state = "title_screen"
