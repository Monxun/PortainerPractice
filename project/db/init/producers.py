import re
import string
import secrets
import random
import requests
from random import randint
from datetime import datetime


import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy import select
from sqlalchemy.orm import session
from  sqlalchemy.sql.expression import func

from models import (
    Applicant, 
    Bank, 
    Merchant, 
    Application, 
    Branch,
    Member,
    Account,
    User,
    OneTimePasscode,
    Transaction,
    UserRegistrationToken
)

from utils import random_bank_name, random_address, random_middle_name

from faker import Faker


#################################################
# DATABASE CONNECTOR

engine = sqlalchemy.create_engine(
    'mysql+pymysql://user:root@localhost:3306/alinedb',
    echo=True
)

inspector = inspect(engine)

for table_name in inspector.get_table_names():
    print(table_name)

#################################################
# DATA PRODUCER

fake = Faker()

Session = session.sessionmaker()
Session.configure(bind=engine)
my_session = Session()

# APPLICANT
def create_applicants(count=10):
    for _ in range(count):
        
        applicant = fake.profile()

        street, city, state, zipcode = random_address()
        middle_name = random_middle_name(applicant)

        applicant_dict = {
            'address': street,
            'city': city,
            'created_at': datetime.now(),
            'date_of_birth': applicant['birthdate'],
            'drivers_license': ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)),
            'email': fake.free_email(),
            'first_name': applicant['name'].split(' ')[0],
            'gender': applicant['sex'],
            'income': random.randrange(5000, 500000),
            'last_modified_at': fake.date_between(start_date='-10y', end_date='today'),
            'last_name': applicant['name'].split(' ')[1],
            'mailing_address': street,
            'mailing_city': city,
            'mailing_state': state,
            'mailing_zipcode': zipcode,
            'middle_name': middle_name,
            'phone': fake.phone_number(),
            'social_security': applicant['ssn'],
            'state': state,
            'zipcode': zipcode,
        }

        # my_session.add(applicant)
        # my_session.commit()


# BANK
def create_banks(count=5):
    for _ in range(count):

        street, city, state, zipcode = random_address()

        bank_dict = {
            'address': street,
            'city': city,
            'routing_number': fake.aba(),
            'state': state,
            'zipcode': zipcode
        }

        # my_session.add(bank)
        # my_session.commit()


# MERCHANT
def create_merchants(count=5):
    for _ in range(count):

        street, city, state, zipcode = random_address()

        merchant_dict = {
            'code': int(''.join(["{}".format(randint(0, 9)) for num in range(0, 8)])),
            'address': street,
            'city': city,
            'description': fake.bs(),
            'name': fake.company(),
            'registered_at': datetime.now(),
            'state': state,
            'zipcode': zipcode
        }
        # my_session.add(merchant)
        # my_session.commit()


# APPLICATION
def create_applications():

    types = ['Business', 'Personal', 'Non-Profit', 'Trust']

    for applicant in my_session.query(Applicant).all():

        application_dict = {
            'application_status': random.choice(['Denied','Active']),
            'application_type': random.choice(types),
            'primary_applicant_id': applicant.id,
        }

        # my_session.add(application)
        # my_session.commit()
    

# BRANCH
def create_branches(count=5):
    banks = my_session.query(Bank).all()
    print(banks)
    for _ in range(count):

        street, city, state, zipcode = random_address()

        branch_dict = {
            'address': street,
            'city': city,
            'name': fake.company(),
            'phone': fake.phone_number(),
            'state': state,
            'zipcode': zipcode,
            'bank_id': 3
        }

        # my_session.add(branch)
        # my_session.commit()


# MEMBER
def create_members():
    branch_ids = [branch.id for branch in my_session.query(Branch).all()]
    for application in my_session.query(Application).filter(Application.application_status=='Active'):
        

        member_dict = {
            'membership_id': ''.join(["{}".format(randint(0, 9)) for num in range(0, 12)]),
            'applicant_id': application.primary_applicant_id,
            'branch_id': random.choice(branch_ids)
        }

        # my_session.add(member)
        # my_session.commit()


