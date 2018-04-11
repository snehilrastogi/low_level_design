from calender.services.base_service import BaseService


class UserService(BaseService):
    @classmethod
    def print_users_calendar(cls, user_obj_list):
        for user in user_obj_list:
            print ("-----User id----- ", user.user_id)
            for event in user.event_objs:
                print ("Event--", event)
            print("\n")

    @classmethod
    def fetch_events_for_an_user(cls, user_obj):
        print ("User ---", user_obj.user_id)
        for event in user_obj.event_objs:
            print ("Event", event)
