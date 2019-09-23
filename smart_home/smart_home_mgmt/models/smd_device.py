from smart_home_mgmt import constants


class SMD:
    def __init__(self, id, name, interface_id, prop_id):
        self.id = id
        self.name = name
        self.interface_id = interface_id
        self.prop_id = prop_id
        self.prop_val = constants.PROP_VAL_INITIAL
        self.status = constants.SMART_HOME_STATUSES[constants.OFF]
        self.set_category()
        self.last_update_time = None
        self.utilization = 0

    def __str__(self):
        return "id :{}, name: {}, interface_id: {} , prop_id:{},  status {}, category {}, last_update_time {}, " \
               "utilization {}".format(
            self.id, self.name, self.interface_id, self.prop_id,
            self.status, self.category, self.last_update_time, self.utilization)

    def __repr__(self):
        return self.__str__()

    def set_prop(self, prop_id=None, prop_val=None):
        self.prop_id = prop_id
        self.prop_val = prop_val

    def set_category(self,):
        if "fan" in self.name.lower():
            self.category = constants.FAN
        elif "light" in self.name.lower():
            self.category = constants.LIGHT
        else:
            self.category = constants.GENERIC

    def set_status(self, status):
        self.status = status

    def set_last_update_time(self, t):
        self.last_update_time = t

    def set_utilization(self, u):
        if u > 0:
            self.utilization = u

    def set_interface_device(self, interface_id):
        self.interface_id = interface_id
