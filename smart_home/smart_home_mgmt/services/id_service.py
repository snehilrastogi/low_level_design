import traceback

from smart_home_mgmt import constants
from smart_home_mgmt.services.base_service import BaseService


class IdService(BaseService):
    @classmethod
    def activate_all_id(cls, id_objs_list):
        try:
            for obj in id_objs_list:
                obj.set_status(constants.INTERFACE_DEVICES_STATUSES[constants.ACTIVE])
                print(obj)
        except Exception as e:
            print("Exception in activating all ID ",
                  traceback.format_exc(), e)
            raise e

    @classmethod
    def activate_id(cls, id_name, id_objs_list):
        try:
            for obj in id_objs_list:
                if obj.name.lower() == id_name.lower():
                    obj.set_status(constants.INTERFACE_DEVICES_STATUSES[constants.ACTIVE])
        except Exception as e:
            print("Exception in activating ID by name ", id_name,
                  traceback.format_exc(), e)
            raise e

    @classmethod
    def deactivate_all_id(cls, id_objs_list):
        try:
            for obj in id_objs_list:
                obj.set_status(constants.INTERFACE_DEVICES_STATUSES[constants.INACTIVE])
        except Exception as e:
            print("Exception in deactivating all id ",
                  traceback.format_exc(), e)
            raise e


    @classmethod
    def deactivate_id(cls, id_name, id_objs_list):
        try:
            for obj in id_objs_list:
                if obj.name.lower() == id_name.lower():
                    obj.set_status(constants.INTERFACE_DEVICES_STATUSES[constants.INACTIVE])
        except Exception as e:
            print("Exception in deactivating ID by name",id_name,
                  traceback.format_exc(), e)
            raise e

    @classmethod
    def check_if_active(cls, id_id, id_objs_list):
        try:
            for obj in id_objs_list:
                if obj.id == id_id and obj.status == constants.ACTIVE:
                    return True
        except Exception as e:
            print("Exception in checking if ID is active by id ",id_id,
                  traceback.format_exc(), e)
        return False

    @classmethod
    def check_if_obj_exists_for_id(cls, id_id, id_objs_list):
        try:
            for obj in id_objs_list:
                if obj.id == id_id:
                    return obj
        except Exception as e:
            print("Exception in checking if ID exists by name ", id_id,
                  traceback.format_exc(), e)
        return None

    @classmethod
    def check_if_obj_exists_for_name(cls, id_name, id_objs_list):
        try:
            for obj in id_objs_list:
                if obj.name.lower() == id_name.lower():
                    return obj
        except Exception as e:
            print("Exception in checking if ID exists by name ", id_name,
                  traceback.format_exc(), e)
        return None

    @classmethod
    def check_if_obj_exists_for_activation(cls, id_activation, id_objs_list):
        try:
            for obj in id_objs_list:
                if obj.activation.lower() == id_activation.lower():
                    return obj
        except Exception as e:
            print("Exception in checking if ID exists by activation ", id_activation,
                  traceback.format_exc(), e)
        return None

    @classmethod
    def attach_mode(cls, id_obj, mode_obj):
        try:
            existing_modes = id_obj.modes
            if len(existing_modes) < 1:
                print("No existing mode -- add")
            if mode_obj.id in existing_modes:
                print("Mode already exist -- no new addition")
            else:
                existing_modes.append(mode_obj.id)
                id_obj.set_modes(existing_modes)
        except Exception as e:
            print("Exception in attaching mode to ID ", id_obj.name, mode_obj.name,
                  traceback.print_exc(), e)
            raise e

    @classmethod
    def set_mode_status_in_id(cls, id_obj, active_mode):
        id_obj.set_mode_status_in_id(active_mode)
        print("Mode set to -- ", active_mode, "for ID --", id_obj.name)














