class BaseService(object):
    @classmethod
    def fetch_avg_rating(cls, obj):
        return obj.get_avg_rating()
