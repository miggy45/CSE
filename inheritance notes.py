class vehicle(object):
  def __init__(self, seats, engine_type, turning_mechanism)
      self.seats = seats
      self.engine_type = engine_type
      self.turning_mechanism = turning_mechanism

  def move(self):
          print("you move forward"
  def change_direction(self):
      print("you change direction")

class car(vehicle):
    def __init__(self, seats, horsepower):
        super(car, self).__init__(seats)

