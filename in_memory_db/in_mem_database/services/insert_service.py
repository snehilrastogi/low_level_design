import traceback

from in_mem_database import constants
from in_mem_database.services.base_service import BaseService
from in_mem_database.services.table_service import TableService


class InsertService(BaseService):
    @classmethod
    def insert_into_db(cls, db_obj, records):
        try:
            tables = db_obj.tables
            if db_obj is None or db_obj.tables is None:
                print("db obj is None or no tables")
                return
            if len(records) < 1:
                print("No records")
                return
            for rec in records:
                table_name = rec['table_name']
                table_obj = TableService.get_table_obj_from_name(tables, table_name)
                if table_obj is None:
                    print("No such table exists ", table_name)
                    return
                j = 0
                num_cols_in_table = len(table_obj.cols)
                for row in rec['rows']:
                    l = len(row)
                    if l != num_cols_in_table:
                        print("row doesnt match column ")
                        return
                    r_i = []
                    for r in range(len(row)):
                        type_col = table_obj.cols[r].type
                        type_constraint = table_obj.cols[r].constraint
                        if type_constraint is None:
                            if row[r] is not None:
                                if type(row[r]) == int:
                                    if type_col.name.lower() != "int":
                                        print("mismatch cols for int")
                                        return
                                    if row[r] < type_col.min_val or row[r] > type_col.max_val:
                                        print("out of range value")
                                        return
                                elif type(row[r]) == str:
                                    if type_col.name.lower() != "string":
                                        print("mismatch cols for string")
                                        return
                                    if len(row[r])> type_col.length:
                                        print("greater than length")
                                        return
                                else:
                                    print("Wrong type")
                                    return
                        elif type_constraint.lower() == constants.CONSTRAINT_NAME.lower():
                            if row[r] is not None:
                                if type(row[r]) == int:
                                    if type_col.name.lower() != "int":
                                        print("mismatch cols for int with constraint")
                                        return
                                    if row[r] < type_col.min_val or row[r] > type_col.max_val:
                                        print("with constraint -- out of range value", type_col.min_val,
                                              type_col.max_val)
                                        return
                                elif type(row[r]) == str:
                                    if type_col.name.lower() != "string":
                                        print("mismatch cols for string with constraint")
                                        return
                                    if len(row[r]) > type_col.length:
                                        print("greater than length")
                                        return
                                else:
                                    print("Wrong type")
                                    return
                            else:
                                print("column cannot have none value")
                                return
                        r_i.append(row[r])
                    table_obj.records[j] = r_i
                    j += 1
        except Exception as e:
            print("exception in inserting", traceback.print_exc(), e)
            raise e