class StringType(object):
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def __unicode__(self):
        return self.__dict__
