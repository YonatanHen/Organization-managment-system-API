from flask import jsonify, Blueprint, request
from sqlalchemy.exc import SQLAlchemyError
from services.endpoint_service import *

ep_bp = Blueprint('endpoint', __name__, url_prefix='/endpoint')

@ep_bp.route('/', methods=['POST'])
def add_endpoint():
    if request.method == 'POST':
        try:
            data = request.get_json()
            
            # Get 'org_id' and 'org_name', allowing at least one of them to be be specified 
            org_id = data.get('org_id')
            org_name = data.get('org_name')

            endpoint = create_endpoint(data['name'], org_id, org_name)
            
            return jsonify({"message": "Endpoint added successfully", "endpoint": endpoint}) 
            
        except KeyError as e:
            # Handle missing 'name' key in the request payload.
            return jsonify({'error': 'The "name" field is required.'}), 400 
        except SQLAlchemyError as e:
            return jsonify({'error': 'Database error occurred.', 'message': str(e.orig)}), 500
        except Exception as e:
            return jsonify({'error': 'An error occurred', 'message': str(e)}), 500
        
        
@ep_bp.route('/<int:id>', methods=['PUT', 'DELETE'])
def update_or_delete_endpoint(id: int):
    if request.method == 'PUT':
        try:
            data = request.get_json()
            
            # Allowing the 'name' to be optional in case we want to update the org only.
            ep_name = data.get('name')
            
            # Get 'org_id' and 'org_name', allowing either to be optional
            org_id = data.get('org_id')
            org_name = data.get('org_name')

            endpoint = update_endpoint(id, ep_name, org_id, org_name)
            
            return jsonify({"message": "Endpoint updated successfully", "endpoint": endpoint})    
                 
        except KeyError:
            return jsonify({'error': 'Some fields in the payload are missing'}), 400
        except SQLAlchemyError as e:
            return jsonify({'error': 'Database error occurred.', 'message': str(e.orig)}), 500
        except Exception as e:
            return jsonify({'error': 'An error occurred', 'message': str(e)}), 500            

    elif request.method == 'DELETE':
        try:
            endpoint = delete_endpoint(id)
            
            return jsonify({"message": "Endpoint deleted successfully", "endpoint": endpoint}) 
        
        except SQLAlchemyError as e:
            return jsonify({'error': 'Database error occurred.', 'message': str(e.orig)}), 500
        except Exception as e:
            return jsonify({'error': 'An error occurred', 'message': str(e)}), 500 
        

@ep_bp.route('/<int:ep_id>/user/<int:user_id>', methods=['GET'])
def get_user_endpoint(ep_id, user_id):
    try:
        user = get_user_from_endpoint(user_id,ep_id)
        
        return jsonify(user)
    
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred.', 'message': str(e.orig)}), 500
    except Exception as e:
        return jsonify({'error': 'An error occurred', 'message': str(e)}), 500  
    

@ep_bp.route('/<int:id>/users', methods=['GET'])
def get_users_endpoint(id):
    try:
        user = get_users_list_from_endpoint(id)
        
        return jsonify(user)
    
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred.', 'message': str(e.orig)}), 500
    except Exception as e:
        return jsonify({'error': 'An error occurred', 'message': str(e)}), 500 