from core.utils import hash_generator
from getpass import getpass
from config import db, app
from models.cashier import Cashier
from sqlalchemy.exc import SQLAlchemyError
import re as regex
from log import *


def phone_validation(phone: str):
    if len(phone) not in [11, 13]:
        return False
    if not (phone.startswith('0') or phone.startswith('+98')):
        print("Phone number error.", end='\t')
        return False
    return True


def email_validation(email: str):
    valid_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if regex.fullmatch(valid_pattern, email):
        return True
    print("Email error.", end='\t')
    return False


@app.cli.command('create-cashier')
def create_cashier():
    username = input('>>> Username: ')
    password = hash_generator(getpass('>>> Password: '))
    phone = input('>>> Phone number [must be unique]: ')
    email = input('>>> Email [must be unique]: ')
    firstname = ''
    lastname = ''
    if not (email_validation(email) and phone_validation(phone)):
        print("Please Enter it in a valid format!")
        logging.info('invalid input for creat_cashier function')
        return False
    if password and username:
        try:
            # user_cashier = Cashier(username=username, password=password, email=email, phone_number=phone,
            #                        first_name=firstname, last_name=lastname)
            user_cashier = Cashier(username, firstname, lastname, phone, email, password)
            db.session.add(user_cashier)
            db.session.commit()
            print('user cashier successfully created')
            logging.info('cashier registerd')
            return True
        except SQLAlchemyError as err:
            print((err.__dict__['orig']))
            logging.error('database not responding')
            return False
