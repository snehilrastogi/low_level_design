from elevator_system import constants
from elevator_system.models.elevator import Elevator
from elevator_system.services.base_service import BaseService
from elevator_system.services.elevator_utility import ElevatorUtility


class ElevatorService(BaseService):
    @classmethod
    def initialize_elevator(cls, starting_floor):
        elevator_obj = Elevator(starting_floor, constants.ON)
        elevator_obj.print_elevator()
        return elevator_obj

    @classmethod
    def move_elevator(cls, requests_data, elevator_obj):
        """
        We are serving as per the request - not taking requests in between -- taking one request at a time -
        can be extended to that
        :param requests_data:
        :param elevator_obj:
        :return:
        """
        if elevator_obj.state == constants.ON:
            for req in requests_data:
                print ("Current Request--", req['status'], req['dest_floor'], "<", req['cust_obj'].id,
                       req['cust_obj'].current_floor, ">")
                if req['status'] == constants.PENDING:
                    cust_obj = req["cust_obj"]
                    dest_floor = req["dest_floor"]
                    if cust_obj.current_floor == dest_floor:
                        print(
                            "current floor", cust_obj.current_floor, "same as destination", dest_floor,
                            "No need for elevator")
                        continue
                    else:
                        direction = ElevatorUtility.calculate_direction(cust_obj.current_floor, dest_floor)
                        source = cust_obj.current_floor
                        ElevatorService.print_movements(source, dest_floor, cust_obj, direction, elevator_obj)
                        req['status'] = constants.COMPLETED
                else:
                    print ("Request ", req, "already served")
        else:
            print("ELEVATOR OUT OF ORDER.. SAD")

    @classmethod
    def print_movements(cls, source, dest, customer_obj, direction, elevator_obj):
        print("Elevator Current Position", elevator_obj.floor)
        # this shows the elevator movement to go to the source floor to take the customer
        elevator_before_direction = ElevatorUtility.calculate_direction(elevator_obj.floor, source)

        if elevator_before_direction == constants.NO_MOVEMENT:
            print ("Lift already on same floor .. opening for customer", customer_obj.id, "customer rode elevator")
            print("Now elevator moving in ", direction, "direction covering...")
            print("From ", source, "to", dest)
            if direction == constants.UP:
                for x in range(source, dest + 1):
                    print (x, ".....",)
            else:
                for x in reversed(range(dest, source+1)):
                    print (x, ".....",)
            print ("reached at destination", dest)
            customer_obj.update_current_floor(dest)
            elevator_obj.update_floor(dest)
            print ("Updated_customer")
            customer_obj.print_customer()
            print("Updated Elevator")
            elevator_obj.print_elevator()
            return

        if elevator_before_direction == constants.UP:
            print("to serve current request .. elevator needs to move", elevator_before_direction)
            print("Elevator moving to", source, "covering")
            for x in range(elevator_obj.floor, source + 1):
                print(x, "........",)
            print("Elevator Reached at", source, "customer", customer_obj.id, "boarding")
            print("To take the customer to the destination")
            print("Now elevator moving in ", direction, "direction covering...")
            print("From ", source, "to", dest)
            if direction == constants.UP:
                for x in range(source, dest + 1):
                    print (x, ".....",)
            else:
                for x in reversed(range(dest, source+1)):
                    print (x, ".....",)
            print ("reached at destination", dest)
            customer_obj.update_current_floor(dest)
            elevator_obj.update_floor(dest)
            print ("Updated_customer")
            customer_obj.print_customer()
            print("Updated Elevator")
            elevator_obj.print_elevator()
            return

        if elevator_before_direction == constants.DOWN:
            print("to serve current request .. elevator needs to move", elevator_before_direction)
            print("Elevator moving to", source, "covering")
            for x in reversed(range(source,elevator_obj.floor+1)):
                print(x, "........",)
            print("Elevator Reached at", source, "customer", customer_obj.id, "boarding")
            print("To take the customer to the destination")
            print("Now elevator moving in ", direction, "direction covering...")
            if direction == constants.UP:
                for x in range(source, dest + 1):
                    print (x, ".....",)
            else:
                for x in reversed(range(dest, source+1)):
                    print (x, ".....",)
            print ("reached at destination", dest)
            customer_obj.update_current_floor(dest)
            elevator_obj.update_floor(dest)
            print ("Updated_customer")
            customer_obj.print_customer()
            print("Updated Elevator")
            elevator_obj.print_elevator()
            return
