from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from application.api.yuhu_user.models import *
from application import db

class UsersSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Users
        sqla_session = db.session

    id = fields.Integer(dump_only=True)
    username = fields.String(attribute='username', required=True, validate=lambda s: len(s.strip()) > 0,error_messages={'required': 'User name required', 'validator_failed': 'The user name cannot be empty'})
    password = fields.String(load_only=True) 