import traceback

from smart_home_mgmt.services.base_service import BaseService


class PropSmdService(BaseService):
    @classmethod
    def check_if_obj_exists_for_id(cls, prop_id, prop_objs_list):
        try:
            for obj in prop_objs_list:
                if obj.id == prop_id:
                    return obj
        except Exception as e:
            print("Exception in checking if prop exists by id ",prop_id,
                  traceback.format_exc(), e)
        return None

    @classmethod
    def check_if_obj_exists_for_name(cls, prop_name, prop_objs_list):
        try:
            for obj in prop_objs_list:
                if obj.name.lower() == prop_name.lower():
                    return obj
        except Exception as e:
            print("Exception in checking if prop exists by name ", prop_name,
                  traceback.format_exc(), e)
        return None
