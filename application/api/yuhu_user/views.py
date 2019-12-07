from flask import Blueprint, render_template, flash, redirect, url_for, jsonify, request
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import or_
from flask_jwt_extended import jwt_required, create_access_token, jwt_refresh_token_required, create_refresh_token, get_jwt_identity
from application.api.yuhu_user.models import *
from application import db
from application.api.yuhu_user.schemas import *
from application.common.status_code import *

# Generate blueprint object
yuhu_user = Blueprint('yuhu_user', __name__)

# register
@yuhu_user.route('/auth', methods=['POST'])
def login():
    json_data = request.get_json()
    user_schema = UsersSchema()
    user_schema.load(json_data)
    username = json_data['username']
    user = Users.query.filter_by(username=username).first()
    if user is None:
        return jsonify({'code': ERROR_USER_PASSWORD[0], 'message': ERROR_USER_PASSWORD[1]})
    if check_password_hash(user.password, json_data['password']):
        # Verify the pass, and assign the JWT token
        jwt_token = create_access_token(identity=username)

        refresh_token = create_refresh_token(identity=username)

        return jsonify({'code': SUCCESS, 'message': '成功', 'token': jwt_token, 'refresh_token': refresh_token})        
    return jsonify({'code': ERROR_USER_PASSWORD[0], 'message': ERROR_USER_PASSWORD[1]})    

@yuhu_user.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user)
    }
    return jsonify(ret), 200

# Add new users
@yuhu_user.route('/', methods=['POST'])
def add_user():
    json_data = request.get_json()
    json_data['password'] = generate_password_hash(json_data['password'])
    users_schema = UsersSchema()
    user = users_schema.load(json_data)
    db.session.add(userA)
    db.session.commit()
    return jsonify({'code': SUCCESS, 'message': '成功', 'data': {'user_id': user.id}})



