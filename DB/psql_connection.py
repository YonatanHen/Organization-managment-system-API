import os
import sys
from sqlalchemy import create_engine
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import Base

#In production environment we must keep credentials secure by enabling them in the activate script of the venv
#In order to simplify the startup process in this task, I exposed the credentials.
#PSQL_USERNAME=os.environ.get('PSQL_USERNAME')
#PSQL_PASSWORD=os.environ.get('PSQL_PASSWORD')
#PSQL_URL=os.environ.get('PSQL_URL')

engine = create_engine(f"postgresql://postgres:password@localhost:5432/postgres")
Base.metadata.create_all(bind=engine)