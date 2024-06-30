import pytest
from src.external_api import convert_from_eur_to_rub, convert_from_usd_to_rub

from unittest.mock import Mock
from unittest.mock import patch

@patch('requests.requests')
def test_convert_from_usd_to_rub(mock_requests):
    mock_requests.return_value.json.return_value = {"result": 60}
    assert convert_from_usd_to_rub(20) == 60
    mock_requests.assert_called_once_with







