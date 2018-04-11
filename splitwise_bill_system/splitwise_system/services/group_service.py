from splitwise_flipkart.models.group import Group
from splitwise_flipkart.services.base_service import BaseService
from splitwise_flipkart.services.user_service import UserService


class GroupService(BaseService):
    @classmethod
    def create_group(self, group, user_obj_list):
        group_obj = Group(group['group_id'], group['group_name'])
        for id in group['users']:
            user_obj = UserService.fetch_user_obj_based_on_id(id, user_obj_list)
            group_obj.add_group_users(user_obj)
        return group_obj

    @classmethod
    def fetch_group_obj_based_on_id(self, id, group_obj_list):
        try:
            print (" group id --", id)
            for group in group_obj_list:
                if group.group_id == id:
                    return group
        except Exception as e:
            print ("exception in fetching group", e)
            raise e
