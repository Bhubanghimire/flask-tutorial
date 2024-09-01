import functools
from crypt import methods
from xxlimited_35 import error

from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash, session, g
from itsdangerous import NoneAlgorithm
from werkzeug.security import generate_password_hash

from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)