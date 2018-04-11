from calender.services.base_service import BaseService


class EventService(BaseService):
    @classmethod
    def print_events(cls, event_obj_list):
        for event in event_obj_list:
            print (event,"\t", EventService.fetch_users_for_an_event(event))

    @classmethod
    def fetch_users_for_an_event(cls, event_obj):
        for user in event_obj.user_objs:
            print ("User -", user.user_id)
