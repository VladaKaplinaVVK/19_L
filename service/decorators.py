import jwt
from flask import request, abort
from constants import JWT_SECRET, JWT_ALG


def auth_requered(func):
    def wrapper(*args, **kwarg):
        if "Authorization" not in request.headers:
            abort(401)
        token = request.headers["Authorization"]
        try:
            jwt.decode(token, JWT_SECRET,  algorithm=[JWT_ALG])
        except Exception as e:
            print(f"JWR decode error {e})")
            abort(401)
        return func(*args, **kwarg)

    return wrapper


def admin_requered(func):
    def wrapper(*args, **kwarg):
        if "Authorization" not in request.headers:
            abort(401)
        token = request.headers["Authorization"]
        try:
            jwt.decode(token, JWT_SECRET, algorithm=[JWT_ALG])
        except Exception as e:
            print(f"JWR decode error {e})")
            abort(401)
        else:
            if data["role"] == "admin":
                return func(*args, **kwarg)
        abort(403)
    return wrapper
