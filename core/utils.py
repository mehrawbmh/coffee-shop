import hashlib
from flask import request, redirect, url_for


def hash_generator(text: str) -> str:
    hash_func = hashlib.sha256()
    hash_func.update(bytes(text, 'utf-8'))
    hashed_value = hash_func.hexdigest()
    return hashed_value


def login_required(func):
    def inner(*args, **kwargs):
        user_id = request.cookies.get('user_logged_in_id', None)
        if user_id:
            return func(*args, **kwargs)
        return redirect(url_for('login'))
    return inner
