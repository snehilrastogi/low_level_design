from elevator_system.services.run_elevator_system import RunElevatorSystem


class Main:
    def main(self, ):
        # total_floors = int(input("enter total floors"))
        # total_customers = int(input("enter total customers"))
        # starting_floor = int(input("Enter Starting Floor"))
        # num_requests = int(input("Enter Total Requests"))
        total_floors = 3
        total_customers = 3
        starting_floor = 1
        num_requests = 3
        RunElevatorSystem(total_floors, total_customers, starting_floor, num_requests).run_elevator_system()


if __name__ == "__main__":
    Main().main()
