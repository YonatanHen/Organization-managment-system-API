from flask import Flask, jsonify, Blueprint, request

user_bp = Blueprint('user', __name__, url_prefix='/user')

# @user_bp.route('/user', methods=['GET', 'POST', 'DELETE'])
# def user(request):
#     if request.method == 'POST':
        
    