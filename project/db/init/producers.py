import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import session

#################################################
# DATABASE CONNECTOR

engine = sqlalchemy.create_engine(
    'mysql+mysqlconnector://username:password@localhost:3306/alinedb',
    echo=True
)

inspector = inspect(engine)

for table_name in inspector.get_table_names():
    print(table_name)

#################################################
# DATA PRODUCER

Session = session.sessionmaker()
Session.configure(bind=engine)
my_session = Session()