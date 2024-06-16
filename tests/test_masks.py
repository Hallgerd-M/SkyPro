import pytest

from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state


@pytest.fixture
def card_number():
    return 1324321343213213


@pytest.fixture
def account_number():
    return 3243213432186753213


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "1324 32** **** 3213"


def test_get_mask_account(account_number):
    assert get_mask_account(account_number) == "**3213"


@pytest.fixture
def transaction():
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
        },
    ]


def test_filter_by_state(my_dictionary):
    assert filter_by_state(my_dictionary) == [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
    ]
