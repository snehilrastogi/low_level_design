import traceback

from cab_system.finding_suitable_cab.services.base_service import BaseService
from cab_system.finding_suitable_cab import constants


class TripService(BaseService):
    @classmethod
    def fetch_driver_based_on_trips(self, trips_obj, customer_obj):
        suitable_driver_list = []
        try:
            for trip in trips_obj:
                if trip.customer.name == customer_obj.name and trip.driver.name not in trip.customer.blacklist_drivers and \
                                trip.customer.name not in trip.driver.blacklist_customers and trip.driver.status == constants.ONLINE:
                    suitable_driver_list.append(trip.driver)
        except Exception as e:
            print("Exception in fetching driver from former trips", customer_obj.name, traceback.format_exc, e)
            raise e

        for driver in suitable_driver_list:
            print("Drivers found ", driver.name, "Avg Rating", driver.avg_rating, "Num of trips",
                  driver.num_trips,
                  "Total Rating", driver.rating, "Blacklist Ciustomers", driver.blacklist_customers, "status",
                  driver.status)
        return suitable_driver_list
