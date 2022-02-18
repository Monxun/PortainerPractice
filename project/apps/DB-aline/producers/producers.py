import re
import random
import string
from random import randint
import secrets

import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import session

from models import *
from utils import random_bank_name

from faker import Faker


#################################################
# DATABASE CONNECTOR

engine = sqlalchemy.create_engine(
    'mysql+mysqlconnector://user:root@localhost:3306/alinedb',
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

def create_applicants(count=100):
    for i in range(count):
        
        applicant = fake.profile()

        address = applicant['address']
        line2 = address.split('\n')[1]

        street = address.split('\n')[0]
        city, state, zipcode = tuple(re.split(', |,| ', line2))

        if applicant['sex'] == 'M':
            middle_name = fake.name_male().split(' ')[0]
        else:
            middle_name = fake.name_female().split(' ')[0]


        applicant = Applicant(
            address=street,
            city=city,
            date_of_birth=applicant['birthdate'],
            drivers_license=''.join(random.choices(string.ascii_uppercase + string.digits, k=8)),
            email=applicant['email'],
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

        session.add(applicant)


def create_banks(count=10):
    for _ in range(count):

        address = fake.address()
        line2 = address.split('\n')[1]

        street = address.split('\n')[0]
        city, state, zipcode = tuple(re.split(', |,| ', line2))

        bank = Bank(
            address=street,
            city=city,
            routing_number=fake.aba(),
            state=state,
            zipcode=zipcode
        )

        session.add(bank)


def create_merchants(count=50):
    for _ in range(count):

        address = fake.address()
        line2 = address.split('\n')[1]

        street = address.split('\n')[0]
        city, state, zipcode = tuple(re.split(', |,| ', line2))

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

        session.add(merchant)


def create_applications():

    statuses = ['New', 'Pending', 'Approved', 'Denied', 'Needs Review', 'Active']
    types = ['Business', 'Personal', 'Non-Profit', 'Trust']

    for applicant in session.query(Applicant).order_by(Applicant.id):

        application = Application(
            application_status=random.choice(statuses),
            application_type=random.choice(types),
            primary_applicant_id=applicant.id,
        )

        session.add(application)
    
        

def create_branches(count=50):
    banks = session.query(Bank).all()
    for _ in range(count):

        address = fake.address()
        line2 = address.split('\n')[1]

        street = address.split('\n')[0]
        city, state, zipcode = tuple(re.split(', |,| ', line2))

        branch = Branch(
            address=street,
            city=city,
            name=fake.company(),
            phone=fake.phone_number(),
            state=state,
            zipcode=zipcode,
            bank_id=random.shuffle(banks)[0]
        )

        session.add(branch)


def create_members():
    branches = session.query(Branch).all()
    for application in session.query(Application).filter(Application.application_status=='Active'):
        
        member = Member(
            membership_id=''.join(["{}".format(randint(0, 9)) for num in range(0, 12)]),
            applicant_id=application.primary_applicant_id,
            branch_id=random.shuffle(branches)[0]
        )

        session.add(member)


def create_accounts():
    for application in session.query(Application).filter(Application.application_status=='Active'):
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
            primary_account_holder_id=session.query(Members).filter(application.primary_application_id)
        )

        session.add(account)


def create_users():
    for member in session.query(Member).all():

        applicant = session.query(Applicant).filter(id=member.applicant_id)

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

        session.add(user)
        

def create_one_time_passcodes():
    for user in session.query(User).all():
        
        otp = OneTimePasscode(
            checked=int(fake.boolean(chance_of_getting_true=98)),
            otp=secrets.token_hex(8),
            user_id=user.id
        )

        session.add(otp)


def create_transactions(count=1000):

    accounts = session.query(Account).all()
    merchants = session.query(Merchant).all()

    for _ in range(count):

        account = random.shuffle(accounts)[0]
        merchant = random.shuffle(merchants)[0]
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
            state=fake.state_abbr()
            type=random.choice(['DEBIT', 'CREDIT']),
            account=account,
            merchant_code=merchant.code
        )
        
        session.add(transaction)


def create_user_registration_tokens(count=200):
    for user in session.query(User).all():
        
        urt = UserRegistrationToken(
            token=secrets.token_hex(16),
            created=fake.date_between(start_date='-10y', end_date='today'),
            expiration_delay=30,
            user_id=user.id,
        )

        session.add(urt)


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
