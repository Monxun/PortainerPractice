import requests
import json
import constants

########################
###  POST  Functions ###
########################

### Unprotected routes ###
def application_post(logger, application, header):
    logger.info('ATTEMPTING TO CREATE APPLICATION FROM...')
    logger.info(json.dumps(application))
    response = requests.post(constants.applications_url, json=application, headers=header)
    log_response(logger, response)
    return json.loads(response.text)

def user_post(logger, user, header):
    logger.info(f'User data: {json.dumps(user)}')
    response = requests.post(constants.registration_url, json=user, headers=header)
    log_response(logger, response)
    return json.loads(response.text)

def user_login(logger, user, header):
    logger.info(f'ATTEMPTING TO LOGIN {user["role"]} USER {user["username"]}...')
    response = requests.post(constants.login_url, json={"username": user["username"], "password": user["password"]}, headers=header)
    log_response(logger, response)
    return response.headers

### Protected routes ###
def bank_post(logger, bank, authenticated_header):
    logger.info(f'Bank data: {json.dumps(bank)}')
    response = requests.post(constants.bank_url, json=bank, headers=authenticated_header)
    log_response(logger, response)
    return json.loads(response.text)

def branch_post(logger, branch, authenticated_header):
    logger.info(f'Branch data: {json.dumps(branch)}')
    response = requests.post(constants.branch_url, json=branch, headers=authenticated_header)
    log_response(logger, response)
    return json.loads(response.text)

def transaction_post(logger, transaction, authenticated_header):
    logger.info(f'Transaction data: {json.dumps(transaction)}')
    response = requests.post(constants.transaction_url, json=transaction, headers=authenticated_header)
    log_response(logger, response)
    return json.loads(response.text)

def log_response(logger, response):
    logger.info(f'response status code: {response.status_code}')
    logger.info(f'response text: {(response.text)}')
    logger.info(f'response headers {(response.headers)}')
