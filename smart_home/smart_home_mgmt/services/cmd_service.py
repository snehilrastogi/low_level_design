import traceback

from smart_home_mgmt.services.base_service import BaseService
from smart_home_mgmt.services.id_service import IdService
from smart_home_mgmt.services.mode_service import ModeService
from smart_home_mgmt.services.prop_smd_service import PropSmdService
from smart_home_mgmt.services.smd_service import SmdService


class CommandService(BaseService):
    @classmethod
    def analyse_command(cls, commands, id_obj_list, smd_obj_list, prop_obj_list, mode_objs_list):
        try:
            if len(commands) <= 0:
                print("No commands")
            for cmd in range(len(commands)):
                val = commands[cmd]
                print("\n ---- execution of cmd -- ", val, "starts ------\n")
                if val[0].lower() == "give":
                    l = len(val)
                    if l < 4 or l > 5:
                        print("Wrong Give Command -- ", val)
                        continue
                    id_device_activation = val[1]
                    smd_device = val[2]
                    if l == 4:
                        smd_status = val[3]
                        cls.run_give_cmd_with_no_prop(id_obj_list, smd_obj_list, id_device_activation, smd_device,
                                                      smd_status)
                    else:
                        prop_name = val[3]
                        prop_val = val[4]
                        cls.run_give_cmd_with_prop(id_obj_list, smd_obj_list, prop_obj_list,
                                                   id_device_activation, smd_device, prop_name, prop_val)
                elif val[0].lower() == "print":
                    if len(val) != 2:
                        print("Wrong Print Command -- ", val)
                        continue
                    if val[1].lower() == "usage":
                        cls.run_usage_cmd(smd_obj_list)
                    else:
                        cls.print_conn_device(val[1], id_obj_list, smd_obj_list, prop_obj_list)

                elif val[0].lower() == "activatemode":
                    if len(val) != 3:
                        print("Wrong activation command -- ", val)
                        continue
                    id_name = val[1]
                    mode_name = val[2]
                    cls.run_activate_mode_cmd(id_name, mode_name, mode_objs_list, id_obj_list, smd_obj_list, prop_obj_list)
                else:
                    print("\n -- Wrong Command-- ", val)
        except Exception as e:
            print("Exception in analysing commands ",
                  traceback.format_exc(), e)
            raise e

    @classmethod
    def run_give_cmd_with_no_prop(cls, id_obj_list, smd_obj_list, id_device_activation, smd_device, smd_status):
        try:
            id_obj = IdService.check_if_obj_exists_for_activation(id_device_activation, id_obj_list)
            if id_obj is None:
                print("Wrong Activation command Given -- ", id_device_activation)
                return
            smd_obj = SmdService.check_if_obj_exists_for_name(smd_device, smd_obj_list)
            if smd_obj is None:
                print("Wrong Smart Home Device --", smd_device)
                return
            if smd_obj.status.lower() == smd_status:
                print("Already in ", smd_status, "mode")
            else:
                SmdService.set_interfaceid_for_smd(id_obj, smd_obj)
                SmdService.set_status(smd_obj, smd_status)
        except Exception as e:
            print("Exception in running 'give' command without properties ", smd_device,
                  traceback.format_exc(), e)
            raise e

    @classmethod
    def run_give_cmd_with_prop(cls, id_obj_list, smd_obj_list, prop_obj_list,
                               id_device_activation, smd_device, prop_name, prop_val):
        try:
            id_obj = IdService.check_if_obj_exists_for_activation(id_device_activation, id_obj_list)
            if id_obj is None:
                print("Wrong Activation command Given -- ", id_device_activation)
                return
            smd_obj = SmdService.check_if_obj_exists_for_name(smd_device, smd_obj_list)
            if smd_obj is None:
                print("Wrong Smart Home Device --", smd_device)
                return

            prop_obj = PropSmdService.check_if_obj_exists_for_name(prop_name, prop_obj_list)
            if prop_obj is None:
                print("Wrong Property being set to Smart Home Device --", prop_name)
                return

            SmdService.set_interfaceid_for_smd(id_obj, smd_obj)
            SmdService.set_property(smd_obj, prop_obj, prop_val)
        except Exception as e:
            print("Exception in running 'give' command with properties ", prop_name,
                  traceback.format_exc(), e)
            raise e

    @classmethod
    def print_conn_device(cls, id_name, id_obj_list, smd_obj_list, prop_obj_list):
        try:
            id_obj = IdService.check_if_obj_exists_for_name(id_name, id_obj_list)
            if id_obj is None:
                print("Wrong Interface device Given -- ", id_name)
                return

            print_list = SmdService.print_conn_smd_to_id(id_obj, smd_obj_list, prop_obj_list)
            if len([print_list]) < 1:
                print (id_name, " -- NO SMD Attached")
                return
            a = ["#", "Category", "Name", "State"]
            print_list.insert(0, a)
            #print ("print_list --- ", print_list)

            for i in range(len(print_list)):
                data = print_list[i]
                #print ("data -- ", data)
                if len(data) == 5:
                    last_val = data[3] + " " + data[4]
                else:
                    last_val = data[3]
                print(data[0], "   ", data[1], "    ", data[2], "    ", last_val)
        except Exception as e:
            print("Exception in printing connected device ", id_name,
                  traceback.format_exc(), e)
            raise e

    @classmethod
    def run_usage_cmd(cls, smd_obj_list):
        try:
            print ("#    ", "Name   ", "Utilization")
            for obj in smd_obj_list:
                u = SmdService.calculate_present_utilization(obj)
                SmdService.update_utilization(obj, u)
                print(obj.id, "   ", obj.name, "  ", obj.utilization, "seconds")
        except Exception as e:
            print("Exception in running print usage command",
                  traceback.format_exc(), e)
            raise e

    @classmethod
    def run_activate_mode_cmd(cls, id_name, mode_name, mode_objs_list, id_obj_list, smd_obj_list, prop_obj_list):
        try:
            mode_obj = ModeService.check_if_obj_exists_for_name(mode_name, mode_objs_list)
            if mode_obj is None:
                print("No such mode exists -- wrong command")

            id_obj = IdService.check_if_obj_exists_for_activation(id_name, id_obj_list)
            if id_obj is None:
                print("Wrong Interface device Given -- ", id_name)
                return
            IdService.attach_mode(id_obj, mode_obj)
            IdService.set_mode_status_in_id(id_obj, active_mode=mode_obj.name)
            cls.generate_give_commands_for_activate_mode_settings(id_obj, mode_obj,id_obj_list, smd_obj_list,
                                                                  prop_obj_list)
        except Exception as e:
            print("Exception in running the activate mode command -- ", id_name, mode_name,
                  traceback.print_exc(), e)
            raise e

    @classmethod
    def generate_give_commands_for_activate_mode_settings(cls, id_obj, mode_obj, id_obj_list, smd_obj_list,
                                                          prop_obj_list):
        try:
            configs = mode_obj.configs
            if configs is None or len(configs) < 1:
                print("No configs present in mode obj ", mode_obj.name, mode_obj.configs)
                return
            for c in range(len(configs)):
                x = configs[c]
                if len(x) < 2 or len(x) > 3:
                    print("Wrong configs -- ", x)
                    return
                smd_id = x[0]
                smd_status = x[1]
                smd_obj = SmdService.check_if_obj_exists_for_id(smd_id, smd_obj_list)
                if smd_obj is None:
                    print("Wrong Smart Home Device --", smd_id)
                    return

                if len(x) == 3:
                    print("Running the mode -- with property")
                    prop_id = smd_obj.prop_id
                    prop_obj = PropSmdService.check_if_obj_exists_for_id(prop_id, prop_obj_list)
                    if prop_obj is None:
                        print("Wrong Property being set to Smart Home Device --", prop_id)
                        return
                    prop_val = x[2]
                    cls.run_give_cmd_with_prop(id_obj_list, smd_obj_list, prop_obj_list,
                               id_obj.activation, smd_obj.name, prop_obj.name, prop_val)
                    return

                print("Running the mode -- without property")
                cls.run_give_cmd_with_no_prop(id_obj_list, smd_obj_list, id_obj.activation, smd_obj.name,
                                              smd_status)
        except Exception as e:
            print("Exception in generating give commands to activate the mode ", id_obj.name, mode_obj.name,
                  traceback.print_exc(), e)
            raise e