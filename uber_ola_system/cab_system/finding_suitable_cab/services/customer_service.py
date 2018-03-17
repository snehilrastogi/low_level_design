import traceback

from cab_system.finding_suitable_cab.services.base_service import BaseService


class CustomerService(BaseService):
    @classmethod
    def fetch_customer(self, customer_obj_list, customer_name):
        cust_obj = None
        try:
            for customer in customer_obj_list:
                if customer.name == customer_name:
                    cust_obj = customer
                    break

        except Exception as e:
            print("Exception in fetching customer ", customer_name, traceback.format_exc, e)
            raise e
        if cust_obj:
            print("Customer found ", cust_obj.name, "Avg Rating", cust_obj.avg_rating, "Num of trips",
                  cust_obj.num_trips,
                  "Total Rating", cust_obj.rating, "Blacklist Drivers", cust_obj.blacklist_drivers)
        return cust_obj