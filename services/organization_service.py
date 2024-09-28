from models import Organization, Endpoint, User
from sqlalchemy.orm import Session
from utils.create_sesssion import get_db_session
    
def get_endpoint_from_organization(ep_id: int, org_id: int, parent_session: Session = None):
    '''
    Find an endpoint who assigned to given organization.
    
    @param ep_id: the endpoint ID
    @param org_id: the organization ID
    @param parent_session: Session instance from the parent function, if provided

    :returns: endpoint object in JSON format
    
    :raises: ValueError: if endpoint ID was not found in the organization.
    '''
    if not parent_session:
        session = get_db_session()
    else:
        session = parent_session
        
    endpoint = session.query(Endpoint).filter(Endpoint.id==ep_id, Endpoint.organization_id==org_id).first()
    
    if endpoint is None:
        session.close()
        if parent_session:
            raise ValueError(f"User's endpoint (id #{ep_id}) in organization #{org_id} was found.")
        else:
            raise ValueError(f"No endpoint with id #{ep_id} in organization #{org_id} was found or not exists.")
    
    res = {"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}
    
    if not parent_session:
        session.close()
    
    return res 


def get_endpoints_list_from_organization(org_id: int):
    '''
    Find all endpoints who assigned to given organization.
    
    @param org_id: the organization ID
    
    :returns: List of endpoints objects in JSON format
    
    :raises: ValueError: if no such organization exists
    '''
    session = get_db_session()
    endpoints_list = session.query(Endpoint).filter_by(organization_id=org_id).all()
    
    if len(endpoints_list)==0:
        session.close()
        raise ValueError(f"Organization #{org_id} is not exists or not assigned to any endpoint.")
    
    res = []
    for endpoint in endpoints_list:
        res.append({"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id})
    
    session.close()
    
    return res 


def get_user_from_organization(user_id: int, org_id: int):
    '''
    Find an user who assigned to given organization.
    
    @param user_id: the user ID
    @param org_id: the organization ID
    
    :returns: endpoint object in JSON format
    
    :raises: ValueError: if organization ID was not found in the endpoint that assigned to the given user (ID).
    '''
    session = get_db_session()
    user = session.query(User).filter_by(id=user_id).first()
    
    if user is None:
        session.close()
        raise ValueError(f"No user with id #{user_id} was found")
    
    endpoint=get_endpoint_from_organization(user.endpoint_id, org_id, session)
    
    if endpoint['organization_id']!=org_id:
        session.close()
        raise ValueError(f"No user with id #{user_id} in organization #{org_id} was found.")
    
    res = {"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint['organization_id']}
    
    session.close()
    
    return res 


def create_organization(name: str):
    '''
    Create a new organization
    
    @param name: Name of the new organization
    
    :returns: New organization JSON object    
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
    
    :returns: The updated organization JSON object
    
    :raises: ValueError: if the organization was not found or if the organization name already exists.
    '''
    session=get_db_session()
    
    organization = session.query(Organization).filter_by(id=id).first()
    
    if organization is None:
        session.close()
        raise ValueError(f"Organization with id #{id} wasn't found.")
    
    org_by_name = session.query(Organization).filter_by(name=new_name).first()
    
    if org_by_name is not None:
        session.close()
        raise ValueError(f"Organization '{new_name}' already exists.")
    
    organization.name = new_name
    
    session.commit()
    
    res = {"id": organization.id, "name": organization.name}
    
    session.close()
    
    return res 

def delete_organization(id: int):
    '''
    Delete an organization.
    
    @param id: ID of the organization in the DB
    
    :returns: The deleted organization JSON object
    
    :raises ValueError: If no organization with the given ID was found
    '''
    session=get_db_session()
    
    organization = session.query(Organization).filter_by(id=id).first()
    
    if organization is None:
        session.close()
        raise ValueError(f"No organization with id #{id} was found")
    
    session.delete(organization)
    
    session.commit()
    
    res = {"id": organization.id, "name": organization.name}
    
    session.close()
    
    return res 