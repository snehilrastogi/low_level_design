class User:
    def __init__(self, user_id, user_email, user_name):
        self.user_id = user_id
        self.user_email = user_email
        self.user_name = user_name
        self.total_balance = 0
        #the amount user ower to other
        self.owes_to = {}
        # the amount which other users owes him
        self.owes_from = {}

    def set_total_balance(self, balance):
        self.total_balance = balance

    def __str__(self):
        return "user_id: {}, user_email: {} , ".format(self.user_id, self.user_email)

    def __repr__(self):
        return self.__str__()
