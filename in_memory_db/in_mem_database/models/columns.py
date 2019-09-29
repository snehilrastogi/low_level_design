class Columns(object):
    def __init__(self, name, type, constraint=None):
        self.name = name
        self.type = type
        self.constraint = constraint

    def __str__(self):
        return self.__dict__
