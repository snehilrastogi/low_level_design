import random
#from set import Set

from elevator_system import constants
from elevator_system.services.customer_service import CustomerService


class ElevatorUtility:
    """
    class -A utility to generate requests using random - there could be better ways :/
    """

    @classmethod
    def gen_requests(cls, cust_obj_list, total_floors, num_requests=10):
        requests_data = []
        cust_id_set = set()
        i = 0
        keep_looping = False
        while (not keep_looping):
            cust_index = random.randint(0, len(cust_obj_list) - 1)
            cust_id_set.add(cust_index + 1)
            cust_obj = cust_obj_list[cust_index]
            dest_floor = ElevatorUtility.fetch_start_and_end_floor(total_floors)
            d = {"cust_obj": cust_obj, "dest_floor": dest_floor, "status": constants.PENDING}
            requests_data.append(d)
            i += 1
            if i > num_requests * 2:
                break
            keep_looping = ElevatorUtility.check_if_atleast_one_req_for_all_customers(cust_id_set, len(
                cust_obj_list))

        print("Updated customers")
        CustomerService.print_customers(cust_obj_list)
        print("Requests--")
        for req in requests_data:
            print(
                "Customer - (id ", req["cust_obj"].id, "current floor", req["cust_obj"].current_floor,
                ") Destination -- ", req["dest_floor"])
        # print(requests_data)
        return requests_data

    @classmethod
    def check_if_atleast_one_req_for_all_customers(cls, cust_id_set, len_cust_obj_list):
        # print("len(cust_id_set)", len(cust_id_set), cust_id_set)
        if len(cust_id_set) == 0:
            return True
        for i in range(1, len_cust_obj_list + 1):
            # print ("set i", i)
            if i not in cust_id_set:
                return False
        return True

    @classmethod
    def fetch_start_and_end_floor(cls, total_floors):
        # start_floor = cust_obj.current_floor
        end_floor = random.randint(1, total_floors)
        # while start_floor == end_floor:
        #     start_floor = random.randint(1, total_floors)
        #     end_floor = random.randint(1, total_floors)
        # return start_floor, end_floor
        return end_floor

    @classmethod
    def calculate_direction(cls, start_floor, dest_floor):

        if start_floor < dest_floor:
            direction = constants.DIRECTIONS[constants.UP]
        elif start_floor > dest_floor:
            direction = constants.DIRECTIONS[constants.DOWN]
        else:
            direction = constants.DIRECTIONS[constants.NO_MOVEMENT]
        return direction
