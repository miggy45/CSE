# defining a class
class Shoes(object):
    def __init__(self, lace_color, lighting, brand):    #TWO underscores before and after.
        # things a shoe has
        self.lace_color = lace_color
        self.rgb_lighting = lighting
        self.used = False
        self.brand = brand
        self.clean = True

    def wear(self):
        self.used = True
        self.clean =True
        print("you wear the shoes")

    def wash(self):
        self.clean = True
        print("you clean the shoes")


first_pair = Shoes("red",True,"jordan")
second_pair = Shoes("pink", False, "sketchers")

print(first_pair.brand)
print(second_pair.lace_color)
print(first_pair.clean)

first_pair.wear()
print(first_pair.clean)



class car(object):
    def __init__(self, color, name, model, horsepower):
        self.name = name
        self.color = color
        self.model = model
        self.hp =horsepower
        self.running = False
        self.passengers = 0


    def drive_forward(self):
        if self.running:
            print("you move forward.")
        else:
            print("nothing happens.")

    def turn_on(self):
        if  self.running:
            print("nothing happens.")

    def turn_off(self):
        if self.running:
            self.running = False
            print("car is off ")
        else:
            print("nothing happens")

    def go_for_drive(self, passengers):
        print("%d passengers get in"% passengers)
        self.passengers = passengers
        self.turn_on()
        self.drive_forward()
        self.drive_forward()
        self.drive_forward()
        self.turn_off()
        print("%d passengers get out" % passengers)
        self.passengers = 0


My_car = car("red", "tesla", "x", "9,001")
My_car.go_for_drive(1)

