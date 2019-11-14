class Parking(object):
    def __init__(self, num_of_slots):
        self.slots = [None] * num_of_slots
        self.empty_slots = []
        self.full_slots = []

    def __str__(self):
        return self.__dict__

    def append_to_empty_slots(self, slot_obj):
        self.empty_slots.append(slot_obj)
        self.empty_slots = sorted(self.empty_slots, key=lambda x: x.slot_id)

    def append_to_full_slots(self, slot_obj):
        self.full_slots.append(slot_obj)
        self.full_slots = sorted(self.full_slots, key=lambda x: x.slot_id)
