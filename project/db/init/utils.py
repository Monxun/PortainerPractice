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


def random_address(applicant):

    if applicant:

        address = applicant['address']
        line2 = address.split('\n')[1]

        street = address.split('\n')[0]

        line2_split = line2.split(', ')
        city = line2_split[0]
        state = line2_split[1][0:2]
        zipcode = line2_split[1][-5:]

        return street, city, state, zipcode
    
    else:

        address = fake.address()

        line2 = address.split('\n')[1]

        street = address.split('\n')[0]

        line2_split = line2.split(', ')
        city = line2_split[0]
        state = line2_split[1][0:2]
        zipcode = line2_split[1][-5:]

        return street, city, state, zipcode
