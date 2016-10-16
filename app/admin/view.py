# -*- coding:utf-8 -*-
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.mongoengine import ModelView
from wtforms import fields, widgets


class MyIndexView(AdminIndexView):
    '创建自定义视图'
    @expose('/')
    def index(self):
        # return super(MyIndexView, self).index()
        return self.render('admin/my_master.html')


class UserView(ModelView):
    can_create = False
    can_delete = False


# define wtforms widget and field
class CKTextAreaWidget(widgets.TextArea):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('class_', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(fields.TextAreaField):
    widget = CKTextAreaWidget()


class PostView(ModelView):
    column_display_pk = True

    form_overrides = dict(content=CKTextAreaField)
    create_template = 'admin/create_post.html'
    edit_template = 'admin/edit_post.html'

    column_list = ('id', 'title', 'content', 'author', 'tags', 'status', 'create_time', 'modify_time')
    column_labels = dict(id='ID',
                         title=u'标题'
                         )
    column_choices = {
        'status':[
            (0, 'draft'),
            (1, 'published')
        ]
    }
    column_filters = ('title',)
