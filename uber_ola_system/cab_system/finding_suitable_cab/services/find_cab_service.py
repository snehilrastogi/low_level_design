import traceback

from cab_system.finding_suitable_cab.services.customer_service import CustomerService
from cab_system.finding_suitable_cab.services.driver_sercvice import DriverService
from cab_system.finding_suitable_cab.services.trip_service import TripService
from cab_system.finding_suitable_cab import constants


class FindCabService(object):
    @classmethod
    def execute(self, driver_objs_list, customer_objs_list, trip_objs_list, customer_name):
        if not trip_objs_list:
            print("NO TRIPS")
            return
        customer = CustomerService.fetch_customer(customer_objs_list, customer_name)
        if not customer:
            print("No customer with name ", customer_name, "exists")
            return
        avg_rating = CustomerService.fetch_avg_rating(customer)
        if avg_rating == 0.0:
            return

        if not driver_objs_list:
            print("No driver exists")
            return

        drivers_list = DriverService.fetch_suitable_driver_for_customer(driver_objs_list, customer)
        if not drivers_list:
            print("No suitable match with avg rating for customer", customer_name, "find using trips")
            drivers_list = TripService.fetch_driver_based_on_trips(trip_objs_list, customer)

        if not drivers_list:
            print("No suitable driver for customer", customer.name)
        else:
            FindCabService.print_result(drivers_list, customer)

    #### EXTENSION ###

    @classmethod
    def update_drivers_statuses(cls, driver_objs_list, driver_name):
        driver = DriverService.fetch_driver(driver_objs_list, driver_name)
        if not driver:
            print("No such driver exists")
            return
        DriverService.set_status(driver, constants.DRIVER_STATUS[constants.OFFLINE])

    @classmethod
    def print_result(cls, drivers_list, customer):
        try:
            print("For customer -- ", customer.name, "Avg Rating --", customer.avg_rating)
            for driver in drivers_list:
                print("Name --", driver.name, "Avg Rating --", driver.avg_rating)
        except:
            print("Exception in print", traceback.format_exc)
