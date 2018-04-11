class Group:
    def __init__(self, group_id, group_name):
        self.group_id = group_id
        self.group_name = group_name
        self.group_users = []
        self.balances={}

    def add_group_users(self, user_obj):
        self.group_users.append(user_obj)

    def __str__(self):
        return "group_id: {}, group_name: {} , ".format(self.group_id, self.group_name)

    def __repr__(self):
        return self.__str__()
