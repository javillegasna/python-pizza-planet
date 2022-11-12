import pytest


def report_mock() -> dict:
    return {
        "most_requested_ingredient": {
            "name": "cheese",
            "price": 1,
            "count": 54,
        },
        "most_requested_beverage": {
            "name": "Sprite",
            "price": 1,
            "count": 30,
        },
        "month_with_more_revenue": {
            "name": "March",
            "total": 50,
        },
        "top_3_customers": [
            {
                "dni": "12",
                "name": "Jon",
                "address": "a1",
                "phone": "091",
                "total_spent": 1.5,
            },
            {
                "dni": "13",
                "name": "Ana",
                "address": "a2",
                "phone": "092",
                "total_spent": 150,
            },
            {
                "dni": "14",
                "name": "Marco",
                "address": "a3",
                "phone": "093",
                "total_spent": 154,
            },
        ],
    }


@pytest.fixture
def report_uri():
    return "/report/"


@pytest.fixture
def report():
    return report_mock()


@pytest.fixture
def create_report(client, report_uri) -> dict:
    response = client.get(report_uri, json=report_mock())
    return response
