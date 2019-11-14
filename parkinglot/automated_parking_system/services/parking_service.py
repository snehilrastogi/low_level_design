import traceback

from automated_parking_system import constants
from automated_parking_system.models.parking import Parking
from automated_parking_system.services.base_service import BaseService
from automated_parking_system.services.car_service import CarService
from automated_parking_system.services.parking_slot_service import ParkingSlotService


class ParkingService(BaseService):
    @classmethod
    def initialize_parking_for_given_slots(cls, num_of_slots):
        try:
            parking_obj = Parking(num_of_slots)
            if parking_obj is None:
                print("Parking object is None")
                return
            print("Created a parking for", num_of_slots, "slots")
            parking_obj = ParkingSlotService.initialize_slots(parking_obj)
            for slot in parking_obj.slots:
                parking_obj.append_to_empty_slots(slot)
            if parking_obj is None:
                raise Exception
            return parking_obj
        except Exception as e:
            print("Exception in creating parking with given num of slots %s", num_of_slots,
                  traceback.print_exc(), e)
            raise e

    @classmethod
    def get_slot(cls, parking_obj, slot_num):
        try:
            return parking_obj.slots[slot_num-1]
        except Exception as e:
            print("exception in getting slot from parking for ", slot_num, traceback.print_exc(), e)
            raise e

    @classmethod
    def park_the_car(cls, parking_obj, empty_slot_obj, car_obj):
        try:
            car_exists, slot_id = CarService.find_if_car_exists_for_reg_num(parking_obj, car_obj.reg_num)
            if car_exists and slot_id is not None:
                print("Wrong Car Registration Number as same car already exists in parking at slot", slot_id)
                return
            cls.remove_from_empty_slots(empty_slot_obj, parking_obj)
            ParkingSlotService.park_car_at_slot(empty_slot_obj, car_obj)
            parking_obj.slots[empty_slot_obj.slot_id - 1] = empty_slot_obj
            ParkingService.add_to_full_slots(empty_slot_obj, parking_obj)
            print("Allocated Slot Number ", empty_slot_obj.slot_id)
        except Exception as e:
            print("exception in parking the car ", traceback.print_exc(), e)
            raise e

    @classmethod
    def leave_the_car(cls, parking_obj, slot_obj):
        try:
            if ParkingSlotService.get_slot_status(slot_obj).lower() == constants.EMPTY.lower():
                print("Already empty slot -- cannot vacate")
                return
            cls.remove_from_full_slots(slot_obj, parking_obj)
            ParkingSlotService.vacate_slot(slot_obj)
            parking_obj.slots[slot_obj.slot_id - 1] = slot_obj
            cls.add_to_empty_slots(slot_obj, parking_obj)
            print("Slot number ", slot_obj.slot_id, " is freed")
        except Exception as e:
            print("exception in the process of car leaving the parking", traceback.print_exc(), e)
            raise e

    @classmethod
    def add_to_full_slots(cls, slot_obj, parking_obj):
        try:
            if slot_obj is None or parking_obj is None:
                print("Slot or parking object is none, cannot be added to full slots")
                return
            if len(parking_obj.full_slots) == len(parking_obj.slots):
                print("Already full slots", len(parking_obj.full_slots),"== total slots available:",
                      len(parking_obj.slots)," cant add any more slots")
                return
            parking_obj.append_to_full_slots(slot_obj)
        except Exception as e:
            print("Exception in adding slot to list of free slots", traceback.print_exc(), e)
            raise e

    @classmethod
    def remove_from_full_slots(cls, slot_obj, parking_obj):
        try:
            if slot_obj is None or parking_obj is None:
                print("Slot or parking object is none, cannot be removed from free slots")
                return
            if len(parking_obj.full_slots) == 0:
                print("Already full slots are 0, cant remove further")
                return
            num_full_slots = len(parking_obj.full_slots)
            i = 0
            for i in range(num_full_slots):
                if slot_obj.slot_id == parking_obj.full_slots[i].slot_id:
                    del parking_obj.full_slots[i]
                    break
            if i == num_full_slots:
                print("No slot with id ", slot_obj.slot_id, "exists in full slots list")
                return
            ParkingSlotService.update_slot_status(parking_obj.slots[slot_obj.slot_id - 1], constants.NEITHER)
        except Exception as e:
            print("Exception in adding slot to list of free slots", traceback.print_exc(), e)
            raise e

    @classmethod
    def add_to_empty_slots(cls, slot_obj, parking_obj):
        try:
            if slot_obj is None or parking_obj is None:
                print("Slot or parking object is none, cannot be added to free slots")
                return
            if len(parking_obj.empty_slots) == len(parking_obj.slots):
                print("Already empty slots", len(parking_obj.empty_slots), "== total slots available:",
                      len(parking_obj.slots), " cant add any more slots")
                return
            parking_obj.append_to_empty_slots(slot_obj)
        except Exception as e:
            print("Exception in adding slot to list of free slots", traceback.print_exc(), e)
            raise e

    @classmethod
    def remove_from_empty_slots(cls, slot_obj, parking_obj):
        try:
            if slot_obj is None or parking_obj is None:
                print("Slot or parking object is none, cannot be added to free slots")
                return
            if len(parking_obj.empty_slots) == 0:
                print("Already empty slots are 0, cant remove further")
                return
            i = 0
            num_empty_slots = len(parking_obj.empty_slots)
            for i in range(num_empty_slots):
                if slot_obj.slot_id == parking_obj.empty_slots[i].slot_id:
                    del parking_obj.empty_slots[i]
                    break
            if i == num_empty_slots:
                print("No slot with id ", slot_obj.slot_id, "exists in empty slots list")
                return
            ParkingSlotService.update_slot_status(parking_obj.slots[slot_obj.slot_id - 1], constants.NEITHER)
        except Exception as e:
            print("Exception in adding slot to list of free slots", traceback.print_exc(), e)
            raise e

    @classmethod
    def get_first_free_parking_slot(cls, parking_obj):
        try:
            if len(parking_obj.empty_slots) == 0:
                return None
            return parking_obj.empty_slots[0]
        except Exception as e:
            print("Exception in getting first free parking slot ", traceback.print_exc(), e)
            return None

    @classmethod
    def print_full_slots(cls, parking_obj):
        try:
            if parking_obj is None:
                print("No parking initialized as of now")
                return
            if len(parking_obj.full_slots) == 0:
                print("No Full slots")
                return
            print("Slot No\t\t\t Registration\t\t\t\t Color")
            for i in range(len(parking_obj.full_slots)):
                slot_obj = parking_obj.full_slots[i]
                print(slot_obj.slot_id, "\t\t\t\t", slot_obj.car.reg_num, "\t\t\t\t", slot_obj.car.color)
        except Exception as e:
            print("Exception in print_full_slots_status ", traceback.print_exc(),e)
            raise e

    @classmethod
    def print_empty_slots(cls, parking_obj):
        try:
            if parking_obj is None:
                print("No parking initialized as of now")
                return
            if len(parking_obj.empty_slots) == 0:
                print("No Empty Slots")
                return
            print("Empty Slots")
            for i in range(len(parking_obj.empty_slots)):
                print(parking_obj.empty_slots[i].slot_id)
        except Exception as e:
            print("Exception in print_full_slots_status ", traceback.print_exc(), e)
            raise e

