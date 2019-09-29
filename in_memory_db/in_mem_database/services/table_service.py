import datetime
import traceback

from in_mem_database import constants
from in_mem_database.services.base_service import BaseService


class TableService(BaseService):
    @classmethod
    def get_table_obj_from_name(cls, tables_obj, table_name):
        try:
            if tables_obj is None:
                return None
            for table in tables_obj:
                if table.name.lower() == table_name.lower():
                    print("Found", table.name)
                    return table
            return None
        except Exception as e:
            print("exception in getting table name", traceback.print_exc(), e)
            return None
