from marshmallow import Schema, fields, post_load
from models import Project


class ProjectBaseSchema(Schema):
    name = fields.String()

    @post_load
    def make_institution(self, data, **kwargs):
        return Project(**data)


class ProjectGetSchema(ProjectBaseSchema):
    start_date = fields.Date()
    end_date = fields.Date()


class ProjectGetResponsibleUserSchema(ProjectGetSchema):
    responsible_user = fields.Nested("UserGetSchema", required=True)


class ProjectEndDateSchema(ProjectBaseSchema):
    end_date = fields.Date()

