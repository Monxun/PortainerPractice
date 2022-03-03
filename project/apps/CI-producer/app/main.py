from helpers import helpers
import Producers
import Posts

main_logger = helpers.create_logger("alinedb_dataproducer_main", "logs/main.log", 'w')

#####################
### Setup Headers ###
#####################
header = {
    'Content-type':'application/json',
    'Accept':'application/json'
}

authenticated_header = {
    'Content-type':'application/json',
    'Accept':'application/json',
    'Authorization': ''
}

### CREATE DATA AND POST ###
### Create an admin user, log that user in and grab the Bearer token from the response Authorization header. ###
user = Producers.create_admin()
Posts.user_post(main_logger, user, header)
login_response = Posts.user_login(main_logger, user, header)
authenticated_header['Authorization'] = login_response['Authorization']

## Create a bank based on the authenticated administrator ##
bank = Producers.create_bank()
bank_response = Posts.bank_post(main_logger, bank, authenticated_header)

## Create a branch based on the authenticated administrator ##
branch = Producers.create_branch(bank_response["id"])
branch = Posts.branch_post(main_logger, branch, authenticated_header)

## Create an application and create a member based off that response.
application = Producers.create_application()
application_response = Posts.application_post(main_logger, application, header)
member = Producers.create_member(application_response)
Posts.user_post(main_logger, member, header)

## Check if there is a createdAccounts key in the application_response. If there is then we can create transactions for it. ##
if "createdAccounts" in application_response:
    account_number = application_response["createdAccounts"][0]["accountNumber"]
    # Deposit 50,000.00 into the account before creating a random transaction on this account.
    # The API will automatically deny transactions which would cause the account to become negative.
    deposit = Producers.create_transaction(account_number, 5000000)
    transaction = Producers.create_transaction(account_number)
    deposit_response = Posts.transaction_post(main_logger, deposit, authenticated_header)
    transaction_response = Posts.transaction_post(main_logger, transaction, authenticated_header)