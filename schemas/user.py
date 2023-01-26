from marshmallow import Schema, fields, post_load
from models import User
from schemas.project import ProjectSchema


class UserBaseSchema(Schema):
    name = fields.String()
    surname = fields.String()
    age = fields.Integer()
    RUT = fields.String()
    position = fields.String()
    date_of_birth = fields.Date()

    @post_load
    def make_institution(self, data, **kwargs):
        return User(**data)


class UserGetSchema(UserBaseSchema):
    pass


class UserFullGetSchema(UserBaseSchema):
    projects = fields.Nested(ProjectSchema, many=True)
