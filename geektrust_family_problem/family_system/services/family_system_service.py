from family_system.services.family_service import FamilyService


class FamilySystemService(object):
    def __init__(self, king, queen, commands):
        self.king = king
        self.queen = queen
        self.commands = commands
        self.family_obj = None

    def run_family_system(self, ):
        self.initialize_the_family()
        if self.commands is None:
            print("Nothing to run")
            exit()
        for command in self.commands:
            pass

    def initialize_the_family(self, ):
        self.family_obj = FamilyService.initialize_family(self.king, self.queen)
        if self.family_obj is None:
            print("Issue in initializing family ")
            exit()
        print("Initialized Family ", self.family_obj)