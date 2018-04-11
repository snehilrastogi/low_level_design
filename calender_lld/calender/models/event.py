class Event:
    def __init__(self, event_id, start_time, end_time, location, owner, title, type):
        self.event_id = event_id
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.owner = owner
        self.user_objs = []
        self.title = title
        self.type = type
        # self.state = cal_constants.EVENT_STATE[cal_constants.NEUTRAL]
        self.state = "NEUTRAL"

    def set_event_type(self, type):
        self.type = type

    def set_users(self, user_obj):
        self.user_objs.append(user_obj)

    def set_state(self, state):
        self.state = state

    def get_event(self):
        return self

    def __str__(self):
        return "event id: {}, start_time: {} , end time: {} type: {}".format(self.event_id, self.start_time, self.end_time,
                                                                             self.type)

    def __repr__(self):
        return self.__str__()
