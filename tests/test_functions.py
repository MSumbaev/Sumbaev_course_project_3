import pytest

from utils import functions


PATH = "tests/test_load_data.json"

test_operations = [
    {
        "id": 1,
        "state": "EXECUTED",
        "date": "2020-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
    {
        "id": 2,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    },
    {
        "id": 3,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "48223.05",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431"
    }
]


def get_test_operations():
    return test_operations


def test_load_data():
    assert functions.load_data(PATH) == [{"test": 123, "state": "EXECUTED"}]


def test_get_last_executed_operations():
    assert functions.get_last_executed_operations(get_test_operations(), 2) == test_operations[:2]
    assert functions.get_last_executed_operations(get_test_operations(), 1) == test_operations[:1]
    with pytest.raises(IndexError):
        functions.get_last_executed_operations(get_test_operations())


def test_get_formate_date():
    assert functions.get_format_date(get_test_operations()[1]) == "26.08.2019"


def test_get_description():
    assert functions.get_description(get_test_operations()[0]) == "Перевод организации"


def test_get_formatted_bank_accounts():
    assert functions.get_formatted_bank_accounts(get_test_operations()[0]) == "Maestro 1596 83** **** 5199 -> " \
                                                                               "Счет **9589"

    assert functions.get_formatted_bank_accounts(get_test_operations()[2]) == "Счет **2431"


def test_get_operation_amount():
    assert functions.get_operation_amount(get_test_operations()[1]) == "8221.37 USD"


def test_get_formatted_operations():
    assert functions.get_formatted_operations(get_test_operations())[2] == "12.09.2018 Открытие вклада" \
                                                                           "\nСчет **2431" \
                                                                           "\n48223.05 руб.\n"
