import pytest
from src.masks import get_mask_account, get_mask_card_number

@pytest.fixture
def card_number():
    return 1324321343213213


@pytest.fixture
def account_number():
    return 13243213432186753213



def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "1324 32** **** 3213"

def test_get_mask_account(account_number):
    assert get_mask_account(account_number == "**3213")