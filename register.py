import hashlib
from getpass import getpass
from config import db, app
from models.cashier import Cashier
from sqlalchemy.exc import SQLAlchemyError

hash_func = hashlib.sha256()


@app.cli.command('create-cashier')
def create_cashier():
    username = input('>>> Username : ')
    hash_func.update(bytes(getpass('>>> Password: '), 'utf-8'))
    password = hash_func.hexdigest()
    email = input('>>> Email [optional]: ')
    firstname = ''
    lastname = ''
    phone = ''
    if password and username:
        try:
            user_cashier = Cashier(username=username, password=password, email=email, phone_number=phone,
                                   first_name=firstname, last_name=lastname)
            db.session.add(user_cashier)
            db.session.commit()
            return 'user cashier successfully created'
        except SQLAlchemyError as err:
            return err
