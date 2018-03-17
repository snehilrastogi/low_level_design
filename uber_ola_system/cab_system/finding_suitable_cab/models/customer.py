class Customer:
    def __init__(self, name, customer_rating_by_driver, blacklist_drivers=None):
        if blacklist_drivers is None:
            blacklist_drivers = []
        self.name = name
        self.rating = customer_rating_by_driver
        self.num_trips = 1
        self.avg_rating = customer_rating_by_driver
        self.blacklist_drivers = blacklist_drivers

    def __unicode__(self):
        return self.__dict__

    def set_avg_rating(self, rating):
        self.rating = rating

    def get_avg_rating(self):
        return self.avg_rating

    def append_blacklist_driver(self, driver_name):
        if not self.blacklist_drivers:

            self.blacklist_drivers = [driver_name]
        else:
            self.blacklist_drivers.append(driver_name)
