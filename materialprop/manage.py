import click
from flask.cli import with_appcontext


@click.command("init")
@with_appcontext
def init():
    """Create a new admin user"""
    from materialprop.extensions import db
    from materialprop.models import User

    click.echo("create user")
    user = User(username="admin", email="sandhya.chintalapati@gmail.com", password="Admin@123", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")
