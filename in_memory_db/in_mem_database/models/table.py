class Table(object):
    def __init__(self, name, cols, records=None):
        self.name = name
        self.cols = cols
        self.records= [None]*10

    def __str__(self):
        return self.__dict__
