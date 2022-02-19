import re
import random
import string
from random import randint
import secrets

import sqlalchemy
from sqlalchemy import inspect
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
    for i in range(count):
        
        applicant = fake.profile()

        street, city, state, zipcode = random_address()
        middle_name = random_middle_name(applicant)

        applicant = Applicant(
            address=street,
            city=city,
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
def create_banks(count=5):
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
def create_merchants(count=5):
    for _ in range(count):

        street, city, state, zipcode = random_address()

        merchant = Merchant(
            code=int(''.join(["{}".format(randint(0, 9)) for num in range(0, 8)])),
            address=street,
            city=city,
            description=fake.bs(),
            name=fake.company(),
            registered_at=fake.date_between(start_date='-30y', end_date='today'),
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
def create_branches(count=5):
    banks = my_session.query(Bank).all()
    print(banks)
    for _ in range(count):

        street, city, state, zipcode = random_address()

        branch = Branch(
            address=street,
            city=city,
            name=fake.company(),
            phone=fake.phone_number(),
            state=state,
            zipcode=zipcode,
            bank_id=3
        )

        my_session.add(branch)
        my_session.commit()


# MEMBER
def create_members():
    branch_ids = [id for id in my_session.query(Branch.id).distinct()]
    for application in my_session.query(Application).filter(Application.application_status=='Active'):
        

        member = Member(
            membership_id=''.join(["{}".format(randint(0, 9)) for num in range(0, 12)]),
            applicant_id=application.primary_applicant_id,
            branch_id=4
        )

        my_session.add(member)
        my_session.commit()


# ACCOUNT
def create_accounts():
    for application in my_session.query(Application).filter(Application.application_status=='Active'):
        balance = random.randrange(-5000, 10000000)
        if balance >= 0:
            status = 'CURRENT'
        else:
            status = 'OVERDRAWN'

        account = Account(
            account_type=application.application_type,
            account_number=''.join(["{}".format(randint(0, 9)) for num in range(0, 12)]),
            balance=balance,
            status=status,
            available_balance=balance,
            apy=round(random.uniform(0, 27), 2),
            primary_account_holder_id=my_session.query(Member).filter(application.primary_application_id)
        )

        my_session.add(account)
        my_session.commit()


# USER
def create_users():
    for member in my_session.query(Member).all():
        applicant = my_session.query(Applicant).filter(id=member.applicant_id)

        user = User(
            role=random.choice(['User', 'Admin']),
            enabled=fake.boolean(chance_of_getting_true=90),
            password=secrets.token_hex(16),
            username=applicant.username,
            email=applicant.email,
            first_name=applicant.first_name,
            last_name=applicant.last_name,
            phone=applicant.phone,
            member_id=member.membership_id
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
def create_transactions(count=10):

    account_ids = [id for id in my_session.query(Account.id).distinct()]
    merchant_codes = [id for id in my_session.query(Merchant.code).distinct()]

    for _ in range(count):

        account_id = random.shuffle(account_ids)
        account = my_session.query(Account).filter_by(Account.id==account_id).all()

        date = fake.date_between(start_date='-1y', end_date='today')
        amount = round(random.uniform(0, 20000), 2)

        transaction = Transaction(
            amount=amount,
            date=date,
            description=fake.bs(),
            initial_balance=account.balance,
            last_modified=fake.date_between(start_date='-1y', end_date='today'),
            method=random.choice(['DEBIT', 'CREDIT']),
            posted_balance=amount,
            state=fake.state_abbr(),
            type=random.choice(['DEBIT', 'CREDIT']),
            account=random.shuffle(account_ids)[0],
            merchant_code=random.shuffle(merchant_codes)[0]
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