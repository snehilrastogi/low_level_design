from auto_assignment.services.delivery_executive_service import DeliveryExecutivesService
from auto_assignment.services.order_service import OrdersService


class BaseStrategy(object):
    def execute(self, orders_obj_list, de_obj_list):
        print("Base method called")
        raise NotImplementedError("Cannot be implemented")

    def update_objs(self, order, delivery_executive, order_status, de_status):
        OrdersService.update_status(order, order_status)
        DeliveryExecutivesService.update_status(delivery_executive, de_status)
        new_count = (delivery_executive.delivered_count + 1) % 10
        DeliveryExecutivesService.set_delivered_count(delivery_executive, new_count)

        print("Current Order -", order.order_id, order.status, order.customer.id)
        print("Current Delivery Executive", delivery_executive.de_id, delivery_executive.status)
