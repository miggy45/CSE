class Item(object):
    def __init__(self, name, material):
        self.name = name
        self.material = material


class Tool(Item):
    def __init__(self, name, material, use):
        super(Tool, self).__init__(name, material)
        self.use = use


