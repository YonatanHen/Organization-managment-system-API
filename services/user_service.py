from models import User, Endpoint, Organization
from utils.create_sesssion import get_db_session
from sqlalchemy.orm import Session

def get_endpoint_by_user_id(user_id: int):
    '''
    Find user's registered endpoint by user id.
    
    @param id: The user ID   
    
    :returns: The endpoint JSON object
    
    :raises: ValueError: If the given user ID is not found
    '''
    session = get_db_session()
        
    query_results = session.query(User, Endpoint).join(Endpoint).filter(User.id==user_id).first()
    
    if query_results is None:
        session.close()
        raise ValueError(f"No user with id #{user_id} was found")
    
    _, endpoint = query_results
    
    res = {"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id} 
    
    session.close()
    
    return res


def get_organization_by_user_id(user_id: int):
    '''
    Find user's registered organization by user id.
    
    @param id: The user ID 
    
    :returns: The organization JSON object
    
    :raises: ValueError: If the given user ID is not found
    '''
    session = get_db_session()
        
    query_reuslts = session.query(User, Endpoint, Organization)\
        .select_from(User)\
        .join(Endpoint, User.endpoint_id == Endpoint.id)\
        .join(Organization, Endpoint.organization_id == Organization.id)\
        .filter(User.id == user_id).first()
    
    if query_reuslts is None:
        session.close()
        raise ValueError(f"No user with id #{user_id} was found")
    
    _, _, organization = query_reuslts
    
    res = {"id": organization.id, "name": organization.name}
       
    session.close()
    
    return res 


def create_user(name: str, ep_id: int):
    '''
    Create a new user.
    
    @param name: The name of the new user 
    @param ep_id: The ID of the endpoint
    
    :returns: The created user JSON object
    
    :raises: ValueError: If the given endpoint ID is not found
    '''
    session=get_db_session()
    
    endpoint = session.query(Endpoint).filter_by(id=ep_id).first()

    if endpoint is None: 
        session.close()
        if ep_id:
            raise ValueError(f"Could not find endpoint with id {ep_id}.")

    user = User(name=name)

    endpoint.users.append(user)
    session.add(user) 
    
    session.commit()
    
    res = {"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id }
    
    session.close()
    
    return res 

def update_user(id: int, new_name: str, ep_id: int):
    '''
    Update an existing user.
    
    @param id: The ID of the user in the DB 
    @param new_name: The new name for the user 
    @param ep_id: The ID of the endpoint we want to update 
    
    :returns: The updated user JSON object
    
    :raises: ValueError: If the user or endpoint with the provided ID is not found, or if the new user name already exists
    '''
    if not any([new_name, ep_id]):
        raise ValueError("At least one of 'new_name', or 'ep_id' must be provided in the payload.")
    
    session=get_db_session()
    
    user = session.query(User).filter_by(id=id).first()
    
    if user is None:
        session.close()
        raise ValueError(f"User with id #{id} wasn't found.")
   
    # Update user's name
    if new_name is not None: 
        user_by_name = session.query(User).filter_by(name=new_name).first()
        if user_by_name is not None:
            session.close()
            raise Exception(f"User '{new_name}' already exists.")
    
        user.name = new_name

    # Update endpoint's organization
    endpoint = None
    if ep_id:
        endpoint = session.query(Endpoint).filter_by(id=ep_id).first()

        if endpoint is None:
            session.close()
            raise ValueError(f"Could not find endpoint with id {ep_id}.")
        
        user.endpoint_id = endpoint.id
    else:
        #Else condition set to make sure the same endpoint isn't searched twice
        endpoint = session.query(Endpoint).filter_by(id=user.endpoint_id).first()

    session.commit()
    
    res = {"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id}
    
    session.close()
    
    return res 


def delete_user(id: int):
    '''
    Delete a user.
    
    @param id: The ID of the user in the DB
    
    :returns: The deleted user JSON object
    
    :raises: ValueError: If the user with the given ID is not found
    '''
    session=get_db_session()
    
    user = session.query(User).filter_by(id=id).first()
    
    if user is None:
        session.close()
        raise ValueError(f"No user with id #{id} was found")
    
    endpoint = session.query(Endpoint).filter_by(id=user.endpoint_id).first()
    
    session.delete(user)
    
    session.commit()
    
    res = {"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id} 
       
    session.close()
    
    return res 