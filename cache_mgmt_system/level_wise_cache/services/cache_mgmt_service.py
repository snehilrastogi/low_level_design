import traceback
import re

from level_wise_cache import constants
from level_wise_cache.models.cache import Cache
from level_wise_cache.services.analytics_service import AnalyticsService
from level_wise_cache.services.cache_service import CacheService
from level_wise_cache.services.cache_system_service import CacheSystem


class CacheMgmtService:
    def __init__(self, num_levels, read_times, write_times, input_data):
        self.num_levels = num_levels
        self.read_times = read_times
        self.write_times = write_times
        self.input_data = input_data
        self.cache_objs_dict = dict()
        self.analytics_objs_list = []

    def run_cache_system(self):
        try:
            self.initialize_cache()
            CacheService.print_cache(self.cache_objs_dict)
            for i_data in self.input_data:
                print ("Processing --", i_data)
                try:
                    if "read" in i_data.lower():
                        key = re.findall(r'\"(.+?)\"', i_data)
                        print ("key -- ", key[0], "is to be read")
                        read_time = CacheSystem.read_service(self.cache_objs_dict, key[0])
                        print ("READ TIME:", read_time)
                        try:
                            analytic_data_dict = AnalyticsService.set_analytics_data(read_time, constants.READ)
                            self.analytics_objs_list.append(analytic_data_dict)
                        except Exception as e:
                            print (e)
                    elif "write" in i_data.lower():
                        key_value = re.findall(r'\"(.+?)\"', i_data)
                        write_time = CacheSystem.write_service(self.cache_objs_dict, key_value[0], key_value[1])
                        print ("WRITE TIME:", write_time)
                        analytic_data_dict = AnalyticsService.set_analytics_data(write_time, constants.WRITE)
                        self.analytics_objs_list.append(analytic_data_dict)
                    else:
                        print("Wrong Input")
                except Exception as e:
                    print("Exception in reading/writing", traceback.format_exc, i_data)

            print("analysis of system")
            analytics_data = AnalyticsService.calculate_analytics(self.analytics_objs_list)
            cache_analysis_list = CacheService.set_data_analysis(self.cache_objs_dict)
            self.print_stats(cache_analysis_list, analytics_data)
        except Exception:
            print("Exception", traceback.format_exc)

    def initialize_cache(self, ):
        for i in range(self.num_levels):
            cache_obj = Cache(i + 1, self.read_times[i], self.write_times[i])
            self.cache_objs_dict[i + 1] = cache_obj

    def print_stats(self, cache_analysis_list, analytics_data):
        for data in cache_analysis_list:
            print ("Cache - ", data.get('level'), "--", data.get('num_items'), "/", data.get('capacity'))

        print ("Avg Read Time ", analytics_data.get('avg_read_time'), "avg write time", analytics_data.get('avg_write_time'))
