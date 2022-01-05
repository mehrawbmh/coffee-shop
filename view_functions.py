from flask import render_template, redirect, request, url_for, escape
from config import db
from models.comment import Comment

basic_data = {
    'title': '~ cafe Game&Taste ~',
    'language': 'en-US'

}


def index():
    return render_template('index.html', data=basic_data)


def get_comment():
    name = escape(request.form.get('name'))
    phone = escape(request.form.get('phone'))
    email = escape(request.form.get('email'))
    message = escape(request.form.get('message'))
    # print(name, phone, email, message)
    comment_obj = Comment(name, message, email, phone=phone)
    db.session.add(comment_obj)
    db.session.commit()

    return redirect(url_for('index'))