# ACCOUNT
def create_accounts():
    for member in my_session.query(Member).all():

        print(f"member id: {member.id}")
        balance = random.randrange(-5000, 10000000)
        if balance >= 0:
            status = 'CURRENT'
        else:
            status = 'OVERDRAWN'

        account_dict = {
            'account_type': random.choice(['CHECKING', 'SAVING', 'CHECKING_AND_SAVINGS', 'CREDIT_CARD', 'LOAN']),
            'account_number': ''.join(["{}".format(randint(0, 9)) for num in range(0, 12)]),
            'balance': balance,
            'status': status,
            'available_balance': balance,
            'apy': round(random.uniform(0, 27), 2),
            'primary_account_holder_id': member.id
        }
        # my_session.add(account)
        # my_session.commit()


# USER
def create_users():
    for member in my_session.query(Member).all():
        print(member.membership_id)
        applicant = my_session.query(Applicant).get(member.applicant_id)

        user_dict = {
            'role': random.choice(['admin', 'member']),
            'enabled': fake.boolean(chance_of_getting_true=90),
            'password': secrets.token_hex(16),
            'username': fake.simple_profile()['username'],
            'email': applicant.email,
            'first_name': applicant.first_name,
            'last_name': applicant.last_name,
            'phone': applicant.phone,
            'member_id': member.id
        }
        # my_session.add(user)
        # my_session.commit()
        

# ONETIMEPASSCODE
def create_one_time_passcodes():
    for user in my_session.query(User).all():
        
        otp_dict = {
            'checked': int(fake.boolean(chance_of_getting_true=98)),
            'otp': secrets.token_hex(8),
            'user_id': user.id
        }
        # my_session.add(otp)
        # my_session.commit()


# TRANSACTIONS
def create_transactions(count=10):

    account_ids = [account.id for account in my_session.query(Account).all()]
    print(account_ids)
    merchant_codes = [merchant.code for merchant in my_session.query(Merchant).all()]
    print(merchant_codes)

    for _ in range(count):

        account_id = random.choice(account_ids)
        print(f"account id: {account_id}")
        account = my_session.query(Account).get(account_id)

        date = datetime.now()
        amount = round(random.uniform(0, 20000))

        print(f"account id: {account.id}, date: {date}, amount: {amount}")
        print(f"Description: {fake.bs()}")
        print(f"Balance: {account.balance}")
        print(f"Method: {random.choice(['ACH', 'ATM', 'CREDIT_CARD', 'DEBIT_CARD', 'APP'])}")
        print(f"Account: {random.choice(account_ids)}")
        print(f"Merchant Code: {random.choice(merchant_codes)}")

        transaction_dict = {
            'amount': amount,
            'date': datetime.now(),
            'description': fake.bs(),
            'initial_balance': account.balance,
            'last_modified': datetime.now(),
            'method': random.choice(['ACH', 'ATM', 'CREDIT_CARD', 'DEBIT_CARD', 'APP']),
            'posted_balance': amount,
            'state': fake.state_abbr(),
            'status': random.choice(['COMPLETED', 'DECLINED']),
            'type': random.choice(['DEPOSIT', 'WITHDRAWAL', 'TRANSFER_IN', 'TRANSFER_OUT', 'PURCHASE', 'PAYMENT', 'REFUND', 'VOID']),
            'account_id': account.id,
            'merchant_code': random.choice(merchant_codes)
        }
        # my_session.add(transaction)
        # my_session.commit()


def create_user_registration_tokens():
    for user in my_session.query(User).all():
        
        urt_dict = {
            'token': secrets.token_hex(16),
            'created': fake.date_between(start_date='-10y', end_date='today'),
            'expiration_delay': 30,
            'user_id': user.id,
        }
        # my_session.add(urt)
        # my_session.commit()


if __name__ == '__main__':
    create_applicants()
    create_banks()
    create_merchants()
    create_applications()
    create_branches()
    create_members()
    create_accounts()
    create_users()
    create_one_time_passcodes()
    create_transactions()
    create_user_registration_tokens()

    my_session.close()