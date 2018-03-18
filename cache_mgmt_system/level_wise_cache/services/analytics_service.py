import traceback

from level_wise_cache import constants


class AnalyticsService:
    @classmethod
    def calculate_analytics(cls, analytics_obj_list):
        total_read_time = 0
        total_write_time = 0
        total_reads = 0
        total_writes = 0
        for a in analytics_obj_list:
            if a.get('type') == constants.READ:
                total_read_time += a.get('time')
                total_reads += 1
            if a.get('type') == constants.WRITE:
                total_write_time += a.get('time')
                total_writes += 1
        avg_read = total_read_time / total_reads
        avg_write = total_write_time / total_writes
        analytics_data = {'avg_read_time': avg_read, 'avg_write_time': avg_write}
        return analytics_data

    @classmethod
    def set_analytics_data(self, time, type=constants.READ):
        try:
            analytic_data_dict = {"type": type, "time": time}
            return analytic_data_dict
        except Exception:
            print("Exception in setting analytics", traceback.format_exc())
