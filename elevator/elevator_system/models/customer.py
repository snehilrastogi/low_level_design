class Customer:
    def __init__(self, id):
        self.id = id
        self.current_floor = -1

    def update_current_floor(self, current_floor):
        self.current_floor = current_floor
        return self

    def print_customer(self):
        print ("ID", self.id, "Current Floor", self.current_floor)

    def __unicode__(self):
        self.print_customer()