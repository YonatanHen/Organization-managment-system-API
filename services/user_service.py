from models import User, Endpoint, Organization
from utils.create_sesssion import get_db_session

def create_user(name: str, ep_id: int, ep_name: str):
    '''
    Create a new user.
    @param name: Name of the new user
    @param ep_id: ID of the Endpoint
    @param ep_name: Name of the Endpoint
    @param org_id: ID of the organization
    @param org_name: Name of the organization
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
        raise ValueError(f"Could not find endpoint with id {ep_id} or name {ep_name}.")
    
    user = User(name=name)

    endpoint.users.append(user)
    session.add(user) 
    
    session.commit()
    
    res = {"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id }
    
    session.close()
    
    return res 
