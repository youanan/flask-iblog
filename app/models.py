# -*- coding:utf-8 -*-
from flask_mongoengine import MongoEngine
from datetime import datetime

db = MongoEngine()


class User(db.Document):
    name = db.StringField(required=True, max_length=64)
    password = db.StringField(max_length=256)
    email = db.StringField(max_length=64)
    description = db.StringField(max_length=1024)


class Post(db.Document):
    title = db.StringField(required=True, max_length=64)
    content = db.StringField(required=True)
    author = db.ReferenceField(User)
    tags = db.ListField(db.StringField(max_length=32))
    status = db.IntField(required=True)
    create_time = db.DateTimeField(default=datetime.now)
    modify_time = db.DateTimeField(default=datetime.now)
