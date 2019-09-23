from smart_home_mgmt.services.Home_Mgmt_System import Home_Mgmt_System

interface_devices = [
    {
        "id": 1,
        "name": "GoogleHome",
        "activation": "OK,Google",
        "modes": [1]
    },
    {
        "id": 2,
        "name": "Alexa",
        "activation": "Alexa",
        "modes": [2]
    }
]
smart_home_devices = [
    {
        "id": 1,
        "name": "Smart Charger",
        "id_connected": 1,
        "prop_id": None
    },
    {
        "id": 2,
        "name": "Living Room Fan",
        "id_connected": 1,
        "prop_id": 1
    },
    {
        "id": 3,
        "name": "Drawing Room Light",
        "id_connected": 1,
        "prop_id": 2
    }
]

props = [
    {
        "id": 1,
        "name": "Speed",
        "min_val": 1,
        "max_val": 5
    },
    {
        "id": 2,
        "name": "Bright",
        "min_val": 1,
        "max_val": 10
    }
]

modes = [
    {
        "id": 1,
        "name": "sleep",
        "configs": [[3, "OFF"],[1, "ON"]]
    },
    {
        "id": 2,
        "name": "sleep",
        "configs": [[2, "ON", "3"]] #2 here is smd object id
    },

]
"""
commands = [
    ["add", "ID", "GoogleHome", "Activated by OK,Google"],
    ["add", "ID", "Alexa", "Activated by Alexa"],
    ["add", "SMD", "Light", "Alexa"],
    ["add", "SMD", "Fan", "Google Home"],
    ["add", "SMD", "Smart Charger", "Alexa"],
    #above commands already done via json format

    ["give", "Alexa", "Drawing Room Light", "ON"],
    ["give", "OK,Google", "Living Room Fan", "ON"],
    ["give", "OK,Google", "Living Room Fan", "Speed", 5],
    ["give", "OK,Google", "Living Room Fan", "Speed", 7],
    ["give", "Alexa", "Drawing Room Light", "Bright", 8],
    ["give", "Alexa", "Smart Charger", "ON"],
    ["give", "Alexa", "Smart Charger", "OFF"],
    ["give", "OK,Google", "Living Room Fan", "OFF"],
    ["give", "OK,Google", "Living Room Fan", "Speed", 3],
    #new functionality commands
    ["print", "GoogleHome"],
    ["print", "Alexa"],
    #new functionality commands
    ["print", "usage"],
    #new functionality commands -- add mode done directly via json
    ["addmode", "sleep", "Alexa",{
        "Light": "OFF",
        "Charger": "ON"
    }
    ],
    ["addmode", "sleep", "OK,Google",
     {
        "FAN": ("ON", 3)
     }
    ],
    ["activatemode", "Alexa", "sleep"],
    ["activatemode", "Ok,Google", "sleep"],

    ["print", "GoogleHome"],
    ["print", "Alexa"],
]
"""
commands = [
    ["give", "Alexa", "Drawing Room Light", "ON"],
    ["give", "OK,Google", "Living Room Fan", "ON"],
    ["give", "OK,Google", "Living Room Fan", "Speed", 5],
    ["give", "OK,Google", "Living Room Fan", "Speed", 7],
    ["give", "Alexa", "Drawing Room Light", "Bright", 8],
    ["give", "Alexa", "Smart Charger", "ON"],
    ["give", "Alexa", "Smart Charger", "OFF"],
    ["give", "OK,Google", "Living Room Fan", "OFF"],
    ["give", "OK,Google", "Living Room Fan", "Speed", 3],
    ["print", "GoogleHome"],
    ["print", "Alexa"],
    ["print", "usage"],
    ["activatemode", "Alexa", "sleep"],
    ["print", "GoogleHome"],
    ["print", "Alexa"],
    ["activatemode", "Ok,Google", "sleep"],

    ["print", "GoogleHome"],
    ["print", "Alexa"],
    ["print", "usage"],
]

if __name__ == "__main__":
    home_mgmt_system = Home_Mgmt_System(interface_devices, smart_home_devices, props, commands, modes)
    home_mgmt_system.run_automation_home()
