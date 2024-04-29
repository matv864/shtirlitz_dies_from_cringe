import hashlib


def get_hashing_password(password: str) -> str:
    hash = hashlib.sha256()
    hash.update(bytes(password, 'UTF-8'))
    return hash.hexdigest()
