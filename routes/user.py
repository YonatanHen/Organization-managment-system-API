from flask import jsonify, Blueprint, request
from sqlalchemy.exc import SQLAlchemyError
from services.user_service import *
user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/', methods=['POST'])
def add_user():
    if request.method == 'POST':
        try:
            data = request.get_json()
            
            # Get 'ep_id' and 'ep_name', allowing at least one of them to be be specified 
            ep_id = data.get('ep_id')
            ep_name = data.get('ep_name')

            user = create_user(data['name'], ep_id, ep_name)
            
            return jsonify({"message": "User added successfully", "user": user}) 
            
        except KeyError as e:
            # Handle missing 'name' key in the request payload.
            return jsonify({'error': 'The "name" field is required.'}), 400 
        except SQLAlchemyError as e:
            return jsonify({'error': 'Database error occurred.', 'msg': str(e)}), 500
        except Exception as e:
            return jsonify({'error': 'An error occurred', 'message': str(e)}), 500


@user_bp.route('/<int:id>', methods=['PUT', 'DELETE'])
def update_or_delete_user(id: int):
    if request.method == 'PUT':
        try:
            data = request.get_json()
            
            # Allowing the 'name' to be optional in case we want to update the endpoint only.
            user_name = data.get('name')
            
            # Get 'ep_id' and 'ep_name', allowing either to be optional
            ep_id = data.get('ep_id')
            ep_name = data.get('ep_name')

            user = update_user(id, user_name, ep_id, ep_name)
            
            return jsonify({"message": "user updated successfully", "user": user})    
                 
        except KeyError:
            return jsonify({'error': 'Some fields in the payload are missing'}), 400
        except SQLAlchemyError as e:
            return jsonify({'error': 'Database error occurred.'}), 500
        except Exception as e:
            return jsonify({'error': 'An error occurred', 'message': str(e)}), 500            

    elif request.method == 'DELETE':
        try:
            user = delete_user(id)
            
            return jsonify({"message": "user deleted successfully", "user": user}) 
        
        except SQLAlchemyError as e:
            return jsonify({'error': 'Database error occurred.'}), 500
        except Exception as e:
            return jsonify({'error': 'An error occurred', 'message': str(e)}), 500        
    