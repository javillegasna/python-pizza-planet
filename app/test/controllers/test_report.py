import pytest

from app.controllers import ReportController


def test_get_report(app, create_orders):
    created_report, error = ReportController.get_report()
    pytest.assume(error is None)
    for param, value in created_report.items():
        pytest.assume(value == created_report[param])
        pytest.assume(created_report["most_requested_ingredient"])
        pytest.assume(created_report["most_requested_beverage"])
        pytest.assume(created_report["month_with_more_revenue"])
        pytest.assume(created_report["top_3_customers"])
