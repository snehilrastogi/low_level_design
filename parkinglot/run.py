from automated_parking_system.services.smart_parking_system import SmartParkingSystem

num_parking_slots = 3

commands = [
    {
        "Registration_num": "Reg1",
        "colour": "White",
        "Action": "park",
    },
    {
        "Registration_num": "Reg2",
        "colour": "Red",
        "Action": "park",
    },
    {
        "Registration_num": "Reg3",
        "colour": "Red",
        "Action": "park",
    },
    {
        "Registration_num": "Reg4",
        "colour": "Red",
        "Action": "park",
    },
    {
      "Action": "status allocated",
    },
    {
      "Action": "status free",
    },


]


if __name__ == "__main__":
    smart_parking_system = SmartParkingSystem(num_parking_slots, commands)
    smart_parking_system.run_parking_system()