import csv

def read_dict_from_file(file_name):
    with open(file_name) as file:
        lines =csv.DictReader(file)
        return [dict(line) for line in lines]


def write_dict_to_file(file_name,data):
    with open(file_name, "a+",newline="") as file:
        for record in data:
            file.write(record)


def update_dict_to_file(file_name,data):
    with open(file_name, "w",newline="") as file:
        for record in data:
            file.write(record)

def write_dict_to_file_str(file_name, data):
    with open(file_name, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
