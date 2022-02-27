from os import strerror
import os
import pytest
import datetime

import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy import select
from sqlalchemy.orm import session
from  sqlalchemy.sql.expression import func

#################################################
# DATABASE CONNECTOR
user = os.environ['DB_USERNAME']
password = os.environ['DB_PASSWORD']
host = os.environ['DB_HOST']
port = os.environ['DB_PORT']
name = os.environ['DB_NAME']

engine = sqlalchemy.create_engine(
    f'mysql+pymysql://{user}:{password}@{host}:{port}/{name}',
    echo=True
)

inspector = inspect(engine)

for table_name in inspector.get_table_names():
    print(table_name)

Session = session.sessionmaker()
Session.configure(bind=engine)
my_session = Session()

#################################################
# TEST

'''
Module to test producers.py
'''

from producers import (
    create_applicants,
    create_banks,
    create_merchants,
    create_applications,
    create_branches,
    create_members,
    create_accounts,
    create_users,
    create_one_time_passcodes,
    create_transactions,
    create_user_registration_tokens
)

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


def test_create_applicants() -> None:

    test_object = my_session.query(Applicant).first()

    assert isinstance(test_object.id, int)
    assert isinstance(test_object.address, str)
    assert isinstance(test_object.city, str)
    assert isinstance(test_object.created_at, datetime.datetime)
    assert isinstance(test_object.date_of_birth, datetime.date)
    assert isinstance(test_object.drivers_license, str)
    assert isinstance(test_object.email, str) 
    assert isinstance(test_object.first_name, str)
    assert isinstance(test_object.gender, str)
    assert isinstance(test_object.income, int) 
    assert isinstance(test_object.last_modified_at_at, datetime.datetime) 
    assert isinstance(test_object.last_name, str)
    assert isinstance(test_object.mailing_address, str)
    assert isinstance(test_object.mailing_city, str)
    assert isinstance(test_object.mailing_state, str)
    assert isinstance(test_object.mailing_zipcode, str)
    assert isinstance(test_object.middle_name, str)
    assert isinstance(test_object.phone, str)
    assert isinstance(test_object.social_security, str)
    assert isinstance(test_object.state, str)
    assert isinstance(test_object.zipcode, str)


def test_create_banks() -> None:

    test_object = my_session.query(Bank).first()

    assert isinstance(test_object.id, int)
    assert isinstance(test_object.address, str)
    assert isinstance(test_object.city, str)
    assert isinstance(test_object.routing_number, str)
    assert isinstance(test_object.state, str)
    assert isinstance(test_object.zipcode, str)


def test_create_merchants() -> None:

    test_object = my_session.query(Merchant).first()


    assert isinstance(test_object.code, str)
    assert isinstance(test_object.address, str)
    assert isinstance(test_object.city, str)
    assert isinstance(test_object.description, str)
    assert isinstance(test_object.name, str)
    assert isinstance(test_object.registered_at, datetime.datetime)
    assert isinstance(test_object.state, str)
    assert isinstance(test_object.zipcode, str)


def test_create_applications() -> None:
    
    test_object = my_session.query(Application).first()

    assert isinstance(test_object.id, int)
    assert isinstance(test_object.application_status, str)
    assert isinstance(test_object.application_type, str)
    assert isinstance(test_object.primary_applicant_id, int)


def test_create_branches() -> None:
    
    test_object = my_session.query(Branch).first()

    assert isinstance(test_object.id, int)
    assert isinstance(test_object.address, str)
    assert isinstance(test_object.city, str)
    assert isinstance(test_object.name, str)
    assert isinstance(test_object.phone, str)
    assert isinstance(test_object.state, str)
    assert isinstance(test_object.zipcode, str)
    assert isinstance(test_object.bank_id, int)


def test_create_members() -> None:
    
    test_object = my_session.query(Member).first()

    assert isinstance(test_object.id, int)
    assert isinstance(test_object.membership_id, str)
    assert isinstance(test_object.applicant_id, int)
    assert isinstance(test_object.branch_id, int)


def test_create_accounts() -> None:
    
    test_object = my_session.query(Account).first()

    assert isinstance(test_object.account_type, str)
    assert isinstance(test_object.id, int)
    assert isinstance(test_object.account_number, str)
    assert isinstance(test_object.balance, int)
    assert isinstance(test_object.status, str)
    assert isinstance(test_object.available_balance, int)
    assert isinstance(test_object.apy, float)
    assert isinstance(test_object.primary_account_holder_id, int)


def test_create_users() -> None:

    test_object = my_session.query(User).first()

    assert isinstance(test_object.role, str)
    assert isinstance(test_object.id, int)
    assert isinstance(test_object.enabled, int)
    assert isinstance(test_object.password, str)
    assert isinstance(test_object.username, str)
    assert isinstance(test_object.email, str)
    assert isinstance(test_object.first_name, str)
    assert isinstance(test_object.last_name, str)
    assert isinstance(test_object.phone, str)
    assert isinstance(test_object.member_id, int)


def test_create_one_time_passcodes() -> None:
    
    test_object = my_session.query(OneTimePasscode).first()

    assert isinstance(test_object.id, int)
    assert isinstance(test_object.checked, int)
    assert isinstance(test_object.otp, str)
    assert isinstance(test_object.user_id, int)


def test_create_transactions() -> None:
    
    test_object = my_session.query(Transaction).first()

    assert isinstance(test_object.id, int)
    assert isinstance(test_object.amount, int)
    assert isinstance(test_object.date, datetime.datetime)
    assert isinstance(test_object.description, str)
    assert isinstance(test_object.initial_balance, int)
    assert isinstance(test_object.last_modified, datetime.date)
    assert isinstance(test_object.method, str)
    assert isinstance(test_object.posted_balance, int)
    assert isinstance(test_object.state, str)
    assert isinstance(test_object.status, str)
    assert isinstance(test_object.type, str)
    assert isinstance(test_object.account_id, int)
    assert isinstance(test_object.merchant_code, str)


def test_create_user_registration_tokens() -> None:
    
    test_object = my_session.query(UserRegistrationToken).first()

    assert isinstance(test_object.token, str)
    assert isinstance(test_object.created, datetime.datetime)
    assert isinstance(test_object.expiration_delay, int)
    assert isinstance(test_object.user_id, int)

