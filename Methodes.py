coo_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,

}

class GridOverflowError(Exception):
    """ uhm, that's not in the grid"""

# Python3 program to Split string into characters
def split(word):
    return [char for char in word]

def coordinate_converter(coordinate="", mode="num"):
    if mode == "num":
        coordinate = split(coordinate)
        letters = ""
        numbers = ""
        for element in coordinate: # We separate the letters and numbers
            if 97 <= ord(element) <= 122:  # if string is letter
                aaa = coo_dict[element]
            else:
                numbers = numbers + element

        return (int(numbers), aaa)
    elif mode == "grid":
        if coordinate[1] <= 0 or coordinate[1] >= 11:
            raise GridOverflowError

        aaa = chr(96 + coordinate[1])

    if coordinate[0] <= 0 or coordinate[0] >= 11:
        raise GridOverflowError

    return aaa + str(coordinate[0])


def coordinates_calcs(coordinates, operation, number):
    """
    Calc with coordinates
    :param coordinates: <string> | Coordinates (in lowercase) ex: a1, f5, ...
    :param operation: <string> | "+" or "-"
    :param number: <tupple> | (x, y)
    :return: new coordinates
    """
    coordinates = coordinate_converter(coordinates, "num")
    if operation == "+":
        y_coo = coordinates[1] + number[1]
        x_coo = coordinates[0] + number[0]
        coordinates = (x_coo, y_coo)
    elif operation == "-":
        coordinates = (coordinates[0] - number[0], coordinates[1] - number[1])
    
    return coordinate_converter(coordinates, "grid")
    

def neighbour_cells(coo):
    """
    return the neighbouring cells
    :param coo:
    :return: list, [top, right, down, left]
    """
    top = (0, 1)
    right = (1, 0)
    down = (0, -1)
    left = (-1, 0)
    out = []
    for zz in [top, right, down, left]:
        try:
            out.append(coordinates_calcs(coo, "+", zz))
        except GridOverflowError:
            pass

    return out