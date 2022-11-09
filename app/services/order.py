from flask import Blueprint, request
from ..common.http_methods import GET, POST
from ..controllers import OrderController
from ..decorators.service_response import service_response


order = Blueprint("order", __name__)


@order.route("/", methods=POST)
@service_response
def create_order():
    return OrderController.create(request.json)


@order.route("/id/<_id>", methods=GET)
@service_response
def get_order_by_id(_id: int):
    return OrderController.get_by_id(_id)


@order.route("/", methods=GET)
@service_response
def get_orders():
    return OrderController.get_all()
