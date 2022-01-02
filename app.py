from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://msyqdpue:EDeAjLM4oerJuTAM1TWit6n6zUiyQEaQ@castor.db.elephantsql.com/msyqdpue'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
