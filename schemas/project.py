from marshmallow import Schema, fields, post_load
from models import Project


class ProjectBaseSchema(Schema):
    name = fields.String()
    start_date = fields.Date()
    end_date = fields.Date()

    @post_load
    def make_institution(self, data, **kwargs):
        return Project(**data)


class ProjectSchema(ProjectBaseSchema):
    pass

