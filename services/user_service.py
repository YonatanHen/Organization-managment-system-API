from models import User, Endpoint
from utils.create_sesssion import get_db_session

def create_user(name: str, ep_id: int, ep_name: str):
    '''
    Create a new user.
    @param name: Name of the new user
    @param ep_id: ID of the Endpoint
    @param ep_name: Name of the Endpoint
    '''
    session=get_db_session()
    
    #Trying to find the endpoint by id, then by name. If none of them provided, raise an exception.
    if ep_id is not None:
        endpoint = session.query(Endpoint).filter_by(id=ep_id).first()
    elif ep_name is not None:
        endpoint = session.query(Endpoint).filter_by(name=ep_name).first()
    else:
        session.close()
        raise ValueError(f"Either endpoint name or endpoint id must be provided. Can't add the user.") 
    
    if endpoint is None: 
        session.close()
        if ep_id:
            raise ValueError(f"Could not find endpoint with id {ep_id}.")
        elif ep_name:
            raise ValueError(f"Could not find endpoint with name {ep_name}.")
        
    user = User(name=name)

    endpoint.users.append(user)
    session.add(user) 
    
    session.commit()
    
    res = {"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id }
    
    session.close()
    
    return res 

def update_user(id: int, new_name: str, ep_id: int, new_ep: str):
    '''
    Update an existing user.
    @param id: ID of the user in the DB
    @param name: New name for the user
    @param org_id: ID of the endpoint we want to update
    @param new_org: Name of the endpoint we want to update 
    '''
    if not any([new_name, ep_id, new_ep]):
        raise ValueError("At least one of 'new_name', 'ep_id', or 'new_ep' must be provided in the payload.")
    
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
    if ep_id or new_ep:
        endpoint = None
        if ep_id:
            endpoint = session.query(Endpoint).filter_by(id=ep_id).first()
        elif new_ep:
            endpoint = session.query(Endpoint).filter_by(name=new_ep).first()

        if endpoint is None:
            session.close()
            if ep_id:
                raise ValueError(f"Could not find endpoint with id {ep_id}.")
            elif new_ep:
                raise ValueError(f"Could not find endpoint with name {new_ep}.")
        
        user.endpoint_id = endpoint.id
    else:
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