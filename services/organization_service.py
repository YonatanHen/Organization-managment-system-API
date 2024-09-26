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


def update_organization(id: int, new_name: str):
    '''
    Update the an existing organization.
    @param id: ID of the organization in the DB
    @param name: New name for the organization
    '''
    session=get_db_session()
    
    organization = session.query(Organization).filter_by(id=id).first()
    
    if organization is None:
        raise ValueError(f"Organization with id #{id} wasn't found.")
    
    org_name = session.query(Organization).filter_by(name=new_name).first()
    
    if org_name is not None:
        raise ValueError(f"Organization '{new_name}' already exists.")
    
    organization.name = new_name
    
    session.commit()
    
    res = {"id": organization.id, "name": organization.name}
    
    session.close()
    
    return res 

def delete_organization(id: int):
    session=get_db_session()
    
    organization = session.query(Organization).filter_by(id=id).first()
    
    if organization is None:
        raise ValueError(f"No organization with id #{id} was found")
    
    session.delete(organization)
    
    session.commit()
    
    res = {"id": organization.id, "name": organization.name}
    
    session.close()
    
    return res 