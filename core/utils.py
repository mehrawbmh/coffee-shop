import hashlib


def hash_generator(text: str) -> str:
    hash_func = hashlib.sha256()
    hash_func.update(bytes(text, 'utf-8'))
    hashed_value = hash_func.hexdigest()
    return hashed_value
