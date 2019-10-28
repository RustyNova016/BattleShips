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

