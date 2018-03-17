import random

from auto_assignment import constants
from auto_assignment.utils.datetime_utils import convert_str_to_datetime


class DeliveryExecutive(object):
    def __init__(self, id, de_location, last_delivery_time):
        self.de_id = id
        self.delivery_executive_location = de_location
        self.last_delivery_time = convert_str_to_datetime(last_delivery_time)
        self.status = constants.DELIVERY_EXECUTIVE_STATUSES[constants.FREE]
        self.waiting_time = None
        self.delivered_count = random.randint(0, 10)

    def __str__(self):
        return self.__dict__

    def set_status(self, status):
        self.status = status

    def set_delivered_count(self, count):
        self.delivered_count = count
