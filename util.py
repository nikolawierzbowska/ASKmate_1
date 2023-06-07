# dodatkowe funkcje]
import datetime, connection

def convert_timestamp_to_date(timestamp):
    date = datetime.datetime.fromtimestamp(timestamp)
    return date.strftime("%Y-%m-%d %H:%M:%S")



def generated_id(existing_idea):
    return max(int(identification) for identification in existing_idea) +1

