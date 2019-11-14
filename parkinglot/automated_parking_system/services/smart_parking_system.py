import traceback

from automated_parking_system import constants
from automated_parking_system.services.parking_service import ParkingService
from automated_parking_system.services.parking_system_service import ParkingSystemService


class SmartParkingSystem(object):
    def __init__(self, num_parking_slots, commands):
        self.num_parking_slots = num_parking_slots
        self.commands = commands
        self.cars_obj_list = []
        self.parking_obj = None

    def run_parking_system(self, ):
        try:
            self.initialize_parking_lot()
            if len(self.commands) < 1:
                print("No commands to execute")
                return
            for cmd in self.commands:
                #print("\nRunning cmd ", cmd)
                try:
                    action = cmd['Action']
                    if action.lower() == constants.PARK.lower():
                        ParkingSystemService.park_car(self.parking_obj, cmd['Registration_num'], cmd['colour'])
                    elif action.lower() == constants.LEAVE.lower():
                        ParkingSystemService.vacate_slot(self.parking_obj, cmd['Slot_id'])
                    elif action.lower() == constants.STATUS_ALLOCATED.lower():
                        ParkingSystemService.print_status_of_allocated_slots(self.parking_obj)
                    elif action.lower() == constants.STATUS_FREE.lower():
                        ParkingSystemService.print_status_of_free_objects(self.parking_obj)
                    else:
                        print("Wrong Command %s", cmd)
                except KeyError:
                    print("Action key not found , wrong command", cmd)
        except Exception as e:
            print("Exception in running the parking system ", traceback.print_exc(), e)

    def initialize_parking_lot(self, ):
        try:
            if self.num_parking_slots == 0:
                print("No parking slots")
                exit()
            self.parking_obj = ParkingService.initialize_parking_for_given_slots(self.num_parking_slots)
        except Exception as e:
            print("Exception in initializing the parking or slots ", traceback.print_exc(), e)
            raise e






