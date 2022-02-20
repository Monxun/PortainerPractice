import re
import string
import secrets
import random
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

# SET COUNTS HERE
counts = {}
counts['applicants'] = 10
counts['banks'] = 5
counts['merchants'] = 5
counts['branches'] = 5
counts['transactions'] = 10


# APPLICANT
def create_applicants(count=counts['applicants']):
    for _ in range(count):
        
        applicant = fake.profile()

        street, city, state, zipcode = random_address()
        middle_name = random_middle_name(applicant)

        applicant = Applicant(
            address=street,
            city=city,
            created_at=datetime.now(),
            date_of_birth=applicant['birthdate'],
            drivers_license=''.join(random.choices(string.ascii_uppercase + string.digits, k=8)),
            email=fake.free_email(),
            first_name=applicant['name'].split(' ')[0],
            gender=applicant['sex'],
            income=random.randrange(5000, 500000),
            last_modified_at=fake.date_between(start_date='-10y', end_date='today'),
            last_name=applicant['name'].split(' ')[1],
            mailing_address=street,
            mailing_city=city,
            mailing_state=state,
            mailing_zipcode=zipcode,
            middle_name=middle_name,
            phone=fake.phone_number(),
            social_security=applicant['ssn'],
            state=state,
            zipcode=zipcode,
        )

        my_session.add(applicant)
    my_session.commit()


# BANK
def create_banks(count=counts['banks']):
    for _ in range(count):

        street, city, state, zipcode = random_address()

        bank = Bank(
            address=street,
            city=city,
            routing_number=fake.aba(),
            state=state,
            zipcode=zipcode
        )

        my_session.add(bank)
    my_session.commit()


# MERCHANT
def create_merchants(count=counts['merchants']):
    for _ in range(count):

        street, city, state, zipcode = random_address()

        merchant = Merchant(
            code=int(''.join(["{}".format(randint(0, 9)) for num in range(0, 8)])),
            address=street,
            city=city,
            description=fake.bs(),
            name=fake.company(),
            registered_at=datetime.now(),
            state=state,
            zipcode=zipcode
        )

        my_session.add(merchant)
    my_session.commit()


# APPLICATION
def create_applications():

    types = ['Business', 'Personal', 'Non-Profit', 'Trust']

    for applicant in my_session.query(Applicant).all():

        application = Application(
            application_status=random.choice(['Denied','Active']),
            application_type=random.choice(types),
            primary_applicant_id=applicant.id,
        )

        my_session.add(application)
    my_session.commit()
    

# BRANCH
def create_branches(count=counts['branches']):
    bank_ids = [bank.id for bank in my_session.query(Bank).all()]
    for _ in range(count):

        street, city, state, zipcode = random_address()

        branch = Branch(
            address=street,
            city=city,
            name=fake.company(),
            phone=fake.phone_number(),
            state=state,
            zipcode=zipcode,
            bank_id=random.choice(bank_ids)
        )

        my_session.add(branch)
    my_session.commit()


# MEMBER
def create_members():
    branch_ids = [branch.id for branch in my_session.query(Branch).all()]
    for application in my_session.query(Application).filter(Application.application_status=='Active'):
        
        member = Member(
            membership_id=''.join(["{}".format(randint(0, 9)) for num in range(0, 12)]),
            applicant_id=application.primary_applicant_id,
            branch_id=random.choice(branch_ids)
        )

        my_session.add(member)
    my_session.commit()


# ACCOUNT
def create_accounts():
    for member in my_session.query(Member).all():

        balance = random.randrange(-5000, 10000000)
        
        if balance >= 0:
            status = 'CURRENT'
        else:
            status = 'OVERDRAWN'

        account = Account(
            account_type=random.choice(['CHECKING', 'SAVING', 'CHECKING_AND_SAVINGS', 'CREDIT_CARD', 'LOAN']),
            account_number=''.join(["{}".format(randint(0, 9)) for num in range(0, 12)]),
            balance=balance,
            status=status,
            available_balance=balance,
            apy=round(random.uniform(0, 27), 2),
            primary_account_holder_id=member.id
        )
        my_session.add(account)
    my_session.commit()


# USER
def create_users():
    for member in my_session.query(Member).all():
        applicant = my_session.query(Applicant).get(member.applicant_id)

        user = User(
            role=random.choice(['admin', 'member']),
            enabled=fake.boolean(chance_of_getting_true=90),
            password=secrets.token_hex(16),
            username=fake.simple_profile()['username'],
            email=applicant.email,
            first_name=applicant.first_name,
            last_name=applicant.last_name,
            phone=applicant.phone,
            member_id=member.id
        )

        my_session.add(user)
    my_session.commit()
        

# ONETIMEPASSCODE
def create_one_time_passcodes():
    for user in my_session.query(User).all():
        
        otp = OneTimePasscode(
            checked=int(fake.boolean(chance_of_getting_true=98)),
            otp=secrets.token_hex(8),
            user_id=user.id
        )

        my_session.add(otp)
    my_session.commit()


# TRANSACTIONS
def create_transactions(count=counts['transactions']):

    account_ids = [account.id for account in my_session.query(Account).all()]
    merchant_codes = [merchant.code for merchant in my_session.query(Merchant).all()]

    for _ in range(count):

        account_id = random.choice(account_ids)
        account = my_session.query(Account).get(account_id)
        amount = round(random.uniform(0, 20000))

        transaction = Transaction(
            amount=amount,
            date=datetime.now(),
            description=fake.bs(),
            initial_balance=account.balance,
            last_modified=datetime.now(),
            method=random.choice(['ACH', 'ATM', 'CREDIT_CARD', 'DEBIT_CARD', 'APP']),
            posted_balance=amount,
            state=fake.state_abbr(),
            status=random.choice(['COMPLETED', 'DECLINED']),
            type=random.choice(['DEPOSIT', 'WITHDRAWAL', 'TRANSFER_IN', 'TRANSFER_OUT', 'PURCHASE', 'PAYMENT', 'REFUND', 'VOID']),
            account_id=account.id,
            merchant_code=random.choice(merchant_codes)
        )
        
        my_session.add(transaction)
    my_session.commit()


def create_user_registration_tokens():
    for user in my_session.query(User).all():
        
        urt = UserRegistrationToken(
            token=secrets.token_hex(16),
            created=fake.date_between(start_date='-10y', end_date='today'),
            expiration_delay=30,
            user_id=user.id,
        )

        my_session.add(urt)
    my_session.commit()


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