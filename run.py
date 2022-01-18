from view_functions import index, get_comment, cashier_login, get_orders, cashier_logout, cashier_panel, add_product
from view_functions import show_product, edit_product
from config import app

app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
app.add_url_rule('/comment', 'comment', get_comment, methods=['POST'])
app.add_url_rule('/get_order', 'order', get_orders, methods=['POST'])
app.add_url_rule('/login', 'login', cashier_login, methods=['GET', 'POST'])
app.add_url_rule('/logout', 'logout', cashier_logout)
app.add_url_rule('/cashier-panel', 'cashier_panel', cashier_panel)
app.add_url_rule('/add_product', 'add_product', add_product, methods=['POST', 'GET'])
app.add_url_rule('/show_product', 'show_product', show_product, methods=['GET'])
app.add_url_rule('/edit_product', 'edit_product', edit_product, methods=['POST', 'GET'])

if __name__ == '__main__':
    app.run(debug=True)
