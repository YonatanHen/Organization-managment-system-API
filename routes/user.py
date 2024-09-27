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
        
    