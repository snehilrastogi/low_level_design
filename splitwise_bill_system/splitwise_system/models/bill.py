class Bill:
    def __init__(self, bill_id, group_id, total_amount, paid_by, contribution):
        self.bill_id = bill_id
        self.group_id = group_id
        self.total_amount = total_amount
        self.paid_by = paid_by
        self.contribution = contribution

    def __str__(self):
        return "bill_id :{}, group_id: {}, total_amount: {} , paid_by {}, contribution {}".format(
            self.bill_id, self.group_id, self.total_amount,
            self.paid_by, self.contribution)

    def __repr__(self):
        return self.__str__()
