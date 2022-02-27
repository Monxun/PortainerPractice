from urllib import response
from cryptography.hazmat.primitives import serialization
from flask_login import user_logged_in
from dotenv import load_dotenv
import os
import requests
import jwt


from helpers import helpers
import random
import Producers

from faker import Faker
import json

load_dotenv()

fake = Faker()

main_logger = helpers.create_logger("alinedb_dataproducer_main", "logs/main.log", 'w')


#####################
### Setup Headers ###
#####################
headers = {
    'Content-type':'application/json',
    'Accept':'application/json'
}

private_key = open('/Users/monxu/.ssh/id_rsa', 'r').read()
key = serialization.load_ssh_private_key(private_key.encode(), password=b'aline')

authenticated_header = {
    'Content-type':'application/json',
    'Accept':'application/json',
    'Authorization': 'Bearer '
}

jwt_secret_key = os.getenv('JWT_SECRET_KEY')

applications_url = "http://localhost:8071/applications"
registration_url = "http://localhost:8070/users/registration"
login_url = "http://localhost:8070/login"

# Requires bearer token
bank_url = "http://localhost:8083/banks"
branch_url = "http://localhost:8083/branches"
transaction_url = "http://localhost:8073/transactions"

########################
###  POST  Functions ###
########################

### Unprotected routes ###
def application_post(application):
    main_logger.info('ATTEMPTING TO CREATE APPLICATION FROM...')
    main_logger.info(json.dumps(application))

    token = jwt.encode(payload=application, key=jwt_secret_key)
    authenticated_header['Authorization'] = f'Bearer {token}'
    response = requests.post(applications_url, json=application, headers=headers)

    main_logger.info(f'response status code: {response.status_code}')
    main_logger.info(f'response text: {(response.text)}')
    main_logger.info(f'response headers {(response.headers)}')

    return json.loads(response.text)

def user_post(user):
    main_logger.info(f'User data: {json.dumps(user)}')
    response = requests.post(registration_url, json=user, headers=headers)

    main_logger.info(f'response status code: {response.status_code}')
    main_logger.info(f'response text: {(response.text)}')
    main_logger.info(f'response headers {(response.headers)}')
    return json.loads(response.text)

def user_login(user):
    main_logger.info(f'ATTEMPTING TO LOGIN {user["role"]} USER {user["username"]}...')
    response = requests.post(login_url, json={"username": user["username"], "password": user["password"]}, headers=headers)
    main_logger.info(f'response status code: {response.status_code}')
    main_logger.info(f'response text: {(response.text)}')
    main_logger.info(f'response headers {(response.headers)}')
    return response.headers

### Protected routes ###
def bank_post(bank):
    main_logger.info(f'Bank data: {json.dumps(bank)}')
    response = requests.post(bank_url, json=bank, headers=authenticated_header)

    main_logger.info(f'response status code: {response.status_code}')
    main_logger.info(f'response text: {(response.text)}')
    main_logger.info(f'response headers {(response.headers)}')
    return json.loads(response.text)

def branch_post(branch):
    main_logger.info(f'Branch data: {json.dumps(branch)}')
    response = requests.post(branch_url, json=branch, headers=authenticated_header)

    main_logger.info(f'response status code: {response.status_code}')
    main_logger.info(f'response text: {(response.text)}')
    main_logger.info(f'response headers {(response.headers)}')
    return json.loads(response.text)

def transaction_post(transaction):
    main_logger.info(f'Transaction data: {json.dumps(transaction)}')
    response = requests.post(transaction_url, json=transaction, headers=authenticated_header)

    main_logger.info(f'response status code: {response.status_code}')
    main_logger.info(f'response text: {(response.text)}')
    main_logger.info(f'response headers {(response.headers)}')
    return json.loads(response.text)

### PRODUCERS ###

user = Producers.create_admin()
user_post(user)
login_response = user_login(user)
authenticated_header['Authorization'] = login_response['Authorization']
bank = Producers.create_bank()
bank_response = bank_post(bank)
branch = Producers.create_branch(bank_response["id"])
branch = branch_post(branch)

application = Producers.create_application()
application_response = application_post(application)
member = Producers.create_member(application_response)
user_post(member)

if "createdAccounts" in application_response:
    account_number = application_response["createdAccounts"][0]["accountNumber"]
    transaction = Producers.create_transaction(account_number)
    transaction_response = transaction_post(transaction)