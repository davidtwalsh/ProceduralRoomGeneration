from enum import Enum

class Endpoint:
    def __init__(self,row,col,room,layout):
        self.row = row
        self.col = col
        self.room = room
        self.layout = layout
        self.properties = []


class EndpointProperties(Enum):
    ISCELLHALLWAY = 1




