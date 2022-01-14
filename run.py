from flask import Flask

from view_functions import index, get_comment, cashier_login, get_orders
from config import app
app = Flask(__name__)
app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
app.add_url_rule('/comment', 'comment', get_comment, methods=['POST'])
app.add_url_rule('/get_order', 'order', get_orders, methods=['POST'])
app.add_url_rule('/login', 'login', cashier_login, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run()
