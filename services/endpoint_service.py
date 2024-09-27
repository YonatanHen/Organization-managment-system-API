from models import Endpoint, Organization
from utils.create_sesssion import get_db_session

def create_endpoint(name: str, org_id: int, org_name: str):
    '''
    Create a new endpoint.
    @param name: Name of the new endpoint
    @param org_id: ID of the organization
    @param org_name: Name of the organization
    '''
    session=get_db_session()
    
    #Trying to find the organzition by id, then by name. If none of them provided, raise an exception.
    if org_id is not None:
        organization = session.query(Organization).filter_by(id=org_id).first()
    elif org_name is not None:
        organization = session.query(Organization).filter_by(name=org_name).first()
    else:
        session.close()
        raise ValueError(f"Either organization name or organization id must be provided. Can't add the endpoint.") 
    
    if organization is None: 
        session.close()
        raise ValueError(f"Could not find organization with id {org_id} or name {org_name}.")
    
    endpoint = Endpoint(name=name)

    organization.endpoints.append(endpoint)
    session.add(endpoint) 
    
    session.commit()
    
    res = {"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}
    
    session.close()
    
    return res 


def update_endpoint(id: int, new_name: str, org_id: int, new_org: str):
    '''
    Update an existing endpoint.
    @param id: ID of the endpoint in the DB
    @param name: New name for the endpoint
    @param org_id: ID of the organization we want to update
    @param new_org: Name of the organization we want to update 
    '''
    if not any([new_name, org_id, new_org]):
        raise ValueError("At least one of 'new_name', 'org_id', or 'new_org' must be provided in the payload.")
    
    session=get_db_session()
    
    endpoint = session.query(Endpoint).filter_by(id=id).first()
    
    if endpoint is None:
        session.close()
        raise ValueError(f"Endpoint with id #{id} wasn't found.")
   
    # Update endpoint's name
    if new_name is not None: 
        ep_by_name = session.query(Endpoint).filter_by(name=new_name).first()
        if ep_by_name is not None:
            session.close()
            raise ValueError(f"Endpoint '{new_name}' already exists.")
    
        endpoint.name = new_name

    # Update endpoint's organization
    if org_id or new_org:
        organization = None
        if org_id:
            organization = session.query(Organization).filter_by(id=org_id).first()
        elif new_org:
            organization = session.query(Organization).filter_by(name=new_org).first()

        if organization is None:
            session.close()
            if org_id:
                raise ValueError(f"Could not find organization with id {org_id}.")
            elif new_org:
                raise ValueError(f"Could not find organization with name {new_org}.")
            
        endpoint.organization_id = organization.id

    session.commit()
    
    res = {"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}
    
    session.close()
    
    return res 


def delete_endpoint(id: int):
    '''
    Delete an endpoint.
    @param id: ID of the endpoint in the DB
    '''
    session=get_db_session()
    
    endpoint = session.query(Endpoint).filter_by(id=id).first()
    
    if endpoint is None:
        session.close()
        raise ValueError(f"No endpoint with id #{id} was found")
        
    session.delete(endpoint)
    
    session.commit()
    
    res = {"id": endpoint.id, "name": endpoint.name , "organization_id": endpoint.organization_id}
    
    session.close()
    
    return res 