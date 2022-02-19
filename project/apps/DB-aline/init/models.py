

from sqlalchemy import BigInteger, Column, Date, Float, ForeignKey, Integer, String, Table
from sqlalchemy.dialects.mysql import BIT, DATETIME
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


t_account_sequence = Table(
    'account_sequence', metadata,
    Column('next_val', BigInteger)
)


class Applicant(Base):
    __tablename__ = 'applicant'

    id = Column(BigInteger, primary_key=True)
    address = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    created_at = Column(DATETIME(fsp=6))
    date_of_birth = Column(Date, nullable=False)
    drivers_license = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    first_name = Column(String(255), nullable=False)
    gender = Column(String(255), nullable=False)
    income = Column(Integer, nullable=False)
    last_modified_at = Column(DATETIME(fsp=6))
    last_name = Column(String(255), nullable=False)
    mailing_address = Column(String(255), nullable=False)
    mailing_city = Column(String(255), nullable=False)
    mailing_state = Column(String(255), nullable=False)
    mailing_zipcode = Column(String(255), nullable=False)
    middle_name = Column(String(255))
    phone = Column(String(255), nullable=False, unique=True)
    social_security = Column(String(255), nullable=False, unique=True)
    state = Column(String(255), nullable=False)
    zipcode = Column(String(255), nullable=False)

    applications = relationship('Application', secondary='application_applicant')


class Bank(Base):
    __tablename__ = 'bank'

    id = Column(BigInteger, primary_key=True)
    address = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    routing_number = Column(String(9), nullable=False)
    state = Column(String(255), nullable=False)
    zipcode = Column(String(255))


class Merchant(Base):
    __tablename__ = 'merchant'

    code = Column(String(8), primary_key=True)
    address = Column(String(255))
    city = Column(String(255))
    description = Column(String(255))
    name = Column(String(150), nullable=False)
    registered_at = Column(DATETIME(fsp=6))
    state = Column(String(255))
    zipcode = Column(String(255))


t_otp_sequence = Table(
    'otp_sequence', metadata,
    Column('next_val', BigInteger)
)


class Application(Base):
    __tablename__ = 'application'

    id = Column(BigInteger, primary_key=True)
    application_status = Column(String(255), nullable=False)
    application_type = Column(String(255), nullable=False)
    primary_applicant_id = Column(ForeignKey('applicant.id'), nullable=False, index=True)

    primary_applicant = relationship('Applicant')


class Branch(Base):
    __tablename__ = 'branch'

    id = Column(BigInteger, primary_key=True)
    address = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    phone = Column(String(255), unique=True)
    state = Column(String(255))
    zipcode = Column(String(255))
    bank_id = Column(ForeignKey('bank.id'), index=True)

    bank = relationship('Bank')


t_application_applicant = Table(
    'application_applicant', metadata,
    Column('application_id', ForeignKey('application.id'), primary_key=True, nullable=False),
    Column('applicant_id', ForeignKey('applicant.id'), primary_key=True, nullable=False, index=True)
)


class Member(Base):
    __tablename__ = 'member'

    id = Column(BigInteger, primary_key=True)
    membership_id = Column(String(255), unique=True)
    applicant_id = Column(ForeignKey('applicant.id'), nullable=False, unique=True)
    branch_id = Column(ForeignKey('branch.id'), nullable=False, index=True)

    applicant = relationship('Applicant')
    branch = relationship('Branch')


class Account(Base):
    __tablename__ = 'account'

    account_type = Column(String(31), nullable=False)
    id = Column(BigInteger, primary_key=True)
    account_number = Column(String(255), unique=True)
    balance = Column(Integer, nullable=False)
    status = Column(String(255))
    available_balance = Column(Integer)
    apy = Column(Float)
    primary_account_holder_id = Column(ForeignKey('member.id'), nullable=False, index=True)

    primary_account_holder = relationship('Member')
    members = relationship('Member', secondary='account_holder')


class User(Base):
    __tablename__ = 'user'

    role = Column(String(31), nullable=False)
    id = Column(BigInteger, primary_key=True)
    enabled = Column(BIT(1), nullable=False)
    password = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    email = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    phone = Column(String(255))
    member_id = Column(ForeignKey('member.id'), index=True)

    member = relationship('Member')


t_account_holder = Table(
    'account_holder', metadata,
    Column('member_id', ForeignKey('member.id'), primary_key=True, nullable=False),
    Column('account_id', ForeignKey('account.id'), primary_key=True, nullable=False, index=True)
)


class OneTimePasscode(Base):
    __tablename__ = 'one_time_passcode'

    id = Column(Integer, primary_key=True)
    checked = Column(BIT(1), nullable=False)
    otp = Column(String(255))
    user_id = Column(ForeignKey('user.id'), nullable=False, unique=True)

    user = relationship('User')


class Transaction(Base):
    __tablename__ = 'transaction'

    id = Column(BigInteger, primary_key=True)
    amount = Column(Integer, nullable=False)
    date = Column(DATETIME(fsp=6))
    description = Column(String(255))
    initial_balance = Column(Integer, nullable=False)
    last_modified = Column(DATETIME(fsp=6))
    method = Column(String(255), nullable=False)
    posted_balance = Column(Integer)
    state = Column(String(255), nullable=False)
    status = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    account_id = Column(ForeignKey('account.id'), nullable=False, index=True)
    merchant_code = Column(ForeignKey('merchant.code'), index=True)

    account = relationship('Account')
    merchant = relationship('Merchant')


class UserRegistrationToken(Base):
    __tablename__ = 'user_registration_token'

    token = Column(String(255), primary_key=True)
    created = Column(DATETIME(fsp=6))
    expiration_delay = Column(BigInteger, nullable=False)
    user_id = Column(ForeignKey('user.id'), nullable=False, unique=True)

    user = relationship('User')