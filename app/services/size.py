from flask import Blueprint, request
from ..controllers import SizeController
from ..common.http_methods import GET, POST, PUT
from ..decorators.service_response import service_response

size = Blueprint("size", __name__)


@size.route("/", methods=POST)
@service_response
def create_size():
    return SizeController.create(request.json)


@size.route("/", methods=PUT)
@service_response
def update_size():
    return SizeController.update(request.json)


@size.route("/id/<_id>", methods=GET)
@service_response
def get_size_by_id(_id: int):
    return SizeController.get_by_id(_id)


@size.route("/", methods=GET)
@service_response
def get_sizes():
    return SizeController.get_all()
