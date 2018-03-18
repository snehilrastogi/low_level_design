from level_wise_cache.services.cache_service import CacheService
import traceback


class CacheSystem:
    @classmethod
    def read_data(cls, cache_objs_dict, key, read_time=0):
        """
        :param data:
        :return:
        """
        found = False
        pos = -1
        cache_obj = None
        num_levels = len(cache_objs_dict)
        try:
            for i in range(num_levels):
                print ("Reading at Level", i + 1)

                if i+1 not in cache_objs_dict.keys():
                    print ("Wrong data is present in cache - cache invalidated")
                    return None, False, -1, read_time
                cache_obj = cache_objs_dict[i + 1]
                if not cache_obj:
                    print("No obj at level", i + 1)
                    return None, False, -1, read_time
                read_time += cache_obj.read_time
                print("At level ", i+1, "read time is", read_time)
                found, pos = CacheService.check_if_data_exists(cache_obj, key)
                if found:
                    return cache_obj, found, pos, read_time
        except Exception:
            print(" Exception In read data", key, read_time)
        return cache_obj, found, pos, read_time

    @classmethod
    def write_data(cls, cache_obj, key, value):
        """

        :param data:
        :return:
        """
        data = {'key': key, 'value': value}
        print ("writing at level", cache_obj.level)
        if CacheService.is_full(cache_obj):
            CacheService.remove_from_tail(cache_obj)
            print ("As cache ", cache_obj.level, "is full - so last is removed")
        CacheService.add_to_front(cache_obj, data)

    @classmethod
    def read_service(cls, cache_objs_dict, key):
        """
        :return:read_time
        """
        read_time = 0
        try:
            cache_obj, found, pos, read_time = CacheSystem.read_data(cache_objs_dict, key, read_time)
            if cache_obj is not None and found == True:
                print(key, "Found at level ", cache_obj.level)
                if cache_obj.level == 1:
                    print ("No need to propogate")
                    CacheService.move_to_front(cache_obj, pos)
                else:
                    print("needs propagation")
                    value = CacheService.get_value_for_key(cache_obj, key)
                    if value is None:
                        return
                    for j in range(cache_obj.level - 1):
                        print ("Propgating read data to level", j+1)
                        cache_obj = cache_objs_dict.get(j + 1)
                        CacheSystem.write_data(cache_obj, key, value)
                        read_time += cache_obj.write_time
            else:
                print (key, "Not found at any level-- cache miss")
        except Exception as e:
            print("exception in read service --", key, traceback.format_exc, e)
            raise e
        return read_time

    @classmethod
    def write_service(cls, cache_objs_dict, key, value):
        """

        :param cache_objs_dict:
        :param key:
        :return:write_time
        """
        write_time = 0
        num_levels = len(cache_objs_dict)
        try:
            for i in range(num_levels):
                print ("Checking at Level", i+1)
                cache_obj = cache_objs_dict.get(i + 1)
                found, pos = CacheService.check_if_data_exists(cache_obj, key)
                write_time += cache_obj.read_time
                if found:
                    CacheService.update_key_value(cache_obj, key, value)
                    CacheService.move_to_front(cache_obj, pos)
                else:
                    cache_obj = cache_objs_dict.get(i + 1)
                    CacheSystem.write_data(cache_obj, key, value)
                    write_time += cache_obj.write_time
            print ("caches after writing ", key, "--", value)
            CacheService.print_cache(cache_objs_dict)
        except Exception as e:
            print ("exception in writing serivce", key, value, traceback.format_exc, e)
            raise e
        return write_time
