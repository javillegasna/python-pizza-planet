from flask import Blueprint, request
from ..controllers import BeverageController
from ..common.http_methods import GET, POST, PUT
from ..decorators.service_response import service_response

beverage = Blueprint("beverage", __name__)


@beverage.route("/", methods=POST)
@service_response
def create_beverage():
    return BeverageController.create(request.json)


@beverage.route("/", methods=PUT)
@service_response
def update_beverage():
    return BeverageController.update(request.json)


@beverage.route("/id/<_id>", methods=GET)
@service_response
def get_beverage_by_id(_id: int):
    return BeverageController.get_by_id(_id)


@beverage.route("/", methods=GET)
@service_response
def get_beverages():
    return BeverageController.get_all()
