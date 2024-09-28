from models import Endpoint, Organization, User
from sqlalchemy.orm import Session
from utils.create_sesssion import get_db_session

def get_user_from_endpoint(user_id: int, ep_id: int):
    '''
    Find a user who assigned to given endpoint.
    
    @param user_id: the user ID
    @param ep_id: the endpoint ID
    
    :returns: user JSON
    
    :raises: ValueError: if user ID was not found in the endpoint.
    '''
    session = get_db_session()
    user = session.query(User).filter(User.endpoint_id==ep_id, User.id==user_id).first()
    
    if user is None:
        session.close()
        raise ValueError(f"No user with id #{user_id} in endpoint #{ep_id} was found or not exists.")

    endpoint = session.query(Endpoint).filter_by(id=ep_id).first()
    
    res = {"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id }
    
    session.close()
    
    return res 


def get_users_list_from_endpoint(ep_id: int, parent_session: Session = None):
    '''
    Find all user who assigned to given endpoint.
    
    @param ep_id: the endpoint ID
    @param parent_session: Session instance from the parent function, if provided
    
    :returns: List of user objects in JSON format
    
    :raises: ValueError: if no such endpoint exists
    '''
    if not parent_session:
        session = get_db_session()
    else: 
        session=parent_session
    
    users_list = session.query(User).filter_by(endpoint_id=ep_id).all()
    
    if len(users_list)==0:
        #Don't raise an exception in case we call this function from the parent function since we need to look for multiple endpoints assigned to the organization (and not necessarily assigned to a user)
        if parent_session:
            return []
        
        session.close()
        raise ValueError(f"Endpoint #{ep_id} is not exists or not assigned to any user.")
    
    res = []
    ep_to_org={}
    for user in users_list:
        if user.endpoint_id not in ep_to_org:
            endpoint = session.query(Endpoint).filter_by(id=user.endpoint_id).first()
            ep_to_org[user.endpoint_id] = endpoint.organization_id
            
        res.append({"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": ep_to_org[user.endpoint_id]})
    
    if not parent_session:
        session.close()
    
    return res 

def create_endpoint(name: str, org_id: int, org_name: str):
    '''
    Create a new endpoint.
    
    @param name: Name of the new endpoint
    @param org_id: ID of the organization
    @param org_name: Name of the organization
    
    :returns: New Endpoint object
    
    :raises: ValueError: If the orgnization name/ID not provided or organization could not be found.
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
        raise ValueError(f"Could not find organization with id {org_id}.")
    
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
    
    :returns: The updated endpoint JSON object
    
    :raises: ValueError: if the endpoint wasn't found, or organization ID/name was not found.
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
    
    :returns: The deleted endpoint JSON object
    
    :raises: ValueError: If the given endpoint ID is not found
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