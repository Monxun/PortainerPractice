##########################################################
### Data producer for the Aline Financial API          ###
##########################################################
from faker import Faker
from helpers import helpers
import random

fake = Faker()

def create_applicant():
    gender = helpers.gender()
    name = helpers.generate_name(gender)

    return {"firstName": name[0],
            "middleName": name[1],
            "lastName": name[2],
            "dateOfBirth": fake.date_of_birth(minimum_age=18).strftime(f'%Y-%m-%d'),
            "gender": gender,
            "email": fake.email(),
            "phone": helpers.generate_phone(),
            "socialSecurity": fake.ssn(),
            "driversLicense": helpers.generate_id(),
            "income": round(random.randint(1500000,12000000)),
            "address": fake.street_address(),
            "city": fake.city(),
            "state": fake.state_abbr(),
            "zipcode": fake.zipcode(),
            "mailingAddress": fake.street_address(),
            "mailingCity": fake.city(),
            "mailingState": fake.state_abbr(),
            "mailingZipcode": fake.zipcode()}

def create_application(num=1):
    return {
            "applicationType": random.choice(["CHECKING", "SAVINGS", 
                            "CHECKING_AND_SAVINGS", "CREDIT_CARD", "LOAN"]),
            "noApplicants": False,
            "applicants": [create_applicant() for _ in range(num)]
            }

def create_admin():
    name = helpers.generate_name(helpers.gender())

    return {
        "role": "admin",
        "username": helpers.generate_username(),
        "password": f'Mypassa@dffsfa2',
        "firstName": name[0],
        "lastName": name[1],
        "email": fake.email(),
        "phone": helpers.generate_phone()
    }

def create_member(application_response):
    return {
        "role": "member",
        "username": helpers.generate_username(),
        "password": 'Mypassa@dffsfa2',
        "firstName": application_response['applicants'][0]['firstName'],
        "lastName": application_response['applicants'][0]['lastName'],
        "email": application_response['applicants'][0]['email'],
        "phone": application_response['applicants'][0]['phone'],
        "lastFourOfSSN": application_response['applicants'][0]['socialSecurity'][7:11],
        "membershipId": application_response['createdMembers'][0]['membershipId']
    }

def create_bank():
    routingNumber = 0
    while len(str(routingNumber)) < 9:
        routingNumber = helpers.generate_routing()

    return {
        "routingNumber": routingNumber,
        "address": fake.street_address(),
        "city": fake.city(),
        "state": fake.state_abbr(),
        "zipcode": fake.zipcode()
    }

def create_branch(bankId):
    return {
        "bankID": bankId,
        "name": random.choice(helpers.bank_names),
        "address": fake.street_address(),
        "phone": helpers.generate_phone(),
        "city": fake.city(),
        "state": fake.state_abbr(),
        "zipcode": fake.zipcode()
    }
    
def create_transaction(account_number, value=0):
    type = random.choice([
            "DEPOSIT",
            "WITHDRAWAL",
            "TRANSFER_IN",
            "TRANSFER_OUT",
            "PURCHASE",
            "PAYMENT",
            "REFUND"])
    method = random.choice([
            "ACH",
            "ATM",
            "DEBIT_CARD",
            "APP"])
    if value == 0:
        value = round(random.randint(100,1200000))
    else:
        type = "DEPOSIT"
        method = "ATM"

    return {
        "type": type,
        "method": method,
        "amount": value,
        "merchantCode": "ALINE",
        "description": f"{type} transaction using method: {method}",
        "accountNumber": account_number
    }
