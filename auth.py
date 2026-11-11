from utils import hash_password, validate_email

USERS = {}


def find_user(email):
    return USERS.get(email)


def register_user(email, password):
    if not validate_email(email):
        raise ValueError("Email không hợp lệ")
    USERS[email] = hash_password(password)
    return True


def login(email, password):
    stored = find_user(email)
    return stored == hash_password(password)
