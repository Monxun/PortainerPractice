import mysql.connector
from mysql.connector import errorcode
import os

##############################################################################
# INITIALIZE CURSOR AND CONNECT TO DB

user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']

try:

  cnx = mysql.connector.connect(
    host="localhost",
    user=user,
    password=password
  )

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

cursor = cnx.cursor()

##############################################################################
# CREATE DB AND TABLES

DB_NAME = 'users'

TABLES = {}
TABLES['users'] = (
    "CREATE TABLE `users` ("
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    ") ENGINE=InnoDB")

#CREATE DB
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

#CREATE TABLES
for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name))
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

##############################################################################
# POPULATE TABLES WITH FAKER

from faker import Faker
fake = Faker()

number_of_users = 100

for _ in range(number_of_users):
  first, last = fake.name().split(' ')
  cursor.execute(
            f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8'")


  # try:
  #   cursor.execute("USE {}".format(DB_NAME))
  # except mysql.connector.Error as err:
  #     print("Database {} does not exists.".format(DB_NAME))
  #     if err.errno == errorcode.ER_BAD_DB_ERROR:
  #         create_database(cursor)
  #         print("Database {} created successfully.".format(DB_NAME))
  #         cnx.database = DB_NAME
  #     else:
  #         print(err)
  #         exit(1)
