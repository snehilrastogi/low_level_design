class Elevator:
    def __init__(self, starting_floor, state):
        self.floor = starting_floor
        self.state = state

    def update_floor(self, floor):
        self.floor = floor

    def update_state(self, state):
        self.state = state

    def print_elevator(self):
        print("-----Elevator-----")
        print ("Current Floor", self.floor, "State", self.state)
