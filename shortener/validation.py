from marshmallow import Schema, fields, validate


class CreateShortUrlInputSchema(Schema):

    url_long = fields.Str(required=True, validate=validate.URL(relative=False))
    url_short = fields.Str(required=False, validate=validate.Length(min=1, max=8))
    expiration = fields.DateTime()
