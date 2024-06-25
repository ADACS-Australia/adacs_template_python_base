from {{cookiecutter.__package_name}} import BaseException
import pytest

def failing_funtion() -> None:
    raise BaseException("Function failed")

def test_exception_message() -> None:
    with pytest.raises(BaseException) as result:
        failing_funtion()
    assert str(result.value) == 'Function failed'
