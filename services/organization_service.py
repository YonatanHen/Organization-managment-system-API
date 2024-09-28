from models import Organization, Endpoint
from utils.create_sesssion import get_db_session

def get_endpoint_from_organization(ep_id: int, org_id: int):
    '''
    Find an endpoint who assigned to given organization.
    
    @param ep_id: the endpoint id
    @param org_id: the organization id
    
    @return: endpoint JSON
    
    @raises: ValueError: if endpoint id was not found in the organization.
    '''
    session = get_db_session()
    endpoint = session.query(Endpoint).filter(Endpoint.id==ep_id, Endpoint.organization_id==org_id).first()
    
    if endpoint is None:
        session.close()
        raise ValueError(f"No endpoint with id #{ep_id} in organization #{org_id} was found or not exists.")
    
    res = {"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}
    
    session.close()
    
    return res 


def get_endpoints_list_from_organization(org_id: int):
    '''
    Find all endpoints who assigned to given organization.
    
    @param org_id: the organization id
    
    @return: List of endpoints objects in JSON format
    
    @raises: ValueError: if no such organization exists
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
    Delete an organization
    @param id: ID of the organization in the DB
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