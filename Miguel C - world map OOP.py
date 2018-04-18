class Room(object):
    def __init__(self, name, north, description, east, west, south):
        self.name = name
        self.north = north
        self.description = description
        self.east = east
        self.west = west
        self.south = south


    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize rooms
west_house = Room("west of house", 'north_house')

room1= Room("BACKDOOR", "OUTSIDE", "the backdoor of the store was green with a exit sign looming over it, it slid open",
            None, None,"TOOLROOM")
while True:
    print(current_node.name)
    if Command == 'quite':

       quit(0)
