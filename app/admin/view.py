# -*- coding:utf-8 -*-
from flask_admin.contrib.mongoengine import ModelView
from wtforms import fields, widgets
from flask_admin import AdminIndexView, expose
from flask_login import current_user, login_user, logout_user, login_required
from flask import redirect, url_for, request
from forms import LoginForm


class MyIndexView(AdminIndexView):
    '创建自定义视图'
    @expose('/')
    def index(self):
        if not current_user.is_authenticated():
            return redirect(url_for('.login'))
        return super(MyIndexView, self).index()

    @expose('/login', methods=('GET', 'POST'))
    def login(self):
        form = LoginForm(request.form)
        if request.method == 'POST' and form.validate():
            user = form.get_user()
            login_user(user)
            redirect(url_for('.index'))
        self._template_args['form'] = form
        return super(MyIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        logout_user()
        return redirect(url_for('.index'))



class UserView(ModelView):
    can_create = False
    can_delete = False

    def is_accessible(self):
        return current_user.is_authenticated()


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

    def is_accessible(self):
        return current_user.is_authenticated()
