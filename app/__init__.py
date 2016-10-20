# -*- coding:utf-8 -*-
from flask import Flask
from views import bp
from models import db
from app.admin import create_admin
from flask.ext.login import LoginManager


def create_app():
    # 定义一个工厂函数,被项目根目录run.py使用运行
    app = Flask(__name__)
    # 创建Flask类实例
    app.config.from_object('config')
    # 指定flask配置文件
    register_blueprints(app)
    # 注册蓝图
    register_database(app)
    # 注册数据库
    create_admin(app)
    # 注册flask-admin
    init_login(app)
    # 注册flask-login
    return app


def register_blueprints(app):
    app.register_blueprint(bp)


def register_database(app):
    db.init_app(app)


def init_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.objects(id=user_id).first()
