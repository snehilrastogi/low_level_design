import traceback

from auto_assignment import constants
from auto_assignment.services.delivery_executive_service import DeliveryExecutivesService
from auto_assignment.services.delivery_service_utility import DeliveryServiceUtility
from auto_assignment.services.order_service import OrdersService
from auto_assignment.services.strategy.base_strategy import BaseStrategy


class AssignmentStrategyLowFirstMile(BaseStrategy):
    def execute(self, orders_obj_list, de_obj_list):
        print("Executing strategy AssignmentStrategyFirstMile")
        de_orders_assignments = []
        try:
            next_order = OrdersService.get_next_order_as_per_time_elapsed(orders_obj_list)

            while next_order is not None:
                assignment = dict()
                print("Next order.. ", next_order.order_id, "processing")

                free_delivery_executives = DeliveryExecutivesService.fetch_free_delivery_executives(de_obj_list)
                if not free_delivery_executives:
                    print("No delivery executive in FREE STATE")
                    break
                else:
                    assigned_delivery_executive = DeliveryServiceUtility.assign_order_with_low_first_mile(next_order,
                                                                                                          free_delivery_executives)
                    if not assigned_delivery_executive:
                        print("Error while assigning delivery exec for order", next_order.order_id)
                        continue
                    assignment["order_id"] = next_order.order_id
                    assignment["de_id"] = assigned_delivery_executive.de_id
                    print("assignment is ", assignment)
                    de_orders_assignments.append(assignment)
                self.update_objs(next_order, assigned_delivery_executive,
                                 constants.ORDER_STATUSES[constants.DELIVERY_EXECUTIVE_ASSIGNED],
                                 constants.DELIVERY_EXECUTIVE_STATUSES[constants.BUSY])
                next_order = OrdersService.get_next_order_as_per_time_elapsed(orders_obj_list)
            if not next_order:
                print("All pending orders finished")

            print("AssignmentStrategyLowFirstMile --> Assignments:", de_orders_assignments)

        except Exception as e:
            print("Exception in assigning orders to the delivery executives", traceback.format_exc(), e)
