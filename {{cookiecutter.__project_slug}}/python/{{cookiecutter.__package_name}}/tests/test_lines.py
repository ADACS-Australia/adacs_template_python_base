import {{cookiecutter.__package_name}}.lines as lines
import pytest

# Invalid inputs to 'create_line' and the exceptions expected
invalid_input = [["string", TypeError], [3.1415, TypeError], [-1, ValueError]]


def test_my_module_create_line_invalid_input() -> None:
    """Verify that invalid inputs generate appropriate exceptions"""
    for input_i, ex_expected in invalid_input:
        with pytest.raises(ex_expected):
            lines.create_line(input_i)
