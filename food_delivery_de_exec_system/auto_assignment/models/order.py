from auto_assignment import constants
from auto_assignment.utils.datetime_utils import convert_str_to_datetime


class Order(object):
    def __init__(self, id, restaurant_location, order_time, customer):
        self.order_id = id
        self.restaurant_location = restaurant_location
        self.order_time = convert_str_to_datetime(order_time)
        self.status = constants.ORDER_STATUSES[constants.PENDING]
        self.time_elapsed = None
        self.customer = customer

    def __str__(self):
        return self.__dict__

    def set_status(self, status):
        self.status = status
