class Customer(object):
    def __init__(self, id, rating):
        self.id = id
        self.rating = rating

    def __unicode__(self):
        return self.__dict__
