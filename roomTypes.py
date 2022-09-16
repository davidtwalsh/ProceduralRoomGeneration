from enum import Enum
from pickle import EMPTY_DICT
import colors

class Room(Enum):
    SPAWN = 1
    HALLWAY = 2
    CELL = 3

        


class RoomColors:

    roomColors = {
        Room.SPAWN : colors.WHITE,
        Room.HALLWAY : colors.RED,
        Room.CELL : colors.GREEN
    }

class RoomLayout(Enum):
    VERTICAL = 1
    HORIZONTAL = 2
