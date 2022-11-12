from flask import Blueprint
from app.common.http_methods import GET
from ..controllers import ReportController
from ..decorators.service_response import service_response

report = Blueprint("report", __name__)


@report.route("/", methods=GET)
@service_response
def get_report():
    return ReportController.get_report()
