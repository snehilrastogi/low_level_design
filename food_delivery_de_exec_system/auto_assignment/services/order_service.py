import datetime
import traceback

from auto_assignment import constants
from auto_assignment.services.base_service import BaseService


class OrdersService(BaseService):
    @classmethod
    def get_next_order_as_per_customer_rating(cls, order_list):
        pending_order_list = []
        next_order = None
        try:
            for order in order_list:
                if order.status == constants.ORDER_STATUSES[constants.PENDING]:
                    OrdersService.update_waiting_time(order)
                    pending_order_list.append(order)
            sorted_by_rating = sorted(pending_order_list, key=lambda order: order.customer.rating, reverse=True)
            for order in sorted_by_rating:
                print("id - ", order.order_id, "rating", str(order.customer.rating))
            if sorted_by_rating:
                next_order = sorted_by_rating[0]
                print("Highest Rated Customer order id - ", next_order.order_id, "rating",
                      str(next_order.customer.rating))

        except Exception as e:
            print("Exception in getting the next order for delivery", e, traceback.format_exc)
        return next_order

    @classmethod
    def get_next_order_as_per_time_elapsed(cls, order_list):
        next_order = None
        pending_order_list = []
        try:
            for order in order_list:
                if order.status == constants.ORDER_STATUSES[constants.PENDING]:
                    OrdersService.update_waiting_time(order)
                    pending_order_list.append(order)
            sorted_order_time_elapsed = sorted(pending_order_list, key=lambda order: order.time_elapsed, reverse=True)
            for order in sorted_order_time_elapsed:
                print("id - ", order.order_id, "time elapsed", str(order.time_elapsed))
            if sorted_order_time_elapsed:
                next_order = sorted_order_time_elapsed[0]
                print("Highest Waiting Time order id - ", next_order.order_id, "time elapsed",
                      str(next_order.time_elapsed))
        except Exception as e:
            print("Exception in getting the next order for delivery", e, traceback.format_exc)
        return next_order

    @classmethod
    def update_waiting_time(cls, obj):
        try:
            obj.time_elapsed = datetime.datetime.now() - obj.order_time
        except Exception as e:
            print("Exception in calculating the waiting time for delivery executive", obj, traceback.format_exc(),
                  e)
            raise e
