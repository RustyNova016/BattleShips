from terminaltables import *
from Methodes import *
from Ships import *
from random import *
from time import *
from Settings import *


class battle_grid:
    def __init__(self):
        # first, we create the dictionayry with the coordinates
        self.grid_dict = {}
        char = "a"
        for ia in range(1, 11):
            for ib in range(1,11):
                self.grid_dict[char + str(ib)] = " "

            char = chr(ord(char) + 1)  # Get the ASCII numbr of char, adding 1, returning to string

        # next we create the grid
        self.grid = ["!!not init!!"]
        self.grid_table = "!!not init!!"
        self.grid_dict_backup = "!!not init!!"

    def grid_dict_change(self, coo, change):
        self.grid_dict[coo] = change

    def update_grid(self):
        """ Update self.grid to reflect the dictionairy. Additionaly update the table"""
        self.grid = [[" ", "1", "2","3", "4","5","6","7","8","9","10"]]
        char = "a"
        for ia in range(1, 11):
            row = [char]
            for ib in range(1, 11):
                row.append(self.grid_dict[char + str(ib)])
            char = chr(ord(char) + 1)
            self.grid.append(row)

        self.grid_table = SingleTable(self.grid)
        self.grid_table.inner_row_border = True

    def __str__(self):
        return self.grid_table.table

    def backup_grid(self):
        self.grid_dict_backup = self.grid_dict.copy()

    def reset_grid_dict(self):
        self.grid_dict = self.grid_dict_backup.copy()
        self.update_grid()


common_grid = battle_grid()
ship_grid = battle_grid()
hit_grid = battle_grid()
ship_list = []

class IA:
    def __init__(self):
        self.cells_hitted = []
        self.cells_left = []
        self.AI_name = "CORE"
        self.AI_nickname = "This message should not appear, oh no..."
        char = "a"
        for ia in range(1, 11):
            for ib in range(1,11):
                self.cells_left.append(char + str(ib))
            char = chr(ord(char) + 1)  # Get the ASCII number of char, adding 1, returning to string

    def guess(self):
        pass

    def recalibration(self, results=""):
        pass


class IA_random(IA):
    def __init__(self):
        IA.__init__(self)
        self.AI_name = "Random IA"
        self.AI_nickname = "Sergeant " + choice(AI_nicknames_list)

    def guess(self):
        try:
            choi = choice(self.cells_left)
            self.cells_hitted.append(choi)
            self.cells_left.remove(choi)
            return choi
        except:
            pass


class IA_hunt_destroy(IA):
    def __init__(self):
        IA.__init__(self)
        self.AI_name = "Hunt & destroy"
        self.AI_nickname = "Major " + choice(AI_nicknames_list)
        self.mode = "hunt"
        self.last_coo = "none"
        self.suspected_cells = []

    def guess(self):
        if self.mode == "hunt":
            choi = choice(self.cells_left)
        else:
            choi = self.nexthit

        if choi == self.last_coo:
            print("warning!!!!! same coo !!!!!!")
        else:
            self.cells_hitted.append(choi)
            self.cells_left.remove(choi)
            self.last_coo = choi
        return choi

    def recalibration(self, results=""):
        # first, cleaning input
        ship_status = ""
        if type(results) == list:
            try:
                ship_status = results[1]
            except:
                ship_status = ""
            results = results[0]

        if ship_status == "destroyed":
            self.mode = "hunt"

        # if results == "retry" or results == "":
        #     # That's not supposed to happen, but it should not interfere with the ia
        #     return
        #
        # ... it interfered

        if results == "water hit":
            if self.mode == "hunt":
                # nothing to do
                return
        elif results == "hit":

            if self.mode == "hunt":
                self.mode = "destroy"

        if self.mode == "destroy":
            if results == "hit":
                self.suspected_cells.extend(neighbour_cells(self.last_coo))

            for hitted in self.cells_hitted:
                try:
                    self.suspected_cells.remove(hitted)
                except:
                    pass

            if self.suspected_cells == []:
                self.mode = "hunt"
            else:
                self.nexthit = self.suspected_cells[0]


