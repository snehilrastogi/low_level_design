from in_mem_database.services.database_system import DatabaseSystem

database_name = "Razorpay"

tables = [
    {
        "name": "table1",
        "columns": [
        {
            "name": "t1c1",
            "type": "string",
            "constraint": None
        },
        {
            "name": "t1c2",
            "type": "int",
            "constraint":"NOTNULL"
        },
        {
            "name": "t1c3",
            "type": "string",
            "constraint":"NOTNULL"
        }
        ]
    },
    {
        "name": "table2",
        "columns": [
        {
            "name": "t2c1",
            "type": "string",
            "constraint": None
        },
        {
            "name": "t2c2",
            "type": "int",
            "constraint":"NOTNULL"
        },
        {
            "name": "t2c3",
            "type": "string",
            "constraint":"NOTNULL"
        }
        ]
    }
]

records = [
    {
        "table_name": "table1",
         "rows":[
             [None, 1, "t1r13"],
             ["t1r21", 2, "t1r23"],
             [None, 3, "t1r33"],
         ]
    },
    {
        "table_name": "table2",
         "rows": [
             ["t2r11", 1, "t2r13"],
             ["t2r21", -12, "t2r23"],
             ["snehilrastogirazorpayy", 3, "t2r33"],
         ]
    },

]

commands = [
    "PRINT",
    {"FILTER": ["table1", "col_name", "value"]}  #give the values here
]
if __name__ == "__main__":
    db_obj = DatabaseSystem(database_name, tables, records, commands)
    db_obj.run_db_system()
