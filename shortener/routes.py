from flask_restful import Api
from shortener.views import ShortenerApi


def shortener_routes(api: Api):
    api.add_resource(ShortenerApi, "/api/url/")
