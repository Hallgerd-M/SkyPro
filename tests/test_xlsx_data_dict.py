from unittest.mock import patch

from src.xlsx_data_dict import get_xlsx_data_dict


@patch("pandas.read_excel")
def test_xlsx_data_dict(mock_dict):
    mock_dict.return_list = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {
                "amount": "16210",
                "currency": {"name": "Sol", "code": "PEN"},
            },
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "operationAmount": {
                "amount": "29740",
                "currency": {"name": "Peso", "code": "COP"},
            },
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
        },
    ]
    assert get_xlsx_data_dict("test_log.txt") == [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {
                "amount": "16210",
                "currency": {"name": "Sol", "code": "PEN"},
            },
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "operationAmount": {
                "amount": "29740",
                "currency": {"name": "Peso", "code": "COP"},
            },
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
        },
    ]
    mock_dict.assert_called_once_with("../data/transactions_excel.xlsx")


def test_xlsx_data_dict_1():
    assert get_xlsx_data_dict("../data/test_excel.xlsx") == [{}]
