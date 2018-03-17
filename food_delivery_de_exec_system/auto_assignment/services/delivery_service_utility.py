import traceback

from auto_assignment import constants
from auto_assignment.utils.calculate_haversine_distance import CalculateHaversineDistance


class DeliveryServiceUtility(object):
    @classmethod
    def assign_order_with_low_first_mile(self, order, free_delivery_executives):
        low_first_mile = constants.LOW_FIRST_MILE
        assigned_delivery_executive = None
        print("For order -- ", order.order_id)
        try:
            for de in free_delivery_executives:
                haversine_distance = CalculateHaversineDistance.calculate(order.restaurant_location,
                                                                          de.delivery_executive_location)
                print("with de", de.de_id, " haversine_distance is --", haversine_distance)
                if haversine_distance < low_first_mile:
                    low_first_mile = haversine_distance
                    assigned_delivery_executive = de
            print("lowest Distance", low_first_mile)
        except Exception as e:
            print("Exception in assigning order", e, traceback.format_exc)
        return assigned_delivery_executive
