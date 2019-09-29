import datetime
import traceback

from in_mem_database import constants
from in_mem_database.services.base_service import BaseService
from in_mem_database.services.table_service import TableService


class PrintService(BaseService):
    @classmethod
    def print_tables(cls, db_obj):
        try:
            tables = db_obj.tables
            if db_obj is None or db_obj.tables is None:
                print("db obj is None or no tables")
                return
            for table in tables:
                print(table.name)
                for r in table.records:
                    if r is not None:
                        print(r)
        except Exception as e:
            print("exception in printing", traceback.print_exc(), e)
            raise e