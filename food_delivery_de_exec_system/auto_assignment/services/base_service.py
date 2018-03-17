class BaseService(object):
    @classmethod
    def update_status(cls, obj, status):
        obj.set_status(status)
