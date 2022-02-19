import random
from faker import Faker

fake = Faker()


def random_bank_name():
    banks = [
        'Banktrust Of Alabama',
        'Town Bank Of Westfield',
        'Sandra Cagle Enterprises',
        'Investors Community Bank',
        'Marathon National Bank Of NY',
        'Mutual Of Omaha Bank',
        'Spinnaker Development Group',
        'Susquehanna Bank Pa',
        'Brunswick Bank & Trust CO',
        'First State Bank Of Canadian',
        'First National Community Bank',
        'Huron Community Bank',
        'Tennessee Commerce Bank',
        'Techecentral',
        'Security State Bank',
        'Shorebank Enterprise Cleveland',
        'Lyndon State Bank',
        'Farmers & Merchants Bank',
        'Eagle National Bank Of Miami',
        'Washington Savings Bank Fsb'
    ]

    rand = random.randrange(0, 19)
    
    return banks[rand]


def random_address():

    street = fake.street_address()
    city = fake.city()
    state = fake.state_abbr()
    zipcode = str(fake.postcode())

    return tuple([street, city, state, zipcode])


def random_middle_name(applicant):
    if applicant['sex'] == 'M':
            middle_name = fake.name_male().split(' ')[0]
    else:
        middle_name = fake.name_female().split(' ')[0]

    return middle_name
