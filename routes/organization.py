from flask import Flask, jsonify, Blueprint, request
from  sqlalchemy.exc import SQLAlchemyError
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
            # Handle missing 'name' in the request payload
            return jsonify({'error': 'The "name" field is required.'}), 400 
        except SQLAlchemyError as e:
            return jsonify({'error': 'Database error occurred.', 'message': str(e)}), 500
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
            # Handle missing 'name' in the request payload
            return jsonify({'error': 'The "name" field is required.'}), 400
        except SQLAlchemyError as e:
            return jsonify({'error': 'Database error occurred.'}), 500
        except Exception as e:
            return jsonify({'error': 'An error occurred', 'message': str(e)}), 500            

    elif request.method == 'DELETE':
        try:
            organization = delete_organization(id)
            
            return jsonify({"message": "Organization deleted successfully", "organization": organization}) 
        
        except SQLAlchemyError as e:
            return jsonify({'error': 'Database error occurred.'}), 500
        except Exception as e:
            return jsonify({'error': 'An error occurred', 'message': str(e)}), 500 