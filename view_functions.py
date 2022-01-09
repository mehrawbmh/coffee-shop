from flask import render_template, redirect, request, url_for, escape
from config import db
from models.comment import Comment
from models.products import Product
from models.category import Category

products = Product.query.all()
main_categories = Category.query.filter_by(parent_id=None).all()
food, drink, dessert = [], [], []
for p in products:
    cat_id = p.category_id
    main_cat = Category.query.filter_by(id=cat_id).first()
    parent_id = main_cat.parent_id
    parent = Category.query.get(parent_id)
    if parent.name == 'food':
        food.append(p)
    elif parent.name == 'drink':
        drink.append(p)
    elif parent.name == 'dessert':
        dessert.append(p)
    else:
        raise Exception()  # TODO add exception

basic_data = {
    'title': '~ cafe Game&Taste ~',
    'language': 'en-US',
    'menu_data': {
            'food': food,
            'dessert': dessert,
            'drink': drink
    },
    'links':['index', 'comment', ]
}


def index():
    return render_template('index.html', data=basic_data)


def get_comment():
    name = escape(request.form.get('name'))
    phone = escape(request.form.get('phone'))
    email = escape(request.form.get('email'))
    message = escape(request.form.get('message'))
    comment_obj = Comment(name, message, email, phone=phone)
    db.session.add(comment_obj)
    db.session.commit()

    return redirect(url_for('index'))

def get_orders(orders):
    ...