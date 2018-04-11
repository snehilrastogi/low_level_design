# from calender.cal_constants import EVENT_STATE, ACCEPTED
from calender.models.event import Event
from calender.models.user import User
from calender.services.base_service import BaseService
from calender.services.event_service import EventService
from calender.services.user_service import UserService

ACCEPTED = "ACCEPTED"
NEUTRAL = "NEUTRAL"
REJECTED = "REJECTED"

EVENT_STATE = {
    ACCEPTED: ACCEPTED,
    NEUTRAL: NEUTRAL,
    REJECTED: REJECTED
}

MEETING = "MEETING"
HOLIDAY = "HOLIDAY"
REMINDER = "REMINDER"
EVENT_TYPE = {
    MEETING: MEETING,
    HOLIDAY: HOLIDAY,
    REMINDER: REMINDER,

}

class CalendarMgmtService(BaseService):
    def __init__(self, events_list, users_list):
        self.events_list = events_list
        self.users_list = users_list
        self.event_objs_list = []
        self.users_objs_list = []

    def manage_calendar(self):
        self.initialize()
        EventService.print_events(self.event_objs_list)
        UserService.print_users_calendar(self.users_objs_list)
        self.get_common_free_slot()

    def initialize(self, ):
        for event in self.events_list:
            event_obj = Event(event['event_id'], event['start_time'], event['end_time'], event['location'],
                              event['owner'], event['title'], event['type'])
            self.event_objs_list.append(event_obj)

        for user in self.users_list:
            accepted_events = user['accepted_events']
            user_obj = User(user['user_id'])
            for acc_event in accepted_events:
                event_obj = self.get_event_from_id(acc_event)
                user_obj.add_event(event_obj)
                self.update_event_state(event_obj)
                event_obj.set_users(user_obj)
            self.users_objs_list.append(user_obj)
                # for event in self.event_objs_list:
                #     Calendar().add_to_calender(event_obj, event_obj.user_objs)

    def get_event_from_id(self, event_id):
        for event_obj in self.event_objs_list:
            if event_obj.event_id == event_id:
                return event_obj

    def update_event_state(self, event_obj):
        # event_obj.set_state(constants.EVENT_STATE[constants.ACCEPTED])
        event_obj.set_state(EVENT_STATE[ACCEPTED])
        # event_obj.save()

    def get_common_free_slot(self, ):
        """

        :return:
        """
        d = dict()
        l = []
        free_slots = []
        for user in self.users_objs_list:
            for event in user.event_objs:
                tup = (event.start_time, event.end_time)
                if tup not in l:
                    l.append((event.start_time, event.end_time))
                # if event.start_time in d.keys():
                #     if event.end_time < d[event.start_time]:
                #         d[event.start_time] = event.end_time
                # else:
                #     d[event.start_time] = event.end_time

        # print ("dict of times --", d)
        # sorted_dict = sorted(d.iterkeys())
        # print ("sorted_dict", sorted_dict)

        num_hours = 0
        sorted_list = sorted(l, key=lambda x: x[0])
        print ("sorted_list", sorted_list)

        # checking for initial hours
        if sorted_list[0][0] > 0:
            diff = sorted_list[0][0] - 0
            num_hours += diff
            free_slots.append((0, sorted_list[0][0]))
        count = len(sorted_list)
        i = 0

        while i < count - 1:
            if sorted_list[i + 1][0] - sorted_list[i][1] < 0:
                i += 1
            else:
                diff = sorted_list[i + 1][0] - sorted_list[i][1]
                num_hours += diff
                free_slots.append((sorted_list[i][1], sorted_list[i + 1][0]))
                i += 1

        # checking for later hours
        if sorted_list[i][1] > 0:
            diff = 24 - sorted_list[i][1]
            num_hours += diff
            free_slots.append((sorted_list[i][1], 24))

        print ("Free slots ---", free_slots)
