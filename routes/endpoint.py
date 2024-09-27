from flask import jsonify, Blueprint, request
from sqlalchemy.exc import SQLAlchemyError
from services.endpoint_service import *

ep_bp = Blueprint('endpoint', __name__, url_prefix='/endpoint')

@ep_bp.route('/', methods=['POST'])
def add_endpoint():
    if request.method == 'POST':
        try:
            data = request.get_json()
            
            # Get 'org_id' and 'org_name', allowing either to be optional
            org_id = data.get('org_id')
            org_name = data.get('org_name')

            endpoint = create_endpoint(data['name'], org_id, org_name)
            
            return jsonify({"message": "Endpoint added successfully", "endpoint": endpoint}) 
            
        except KeyError as e:
            # Handle missing 'name' key in the request payload.
            return jsonify({'error': 'The "name" field is required.'}), 400 
        except SQLAlchemyError as e:
            return jsonify({'error': 'Database error occurred.', 'message': str(e)}), 500
        except Exception as e:
            return jsonify({'error': 'An error occurred', 'message': str(e)}), 500
        
@ep_bp.route('/<int:id>', methods=['PUT', 'DELETE'])
def update_or_delete_endpoint(id: int):
    if request.method == 'PUT':
        try:
            data = request.get_json()

            endpoint = update_endpoint(id, data['name'])
            
            return jsonify({"message": "Endpoint updated successfully", "endpoint": endpoint})    
                 
        except KeyError:
            # Handle missing 'name' in the request payload
            return jsonify({'error': 'The "name" field is required.'}), 400
        except SQLAlchemyError as e:
            return jsonify({'error': 'Database error occurred.'}), 500
        except Exception as e:
            return jsonify({'error': 'An error occurred', 'message': str(e)}), 500            

    elif request.method == 'DELETE':
        try:
            endpoint = delete_endpoint(id)
            
            return jsonify({"message": "Endpoint deleted successfully", "endpoint": endpoint}) 
        
        except SQLAlchemyError as e:
            return jsonify({'error': 'Database error occurred.'}), 500
        except Exception as e:
            return jsonify({'error': 'An error occurred', 'message': str(e)}), 500 