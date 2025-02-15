from flask import jsonify, Blueprint, request
from sqlalchemy.exc import SQLAlchemyError
from services.user_service import *

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/', methods=['POST'])
def add_user():
    if request.method == 'POST':
        try:
            data = request.get_json()

            user = create_user(data['name'], data['ep_id'])
            
            return jsonify({"message": "User added successfully", "user": user}) 
            
        except KeyError as e:
            # Handle missing 'name' key in the request payload.
            return jsonify({'error': 'The "name" field is required.'}), 400 
        except SQLAlchemyError as e:
            return jsonify({'error': 'Database error occurred.'}), 500
        except ValueError as e:
            err_msg=str(e)
            if err_msg == f"User '{data['name']}' already exists.":
                return jsonify({'error': err_msg}), 409
            return jsonify({'error': err_msg}), 404
        except Exception as e:
            return jsonify({'error': 'An error occurred', 'message': str(e)}), 500


@user_bp.route('/<int:id>', methods=['PUT', 'DELETE'])
def update_or_delete_user(id: int):
    if request.method == 'PUT':
        try:
            data = request.get_json()
            
            # Allowing the 'name' to be optional in case we want to update the endpoint only.
            user_name = data.get('name')
            
            # Get 'ep_id', allowing to be optional
            ep_id = data.get('ep_id')

            user = update_user(id, user_name, ep_id)
            
            return jsonify({"message": "user updated successfully", "user": user})    
                 
        except KeyError:
            return jsonify({'error': 'Some fields in the payload are missing'}), 400
        except SQLAlchemyError as e:
            return jsonify({'error': 'Database error occurred.'}), 500
        except ValueError as e:
            err_msg=str(e)
            if err_msg == f"User '{data['name']}' already exists.":
                return jsonify({'error': err_msg}), 409
            return jsonify({'error': err_msg}), 404
        except Exception as e:
            return jsonify({'error': 'An error occurred', 'message': str(e)}), 500            

    elif request.method == 'DELETE':
        try:
            user = delete_user(id)
            
            return jsonify({"message": "user deleted successfully", "user": user}) 
        
        except SQLAlchemyError as e:
            return jsonify({'error': 'Database error occurred.'}), 500
        except ValueError as e:
            return jsonify({'error': str(e)}), 404
        except Exception as e:
            return jsonify({'error': 'An error occurred', 'message': str(e)}), 500         
    

@user_bp.route('/<int:id>/endpoint', methods=['GET'])
def get_endpoint(id):
    try:
        endpoint = get_endpoint_by_user_id(id)
        
        return jsonify(endpoint)
    
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred.', 'message': str(e)}), 500
    except ValueError as e:
            return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred', 'message': str(e)}), 500


@user_bp.route('/<int:id>/organization', methods=['GET'])
def get_organization(id):
    try:
        organization = get_organization_by_user_id(id)
        
        return jsonify(organization)
    
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred.'}), 500
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred', 'message': str(e)}), 500  