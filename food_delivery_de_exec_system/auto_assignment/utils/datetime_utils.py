import datetime
import traceback


def convert_str_to_datetime(date_str):
    new_order_time = date_str
    try:
        if type(date_str) == str:
            new_order_time = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except Exception as e:
        print("Exception in converting the order time %s to proper datetime format", date_str,
              traceback.format_exc(), e)
        raise e
    return new_order_time
