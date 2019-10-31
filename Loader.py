from __future__ import print_function, unicode_literals
from pprint import *
from PyInquirer import *
from Methodes import *
from Ships import *
from random import *
from time import *
from os import path
from pathlib import Path
#from colorclass import Color, Windows

loading_errors = []

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


settings = {
    "music": True,
    "show ai grid": False,
    "debug mode": False,
    "N_Players": 0,
    "N_AI_Random": 1,
    "N_AI_hunt_destroy": 1,
    "N_AI_chess": 0,
    "N_AI_heatmap": 0
}

style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#ff1474 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#ff1474 bold',
    Token.Question: '',
})

class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end


data_folder = Path(os.path.dirname(__file__), "Data")

name_file_path = data_folder / "names.txt"

# insert filler names
with open(path.join(name_file_path), 'r') as f:
    AI_nicknames_list = [line.strip() for line in f]

# if settings["music"] == True:
#     from pygame import

a = 4
