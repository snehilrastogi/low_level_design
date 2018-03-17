from cab_system.finding_suitable_cab import constants


class Driver:
    def __init__(self, name, driver_rating_by_customer, blacklist_customers=None):
        if blacklist_customers is None:
            blacklist_customers = []
        self.name = name
        self.rating = driver_rating_by_customer
        self.num_trips = 1
        self.status = constants.DRIVER_STATUS[constants.ONLINE]
        self.avg_rating = driver_rating_by_customer
        self.blacklist_customers = blacklist_customers

    def __unicode__(self):
        return self.__dict__


    def update_status(self, status):
        self.status = status

    def get_avg_rating(self):
        return self.avg_rating

    def append_blacklist_customer(self, customer_name):
        if not self.blacklist_customers:
            self.blacklist_customers = [customer_name]
        else:
            self.blacklist_customers.append(customer_name)
