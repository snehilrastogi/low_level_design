import traceback

from smart_home_mgmt.models.interface_device import ID
from smart_home_mgmt.models.mode import MODE
from smart_home_mgmt.models.prop_of_smd import PROPSMD
from smart_home_mgmt.models.smd_device import SMD
from smart_home_mgmt.services.base_service import BaseService
from smart_home_mgmt.services.cmd_service import CommandService
from smart_home_mgmt.services.id_service import IdService


class Home_Mgmt_System(BaseService):
    def __init__(self, interface_devices, smart_home_devices, props, commands, modes):
        self.interface_devices = interface_devices
        self.smart_home_devices = smart_home_devices
        self.commands = commands
        self.modes = modes
        self.props = props
        self.id_obj_list = []
        self.smd_obj_list = []
        self.props_obj_list = []
        self.mode_objs_list = []

    def run_automation_home(self,):
        try:
            if len(self.smart_home_devices) < 1:
                print("No smart home devices present -- Exiting")
                exit()
            self.intialize()
            IdService.activate_all_id(self.id_obj_list)
            #SmdService.activate_all_smd(self.smd_obj_list)
            CommandService.analyse_command(self.commands, self.id_obj_list, self.smd_obj_list, self.props_obj_list, self.mode_objs_list)
        except Exception as e:
            print("Exception in running automation home system ",
                  traceback.format_exc(), e)

    def intialize(self,):
        #can move these to individual service class also -- as objects ideally should not be accessed here directly
        try:
            for id in self.interface_devices:
                id_obj = ID(id['id'], id['name'], id['activation'], id['modes'])
                self.id_obj_list.append(id_obj)

            for smd in self.smart_home_devices:
                smd_obj = SMD(smd['id'], smd['name'], smd['id_connected'], smd['prop_id'])
                self.smd_obj_list.append(smd_obj)

            for prop in self.props:
                prop_obj = PROPSMD(prop['id'], prop['name'], prop['min_val'], prop['max_val'])
                self.props_obj_list.append(prop_obj)

            for mode in self.modes:
                mode_obj = MODE(mode['id'], mode['name'], mode['configs'])
                self.mode_objs_list.append(mode_obj)

        except Exception as e:
            print("Exception in initializing objects for provided data ",
                  traceback.format_exc(), e)
            raise e