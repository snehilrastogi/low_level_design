from splitwise_flipkart.models.user import User
from splitwise_flipkart.services.base_service import BaseService


class UserService(BaseService):
    @classmethod
    def create_user(self, user):
        user_obj = User(user['user_id'], user['user_email'], user['user_name'])
        return user_obj

    @classmethod
    def fetch_user_obj_based_on_id(self, id, user_obj_list):
        try:
            for user in user_obj_list:
                if user.user_id == id:
                    return user
        except Exception as e:
            print ("exception in fetching user", e)
            raise e
