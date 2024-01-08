# views.py
from flask import Blueprint, jsonify
from .models import User

app_bp = Blueprint('app', __name__)

@app_bp.route('/user/<username>', methods=['GET'])
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'username': user.username})
    else:
        return jsonify({'error': 'User not found'}), 404
    

@app_bp.route('/')
def index():
    return b'Hello, World!'


@app_bp.route('/hello')
def hello():
    return b'Hello, World!'