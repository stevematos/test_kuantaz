from config.constants import PATH_SWAGGER_DOCS
from config.exceptions import UserNotFound
from config.http_status_code import HTTP_200_OK, HTTP_400_BAD_REQUEST
from flasgger import swag_from
from flask import Blueprint
from services.user import read_all_users, read_user_by_rut

user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("/", methods=["GET"])
@swag_from(f"{PATH_SWAGGER_DOCS}/user/read_all.yml")
def read_all():
    try:
        return read_all_users(), HTTP_200_OK
    except UserNotFound as e:
        return {"error": e.__str__()}, HTTP_400_BAD_REQUEST


@user_bp.route("/<rut>", methods=["GET"])
@swag_from(f"{PATH_SWAGGER_DOCS}/user/read_by_rut.yml")
def read_by_rut(rut: str):
    try:
        return read_user_by_rut(rut), HTTP_200_OK
    except UserNotFound as e:
        return {"error": e.__str__()}, HTTP_400_BAD_REQUEST
