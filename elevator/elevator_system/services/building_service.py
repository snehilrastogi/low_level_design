from elevator_system.models.building import Building


class BuildingService:
    @classmethod
    def initialize_building(cls, total_floors, customers_objs_list, elevator_obj):
        building_obj = Building(total_floors, customers_objs_list, elevator_obj)
        return building_obj