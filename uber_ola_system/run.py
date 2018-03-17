from cab_system.finding_suitable_cab.services.cab_assignment_system import CabAssignmentSystem

trips = [
    {
        "driver_name": "d1",
        "driver_rating_by_customer":4,
        "customer_name":"c1",
        "customer_rating_by_driver": 5,

    },
    {
        "driver_name": "d1",
        "driver_rating_by_customer": 5,
        "customer_name": "c2",
        "customer_rating_by_driver": 4,
    },
    {
        "driver_name": "d1",
        "driver_rating_by_customer": 1,
        "customer_name": "c3",
        "customer_rating_by_driver": 2,
    },
    {
        "driver_name": "d2",
        "driver_rating_by_customer":5,
        "customer_name":"c1",
        "customer_rating_by_driver": 1,
    },
    {
        "driver_name": "d2",
        "driver_rating_by_customer": 5,
        "customer_name": "c2",
        "customer_rating_by_driver": 5,
    },
    {
        "driver_name": "d2",
        "driver_rating_by_customer": 4,
        "customer_name": "c3",
        "customer_rating_by_driver": 5,
    },
    {
        "driver_name": "d3",
        "driver_rating_by_customer": 3,
        "customer_name": "c1",
        "customer_rating_by_driver": 2,
    },
    {
        "driver_name": "d3",
        "driver_rating_by_customer": 4,
        "customer_name": "c1",
        "customer_rating_by_driver": 5,
    },
    {
        "driver_name": "d3",
        "driver_rating_by_customer": 3,
        "customer_name": "c1",
        "customer_rating_by_driver": 3,
    },
]
input_data = ["c1", "c2", "c3", "c4", "c5"]

if __name__ == "__main__":
    cab_assignment_system = CabAssignmentSystem(trips, input_data)
    cab_assignment_system.run_cab_system()
