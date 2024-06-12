import pytest
from src.widget import mask_account_card

@pytest.fixture
def card_or_account_info():
    return "Maestro 2345234545674567"


def test_mask_account_card(card_or_account_info):
    assert mask_account_card(card_or_account_info) == "Maestro 2345 23** **** 4567"
