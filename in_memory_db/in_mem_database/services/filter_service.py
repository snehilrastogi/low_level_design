import traceback

from in_mem_database.services.base_service import BaseService
from in_mem_database.services.table_service import TableService


class FilterService(BaseService):
    @classmethod
    def filter_values(cls, db_obj, table_name, column_name, value):
        print("Filter service")
        try:
            tables = db_obj.tables
            if db_obj is None or db_obj.tables is None:
                print("db obj is None or no tables")
                return
            table_obj = TableService.get_table_obj_from_name(tables, table_name)
            if table_obj is None:
                print("No such table exists ", table_name)
                return
            if table_obj.records is None:
                print("no record exists in table", table_name)
                return
            cols = table_obj.cols
            col_num, col = cls.find_column_by_name(cols, column_name)
            if cols is None or col == False:
                print("No such column exists")
                return
            ans = []
            for row in table_obj.records:
                if row is None:
                    break
                if row[col_num] == value:
                    ans.append(row)
            print("Rows found for value ", value)
            print(ans)
        except Exception as e:
            print("exception in filtering", traceback.print_exc(), e)
            raise e

    @classmethod
    def find_column_by_name(cls, cols_obj, col_name):
        i = 0
        for c in cols_obj:
            if c.name.lower() == col_name.lower():
                return i,True
            i += 1
        return -1, False

