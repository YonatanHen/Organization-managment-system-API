from flask import jsonify, Blueprint, request
from sqlalchemy.exc import SQLAlchemyError
from services.organization_service import *

org_bp = Blueprint('organization', __name__, url_prefix='/organization')

@org_bp.route('/', methods=['POST'])
def add_organization():
    if request.method == 'POST':
        try:
            data = request.get_json()

            organization = create_organization(data['name'])
            
            return jsonify({"message": "Organization added successfully", "organization": organization}) 
            
        except KeyError:
            # Handle missing or empty 'name' in the request payload
            return jsonify({'error': 'The "name" field is required.'}), 400 
        except SQLAlchemyError as e:
            return jsonify({'error': 'Database error occurred.'}), 500
        except ValueError as e:
            err_msg=str(e)
            if err_msg == f"Organization '{data['name']}' already exists.":
                return jsonify({'error': err_msg}), 409
            return jsonify({'error': err_msg}), 404
        except Exception as e:
            return jsonify({'error': 'An error occurred', 'message': str(e)}), 500
          

@org_bp.route('/<int:id>', methods=['PUT', 'DELETE'])
def update_or_delete_organization(id: int):
    if request.method == 'PUT':
        try:
            data = request.get_json()

            organization = update_organization(id, data['name'])
            
            return jsonify({"message": "Organization updated successfully", "organization": organization})    
                 
        except KeyError:
            # Handle missing or empty 'name' in the request payload
            return jsonify({'error': 'The "name" field is required.'}), 400
        except SQLAlchemyError as e:
            return jsonify({'error': 'Database error occurred.'}), 500
        except ValueError as e:
            return jsonify({'error': str(e)}), 404        
        except Exception as e:
            return jsonify({'error': 'An error occurred', 'message': str(e)}), 500            

    elif request.method == 'DELETE':
        try:
            organization = delete_organization(id)
            
            return jsonify({"message": "Organization deleted successfully", "organization": organization}) 
        
        except SQLAlchemyError as e:
            return jsonify({'error': 'Database error occurred.'}), 500
        except ValueError as e:
            return jsonify({'error': str(e)}), 404
        except Exception as e:
            return jsonify({'error': 'An error occurred', 'message': str(e)}), 500

@org_bp.route('/<int:org_id>/user/<int:user_id>', methods=['GET'])
def get_user_organization(org_id, user_id):
    try:
        user = get_user_from_organization(user_id, org_id)
        
        return jsonify(user)
    
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred.'}), 500
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred', 'message': str(e)}), 500  
    

@org_bp.route('/<int:id>/users', methods=['GET'])
def get_users_organization(id):
    try:
        users = get_users_list_from_organization(id)
        
        return jsonify(users)
    
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred.'}), 500
    except ValueError as e:
            return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred', 'message': str(e)}), 500
        
@org_bp.route('/<int:org_id>/endpoint/<int:ep_id>', methods=['GET'])
def get_endpoint_organization(org_id, ep_id):
    try:
        endpoint = get_endpoint_from_organization(ep_id, org_id)
        
        return jsonify(endpoint)
    
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred.'}), 500
    except ValueError as e:
            return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred', 'message': str(e)}), 500  
    

@org_bp.route('/<int:id>/endpoints', methods=['GET'])
def get_endpoints_organization(id):
    try:
        endpoints = get_endpoints_list_from_organization(id)
        
        return jsonify(endpoints)
    
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred.'}), 500
    except ValueError as e:
            return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred', 'message': str(e)}), 500 