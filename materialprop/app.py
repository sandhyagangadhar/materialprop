from flask import Flask
from materialprop import api
from materialprop import auth
from materialprop import manage
from materialprop.extensions import apispec
from materialprop.extensions import db
from materialprop.extensions import jwt
from materialprop.extensions import migrate


def create_app(testing=False):
    """Application factory, used to create application"""
    app = Flask("materialprop")
    app.config.from_object("materialprop.config")

    if testing is True:
        app.config["TESTING"] = True

    configure_extensions(app)
    configure_cli(app)
    # configure_apispec(app)
    register_blueprints(app)

    return app


def configure_extensions(app):
    """Configure flask extensions"""
    db.init_app(app)
    # jwt.init_app(app)
    migrate.init_app(app, db)


def configure_cli(app):
    """Configure Flask 2.0's cli for easy entity management"""
    app.cli.add_command(manage.init)


def configure_apispec(app):
    """Configure APISpec for swagger support"""
    apispec.init_app(app, security=[{"jwt": []}])
    apispec.spec.components.security_scheme(
        "jwt", {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    )
    apispec.spec.components.schema(
        "PaginatedResult",
        {
            "properties": {
                "total": {"type": "integer"},
                "pages": {"type": "integer"},
                "next": {"type": "string"},
                "prev": {"type": "string"},
            }
        },
    )


def register_blueprints(app):
    """Register all blueprints for application"""
    # app.register_blueprint(auth.views.blueprint)
    app.register_blueprint(api.views.blueprint)
