# -*- coding:utf-8 -*-
from flask import Blueprint, render_template
from models import Post


bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    posts = Post.objects.all()
    return render_template("index.html", posts=posts)


