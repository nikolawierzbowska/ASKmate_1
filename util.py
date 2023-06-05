def generate_id(existing_ids):
    return max(int(identification) for identification in existing_ids) + 1
