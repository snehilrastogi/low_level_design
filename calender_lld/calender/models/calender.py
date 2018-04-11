class Calendar:
    def __init__(self):
        self.calender_data = {}

    def add_to_calender(self, user_obj, event_obj):
        if event_obj in self.calender_data:
            self.calender_data[event_obj].append(user_obj)

        else:
            self.calender_data[event_obj] = [user_obj]
