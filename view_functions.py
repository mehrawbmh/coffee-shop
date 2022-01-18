from datetime import datetime
from flask import render_template, redirect, request, url_for, escape, Response, make_response, flash
from config import db
from models.baskets import Basket
from models.comment import Comment
from models.orders import Order
from models.products import Product
from models.category import Category
from models.cashier import Cashier
from models.table import Table
from models.baskets import BasketItem, Basket
from core.utils import hash_generator, login_required
from core.exceptions import FrontError, DBError

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
        raise DBError('products', "The product category wasn't one of these three:[food,drink,dessert]")
discount_list = sorted(discount_list, key=lambda x: x.discount, reverse=True)
available_tables = [table.table_number for table in Table.query.filter_by(in_use=False).all()]
basic_data = {
    'title': '~ cafe Game&Taste ~',
    'language': 'en-US',
    'menu_data': {
        'food': food,
        'dessert': dessert,
        'drink': drink
    },
    'tables': available_tables,
    'links': ['index', 'comment', 'order'],
    'maximum_offer': 5
}
cashier_data = {
    'title': 'Cashier',
    'links': ['dashboard', 'add_product', 'home'],
    'language': 'en_US'
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


def create_new_basket(orders):
    total_price = 0
    with_discount = 0
    table_num = orders[-1]
    try:
        table_id = Table.query.filter_by(table_number=table_num).first().id
        Table.change_table_status(table_id)
        basket_object = Basket.make_new(table_id)
        for i in range(0, len(orders) - 1, 2):
            product_id = orders[i]
            count = orders[i + 1]
            new_item = BasketItem(product_id, basket_object.id, count)
            total_price += new_item.total_price()
            with_discount += new_item.total_price_with_discount()
            db.session.add(new_item)
        db.session.commit()
    except:
        raise FrontError("creating new instance of basket or basket items failed.")
    return basket_object, total_price, with_discount


def get_orders():
    if request.method == 'POST':
        try:
            orders = request.json
            basket_response = create_new_basket(orders)
            basket = basket_response[0]
            total_price = basket_response[1]
            total_with_discount = basket_response[2]
            final_order = Order.add_order(total_price=total_price, total_price_discount=total_with_discount,
                                          basket_id=basket.id)
            print(final_order)
            return Response(f'{total_with_discount}, {Order.id}', 201)
        except Exception:
            return Response('failed', 400)
    return Response('method not allowed', 405)


def cashier_login():
    basic_data['title'] = 'Cashier | Login'
    if request.method == 'GET':
        user_id = request.cookies.get('user_logged_in_id', None)
        if user_id:
            return redirect(url_for('cashier_panel'))
        else:
            return render_template('cashier_login.html', data=basic_data)
    elif request.method == 'POST':
        username = escape(request.form['username'])
        password = hash_generator(escape(request.form['password']))
        user = Cashier.query.filter_by(username=username).first()
        if user:
            if password == user.password:
                resp = make_response(redirect(url_for('cashier_panel')))
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


@login_required
def cashier_panel():
    return render_template('cashier/index.html', data=cashier_data)
