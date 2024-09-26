from models import Organization
from utils.create_sesssion import get_db_session

def create_organization(name: str):
    '''
    Create a new organization
    @param name: Name of the new organizationre
    '''
    session=get_db_session()
    
    organization = Organization(name=name)
    
    session.add(organization)
    session.commit()
    
    res = {"id": organization.id, "name": organization.name}
    
    session.close()
    
    return res 


def update_organization(id: int, name: str):
    '''
    Update the name of an existing organization
    @param name: New name for the organization
    '''
    with session_scope() as session:
        session.query(Organization).filter()
    