from sqlalchemy.types import String
from sqlalchemy import create_engine
from app import app
from models import Company
import models
engine = create_engine('postgresql://localhost/startup_fairy')

# NOTE: startup_fairy is a database created on my local computer
# NOTE: pip installed psycopg2

models.db.create_all()


    
