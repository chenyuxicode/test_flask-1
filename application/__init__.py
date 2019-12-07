from flask import Flask, request, make_response, redirect, abort, render_template
from flask_script import Manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_jwt_extended import JWTManager

# Create a database connection
db = SQLAlchemy()
jwt = JWTManager()

# Use factory method to create app for testing
def create_app(config=None):
    app = Flask(__name__)
    if config is not None:
        # Load configuration information
        app.config.from_object(config)

    # Register blueprint object
    from application.common.error_handler import error
    from application.api.yuhu_user.views import yuhu_user

    app.register_blueprint(error, url_prefix='/error')
    app.register_blueprint(yuhu_user, url_prefix='/yuhu_user')

    #
    db.init_app(app)
    jwt.init_app(app)

    return app






