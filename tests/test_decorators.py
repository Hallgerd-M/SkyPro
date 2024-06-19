import pytest
from src.decorators import log, my_function

def test_log(capsys):
    with pytest.raises(Exception):
        captured = capsys.readouterr()
        assert captured.out == "my_function error\n"
    @log
    def my_function(x = 2, y = 3):
        return x + y



"""
    result = my_function(2, 3)
   


def test_retry_decorator():
    with pytest.raises(Exception, match="Max retries exceeded"):
        example_function()

        hello_world()
        captured = capsys.readouterr()
        assert captured.out == "Hello, world!\n"
"""