def Generate_map():
    ship_list = []
    grid_used = []
    ship_grid = battle_grid()
    common_grid = battle_grid()
    hit_grid = battle_grid()

    def place_random_ship(ship_type):
        global ship
        while 1:
            try:
                pos = chr(96 + randint(1, 10)) + str(randint(1, 10))
                direction = choice(["up", "down", "right", "left"])

                if ship_type == "destroyer":
                    ship = Destroyer(pos, direction)
                elif ship_type == "carrier":
                    ship = Carrier(pos, direction)
                elif ship_type == "cruiser":
                    ship = Cruiser(pos, direction)
                elif ship_type == "battleship":
                    ship = Battleship(pos, direction)
                elif ship_type == "submarine":
                    ship = Submarine(pos, direction)

                overlap = False
                for cells in ship.grid_cells:
                    if cells in grid_used:
                        overlap = True

                if overlap == False:
                    grid_used.extend(ship.grid_cells)

                    if ship_type == "destroyer":
                        for coo in ship.grid_cells:
                            common_grid.grid_dict[coo] = "d"
                            ship_grid.grid_dict[coo] = "d"
                    elif ship_type == "carrier":
                        for coo in ship.grid_cells:
                            common_grid.grid_dict[coo] = "C"
                            ship_grid.grid_dict[coo] = "C"
                    elif ship_type == "cruiser":
                        for coo in ship.grid_cells:
                            common_grid.grid_dict[coo] = "c"
                            ship_grid.grid_dict[coo] = "c"
                    elif ship_type == "battleship":
                        for coo in ship.grid_cells:
                            common_grid.grid_dict[coo] = "b"
                            ship_grid.grid_dict[coo] = "b"
                    elif ship_type == "submarine":
                        for coo in ship.grid_cells:
                            common_grid.grid_dict[coo] = "s"
                            ship_grid.grid_dict[coo] = "s"

                    ship_list.append(ship)
                    break
            except GridOverflowError:
                pass

    place_random_ship("destroyer")
    place_random_ship("carrier")
    place_random_ship("cruiser")
    place_random_ship("battleship")
    place_random_ship("submarine")
    return common_grid, hit_grid, ship_grid, ship_list


def SpeedrunMode():

    # generating the map

    common_grid, hit_grid, ship_grid, ship_list = Generate_map()

    def gamehost(coo):
        # global common_grid, hit_grid, ship_grid

        # 1) valid coordinates?
        # 2) coordinates  already given?
        # 3) is there water?
        #    then, what's the ship to hit?

        try:
            location_data = common_grid.grid_dict[coo]
        except KeyError:
            return ["retry", str(coo) + " isn't a valid coordinate"]

        hit_data = hit_grid.grid_dict[coo]

        if hit_data == "-" or hit_data == "+":
            return ["retry", "already hited"]

        if type(location_data) == str:
            if location_data == " ":
                common_grid.grid_dict_change(coo, "-")
                hit_grid.grid_dict_change(coo, "-")
                return ["water hit"]
            else:
                # Coo are hiting a ship
                # ask all the ships if tey are the one hitted
                # look if he sunk
                # return info

                for ship in ship_list:
                    hit_dectecc = ship.hit_detection(coo)
                    if hit_dectecc[0] == "hit":
                        common_grid.grid_dict_change(coo, ["+", common_grid.grid_dict[coo]])
                        hit_grid.grid_dict[coo] = "+"
                        return hit_dectecc

    # ready to start the game

    common_grid.update_grid()
    ship_grid.backup_grid()
    common_grid.backup_grid()
    hit_grid.update_grid()
    hit_grid.backup_grid()
    scoreboard = []

    player_list = []
    if settings["N_Players"] != 0:
        for i in range(1, settings["N_Players"] + 1):
            player_list.append("Player " + str(i))

    if player_list != []:
        for player in player_list:
            i = 0

            ship_grid.reset_grid_dict()
            hit_grid.reset_grid_dict()
            common_grid.reset_grid_dict()
            for shhip in ship_list:
                shhip.reset()

            print(hit_grid)
            while 1:
                bruh = input("")
                i += 1
                bruh = gamehost(bruh)
                hit_grid.update_grid()
                common_grid.update_grid()
                print(hit_grid)

                if bruh[0] == "water hit":
                    print("Water")
                elif bruh[0] == "retry":
                    print("Invalid coordinates, try again")
                    i += -1
                elif bruh[0] == "hit":
                    if bruh[1] == "operational":
                        print("hit")
                    else:
                        print(bruh[2] + " sunken!")
                #sleep(1)

                gamewon = True
                for shit in ship_list:
                    if shit.status == "operational":
                        gamewon = False

                if gamewon:
                    break

            print("---------------------------------------------------")
            scoreboard.append([player, i])

    IA_list = []
    if settings["N_AI_Random"] != 0:
        for i in range(0, settings["N_AI_Random"]):
            IA_list.append(IA_random())

    if settings["N_AI_hunt_destroy"] != 0:
        for i in range(0, settings["N_AI_hunt_destroy"]):
            IA_list.append(IA_hunt_destroy())

    if IA_list != []:
        for AI in IA_list:
            i = 0

            ship_grid.reset_grid_dict()
            hit_grid.reset_grid_dict()
            common_grid.reset_grid_dict()
            for shhip in ship_list:
                shhip.reset()

            while 1:
                bruh = AI.guess()
                i += 1

                bruh = gamehost(bruh)
                hit_grid.update_grid()
                common_grid.update_grid()
                print(common_grid)
                #rint(hit_grid)

                AI.recalibration(bruh)
                if bruh[0] == "retry":
                    i += -1
                #sleep(1)

                gamewon = True
                for shit in ship_list:
                    if shit.status == "operational":
                        gamewon = False

                if gamewon:
                    break

            print("---------------------------------------------------")
            scoreboard.append([AI.AI_nickname, i])

    def takeSecond(elem):
        return elem[1]
    scoreboard.sort(key=takeSecond)
    scoreboard.insert(0, ["Player name", "Score"])
    scoreboard = SingleTable(scoreboard)
    print(scoreboard.table)
