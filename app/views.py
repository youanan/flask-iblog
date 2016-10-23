# -*- coding:utf-8 -*-
from flask import Blueprint, render_template
from models import Post, User


bp = Blueprint('blog', __name__)


@bp.route('/')
@bp.route('/<int:page>')
def index(page=1):
    paginator = Post.objects.paginate(page=page, per_page=5)
    return render_template("index.html", paginator=paginator)


@bp.route('/posts/<string:post_id>')
def get_post(post_id):
    post = Post.objects(id=post_id).first()
    return render_template("post.html", post=post)

@bp.route('/about')
def about():
    user = User.objects.first()
    return render_template("about.html",user=user)