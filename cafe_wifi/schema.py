from marshmallow import Schema, fields


class CafeSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    map_url = fields.Str(required=True)
    img_url = fields.Str(required=True)
    location = fields.Str(required=True)
    has_sockets = fields.Boolean(required=True)
    has_toilet = fields.Boolean(required=True)
    has_wifi = fields.Boolean(required=True)
    can_take_calls = fields.Boolean(required=True)
    seats = fields.Str(required=False)
    coffee_price = fields.Str(required=False)


class UpdateCafeSchema(Schema):
    has_sockets = fields.Boolean(required=False, allow_none=True)
    has_toilet = fields.Boolean(required=False, allow_none=True)
    has_wifi = fields.Boolean(required=False, allow_none=True)
    can_take_calls = fields.Boolean(required=False, allow_none=True)
    seats = fields.Str(required=False, allow_none=True)
    coffee_price = fields.Str(required=False, allow_none=True)


class PaginationSchema(Schema):
    page = fields.Int()
    page_size = fields.Int()


class BasePageSchema(Schema):
    page = fields.Int(required=True, dump_only=True)
    per_page = fields.Int(required=True, dump_only=True)
    pages = fields.Int(required=True, dump_only=True)
    total = fields.Int(required=True, dump_only=True)


class PageCafeSchema(BasePageSchema):
    items = fields.List(fields.Nested(CafeSchema(), dump_only=True))

