from flask import Flask, jsonify, Blueprint, request

org_bp = Blueprint('organization', __name__, url_prefix='/organization')
