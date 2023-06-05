def read_table_from_file(file_name, separator=','):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        return [element.replace("\n", "").split(separator) for element in lines]
    except IOError:
        return "File not found"

def write_table_to_file(file_name, table, separator=','):
    with open(file_name, "a+") as file:
        for record in table:
            row = separator.join(record)
            file.write(row + "\n")