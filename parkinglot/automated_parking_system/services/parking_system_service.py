import traceback

from automated_parking_system.services.base_service import BaseService
from automated_parking_system.services.car_service import CarService
from automated_parking_system.services.parking_service import ParkingService


class ParkingSystemService(BaseService):
    @classmethod
    def park_car(cls, parking_obj, reg_num, color):
        try:
            if parking_obj is None:
                print("Parking not initialized")
                return
            empty_slot_obj = ParkingService.get_first_free_parking_slot(parking_obj)
            if empty_slot_obj is None:
                print("Sorry, Parking Lot is Full")
                return
            car_obj = CarService.create_car_obj(reg_num, color)
            ParkingService.park_the_car(parking_obj, empty_slot_obj, car_obj)
        except Exception as e:
            print("Exception in parking the car", traceback.print_exc(), e)

    @classmethod
    def vacate_slot(cls, parking_obj, slot_num):
        try:
            if parking_obj is None:
                print("Parking not initialized")
                return
            if slot_num > len(parking_obj.slots) or slot_num <= 0:
                print("Wrong slot number ", slot_num, "only ", len(parking_obj.slots), "are available starting from 1")
                return
            slot_obj = ParkingService.get_slot(parking_obj, slot_num)
            if slot_obj is None:
                print("Slot object for ", slot_num, "is None")
            ParkingService.leave_the_car(parking_obj, slot_obj)
        except Exception as e:
            print("Exception in vacating slot", slot_num, traceback.print_exc(), e)

    @classmethod
    def print_status_of_allocated_slots(cls, parking_obj):
        try:
            if parking_obj is None:
                print("Parking not initialized")
                return
            ParkingService.print_full_slots(parking_obj)
        except Exception as e:
            print("Exception in printing status of allocated slots", traceback.print_exc(), e)

    @classmethod
    def print_status_of_free_objects(cls, parking_obj):
        try:
            if parking_obj is None:
                print("Parking not initialized ")
                return
            ParkingService.print_empty_slots(parking_obj)
        except Exception as e:
            print("Exception in printing empty slots", traceback.print_exc(), e)
            return