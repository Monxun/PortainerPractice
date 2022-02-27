from urllib import response
from flask_login import user_logged_in
from dotenv import load_dotenv
import requests
import helper
import random
import producer
from faker import Faker
import json
import os

fake = Faker()

main_logger = helper.create_logger("alinedb_dataproducer_main", "main.log", 'w')

load_dotenv()


#####################
### Setup Headers ###
#####################
headers = {
    'Content-type':'application/json',
    'Accept':'application/json'
}

jwt = os.getenv('JWT_SECRET_KEY')

authenticated_header = {
    'Content-type':'application/json',
    'Accept':'application/json',
    'Authorization': ''
}

bank_url = 'http://localhost:8083'
transaction_url = 'http://localhost:8073'
underwriter_url = 'http://localhost:8071'
user_url = 'http://localhost:8070'

#####################
##### ENDPOINTS #####
#####################

applications_url = f"{underwriter_url}/applications"
registration_url = f"{user_url}/users/registration"
login_url = f"{user_url}/login"

# Requires bearer token
bank_url = f"{bank_url}/banks"
branch_url = f"{bank_url}/branches"
transaction_url = f"{transaction_url}/transactions"

########################
###  POST  Functions ###
########################

### Unprotected routes ###
def application_post(application):
    main_logger.info('ATTEMPTING TO CREATE APPLICATION FROM...')
    main_logger.info(json.dumps(application))
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

user = producer.create_admin()
user_post(user)
login_response = user_login(user)
authenticated_header['Authorization'] = login_response['Authorization']
bank = producer.create_bank()
bank_response = bank_post(bank)
print(bank_response)
branch = producer.create_branch(bank_response["id"])
branch = branch_post(branch)

application = producer.create_application()
application_response = application_post(application)
print(application_response)
member = producer.create_member(application_response)
user_post(member)

if "createdAccounts" in application_response:
    account_number = application_response["createdAccounts"][0]["accountNumber"]
    transaction = producer.create_transaction(account_number)
    transaction_response = transaction_post(transaction)