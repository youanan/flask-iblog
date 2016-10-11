from flask_admin import AdminIndexView, expose


class MyIndexView(AdminIndexView):

    @expose('/')
    def index(self):
        return super(MyIndexView, self).index()
