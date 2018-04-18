class Character(object):
    def __init__(self, name, health, status_effects, attack, inventory):
        self.name = name
        self.health = health
        self.status_effects = status_effects
        self.attack = attack
        self.inventory = inventory

Character("Victor", 100, "strength, speed", "knife, weapons","sleep, lanturn, sleeping bag")
