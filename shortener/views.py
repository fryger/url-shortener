from flask import Response, redirect
from flask import request, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from shortener.service import (
    create_short_url,
    list_short_url,
    delete_short_url,
    resolve_short_url,
)

from utils.http_code import HTTP_302_FOUND


class ShortenerApi(Resource):
    @staticmethod
    @jwt_required()
    def post() -> Response:
        input_data = request.get_json()
        response, status = create_short_url(request, input_data)
        return make_response(response, status)

    @staticmethod
    @jwt_required()
    def get() -> Response:
        response, status = list_short_url(request)
        return make_response(response, status)

    @staticmethod
    @jwt_required()
    def delete() -> Response:
        input_data = request.get_json()
        response, status = delete_short_url(request, input_data)
        return make_response(response, status)


class Resolver(Resource):
    @staticmethod
    def get(short_url) -> Response:
        response, status = resolve_short_url(request, short_url)

        if status == HTTP_302_FOUND:
            return redirect(response)

        return make_response(response, status)
