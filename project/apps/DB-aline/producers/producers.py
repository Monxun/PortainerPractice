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

        applicant = Applicant(
            address=fake.address()
        )


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
