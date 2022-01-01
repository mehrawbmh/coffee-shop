from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://msyqdpue:EDeAjLM4oerJuTAM1TWit6n6zUiyQEaQ@castor.db.elephantsql.com/msyqdpue'
db = SQLAlchemy(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()