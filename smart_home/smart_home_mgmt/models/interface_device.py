from smart_home_mgmt import constants


class ID:
    def __init__(self, id, name, activation, modes=None):
        self.id = id
        self.name = name
        self.activation = activation
        self.status = constants.INTERFACE_DEVICES_STATUSES[constants.INACTIVE]
        self.modes = modes
        self.active_mode = None

    def __str__(self):
        return "id :{}, name: {}, activation: {}, status {}, modes {}".format(
            self.id, self.name, self.activation,
            self.status, self.modes)

    def __repr__(self):
        return self.__str__()

    def set_status(self, status):
        self.status = status

    def set_modes(self, modes):
        self.modes = modes

    def set_mode_status_in_id(self, active_mode):
        self.active_mode = active_mode
