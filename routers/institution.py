from flask import Blueprint, request

from config.exceptions import InstitutionNotFound, InstitutionErrorValidation
from config.http_status_code import HTTP_400_BAD_REQUEST, HTTP_200_OK
from services.institution import create_institution, get_institution, updated_institution, deleted_institution

institution_bp = Blueprint('institution', __name__, url_prefix='/institution')


@institution_bp.route('/', methods=['POST'])
def create():
    data = request.json
    try:
        return create_institution(data), HTTP_200_OK
    except InstitutionErrorValidation as e:
        return {'error': e.__str__()}, HTTP_400_BAD_REQUEST


@institution_bp.route('/<id>', methods=['GET'])
def read(id: int):
    try:
        return get_institution(id), HTTP_200_OK
    except InstitutionNotFound as e:
        return {'error': e.__str__()}, HTTP_400_BAD_REQUEST


@institution_bp.route('/<id>', methods=['PUT'])
def update(id: int):
    data = request.json
    try:
        return updated_institution(id, data), HTTP_200_OK
    except InstitutionNotFound as e:
        return {'error': e.__str__()}, HTTP_400_BAD_REQUEST


@institution_bp.route('/<id>', methods=['DELETE'])
def delete(id: int):
    try:
        return deleted_institution(id), HTTP_200_OK
    except InstitutionNotFound as e:
        return {'error': e.__str__()}, HTTP_400_BAD_REQUEST