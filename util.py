import random
import string


def generate_id(number_of_small_letters=4):
    found = False
    while not found:
        identification = []
        identification.extend(random.sample(string.ascii_lowercase, number_of_small_letters))
        random.shuffle(identification)
        return ''.join(identification)
