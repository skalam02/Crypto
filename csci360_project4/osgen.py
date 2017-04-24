from base64 import b64encode
from os import urandom

def osgen():
    random_bytes = urandom(6)
    salt = b64encode(random_bytes).decode('utf-8')
    return salt