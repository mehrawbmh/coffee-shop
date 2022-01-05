from view_functions import index, get_comment
from config import app

app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
app.add_url_rule('/comment', 'comment', get_comment, methods=['POST'])

if __name__ == '__main__':
    app.run()
