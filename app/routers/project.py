from flask import Blueprint

from config.constants import PATH_SWAGGER_DOCS
from config.exceptions import UserNotFound
from config.http_status_code import HTTP_400_BAD_REQUEST, HTTP_200_OK
from services.project import read_all_projects, read_projects_with_days_to_end
from flasgger import swag_from

project_bp = Blueprint('project', __name__, url_prefix='/project')


@project_bp.route('/', methods=['GET'])
@swag_from(f'{PATH_SWAGGER_DOCS}/project/read_all.yml')
def read_all():
    try:
        return read_all_projects(), HTTP_200_OK
    except UserNotFound as e:
        return {'error': e.__str__()}, HTTP_400_BAD_REQUEST


@project_bp.route('/count-days-to-end', methods=['GET'])
@swag_from(f'{PATH_SWAGGER_DOCS}/project/read_days_to_end.yml')
def read_days_to_end():
    try:
        return read_projects_with_days_to_end(), HTTP_200_OK
    except UserNotFound as e:
        return {'error': e.__str__()}, HTTP_400_BAD_REQUEST