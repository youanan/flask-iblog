from flask_admin import Admin


def create_admin(app=None):
    admin = Admin(app, name="iBlogAdmin")
