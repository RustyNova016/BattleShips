from Methodes import *


class Ship:
    def __init__(self, size, head_coordinates, direction):
        self.ship_name = "CORE"
        self.size = size
        self.grid_cells = [head_coordinates]
        if direction == "up":
            partoffset = (0, 1)
        elif direction == "down":
            partoffset = (0, -1)
        elif direction == "right":
            partoffset = (-1, 0)
        elif direction == "left":
            partoffset = (1, 0)
        else:
            partoffset = "!!!not init!!!"

        writer = head_coordinates
        for i in range(2, self.size + 1):
            calcs = coordinates_calcs(writer, "+", partoffset)
            self.grid_cells.append(calcs)
            writer = coordinates_calcs(writer, "+", partoffset)

        self.hit_cells = []
        self.status = "operational"

    def hit_detection(self, hit_coo):
        if hit_coo in self.grid_cells:
            self.hit_cells.append(hit_coo)
            if self.hit_cells.__len__() == self.grid_cells.__len__():
                self.status = "destroyed"

            out = ["hit", self.status]
            if self.status == "destroyed":
                out.append(self.ship_name)

            return out
        else:
            return ["not hit"]

    def reset(self):
        self.hit_cells = []
        self.status = "operational"


class Destroyer(Ship):
    def __init__(self, head_coordinates, directiontest):
        Ship.__init__(self, 2, head_coordinates, directiontest)
        self.ship_name = "Destroyer"


class Carrier(Ship):
    def __init__(self, head_coordinates, direction):
        Ship.__init__(self, 5, head_coordinates, direction)
        self.ship_name = "Carrier"


class Battleship(Ship):
    def __init__(self, head_coordinates, direction):
        Ship.__init__(self, 4, head_coordinates, direction)
        self.ship_name = "Battleship"


class Cruiser(Ship):
    def __init__(self, head_coordinates, direction):
        Ship.__init__(self, 3, head_coordinates, direction)
        self.ship_name = "Cruiser"


class Submarine(Ship):
    def __init__(self, head_coordinates, direction):
        Ship.__init__(self, 3, head_coordinates, direction)
        self.ship_name = "Submarine"
