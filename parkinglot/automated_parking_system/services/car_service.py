import traceback

from automated_parking_system.models.car import Car
from automated_parking_system.services.base_service import BaseService


class CarService(BaseService):

    @classmethod
    def find_if_car_exists_for_reg_num(cls, parking_obj, reg_num):
        try:
            if parking_obj is None:
                print("Parking is not there")
                return False, None
            if len(parking_obj.full_slots) == 0:
                return False, None
            for slot in parking_obj.full_slots:
                if slot.car is not None and slot.car.reg_num.lower() == reg_num.lower():
                    print("found car at slot ", slot.slot_id)
                    return True, slot.slot_id
        except Exception as e:
            print("Exception in finding car for reg num", reg_num, traceback.print_exc(),
                  e)
        return False, None

    @classmethod
    def create_car_obj(cls, reg_num, color):
        return Car(reg_num, color)