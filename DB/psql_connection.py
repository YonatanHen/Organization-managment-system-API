import os
import sys
from sqlalchemy import create_engine
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import Base

# Load environment variables from .env file
load_dotenv()

PSQL_USERNAME=os.environ.get('PSQL_USERNAME')
PSQL_PASSWORD=os.environ.get('PSQL_PASSWORD')
PSQL_URL=os.environ.get('PSQL_URL')

engine = create_engine(f"postgresql://{PSQL_USERNAME}:{PSQL_PASSWORD}@{PSQL_URL}")
Base.metadata.create_all(bind=engine)