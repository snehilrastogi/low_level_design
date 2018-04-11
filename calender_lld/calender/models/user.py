class User:
    def __init__(self, user_id, ):
        self.user_id = user_id
        self.event_objs = []

    def add_event(self, event_obj):
        self.event_objs.append(event_obj)

    def get_user(self):
        return self

    def __str__(self):
        return "user id: {}".format(self.user_id)

    def __repr__(self):
        return self.__str__()
