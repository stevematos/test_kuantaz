from config.exceptions import InstitutionNotFound, InstitutionErrorValidation
from queries.institution import add_institution, get_institution_by_id, update_institution, delete_product
from schemas.institution import InstitutionSchema, InstitutionUpdateSchema

from marshmallow import ValidationError
from sqlalchemy.exc import NoResultFound


def create_institution(data: dict) -> dict:
    schema = InstitutionSchema()
    try:
        institution = schema.load(data)
    except ValidationError as e:
        raise InstitutionErrorValidation(e.messages)

    add_institution(institution)

    return {'message': 'Institution created successfully'}


def get_institution(_id: int):
    schema = InstitutionSchema()

    try:
        institution = get_institution_by_id(_id)
    except NoResultFound:
        raise InstitutionNotFound()

    return schema.dump(institution)


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
