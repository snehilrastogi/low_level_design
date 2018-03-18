import random

from elevator_system.models.customer import Customer
from elevator_system.services.base_service import BaseService


class CustomerService(BaseService):
    @classmethod
    def initialize_customer(self, id, total_floors):
        cust_obj = Customer(id)
        start_floor = random.randint(1, total_floors)
        cust_obj.update_current_floor(start_floor)
        return cust_obj

    @classmethod
    def print_customers(cls, cust_obj_list):
        print("Total Customers", len(cust_obj_list))
        for cust_obj in cust_obj_list:
            print("ID --", cust_obj.id, "Current Floor", cust_obj.current_floor)
