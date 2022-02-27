from faker import Faker
from helper import helper
import random

fake = Faker()

producer_logger = helper.create_logger("alinedb_dataproducer_Applicants", "./logs/data_producer.logs", "w")

def create_applicant():
    gender = random.choice(["MALE", "FEMALE"])
    name = helper.generate_name(gender)

    return {"firstName": name[0],
            "middleName": name[1],
            "lastName": name[2],
            "dateOfBirth": fake.date_of_birth(minimum_age=18).strftime(f'%Y-%m-%d'),
            "gender": gender,
            "email": fake.email(),
            "phone": helper.generate_phone(),
            "socialSecurity": fake.ssn(),
            "driversLicense": helper.generate_id(),
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
    name = helper.generate_name(helper.gender())

    return {
        "role": "admin",
        "username": helper.generate_username(),
        "password": f'Mypassa@dffsfa2',
        "firstName": name[0],
        "lastName": name[1],
        "email": fake.email(),
        "phone": helper.generate_phone()
    }

def create_member(application_response):
    return {
        "role": "member",
        "username": helper.generate_username(),
        "password": 'Mypassa@dffsfa2',
        "firstName": application_response['applicants'][0]['firstName'],
        "lastName": application_response['applicants'][0]['lastName'],
        "email": application_response['applicants'][0]['email'],
        "phone": application_response['applicants'][0]['phone'],
        "lastFourOfSSN": application_response['applicants'][0]['socialSecurity'][7:11],
        "membershipId": application_response['createdMembers'][0]['membershipId']
    }

def create_bank():
    return {
        "routingNumber": helper.generate_routing(),
        "address": fake.street_address(),
        "city": fake.city(),
        "state": fake.state_abbr(),
        "zipcode": fake.zipcode()
    }

def create_branch(bankId):
    return {
        "bankID": bankId,
        "name": random.choice(helper.bank_names),
        "address": fake.street_address(),
        "phone": helper.generate_phone(),
        "city": fake.city(),
        "state": fake.state_abbr(),
        "zipcode": fake.zipcode()
    }
    
def create_transaction(account_number):
    type = random.choice([
            "DEPOSIT",
            "WITHDRAWAL",
            "TRANSFER_IN",
            "TRANSFER_OUT",
            "PURCHASE",
            "PAYMENT",
            "REFUND",
            "VOID"])
    method = random.choice([
            "ACH",
            "ATM",
            "DEBIT_CARD",
            "APP"])
    return {
        "type": type,
        "method": method,
        "amount": round(random.randint(100,1200000)),
        "merchantCode": "ALINE",
        "description": f"{type} transaction using method: {method}",
        "accountNumber": account_number
    }