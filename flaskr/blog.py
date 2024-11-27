import functools
from crypt import methods
from wsgiref.util import request_uri
from xxlimited_35 import error

from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash, session, g
from itsdangerous import NoneAlgorithm
from werkzeug.security import generate_password_hash

from flaskr.auth import login_required
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


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(

                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?,?,?)',(title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))
    return render_template('blog/create.html')


@bp.route('/<int:id>/update')
@login_required
def update(id):
    post = "test"
    return render_template('blog/update.html', post=post)
