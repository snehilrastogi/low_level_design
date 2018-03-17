import traceback

from auto_assignment import constants
from auto_assignment.services.delivery_executive_service import DeliveryExecutivesService
from auto_assignment.services.order_service import OrdersService
from auto_assignment.services.strategy.base_strategy import BaseStrategy


class AssignmentStartegyPremiumCustomer(BaseStrategy):
    def execute(self, orders_obj_list, de_obj_list):
        print("Executing strategy AssignmentStartegyPremiumCustomer")
        de_orders_assignments = []
        try:
            next_order = OrdersService.get_next_order_as_per_customer_rating(orders_obj_list)

            while next_order is not None:
                assignment = dict()
                print("Next order.. ", next_order.order_id, "processing")
                assigned_delivery_executive = DeliveryExecutivesService.fetch_delivery_executives_by_equal_distribution(
                    de_obj_list)
                if not assigned_delivery_executive:
                    print("No delivery executive in FREE STATE")
                    break
                else:
                    assignment["order_id"] = next_order.order_id
                    assignment["de_id"] = assigned_delivery_executive.de_id
                    print("assignment is ", assignment)
                    de_orders_assignments.append(assignment)
                self.update_objs(next_order, assigned_delivery_executive,
                                 constants.ORDER_STATUSES[constants.DELIVERY_EXECUTIVE_ASSIGNED],
                                 constants.DELIVERY_EXECUTIVE_STATUSES[constants.BUSY])
                next_order = OrdersService.get_next_order_as_per_customer_rating(orders_obj_list)
            if not next_order:
                print("All pending orders finished")

            print("AssignmentStartegyPremiumCustomer --> Assignments:", de_orders_assignments)

        except Exception as e:
            print("Exception in assigning orders to the delivery executives", traceback.format_exc(), e)
