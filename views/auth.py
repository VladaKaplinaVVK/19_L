from os import abort

from flask import request
from flask_restx import Resource, Namespace
from implemented import auth_service
from service.decorators import *

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    @auth_requered
    def post(self):
        req_json = request.json
        username = req_json.get("username")
        password = req_json.get("password")
        if not (username or password):
            return "Необходимо имя и пароль", 400

        tokens = auth_service.generate_tokens(username, password)
        if tokens:
            return tokens
        else:
            return "Ошибка в запросе", 400

    @auth_requered
    def put(self):
        req_json = request.json
        ref_token = req_json.get("refresh_token")
        if not ref_token:
            return "Не задан токен", 400

        tokens = auth_service.approve_refresh_token(ref_token)
        if tokens:
            return tokens
        else:
            return "Ошибка в запросе", 400
