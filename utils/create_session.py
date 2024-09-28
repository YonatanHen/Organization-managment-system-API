from sqlalchemy.orm import sessionmaker
from DB.psql_connection import engine

def get_db_session():
    """Create and return new DB session"""
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = Session()
    return session