from marshmallow import Schema, fields, validate


class GetPublicRecipesSchema(Schema):
    page = fields.Integer(required=True)
    per_page = fields.Integer(required=True)
    category = fields.String(
        allow_none=True, validate=validate.OneOf(["Doce", "Salgado", "Bebida"])
    )
    preparation_time = fields.Integer(allow_none=True)
    difficulty = fields.String(
        allow_none=True, validate=validate.OneOf(["Fácil", "Intermediário", "Difícil"])
    )
    portion_size = fields.Integer(allow_none=True)