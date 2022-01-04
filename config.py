from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://msyqdpue:EDeAjLM4oerJuTAM1TWit6n6zUiyQEaQ@castor.db.elephantsql.com/msyqdpue'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)