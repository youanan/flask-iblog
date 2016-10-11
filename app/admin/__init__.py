from flask_admin import Admin
from view import MyIndexView


def create_admin(app=None):
    admin = Admin(app, name="iBlogAdmin",
                  index_view=MyIndexView(),
                  base_template='admin/my_master.html')



