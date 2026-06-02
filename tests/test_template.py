import pytest
from utils import bake_in_temp_dir, run_inside_dir

test_these_changes_to_defaults = [
    ({"author": "O'connor"}, 0, None),
    ({"author": 'name "quote" name'}, 0, None),
    ({"author": "Last, First"}, 0, None),
    ({"project_name": "something-with-a-dash"}, 0, None),
    ({"project_name": "something with a space"}, 0, None),
]


@pytest.fixture(params=test_these_changes_to_defaults)
def bake_path(cookies, request):
    extra_context = request.param[0]
    exit_code_expected = request.param[1]
    exception_expected = request.param[2]
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:
        assert result.exit_code == exit_code_expected
        assert result.exception is exception_expected
        assert result.project_path.is_dir()
        # Create a virtual env for testing this bake
        assert run_inside_dir(
            "python -m venv venv", result.project_path, source_env=False
        )
        # Install the baked project into its environment (with dev extras for pytest-cov etc.)
        assert run_inside_dir("poetry install --extras dev", result.project_path)
        yield result.project_path


def test_bake_and_check_poetry(bake_path):
    assert run_inside_dir("poetry check --lock", bake_path)


def test_bake_and_run_tests(bake_path):
    assert run_inside_dir("poetry run pytest", bake_path)


def test_template_make_docs(bake_path):
    assert run_inside_dir("poetry run make docs", bake_path)


def test_template_run_black(bake_path):
    assert run_inside_dir("poetry run black .", bake_path)


def test_template_run_ruff(bake_path):
    assert run_inside_dir("poetry run ruff check .", bake_path)
