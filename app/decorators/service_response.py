from functools import wraps
from flask import jsonify


def service_response(service):
    @wraps(service)
    def wrapper_service(*args, **kwargs):
        items, error = service(*args, **kwargs)
        response = items if not error else {"error": error}
        status_code = 200 if items else 404 if not error else 400
        return jsonify(response), status_code

    return wrapper_service
