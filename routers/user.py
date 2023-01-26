from flask import Blueprint

from config.exceptions import UserNotFound
from config.http_status_code import HTTP_400_BAD_REQUEST, HTTP_200_OK
from services.user import read_user, read_all_users

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/', methods=['GET'])
def read_all():
    try:
        return read_all_users(), HTTP_200_OK
    except UserNotFound as e:
        return {'error': e.__str__()}, HTTP_400_BAD_REQUEST


@user_bp.route('/<rut>', methods=['GET'])
def read(rut: str):
    try:
        return read_user(rut), HTTP_200_OK
    except UserNotFound as e:
        return {'error': e.__str__()}, HTTP_400_BAD_REQUEST
