from family_system.services.family_system_service import FamilySystemService

King = "SHAN"
Queen = "ANGA"
Commands = [
    "ADD_WIFE"
    "ADD_CHILD"

]



if __name__ == "__main__":
    family_system_obj = FamilySystemService(King, Queen, Commands)
    family_system_obj.run_family_system()