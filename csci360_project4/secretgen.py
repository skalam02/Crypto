import secrets
import string


def secretgen():
    alphabet=string.ascii_letters + string.digits
    while True:
        salt = ''.join(secrets.choice(alphabet) for i in range(8))
        if (any(c.islower() for c in salt)
            and any(c.isupper() for c in salt)
            and sum(c.isdigit() for c in salt) >= 3):
            break
    return salt