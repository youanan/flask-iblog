# -*- coding:utf-8 -*-
from flask_admin import Admin
from view import MyIndexView, UserView, PostView
from app.models import User, Post


def create_admin(app=None):
    admin = Admin(app,
                  name="iBlogAdmin",
                  index_view=MyIndexView(),
                  base_template='admin/my_master.html')
    admin.add_view(UserView(User, endpoint='users', name="UserList"))
    admin.add_view(PostView(Post))


