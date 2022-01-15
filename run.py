from view_functions import index, get_comment, cashier_login, get_orders, cashier_logout
from config import app

app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
app.add_url_rule('/comment', 'comment', get_comment, methods=['POST'])
app.add_url_rule('/get_order', 'order', get_orders, methods=['POST'])
app.add_url_rule('/login', 'login', cashier_login, methods=['GET', 'POST'])
app.add_url_rule('/logout', 'logout', cashier_logout)

if __name__ == '__main__':
    app.run(debug=True)
