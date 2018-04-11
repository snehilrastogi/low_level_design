import traceback

from splitwise_flipkart.services.bill_service import BillService
from splitwise_flipkart.services.group_service import GroupService
from splitwise_flipkart.services.user_service import UserService


class BillMgmtSystem:
    def __init__(self, bills_list, groups_list, users_list):
        self.users_list = users_list
        self.groups_list = groups_list
        self.bills_list = bills_list
        self.user_obj_list = []
        self.group_objs_list = []
        self.bill_objs_list = []

    def manage_bill(self, ):
        self.initialize()
        try:
            BillService.group_wise_balances(self.user_obj_list, self.group_objs_list, self.bill_objs_list)
        except Exception:
            print ("exception in managing bills", traceback.format_exc())

        BillService.print_group_balances(self.group_objs_list)
        BillService.print_individual_balances(self.user_obj_list)

    def initialize(self):
        for user in self.users_list:
            user_obj = UserService.create_user(user)
            self.user_obj_list.append(user_obj)

        for group in self.groups_list:
            group_obj = GroupService.create_group(group, self.user_obj_list)
            self.group_objs_list.append(group_obj)

        for bill in self.bills_list:
            bill_obj = BillService.create_bill(bill)
            self.bill_objs_list.append(bill_obj)

        # self.print_all_data()

    def print_all_data(self, ):
        for user in self.user_obj_list:
            print ("User --", user)

        for group in self.group_objs_list:
            print ("Group --", group)

        for bill in self.bill_objs_list:
            print ("bill --", bill)
