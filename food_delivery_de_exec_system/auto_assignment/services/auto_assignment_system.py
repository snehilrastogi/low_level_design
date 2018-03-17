from auto_assignment import constants
from auto_assignment.models.customer import Customer
from auto_assignment.models.delivery_executive import DeliveryExecutive
from auto_assignment.models.order import Order
from auto_assignment.services.strategy.strategy_factory import StrategyFactory


class AutoAssignmentSystem(object):
    def __init__(self, orders, delivery_executives):
        self.orders = orders
        self.delivery_executives = delivery_executives
        self.orders_obj_list = []
        self.de_obj_list = []

    def run_auto_assignment_system(self, ):
        print("strategy - 1")
        self.initialize()
        strategy_obj = StrategyFactory.factory(constants.LOW_FIRST_MILE_STRATEGY)
        strategy_obj.execute(self.orders_obj_list, self.de_obj_list)

        print("strategy -2")
        self.initialize()
        strategy_obj = StrategyFactory.factory(constants.PREMIUM_FIRST_MILE_STRATEGY)
        strategy_obj.execute(self.orders_obj_list, self.de_obj_list)

    def initialize(self, ):
        self.initialize_order_objects()
        self.initialize_de_objects()

    def initialize_order_objects(self, ):
        for order in self.orders:
            customer = Customer(order['customer']['id'], order['customer']['rating'])
            order_obj = Order(order['id'], order['restaurant_location'], order['order_time'], customer)
            if order_obj:
                self.orders_obj_list.append(order_obj)

    def initialize_de_objects(self, ):
        for de in self.delivery_executives:
            de_obj = DeliveryExecutive(de['id'], de['de_current_location'],
                                       de['last_order_delivery_time'])
            if de_obj:
                self.de_obj_list.append(de_obj)
