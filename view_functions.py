import datetime

from flask import render_template, redirect, request, url_for, escape, Response, make_response
from config import db
from models.baskets import Basket
from models.comment import Comment
from models.products import Product
from models.category import Category
from models.cashier import Cashier
from core.utils import hash_generator


products = Product.query.all()
# main_categories = Category.query.filter_by(parent_id=None).all()
food, drink, dessert = [], [], []
discount_list = []
for p in products:
    if p.discount:
        discount_list.append(p)
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
discount_list = sorted(discount_list, key=lambda x: x.discount, reverse=True)
basic_data = {
    'title': '~ cafe Game&Taste ~',
    'language': 'en-US',
    'menu_data': {
        'food': food,
        'dessert': dessert,
        'drink': drink
    },
    'links': ['index', 'comment', 'order'],
    'maximum_offer':5
}


def index():
    return render_template('index.html', data=basic_data, offers=discount_list)


def get_comment():
    name = escape(request.form.get('name'))
    phone = escape(request.form.get('phone'))
    email = escape(request.form.get('email'))
    message = escape(request.form.get('message'))
    comment_obj = Comment(name, message, email, phone=phone)
    db.session.add(comment_obj)
    db.session.commit()

    return redirect(url_for('index'))


def get_orders():
    if request.method == 'POST':
        orders = request.json
        orders = {
            "basket_items": [
                {
                    "item_id": 23,
                    "number": 1
                },
                {
                    "item_id": 24,
                    "number": 3
                }
            ]
        }
        orders = orders.get("basket_items")
        if orders:
            now = datetime.datetime.now()
            basket = {
                "id": 1,
                "table_id": 3,
                "created_at": now,
                "updated_at": now
            }
            orders = list(map(
                lambda x: {
                    "product_id": x.get("item_id"),
                    "count": x.get("number"),
                    "basket_id": basket.get("id")
                },
                orders
            ))
            database_session = db.session
            database_session.bulk_save_objects(orders)
            database_session.commit()
            return Response('ok', 201)
        return Response('failed', 400)
    return Response('method not allowed', 405)


def cashier_login():
    basic_data['title'] = 'Cashier | Login'
    if request.method == 'GET':
        user_id = request.cookies.get('user_logged_in_id', None)
        if user_id:
            user = Cashier.query.filter_by(id=user_id).first()
            return f'welcome {user.username}'  # todo: return render_temp   late('cashier_dashbord.html', user=user)
        else:
            return render_template('cashier_login.html', data=basic_data)
    elif request.method == 'POST':
        username = escape(request.form['username'])
        password = hash_generator(escape(request.form['password']))
        user = Cashier.query.filter_by(username=username).first()
        if user:
            if password == user.password:
                resp = make_response(f'welcome {user.username}')  # todo: redirect(url_for('cashier_dashbord'))
                resp.set_cookie('user_logged_in_id', str(user.id))
                return resp
        else:
            return 'unknown user', 401
    else:
        return 'Method not allowed', 405


def cashier_logout():
    resp = make_response(redirect(url_for('login')))
    resp.delete_cookie('user_logged_in_id')
    return resp
