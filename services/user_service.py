from models import User, Endpoint, Organization
from utils.create_sesssion import get_db_session
from sqlalchemy.orm import Session

def get_endpoint_by_user_id(id: int, parent_session: Session = None):
    '''
    Find user's registered endpoint by user id.
    @param id: the user id   
    @paran parent_session: Session instance from parent function
    '''
    if not parent_session:
        session = get_db_session()
    else:
        session = parent_session
    
    user = session.query(User).filter_by(id=id).first()
    
    if user is None:
        session.close()
        raise ValueError(f"No user with id #{id} was found")
    
    endpoint = session.query(Endpoint).filter_by(id=user.endpoint_id).first()

    res = {"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id} 
    
    if not parent_session:
        session.close()
    
    return res


def get_organization_by_user_id(id: int):
    '''
    Find user's registered organiztion by user id.
    @param id: the user id 
    '''
    session = get_db_session()
    
    endpoint = get_endpoint_by_user_id(id, session)
    
    organization=session.query(Organization).filter_by(id=endpoint['organization_id']).first()
    
    res = {"id": organization.id, "name": organization.name}
       
    session.close()
    
    return res 


def create_user(name: str, ep_id: int):
    '''
    Create a new user.
    @param name: Name of the new user 
    @param ep_id: ID of the Endpoint 
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
    @param id: ID of the user in the DB 
    @param name: New name for the user 
    @param ep_id: ID of the endpoint we want to update 
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
            raise ValueError(f"User '{new_name}' already exists.")
    
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
    @param id: ID of the user in the DB
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