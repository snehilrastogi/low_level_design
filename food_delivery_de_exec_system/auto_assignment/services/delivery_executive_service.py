import datetime
import traceback

from auto_assignment import constants
from auto_assignment.services.base_service import BaseService


class DeliveryExecutivesService(BaseService):
    @classmethod
    def fetch_free_delivery_executives(cls, delivery_executives):
        de_list = delivery_executives
        waiting_delivery_executives = []
        try:
            for de in de_list:
                if de.status == constants.DELIVERY_EXECUTIVE_STATUSES[constants.FREE]:
                    DeliveryExecutivesService.update_waiting_time(de)
                    waiting_delivery_executives.append(de)
            free_delivery_executives = sorted(waiting_delivery_executives, key=lambda de: de.waiting_time, reverse=True)
            for de in free_delivery_executives:
                print("id", de.de_id, "waiting_time", str(de.waiting_time))
        except Exception as e:
            print("Exception in fetching the free delivery executive", e, traceback.format_exc)
            raise e
        return free_delivery_executives

    @classmethod
    def fetch_delivery_executives_by_equal_distribution(self, delivery_executives):
        de_list = delivery_executives
        waiting_delivery_executives = []
        next_delivery_executive = None
        try:
            for de in de_list:
                if de.status == constants.DELIVERY_EXECUTIVE_STATUSES[constants.FREE]:
                    DeliveryExecutivesService.update_waiting_time(de)
                    waiting_delivery_executives.append(de)

            sorted_delivery_executives = sorted(waiting_delivery_executives, key=lambda de: de.delivered_count)
            for de in sorted_delivery_executives:
                print("id", de.de_id, "delivered_count", de.delivered_count)
            if sorted_delivery_executives:
                next_delivery_executive = sorted_delivery_executives[0]
                print("Least Count delivery_executive id - ", next_delivery_executive.de_id, "delivered_count",
                      str(next_delivery_executive.delivered_count))
        except Exception as e:
            print("Exception in fetching the delivery executive by equal_distribution", e, traceback.format_exc)
            raise e
        return next_delivery_executive

    @classmethod
    def set_delivered_count(cls, delivery_exec_obj, count):
        delivery_exec_obj.set_delivered_count(count)

    @classmethod
    def update_waiting_time(cls, obj):
        try:
            obj.waiting_time = datetime.datetime.now() - obj.last_delivery_time
        except Exception as e:
            print("Exception in calculating the waiting time for delivery executive", obj, traceback.format_exc(),
                  e)
            raise e