class IntType(object):
    def __init__(self, name, min_val, max_val):
        self.name = name
        self.min_val = min_val
        self.max_val = max_val

    def __unicode__(self):
        return self.__dict__