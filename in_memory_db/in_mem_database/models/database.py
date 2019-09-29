class Database(object):
    def __init__(self, name, tables):
        self.name = name
        self.tables = tables

    def __str__(self):
        return self.__dict__

    def add_table(self, table_obj):
        if self.tables is None:
            self.tables = [table_obj]
        else:
            self.tables.append(table_obj)
