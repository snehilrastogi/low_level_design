from elevator_system.services.building_service import BuildingService
from elevator_system.services.customer_service import CustomerService
from elevator_system.services.elevator_service import ElevatorService
from elevator_system.services.elevator_utility import ElevatorUtility


class RunElevatorSystem:
    def __init__(self, total_floors, total_customers, starting_floor, num_requests=10):
        self.total_floors = total_floors
        self.total_customers = total_customers
        self.starting_floor = starting_floor
        self.num_requests = num_requests
        self.customers_objs_list = []
        self.building_obj = None
        self.elevator_obj = None

    def run_elevator_system(self, ):
        self.initialize()
        ElevatorService.move_elevator(self.requests_data, self.elevator_obj)

    def initialize(self, ):
        print("Total floors", self.total_floors)
        for i in range(self.total_customers):
            cust_obj = CustomerService.initialize_customer(i + 1, self.total_floors)
            self.customers_objs_list.append(cust_obj)
        CustomerService.print_customers(self.customers_objs_list)
        self.elevator_obj = ElevatorService.initialize_elevator(self.starting_floor)
        self.building_obj = BuildingService.initialize_building(self.total_floors, self.customers_objs_list,
                                                                self.elevator_obj)
        self.requests_data = ElevatorUtility.gen_requests(self.customers_objs_list, self.total_floors,
                                                          self.num_requests)
