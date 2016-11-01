from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgres://root:12Ajrator@localhost/postgres')

session = DBSession()
with open('/static/data/db_dump/finorg_sample.json') as f:
    data = f.read()
    jsondata = json.loads(data)
    
