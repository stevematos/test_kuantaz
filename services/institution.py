from config.exceptions import InstitutionNotFound, InstitutionErrorValidation
from queries.institution import add_institution, get_institution_by_id, update_institution, delete_product, \
    get_all_institutions
from schemas.institution import InstitutionValidationSchema, InstitutionUpdateSchema, \
    InstitutionGetSchema

from marshmallow import ValidationError
from sqlalchemy.exc import NoResultFound

from utils.institution import adding_extra_data


def create_institution(data: dict) -> dict:
    schema = InstitutionValidationSchema()
    try:
        institution = schema.load(data)
    except ValidationError as e:
        raise InstitutionErrorValidation(e.messages)

    add_institution(institution)

    return {'message': 'Institution created successfully'}


def read_all_institutions() -> list[dict]:
    schema = InstitutionGetSchema(many=True)
    return schema.dump(get_all_institutions())


def read_institution(_id: int) -> dict:
    try:
        institution = get_institution_by_id(_id, is_dump=True)
    except NoResultFound:
        raise InstitutionNotFound()

    return institution


def updated_institution(_id: int, data: dict) -> dict:
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


def deleted_institution(_id: int) -> dict:
    try:
        get_institution_by_id(_id)
    except NoResultFound:
        raise InstitutionNotFound()

    delete_product(_id)

    return {'message': 'Institution deleted successfully'}


def read_institutions_with_address_google_maps() -> list[dict]:
    schema = InstitutionGetSchema(many=True)

    institutions = get_all_institutions()
    data_institutions = schema.dump(institutions)

    data_institutions = [adding_extra_data(data_institution) for data_institution in data_institutions]

    return data_institutions
