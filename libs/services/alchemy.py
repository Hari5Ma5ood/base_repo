import os

from sqlalchemy import create_engine, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

base = declarative_base()

#TODO: as it is not deployed and no DB is formed on any server so, needs to add this db in local server (No schema required for time being)

# database = os.environ.get('DB', 'alpine_portal')
# host = os.environ.get('HOST', "127.0.0.1") # '10.1.17.209')
# port = os.environ.get('PORT', 5432)
username = os.environ.get('DB_USER', 'postgres')
password = os.environ.get('DB_PASSWORD', 'postgres')
#
# engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')
# session = sessionmaker(bind=engine)
# session = session()

# TODO: NOTE -->> This section is just for testing
# query = 'select * from cr_units limit 10'
# returned_data = session.execute(text(query)) #TODO: Note-->> This is an old method but can be used
# returned_data = session.query(text("cr_units")).all() #Note -->> a table which is created here can be used without cascade
# for row in returned_data:
#     print(row)

# TODO: start making call from here

class Alchemy():
    def __init__(self):
        self.engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')
        session = sessionmaker(bind=self.engine)
        self.session = session()

    def get_table_data(self, table_name, query):
        try:
            query = 'select * from cr_units limit 10'
            returned_data = session.execute(text(query))
            for row in returned_data:
                print(row)
        except Exception as e:
            print(e)