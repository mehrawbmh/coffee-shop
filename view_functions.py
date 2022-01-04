from flask import render_template, redirect, request, url_for
# from models.comment import Comment

basic_data = {
    'title' : 'Game&Taste cafe',
    'language' : 'en-US'
}


def index():
    return render_template('index.html', data=basic_data)


def get_comment():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    message = request.form.get('message')
    print(name,phone,email,message)
    # comment_obj = Comment(name, message, email, phone=phone)
    return redirect(url_for('index'))
