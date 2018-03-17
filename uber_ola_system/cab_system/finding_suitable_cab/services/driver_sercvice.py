import traceback

from cab_system.finding_suitable_cab.services.base_service import BaseService
from cab_system.finding_suitable_cab import constants


class DriverService(BaseService):
    @classmethod
    def fetch_suitable_driver_for_customer(self, driver_objs_list, customer_obj):
        suitable_driver_list = []
        try:
            for driver in driver_objs_list:
                if driver.avg_rating >= customer_obj.avg_rating and customer_obj.name not in driver.blacklist_customers and \
                                driver.name not in customer_obj.blacklist_drivers and driver.status == constants.ONLINE:
                    suitable_driver_list.append(driver)
        except Exception as e:
            print("Exception in fetching driver ", customer_obj.name, traceback.format_exc, e)
            raise e
        for driver in suitable_driver_list:
            print("Drivers found ", driver.name, "Avg Rating", driver.avg_rating, "Num of trips",
                  driver.num_trips,
                  "Total Rating", driver.rating, driver.blacklist_customers)
        return suitable_driver_list

    @classmethod
    def set_status(self, driver_obj, status):
        driver_obj.update_status(status)

    @classmethod
    def fetch_driver(self, driver_obj_list, driver_name):
        driver_obj = None
        try:
            for driver in driver_obj_list:
                if driver.name == driver_name:
                    driver_obj = driver
                    break

        except Exception as e:
            print("Exception in fetching customer ", driver_name, traceback.format_exc, e)
            raise e
        if driver_obj:
            print("Driver found ", driver_obj.name, "Avg Rating", driver_obj.avg_rating, "Num of trips",
                  driver_obj.num_trips,
                  "Total Rating", driver_obj.rating, "Blacklist", driver_obj.blacklist_customers, "status", driver.status)
        return driver_obj
