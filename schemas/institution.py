from marshmallow import Schema, fields, post_load
from models import Institution


class InstitutionBaseSchema(Schema):
    name = fields.String()
    description = fields.String()
    address = fields.String()

    @post_load
    def make_institution(self, data, **kwargs):
        return Institution(**data)


class InstitutionValidationSchema(InstitutionBaseSchema):
    name = fields.String(required=True)
    description = fields.String(required=True)
    address = fields.String(required=True)


class InstitutionGetSchema(InstitutionBaseSchema):
    pass


class InstitutionFullGetSchema(InstitutionBaseSchema):
    projects = fields.Nested("ProjectGetResponsibleUserSchema", many=True)


class InstitutionUpdateSchema(InstitutionBaseSchema):
    pass
