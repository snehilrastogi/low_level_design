from automated_parking_system import constants


class ParkingSlot(object):
    def __init__(self, slot_id):
        self.slot_id = slot_id
        self.status = constants.PARKING_SLOT_STATUSES[constants.EMPTY]
        self.car = None

    def __str__(self):
        return self.__dict__

    def set_car(self, car_obj):
        self.car = car_obj

    def set_status(self, status):
        self.status = status

