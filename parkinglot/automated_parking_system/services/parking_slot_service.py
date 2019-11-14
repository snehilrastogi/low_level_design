import traceback

from automated_parking_system import constants
from automated_parking_system.models.parking_slot import ParkingSlot
from automated_parking_system.services.base_service import BaseService


class ParkingSlotService(BaseService):
    @classmethod
    def initialize_slots(cls, parking_obj):
        try:
            n = len(parking_obj.slots)
            for i in range(0, n):
                parking_obj.slots[i] = ParkingSlot(i+1)
            return parking_obj
        except Exception as e:
            print("Exception in initializing slots ", traceback.print_exc(),
                  e)
            return None

    @classmethod
    def park_car_at_slot(cls, slot_obj, car):
        try:
            slot_obj.set_car(car)
            slot_obj.set_status(constants.FULL)
        except Exception as e:
            print("Exception in initializing parking car at a slot %s ", slot_obj.slot_id,
                  traceback.print_exc(),e)
            raise e

    @classmethod
    def vacate_slot(cls, slot_obj):
        try:
            slot_obj.set_car(None)
            slot_obj.set_status(constants.EMPTY)
        except Exception as e:
            print("Exception in initializing parking car at a slot %s ", slot_obj.slot_id,
                  traceback.print_exc(), e)
            raise e

    @classmethod
    def update_slot_status(cls, slot_obj, status):
        slot_obj.set_status(status)

    @classmethod
    def get_slot_status(cls, slot_obj):
        return slot_obj.status

