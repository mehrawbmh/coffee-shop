import argparse
from models.cashier import Cashier
from config import db


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Register")
    parser.add_argument('-f', '--first_name', metavar='FirstName', type=str, action='store', required=True,  help=' Your first name')
    parser.add_argument('-l', '--last_name', metavar='LastName', type=str, action='store', required=True, help='your last name')
    parser.add_argument('-ph', '--phone_number', metavar='PhoneNumber', type=int, action='store', required=True, help='your phone number')
    parser.add_argument('-e', '--email', metavar='Email', type=str, action='store', required=True, help='your email')
    parser.add_argument('-p', '--password', metavar='Password', type=str, action='store', required=True, help='your password')
    args = parser.parse_args()

    u = Cashier(first_name=args.first_name, last_name=args.last_name, phone_number=args.phone_number, password=args.password, email=args.email)
    db.session.add(u)
    db.session.commit()
