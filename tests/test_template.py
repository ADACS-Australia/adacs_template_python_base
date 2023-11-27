import pytest
from utils import bake_in_temp_dir, run_inside_dir

test_these_changes_to_defaults = [
    ({"author": "Oconnor"}, 0, None),
    ({"author": 'name "quote" name'}, 0, None),
    ({"project_name": "something-with-a-dash"}, 0, None),
    ({"project_name": "something with a space"}, 0, None),
]


@pytest.fixture(params=test_these_changes_to_defaults)
def bake_path(cookies, request):
    extra_context = request.param[0]
    exit_code_expected = request.param[1]
    exception_expected = request.param[2]
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:
        assert result.project_path.is_dir()
        assert result.exit_code == exit_code_expected
        assert result.exception is exception_expected
        yield result.project_path


def test_bake_and_run_tests(bake_path):
    run_inside_dir("pytest", bake_path) == 0


def test_template_make_docs(bake_path):
    run_inside_dir("make docs", bake_path) == 0


def test_template_run_black(bake_path):
    run_inside_dir("black .", bake_path) == 0


def test_template_run_ruff(bake_path):
    run_inside_dir("ruff .", bake_path) == 0
