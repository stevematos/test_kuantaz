from flask import Blueprint

from config.exceptions import UserNotFound
from config.http_status_code import HTTP_400_BAD_REQUEST, HTTP_200_OK
from services.project import read_all_projects

project_bp = Blueprint('project', __name__, url_prefix='/project')


@project_bp.route('/', methods=['GET'])
def read_all():
    try:
        return read_all_projects(), HTTP_200_OK
    except UserNotFound as e:
        return {'error': e.__str__()}, HTTP_400_BAD_REQUEST
