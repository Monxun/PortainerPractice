import string
import random
from faker import Faker
import logging

fake = Faker()

bank_names = [
    "Essence Credit Union",
    "Marshall Banks Inc.",
    "Esteem Financial Inc.",
    "Paradise Corporation",
    "United Financial Holdings",
    "Jones Holdings",
    "Azure Holding Company",
    "Golden Gates Trust Corp.",
    "Velvet Trust Corp.",
    "Reliance Holdings Inc."
]

def generate_id(size=7, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def generate_routing(size=9):
    return int(''.join(random.choice(string.digits) for _ in range(size)))

def generate_password(minSize=14):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(minSize))

def generate_phone():
    return f'{random.randrange(100, 1000, 3)}-{random.randrange(100, 1000, 3)}-{random.randrange(1000, 10000, 4)}'

def gender():
    return random.choice(["MALE", "FEMALE"])

def generate_name(gender):
    if gender == 'MALE' or gender == 'M':
        first_name = fake.first_name_male()
        middle_name = fake.first_name_male()
        last_name = fake.last_name_male()
    else:
        first_name = fake.first_name_female()
        middle_name = fake.first_name_female()
        last_name = fake.last_name_male()

    return (first_name, middle_name, last_name)

def generate_username(size=12):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))

''' Don't think I'll actually need this anymore but commenting it out until I'm certain.
def split_address(address):
    address_to_split = address.replace(',', '\n').split('\n')
    return_address = {}
    if len(address_to_split) == 2:
        # Looks like a military address
        # For data producing purposes I'll use the first index for the address line
        # I'll split the second line to get the PO (APO/FPO), US military 'state' code and zip
        po_state_zip = address_to_split[1].split(' ')

        return_address['street'] = address_to_split[0]
        return_address['city'] = po_state_zip[0]
        return_address['state'] = po_state_zip[1]
        return_address['zip'] = po_state_zip[2]

    elif len(address_to_split) == 3:
        # Looks like a regular address
        # Pull the street and suite/apt info from the first part of the address
        state_zip = address_to_split[2].strip().split(' ')

        return_address['street'] = address_to_split[0]
        return_address['city'] = address_to_split[1]
        return_address['state'] = state_zip[0]
        return_address['zip'] = state_zip[1]

    return return_address
'''

log_format = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

def create_logger(name, filename, mode='a', level=logging.INFO):
    '''Helper function to setup seperate loggers.
    '''
    file_handler = logging.FileHandler(filename, mode)
    file_handler.setFormatter(log_format)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)

    return logger