from splitwise_system.models.bill import Bill
from splitwise_system.services.base_service import BaseService
from splitwise_system.services.group_service import GroupService
from splitwise_system.services.user_service import UserService


class BillService(BaseService):
    @classmethod
    def create_bill(self, bill):
        bill_obj = Bill(bill['bill_id'], bill['group_id'], bill['total_amount'], bill['paid_by'], bill['contribution'])
        return bill_obj

    @classmethod
    def group_wise_balances(self, user_obj_list, group_objs_list, bill_objs_list):
        try:
            group_wise = {}
            for bill_obj in bill_objs_list:
                paid_user_objs = {}
                group_obj = GroupService.fetch_group_obj_based_on_id(bill_obj.group_id, group_objs_list)
                group_wise[group_obj.group_id] = []
                for paid in bill_obj.paid_by:
                    user_obj = UserService.fetch_user_obj_based_on_id(paid['user_id'], user_obj_list)
                    paid_user_objs[user_obj.user_id] = paid['share']

                # print ("paid_user_objs", paid_user_objs)

                for contri in bill_obj.contribution:
                    ans = {}
                    user_obj = UserService.fetch_user_obj_based_on_id(contri['user_id'], user_obj_list)
                    # print ("Group --", group_obj.group_id)

                    if user_obj.user_id in paid_user_objs:
                        balance = paid_user_objs[user_obj.user_id] - contri['share']
                        if user_obj.user_id in group_obj.balances:
                            group_obj.balances[user_obj.user_id] = group_obj.balances[user_obj.user_id] + \
                                                                   (paid_user_objs[user_obj.user_id] - contri['share'])
                        else:
                            group_obj.balances[user_obj.user_id] = balance
                        user_obj.total_balance += balance
                        ans[user_obj.user_id] = user_obj.total_balance
                    else:
                        balance = user_obj.total_balance - contri['share']
                        if user_obj.user_id in group_obj.balances:
                            group_obj.balances[user_obj.user_id] = group_obj.balances[user_obj.user_id] - contri[
                                'share']
                        else:
                            group_obj.balances[user_obj.user_id] = -1 * contri['share']

                        ans[user_obj.user_id] = balance
                        user_obj.total_balance = user_obj.total_balance - contri['share']

                    group_wise[group_obj.group_id].append(ans)
        except Exception as e:
            print ("exception in generating balances", e)
            raise e

    @classmethod
    def print_group_balances(cls, group_objs_list):
        print ("--- Group Balances ---")
        for group in group_objs_list:
            print ("Group id -- ", group.group_id, "Balances--", group.balances)

    @classmethod
    def print_individual_balances(cls, user_obj_list):
        print ("--- Individual Balances ---")
        for user in user_obj_list:
            print ("User id -", user.user_id, "balance --", user.total_balance)
