import re

import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import session
from models import 

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
        city, state, zipcode = re.split(', |,| ', line2)

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
        pass


def create_merchants(count=50):
    for _ in range(count):
        pass


def create_applications(count=200):
    for _ in range(count):
        pass


def create_branches(count=50):
    for _ in range(count):
        pass


def create_members(count=200):
    for _ in range(count):
        pass


def create_accounts(count=200):
    for _ in range(count):
        pass


def create_users(count=200):
    for _ in range(count):
        pass


def create_one_time_passcodes(count=200):
    for _ in range(count):
        pass


def create_transactions(count=200):
    for _ in range(count):
        pass


def create_user_registration_tokens(count=200):
    for _ in range(count):
        pass


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
