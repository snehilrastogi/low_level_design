import traceback

from family_system import constants
from family_system.models.person import Person
from family_system.services.base_service import BaseService


class PersonService(BaseService):
    @classmethod
    def initialize_person(cls, name, sex):
        try:
            person_obj = Person(name, sex)
            return person_obj
        except Exception as e:
            print("Exception in initializing the king and queen ", name, sex, traceback.print_exc(), e)
            raise e

    @classmethod
    def set_generation(cls, person, generation):
        try:
            if person is None:
                print("set_generation - Person doesn't exist")
                return
            if generation < 1:
                print("Wrong generation ", generation)
                return
            person.set_generation(generation)
        except Exception as e:
            print("Exception in settig the generation for person ", person, traceback.print_exc(), e)
            raise e

    @classmethod
    def set_spouse(cls, person , spouse):
        try:
            if person is None or spouse is None:
                print("set_spouse - Either person or its spouse is None", person, spouse)
                return
            if person.spouse is not None:
                print("set_spouse - person ", person.name, "spouse already exists -- ", person.spouse.name)
                return
            if spouse.spouse is not None and spouse.spouse != person:
                print("set_spouse - Some other person mentioned as spouse's spouse", spouse.spouse)
                return
            person.set_spouse(spouse)
            spouse.set_spouse(person)
        except Exception as e:
            print("Exception in setting the spouse for ", person, spouse, traceback.print_exc(), e)
            raise e

    @classmethod
    def set_is_part_of_shan(cls, person, is_part):
        try:
            if person is None:
                print("set_is_part_of_shan - Person doesn't exist")
                return
            person.set_is_part_of_shan(is_part)
        except Exception as e:
            print("Exception in setting is part of shan ", person, traceback.print_exc(), e)
            raise e

    @classmethod
    def add_son(cls, person, son_obj):
        try:
            if person is None:
                print("add_son - Person doesn't exist")
                return
            if son_obj is None or son_obj.sex != constants.MALE:
                print("Son is None or not correct")
                return

            person.set_son(son_obj)
        except Exception as e:
            print("Exception in adding son ", person, traceback.print_exc(), e)
            raise e

    @classmethod
    def add_daughter(cls, person, daughter_obj):
        try:
            if person is None:
                print("add_daughter - Person doesn't exist")
                return
            if daughter_obj is None or daughter_obj.sex != constants.FEMALE:
                print("Daughter is None or not correct")
                return
            person.set_daughter(daughter_obj)
        except Exception as e:
            print("Exception in adding daughter ", person, traceback.print_exc(), e)
            raise e

    @classmethod
    def add_mother(cls, person, mother_obj):
        try:
            if person is None:
                print("add_mother - Person doesn't exist")
                return
            if mother_obj is None or mother_obj.sex != constants.FEMALE:
                print("Mother is None or not correct")
                return
            person.set_mother(mother_obj)
            if person.sex == constants.MALE:
                cls.add_son(mother_obj, )
        except Exception as e:
            print("Exception in adding mother ", person, traceback.print_exc(), e)
            raise e

    @classmethod
    def add_father(cls, person, father_obj):
        try:
            if person is None:
                print("add_father - Person doesn't exist")
                return
            if father_obj is None or father_obj.sex != constants.FEMALE:
                print("Father is None or not correct")
                return
            person.set_father(father_obj)
        except Exception as e:
            print("Exception in adding father ", person, traceback.print_exc(), e)
            raise e
