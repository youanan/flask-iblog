# -*- coding:utf-8 -*-
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.mongoengine import ModelView

class MyIndexView(AdminIndexView):
    '创建自定义视图'
    @expose('/')
    def index(self):
        #return super(MyIndexView, self).index()
        return self.render('admin/my_master.html')

class UserView(ModelView):
    can_create = False
    can_delete = False

class PostView(ModelView):
    pass