from flask import Blueprint, request

from config.exceptions import InstitutionNotFound, InstitutionErrorValidation
from config.http_status_code import HTTP_400_BAD_REQUEST, HTTP_200_OK
from services.institution import create_institution, read_institution, updated_institution, deleted_institution, \
    read_all_institutions

institution_bp = Blueprint('institution', __name__, url_prefix='/institution')


@institution_bp.route('/', methods=['POST'])
def create():
    data = request.json
    try:
        return create_institution(data), HTTP_200_OK
    except InstitutionErrorValidation as e:
        return {'error': e.__str__()}, HTTP_400_BAD_REQUEST


@institution_bp.route('/', methods=['GET'])
def read_all():
    try:
        return read_all_institutions(), HTTP_200_OK
    except InstitutionErrorValidation as e:
        return {'error': e.__str__()}, HTTP_400_BAD_REQUEST


@institution_bp.route('/<id>', methods=['GET'])
def read_by_id(id: int):
    try:
        return read_institution(id), HTTP_200_OK
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
