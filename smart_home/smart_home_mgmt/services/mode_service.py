import traceback

from smart_home_mgmt.services.base_service import BaseService


class ModeService(BaseService):
    @classmethod
    def check_if_obj_exists_for_name(cls, mode_name, mode_objs_list):
        try:
            for mode in mode_objs_list:
                if mode.name.lower() == mode_name.lower():
                    return mode
        except Exception as e:
            print("Exception in finding if mode obj exists for a given name ", mode_name, traceback.print_exc(), e)
        return None

    @classmethod
    def print_mode(cls, mode_obj):
        try:
            print ("ID -- ", mode_obj.id, "  Name ", mode_obj.name, " Configs --")
            configs = mode_obj.configs
            for c in range(len(configs)):
                val = configs[c]
                for k in range(len(val)):
                    print(k)
        except Exception as e:
            print("Exception in print the mode obj", traceback.print_exc(), e)
            raise e