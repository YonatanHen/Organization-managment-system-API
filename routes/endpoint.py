from flask import Flask, jsonify, Blueprint, request

ep_bp = Blueprint('endpoint', __name__, url_prefix='/endpoint')
