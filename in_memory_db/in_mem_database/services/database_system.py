import traceback

from in_mem_database import constants
from in_mem_database.models.columns import Columns
from in_mem_database.models.database import Database
from in_mem_database.models.int_type import IntType
from in_mem_database.models.string_type import StringType
from in_mem_database.models.table import Table
from in_mem_database.services.filter_service import FilterService
from in_mem_database.services.insert_service import InsertService
from in_mem_database.services.print_service import PrintService


class DatabaseSystem(object):
    def __init__(self, database_name, tables, records, commands):
        self.database_name = database_name
        self.tables = tables
        self.records = records
        self.commands = commands
        self.db_obj = None
        self.tables_obj = []

    def run_db_system(self, ):
        self.initialize()
        InsertService.insert_into_db(self.db_obj, self.records)
        PrintService.print_tables(self.db_obj)
        FilterService.filter_values(self.db_obj, "table1", "t1c1", None)

    def initialize(self, ):
        try:
            self.db_obj = Database(self.database_name, None)
            if self.db_obj is None:
                print("database object is None ")
                exit()
            for table in self.tables:
                table_name = table['name']
                col_objs = []
                for col in table['columns']:
                    data_type = col['type']
                    constraint = col['constraint']
                    if constraint is not None and constraint.lower() != constants.CONSTRAINT_NAME.lower():
                        print("Wrong Constraint", constraint)
                        break

                    if data_type.lower() == constants.STRING.lower():
                        type_obj = StringType(constants.STRING, constants.STRING_LENGTH)
                    elif data_type.lower() == constants.INT.lower():
                        type_obj = IntType(constants.INT, constants.INT_MIN_VAL, constants.INT_MAX_VAL)
                    else:
                        print("Wrong column value")
                        type_obj = None
                        break
                    col_obj = Columns(col['name'], type_obj, constraint)
                    col_objs.append(col_obj)
                table_obj = Table(table_name, col_objs)
                self.tables_obj.append(table_obj)
                self.db_obj.add_table(table_obj)
        except Exception as e:
            print("Exception in initializing the db or tables ", traceback.print_exc(), e)
