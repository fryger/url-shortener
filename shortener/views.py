from flask import Response
from flask import request, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from shortener.service import create_short_url, list_short_url


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
