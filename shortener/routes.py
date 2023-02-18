from flask_restful import Api
from shortener.views import ShortenerApi, Resolver


def shortener_routes(api: Api):
    api.add_resource(ShortenerApi, "/api/url/")
    api.add_resource(Resolver, "/<short_url>")
