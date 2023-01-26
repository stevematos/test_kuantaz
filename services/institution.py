from config.exceptions import InstitutionNotFound, InstitutionErrorValidation
from queries.institution import add_institution, get_institution_by_id, update_institution, delete_product, \
    get_all_institutions
from schemas.institution import InstitutionValidationSchema, InstitutionUpdateSchema, InstitutionFullGetSchema, \
    InstitutionGetSchema

from marshmallow import ValidationError
from sqlalchemy.exc import NoResultFound


def create_institution(data: dict) -> dict:
    schema = InstitutionValidationSchema()
    try:
        institution = schema.load(data)
    except ValidationError as e:
        raise InstitutionErrorValidation(e.messages)

    add_institution(institution)

    return {'message': 'Institution created successfully'}


def read_all_institutions():
    schema = InstitutionGetSchema(many=True)
    return schema.dump(get_all_institutions())


def read_institution(_id: int):
    try:
        institution = get_institution_by_id(_id, is_dump=True)
    except NoResultFound:
        raise InstitutionNotFound()

    return institution


def updated_institution(_id: int, data: dict):
    schema = InstitutionUpdateSchema()

    try:
        get_institution_by_id(_id)
    except NoResultFound:
        raise InstitutionNotFound()

    try:
        institution = schema.load(data)
    except ValidationError as e:
        raise InstitutionErrorValidation(e.messages)

    update_institution(_id, institution)

    return {'message': 'Institution updated successfully'}


def deleted_institution(_id: int):
    try:
        get_institution_by_id(_id)
    except NoResultFound:
        raise InstitutionNotFound()

    delete_product(_id)

    return {'message': 'Institution deleted successfully'}
