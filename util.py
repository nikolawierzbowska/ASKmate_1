# dodatkowe funkcje]
import datetime, connection


def convert_timestamp_to_date(timestamp):
    date = datetime.datetime.fromtimestamp(timestamp)
    return date.strftime("%Y-%m-%d %H:%M:%S")


def generated_id(file):
    data = connection.read_dict_from_file(file)
    existing_id =[int(line["id"]) for line in data]
    return max(int(identification) for identification in existing_id) +1 if existing_id else 0


def get_time():
    current_date =datetime.datetime.now()
    return int(datetime.datetime.timestamp(current_date))
