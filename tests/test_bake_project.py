import datetime
from utils import bake_in_temp_dir


def test_year_in_license_file(cookies):
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project_path / "LICENSE"
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read_text()


def test_bake_with_defaults(cookies):

    check_toplevel_pathnames = [
        ".git",
        ".github",
        ".gitignore",
        ".pre-commit-config.yaml",
        ".pre-commit-db.json",
        ".readthedocs.yml",
        "LICENSE",
        "Makefile",
        "README.md",
        "docs",
        "pyproject.toml",
        "python",
    ]

    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_pathnames = [
            path_i.name for path_i in result.project_path.iterdir()
        ]

        for filename_i in check_toplevel_pathnames:
            assert filename_i in found_toplevel_pathnames
