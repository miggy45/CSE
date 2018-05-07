class Item(object):
    def __init__(self, name, material, amount):
        self.name = name
        self.material = material
        self.amount = amount


class Tool(Item):
    def __init__(self, name, material, amount, use):
        super(Tool, self).__init__(name, material)
        self.material = material
        self.amount = amount
        self.use = use


class Backpack(Tool):
    def __init__(self, name, material,amount, use):
        super(Backpack, self).__init__(name, material, amount, use)
        self.name = name
        self.material = material
        self.amount = amount
        self.use = use

    def backpack_use(self):
        print("" % self.use)


class Character(object):
    def __init__(self, name, health, status_effects, attack, inventory):

        self.name = name
        self.health = health
        self.status_effects = status_effects
        self.attack = attack
        self.inventory = inventory


    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


victor = Character("Victor", 100, "sleep", 0, ["lantern", "sleeping bag"])

west_house = ("west of house", "north_house", None)


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

