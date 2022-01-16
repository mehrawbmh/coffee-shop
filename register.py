from core.utils import hash_generator
from getpass import getpass
from config import db, app
from models.cashier import Cashier
from sqlalchemy.exc import SQLAlchemyError


# TODO email and phone number validation

@app.cli.command('create-cashier')
def create_cashier():
    username = input('>>> Username: ')
    password = hash_generator(getpass('>>> Password: '))
    phone = input('>>> Phone number [must be unique]: ')
    email = input('>>> Email [must be unique]: ')
    firstname = ''
    lastname = ''
    if password and username:
        try:
            # user_cashier = Cashier(username=username, password=password, email=email, phone_number=phone,
            #                        first_name=firstname, last_name=lastname)
            user_cashier = Cashier(username, firstname, lastname, phone, email,password)
            db.session.add(user_cashier)
            db.session.commit()
            print('user cashier successfully created')
            return True
        except SQLAlchemyError as err:
            print((err.__dict__['orig']))
            return False
