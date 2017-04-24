import secrets
from osgen import *
from secretgen import *

def salt():
    decision=secrets.randbelow(2)
    if (decision):
        return secretgen()
    else:
        return osgen()
