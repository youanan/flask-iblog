# -*- coding:utf-8 -*-
from flask import Blueprint, render_template
from models import Post


bp = Blueprint('blog', __name__)


@bp.route('/')
@bp.route('/<int:page>')
def index(page=1):
    paginator = Post.objects.paginate(page=page, per_page=5)
    return render_template("index.html", paginator=paginator)


