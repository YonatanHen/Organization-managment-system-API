from flask import Flask, jsonify, Blueprint, request

user_bp = Blueprint('user', __name__, url_prefix='/user')
