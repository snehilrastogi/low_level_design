import datetime
import traceback

from smart_home_mgmt import constants
from smart_home_mgmt.services.base_service import BaseService
from smart_home_mgmt.services.prop_smd_service import PropSmdService


class SmdService(BaseService):
    @classmethod
    def activate_all_smd(cls, smd_objs_list):
        try:
            for obj in smd_objs_list:
                obj.set_status = constants.SMART_HOME_STATUSES[constants.ON]
        except Exception as e:
            print("Exception in activating all smd ",
                  traceback.format_exc(), e)
            raise e

    @classmethod
    def activate_smd(cls, smd_name, smd_objs_list):
        try:
            for obj in smd_objs_list:
                if obj.name.lower() == smd_name.lower():
                    obj.set_status = constants.INTERFACE_DEVICES_STATUSES[constants.ON]
        except Exception as e:
            print("Exception in activating smd by name", smd_name,
                  traceback.format_exc(), e)
            raise e

    @classmethod
    def deactivate_all_id(cls, smd_objs_list):
        try:
            for obj in smd_objs_list:
                obj.set_status = constants.INTERFACE_DEVICES_STATUSES[constants.OFF]
        except Exception as e:
            print("Exception in deactivating all smd ",
                  traceback.format_exc(), e)
            raise e


    @classmethod
    def deactivate_id(cls, smd_name, smd_objs_list):
        try:
            for obj in smd_objs_list:
                if obj.name.lower() == smd_name.lower():
                    id.set_status = constants.INTERFACE_DEVICES_STATUSES[constants.OFF]
        except Exception as e:
            print("Exception in deactivating smd by id ",
                  traceback.format_exc(), e)
            raise e

    @classmethod
    def check_if_active(cls, smd_id, smd_objs_list):
        try:
            for obj in smd_objs_list:
                if obj.id == smd_id and obj.status == constants.ACTIVE:
                    return True
        except Exception as e:
            print("Exception in checking if smd is active", smd_id,
                  traceback.format_exc(), e)
        return False

    @classmethod
    def check_if_obj_exists_for_id(cls, smd_id, smd_objs_list):
        try:
            for obj in smd_objs_list:
                if obj.id == smd_id:
                    return obj
        except Exception as e:
            print("Exception in checking if smd exists for id ", smd_id,
                  traceback.format_exc(), e)
        return None

    @classmethod
    def check_if_obj_exists_for_name(cls, smd_name, smd_objs_list):
        try:
            for obj in smd_objs_list:
                if obj.name.lower() == smd_name.lower():
                    return obj
        except Exception as e:
            print("Exception in checking if smd exists for name ", smd_name,
                  traceback.format_exc(), e)
        return None

    @classmethod
    def find_smd_attached_to_id(cls, id_id, smd_objs_list):
        c = []
        try:
            for obj in smd_objs_list:
                if obj.interface_id == id_id:
                    c.append(obj)
        except Exception as e:
            print("Exception in checking if smd exists for some id device ", id,
                  traceback.format_exc(), e)
        return c

    @classmethod
    def set_status(cls, smd_obj, smd_status):
        try:
            cls.update_last_update_time(smd_obj, smd_status)
            if smd_obj is not None and smd_status.upper() in [constants.ON, constants.OFF]:
                smd_obj.set_status(smd_status)
                print("OK", smd_obj.name, " set to ", smd_status.upper())
            else:
                print("Wrong Updates - either obj is None or status is wrong")
        except Exception as e:
            print("Exception in setting new status for smd ", smd_obj.id, smd_obj.name,
                  traceback.format_exc(), e)
            raise e


    @classmethod
    def set_property(cls, smd_obj, prop_obj, prop_val):
        try:
            if smd_obj is not None and smd_obj.status == constants.SMART_HOME_STATUSES[constants.ON] \
                    and prop_obj is not None:
                if prop_obj.max_val >= prop_val >= prop_obj.min_val:
                    smd_obj.set_prop(prop_obj.id, prop_val)
                    print("OK", smd_obj.name, " ", prop_obj.name , "set to value", prop_val)
                else:
                    print("Sorry", "Wrong value of Property ", prop_obj.name, prop_val, "is out of range for "
                                                                                        "[", prop_obj.min_val,
                          prop_obj.max_val, "]")
            else:
                if smd_obj.status == constants.SMART_HOME_STATUSES[constants.OFF]:
                    print(smd_obj.name , "is in OFF MODE , cant change")
                else:
                    print("Wrong Updates - object is None")
        except Exception as e:
            print("Exception in setting property for smd ", smd_obj.id, smd_obj.name,prop_obj.name, prop_val,
                  traceback.format_exc(), e)
            raise e


    @classmethod
    def print_conn_smd_to_id(cls, id_obj, smd_obj_list, prop_obj_list):
        c = []
        try:
            smd_attached_list = cls.find_smd_attached_to_id(id_obj.id, smd_obj_list)
            for obj in smd_attached_list:
                d = [obj.id, obj.category, obj.name, obj.status]
                if obj.prop_id is not None and obj.status == constants.SMART_HOME_STATUSES[constants.ON]:
                    prop_obj = PropSmdService.check_if_obj_exists_for_id(obj.prop_id, prop_obj_list)
                    if prop_obj is not None:
                        s = "[" + str(obj.name) + "=" + str(obj.prop_val) + "]"
                        d.append(s)
                c.append(d)
        except Exception as e:
            print("Exception in printing connected smd to id details ", id_obj.id, id_obj.name,
                  traceback.format_exc(), e)
        return c

    @classmethod
    def update_last_update_time(cls, smd_obj, smd_status):
        try:
            if smd_obj.status.lower() == smd_status.lower():
                print(" same status -- no change in last update time and utilization")
            else:
                prev_t = smd_obj.last_update_time
                p_u = smd_obj.utilization
                if prev_t is None or smd_status.lower() == "on":
                    smd_obj.set_last_update_time(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    return
                if smd_status.lower() == "off":
                    update_time = smd_obj.last_update_time
                    if type(update_time) == str:
                        update_time = datetime.datetime.strptime(smd_obj.last_update_time, "%Y-%m-%d %H:%M:%S")
                    in_bet_time = (datetime.datetime.now() - update_time).total_seconds()
                    cls.update_utilization(smd_obj, p_u+in_bet_time)
        except Exception as e:
            print("Exception in updating last update time for smd ", smd_obj.id, smd_obj.name,
                  traceback.format_exc(), e)
            raise e

    @classmethod
    def update_utilization(cls, smd_obj, u):
        smd_obj.set_utilization(u)

    @classmethod
    def calculate_present_utilization(cls, smd_obj):
        try:
            u = smd_obj.utilization
            if smd_obj.status.lower() == "on":
                update_time = smd_obj.last_update_time
                if type(update_time) == str:
                    update_time = datetime.datetime.strptime(update_time, "%Y-%m-%d %H:%M:%S")
                in_bet_time = (datetime.datetime.now() - update_time).total_seconds()
                #print(" in bet time -- ", in_bet_time)
                u = u + in_bet_time
            #print("Utilization after calculation -- ", u)
            return u
        except Exception as e:
            print("Exception in calculating utilization ", smd_obj.id, smd_obj.name,
                  traceback.format_exc(), e)
            raise e

    @classmethod
    def set_interfaceid_for_smd(cls, id_obj, smd_obj):
        try:
            if smd_obj.interface_id == id_obj.id:
                print("Already assigned to same Interface device -- no updates")
                return
            smd_obj.set_interface_device(id_obj.id)
            print("Assigned", smd_obj.name, "to Interface device", id_obj.name)
        except Exception as e:
            print("Exception in updating ID device for smd")
            raise e



