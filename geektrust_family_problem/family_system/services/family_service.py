import traceback

from family_system import constants
from family_system.models.family import Family
from family_system.services.base_service import BaseService
from family_system.services.person_service import PersonService


class FamilyService(BaseService):

    @classmethod
    def initialize_family(cls, king, queen):
        try:
            king_obj = PersonService.initialize_person(king, constants.MALE)
            queen_obj = PersonService.initialize_person(queen, constants.FEMALE)
            PersonService.set_generation(king_obj, 1)
            PersonService.set_generation(queen_obj, 1)
            PersonService.set_spouse(king_obj, queen_obj)
            PersonService.set_spouse(queen_obj, king_obj)
            PersonService.set_is_part_of_shan(king_obj, True)
            PersonService.set_is_part_of_shan(queen_obj, True)
            family_obj = Family(constants.FAMILY_NAME, king_obj, queen_obj, [king_obj, queen_obj])
            return family_obj

        except Exception as e:
            print("Exception in initializing the family for king and queen ", king , queen, traceback.print_exc(), e)
            return None

    @classmethod
    def add_child(cls, family_obj, name, sex, mother_name):
        try:
            if family_obj is None:
                print("family is none")
                return
            mother_obj = cls.find_if_person_exists_for_name(family_obj, mother_name)
            if mother_obj is None:
                print("No such person exists ", mother_name)
                return
            if mother_obj.sex != constants.FEMALE or mother_obj.spouse is None:
                print("Mother not a female or no spouse")
                return
            child_obj = PersonService.initialize_person(name, sex)
        except Exception as e:
            print ("Exception in adding child ", name, sex, mother_name)
            raise e

    @classmethod
    def add_wife(cls, family_obj, name, sex, mother_name):
        pass

    @classmethod
    def add_husband(self, family_obj, name, sex, mother_name):
        pass

    @classmethod
    def find_if_person_exists_for_name(cls, family_obj, name):
        try:
            if family_obj is None:
                print("family is none")
                return None
            members = family_obj.family_members
            if members is None:
                print("No family members as of now")
                return None
            for member in members:
                if member.name.lower() == name.lower():
                    return member
            return None
        except Exception as e:
            print("Exception in finding if person exists for name ", name, traceback.print_exc(), e)
        return None