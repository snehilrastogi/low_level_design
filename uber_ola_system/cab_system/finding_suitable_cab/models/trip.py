class Trip:
    def __init__(self, driver, driver_rating_by_customer, customer, customer_rating_by_driver):
        self.customer = customer
        self.driver = driver
        self.customer_rating_by_driver = customer_rating_by_driver
        self.driver_rating_by_customer = driver_rating_by_customer

    def __unicode__(self):
        return self.__dict__
