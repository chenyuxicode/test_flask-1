from flask import Blueprint, render_template, flash, redirect, url_for, jsonify, request
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError
from application.common.status_code import *
from application import jwt

error = Blueprint('error', __name__)

# Catch validation errors
@error.app_errorhandler(ValidationError)
def valid_valid_error(e):
    return jsonify({'code': ERROR_PARAM, 'message': e.messages})

# Catch a database unique constraint error
@error.app_errorhandler(IntegrityError)
def valid_valid_error(e):
    return jsonify({'code': ERROR_INTERNAL, 'message': 'Violation of a unique constraint'})

@jwt.expired_token_loader
def expired_token_callback(expired_token):
    token_type = expired_token['type']
    return jsonify({
        'code': ERROR_PARAM,
        'msg': 'The {} token has expired'.format(token_type)
    })