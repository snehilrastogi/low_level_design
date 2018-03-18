from level_wise_cache.services.base_service import BaseService


class CacheService(BaseService):
    @classmethod
    def check_if_data_exists(cls, cache_obj, key):
        pos = -1
        for cache_data in cache_obj.data_list:
            pos += 1
            if cache_data['key'] == key:
                return True, pos
        return False, pos

    @classmethod
    def move_to_front(self, cache_obj, pos):
        data = cache_obj.data_list.pop(pos)
        cache_obj.data_list.insert(0, data)

    @classmethod
    def remove_from_tail(self, cache_obj):
        data = None
        if not self.is_empty(cache_obj):
            len = self.get_len(cache_obj)
            data = cache_obj.data_list.pop(len - 1)
        print ("Removed data from cache", cache_obj.level, "--", data)

    @classmethod
    def add_to_front(self, cache_obj, data):
        if not self.is_full(cache_obj):
            cache_obj.data_list.insert(0, data)

    @classmethod
    def get_len(self, cache_obj):
        return len(cache_obj.data_list)

    @classmethod
    def print_cache(self, cache_objs_dict):
        for key, value in cache_objs_dict.items():
            c = value
            print(
                "Level", c.level, "Read Time", c.read_time, "Write Time", c.write_time, "capacity", c.capacity,
                "data --",
                c.data_list)

    @classmethod
    def get_cache_level_list(self, cache_dict, level):
        if cache_dict.get(level) is None:
            print ("No such level exists")
            return

        cache_obj = cache_dict.get(level)
        return cache_obj

    @classmethod
    def is_empty(self, cache_obj):
        if cache_obj.data_list is None:
            return True
        return False

    @classmethod
    def is_full(self, cache_obj):
        if len(cache_obj.data_list) == cache_obj.capacity:
            return True
        return False

    @classmethod
    def fetch_cache_obj(cls, cache_objs_dict, level):
        return cache_objs_dict.get(level)

    @classmethod
    def update_key_value(cls, cache_obj, key, value):
        for data in cache_obj.data_list:
            if data['key'] == key:
                data['value'] = value

    @classmethod
    def get_value_for_key(cls, cache_obj, key):
        for data in cache_obj.data_list:
            if data['key'] == key:
                return data['value']

        return None

    @classmethod
    def set_data_analysis(cls, cache_objs_dict):
        cache_analysis_list = []
        for key, value in cache_objs_dict.items():
            cache_analysis_dict = {'level': key, 'capacity':value.capacity, 'num_items':CacheService.get_len(value)}
            cache_analysis_list.append(cache_analysis_dict)
        return cache_analysis_list



