import traceback

from cab_system.finding_suitable_cab.models.customer import Customer
from cab_system.finding_suitable_cab.models.driver import Driver
from cab_system.finding_suitable_cab.models.trip import Trip
from cab_system.finding_suitable_cab.services.find_cab_service import FindCabService


class CabAssignmentSystem(object):
    def __init__(self, trips, input_data):
        self.trips = trips
        self.input_data = input_data
        self.driver_objs = []
        self.customer_objs = []
        self.trip_objs = []

    def run_cab_system(self, ):
        try:
            # print(self.driver_objs)
            self.initialize()
            self.find_cabs()
            #
            # ### EXTENSION ###
            print("make few offline")
            driver_names = ["d2"]
            for driver_name in driver_names:
                FindCabService.update_drivers_statuses(self.driver_objs, driver_name)

            self.find_cabs()

        except Exception:
            print("Exception in running the cab system", traceback.format_exc)

    def find_cabs(self):
        for cust_name in self.input_data:
            try:
                FindCabService.execute(self.driver_objs, self.customer_objs, self.trip_objs, cust_name)
            except Exception as e:
                print("Exception in fetching data for customer", cust_name, e, traceback.format_exc)

    def initialize(self, ):
        """
        initializing the data
        :return:
        """
        for trip in self.trips:
            driver = self.fetch_driver_obj(trip['driver_name'], trip['driver_rating_by_customer'],
                                           trip['customer_name'], trip['customer_rating_by_driver'])
            customer = self.fetch_customer_obj(trip['driver_name'], trip['driver_rating_by_customer'],
                                               trip['customer_name'], trip['customer_rating_by_driver'])
            trip_obj = Trip(driver, trip['driver_rating_by_customer'],
                            customer, trip['customer_rating_by_driver'])
            self.trip_objs.append(trip_obj)

    def fetch_driver_obj(self, driver_name, driver_rating_by_customer, customer_name, customer_rating_by_driver):
        found = False
        driver_obj = None
        for driver in self.driver_objs:
            if driver.name == driver_name:
                found = True
                driver.num_trips += 1
                driver.rating += float(driver_rating_by_customer)
                driver.avg_rating = float(driver.rating / driver.num_trips)
                # driver.avg_rating = format(avg_rating, 2)
                driver.avg_rating = float("{0:.2f}".format(driver.avg_rating))
                if customer_rating_by_driver == 1:
                    driver.append_blacklist_customer(customer_name)
                driver_obj = driver
                break

        if not found:
            driver_obj = Driver(driver_name, driver_rating_by_customer)
            if customer_rating_by_driver == 1:
                driver_obj.append_blacklist_customer(customer_name)
            self.driver_objs.append(driver_obj)

        print("Drivers saved ", driver_obj.name, "Avg Rating", driver_obj.avg_rating, "Num of trips",
              driver_obj.num_trips,
              "Total Rating", driver_obj.rating, "Blacklist Customers", driver_obj.blacklist_customers, "status",
              driver_obj.status)
        return driver_obj

    def fetch_customer_obj(self, driver_name, driver_rating_by_customer, customer_name, customer_rating_by_driver):
        found = False
        customer_obj = None
        for customer in self.customer_objs:
            if customer.name == customer_name:
                found = True
                customer.num_trips += 1
                customer.rating += float(customer_rating_by_driver)
                customer.avg_rating = float(customer.rating / customer.num_trips)
                customer.avg_rating =  float("{0:.2f}".format(customer.avg_rating))
                # customer.avg_rating = format(avg_rating, 2)
                if driver_rating_by_customer == 1:
                    customer.append_blacklist_driver(driver_name)
                customer_obj = customer
                break

        if not found:
            customer_obj = Customer(customer_name, customer_rating_by_driver)
            if driver_rating_by_customer == 1:
                print ("IN here - blacklist check")
                customer_obj.append_blacklist_driver(driver_name)
            self.customer_objs.append(customer_obj)

        print("Customer saved ", customer_obj.name, "Avg Rating", customer_obj.avg_rating, "Num of trips",
              customer_obj.num_trips,
              "Total Rating", customer_obj.rating, "Blacklist Drivers", customer_obj.blacklist_drivers)

        return customer_obj
