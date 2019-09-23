from smart_home_mgmt import constants

class PROPSMD:
    def __init__(self, id, name, min_val, max_val):
        self.id = id
        self.name = name
        self.min_val = min_val
        self.max_val = max_val

    def __str__(self):
        return "id :{}, name: {}, min_val: {}, max_val {}".format(
            self.id, self.name, self.min_val,
            self.max_val)

    def __repr__(self):
        return self.__str__()