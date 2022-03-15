# import os

# BANK_URL = os.environ['BANK_URL']
# TRANSACTION_URL = os.environ['TRANSACTION_URL']
# UNDERWRITER_URL = os.environ['UNDERWRITER_URL']
# USER_URL = os.environ['USER_URL']

# applications_url = f"http://{UNDERWRITER_URL}/applications"
# registration_url = f"http://{USER_URL}/users/registration"
# login_url = f"http://{USER_URL}/login"

# # Requires bearer token
# bank_url = f"http://{BANK_URL}/banks"
# branch_url = f"http://{BANK_URL}/branches"
# transaction_url = f"http://{TRANSACTION_URL}/transactions"

# Kubernetes ingress
applications_url = "http://aline-financial.com/applications"
registration_url = "http://aline-financial.com/users/registration"
login_url = "http://aline-financial.com/login"

# Requires bearer token
bank_url = "http://aline-financial.com/banks"
branch_url = "http://aline-financial.com/branches"
transaction_url = "http://aline-financial.com/transactions"