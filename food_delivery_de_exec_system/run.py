from auto_assignment.services.auto_assignment_system import AutoAssignmentSystem

orders = [
    {
        "restaurant_location": (13.006752, 77.561737),
        "id": 123,
        "order_time": "2018-02-24 13:16:07",
        "customer": {
            "id": "CUST01",
            "rating": 4.4
        }
    },

    {
        "restaurant_location": (14.006152, 78.561737),
        "id": 124,
        "order_time": "2018-02-24 13:15:07",
        "customer": {
            "id": "CUST02",
            "rating": 3.1
        }
    },
    {
        "restaurant_location": (13.006252, 78.461737),
        "id": 125,
        "order_time": "2018-02-24 13:17:07",
        "customer": {
            "id": "CUST03",
            "rating": 3.8
        }
    },
    {
        "restaurant_location": (14.006552, 75.961098),
        "id": 126,
        "order_time": "2018-02-24 13:15:07",
        "customer": {
            "id": "CUST04",
            "rating": 4.0
        }
    }
]

delivery_executives = [
    {
        "de_current_location": (14.006752, 77.001737),
        "id": 981,
        "last_order_delivery_time": "2018-02-24 13:00:07"
    },
    {
        "de_current_location": (13.006352, 78.001737),
        "id": 982,
        "last_order_delivery_time": "2018-02-24 13:01:07"
    },
    {
        "de_current_location": (14.006252, 79.001737),
        "id": 983,
        "last_order_delivery_time": "2018-02-24 13:12:07"
    },
    {
        "de_current_location": (14.006552, 75.961098),
        "id": 984,
        "last_order_delivery_time": "2018-02-24 13:15:07"
    }
]
if __name__ == "__main__":
    auto_assignment_obj = AutoAssignmentSystem(orders, delivery_executives)
    auto_assignment_obj.run_auto_assignment_system()
