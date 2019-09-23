from splitwise_system.services.bill_mgmt_system import BillMgmtSystem

bills = [
    {
        "bill_id": 1,
        "group_id": 1,
        "total_amount": 300,
        "paid_by": [{'user_id': 1, 'share': 300}],
        "contribution": [{'user_id': 1, 'share': 100},
                         {'user_id': 2, 'share': 200}]

     },
    {
        "bill_id": 2,
        "group_id": 1,
        "total_amount": 500,
        "paid_by": [{'user_id': 2, 'share': 500}],
        "contribution": [{'user_id': 1, 'share': 250},
                         {'user_id': 2, 'share': 250}]

    },
    {
        "bill_id": 3,
        "group_id": 2,
        "total_amount": 100,
        "paid_by": [{'user_id': 3, 'share': 100}],
        "contribution": [{'user_id': 2, 'share': 10},
                         {'user_id': 3, 'share': 90}]

    },
    {
        "bill_id": 4,
        "group_id": 2,
        "total_amount": 300,
        "paid_by": [{'user_id': 3, 'share': 100}, {'user_id': 2, 'share': 200}],
        "contribution": [{'user_id': 2, 'share': 150},
                         {'user_id': 3, 'share': 150}]

    },
]

users = [
    {
        "user_id": 1,
        "user_email": "abc@xyz.com",
        "user_name": "A1",
    },
    {
        "user_id": 2,
        "user_email": "abc@xyz.com",
        "user_name": "A1",
    },
    {
        "user_id": 3,
        "user_email": "abc@xyz.com",
        "user_name": "A1",
    }

]

groups = [
    {
        "group_id": 1,
        "users": [1, 2],
        "group_name": "G1",
    },
    {
        "group_id": 2,
        "users": [2, 3],
        "group_name": "G2",
    },
    {
        "group_id": 3,
        "users": [1, 2, 3],
        "group_name": "G3",
    },

]

if __name__ == "__main__":
    bill_mgmt_obj = BillMgmtSystem(bills, groups, users)
    bill_mgmt_obj.manage_bill()
