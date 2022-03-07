from marshmallow import Schema, fields
from marshmallow_enum import EnumField
from app.utils.category_enum_type import CategoryEnumType
from app.utils.difficulty_enum_type import DifficultyEnumType


class GetRecepisSchema(Schema):
    page = fields.Integer(required=True)
    per_page = fields.Integer(required=True)
    category = EnumField(CategoryEnumType, allow_none=True)
    preparation_time = fields.String(allow_none=True)
    difficulty = EnumField(DifficultyEnumType, allow_none=True)
    portion_size = fields.String(allow_none=True)