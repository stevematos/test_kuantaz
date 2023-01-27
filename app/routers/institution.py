from config.constants import PATH_SWAGGER_DOCS
from config.exceptions import InstitutionErrorValidation, InstitutionNotFound
from config.http_status_code import HTTP_200_OK, HTTP_400_BAD_REQUEST
from flasgger import swag_from
from flask import Blueprint, request
from services.institution import (
    create_institution,
    deleted_institution,
    read_all_institutions,
    read_institution,
    read_institutions_with_address_google_maps,
    updated_institution,
)

institution_bp = Blueprint("institution", __name__, url_prefix="/institution")


@institution_bp.route("/", methods=["POST"])
@swag_from(f"{PATH_SWAGGER_DOCS}/institution/create.yml")
def create():
    data = request.json
    try:
        return create_institution(data), HTTP_200_OK
    except InstitutionErrorValidation as e:
        return {"error": e.__str__()}, HTTP_400_BAD_REQUEST


@institution_bp.route("/", methods=["GET"])
@swag_from(f"{PATH_SWAGGER_DOCS}/institution/read_all.yml")
def read_all():
    try:
        return read_all_institutions(), HTTP_200_OK
    except InstitutionErrorValidation as e:
        return {"error": e.__str__()}, HTTP_400_BAD_REQUEST


@institution_bp.route("/<id>", methods=["GET"])
@swag_from(f"{PATH_SWAGGER_DOCS}/institution/read_by_id.yml")
def read_by_id(id: int):
    try:
        return read_institution(id), HTTP_200_OK
    except InstitutionNotFound as e:
        return {"error": e.__str__()}, HTTP_400_BAD_REQUEST


@institution_bp.route("/<id>", methods=["PUT"])
@swag_from(f"{PATH_SWAGGER_DOCS}/institution/update.yml")
def update(id: int):
    data = request.json
    try:
        return updated_institution(id, data), HTTP_200_OK
    except InstitutionNotFound as e:
        return {"error": e.__str__()}, HTTP_400_BAD_REQUEST


@institution_bp.route("/<id>", methods=["DELETE"])
@swag_from(f"{PATH_SWAGGER_DOCS}/institution/delete.yml")
def delete(id: int):
    try:
        return deleted_institution(id), HTTP_200_OK
    except InstitutionNotFound as e:
        return {"error": e.__str__()}, HTTP_400_BAD_REQUEST


@institution_bp.route("/address-google-maps", methods=["GET"])
@swag_from(f"{PATH_SWAGGER_DOCS}/institution/read_all_address_google_maps.yml")
def read_all_address_google_maps():
    try:
        return read_institutions_with_address_google_maps(), HTTP_200_OK
    except InstitutionErrorValidation as e:
        return {"error": e.__str__()}, HTTP_400_BAD_REQUEST
