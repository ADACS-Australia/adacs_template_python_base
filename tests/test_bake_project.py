import datetime
import pathlib
from utils import bake_in_temp_dir


def test_year_in_license_file(cookies):
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project_path / "LICENSE"
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read_text()


def test_bake_with_defaults(cookies):

    # List of filenames that need to be present in a properly rendered template
    check_toplevel_pathnames = [
        ".git",
        ".github",
        ".gitignore",
        ".pre-commit-config.yaml",
        ".pre-commit-db.json",
        ".readthedocs.yml",
        "LICENSE",
        "README.md",
        "docs",
        "docs/Makefile",
        "pyproject.toml",
        "python",
    ]

    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_pathnames = set()
        root_dir = result.project_path
        git_path = root_dir / ".git"
        for path_i in root_dir.rglob("*"):
            if git_path not in path_i.parents:
                found_toplevel_pathnames.add(path_i)
            else:
                found_toplevel_pathnames.add(git_path)

        # Check that the needed files from the base project are present
        for path_i in check_toplevel_pathnames:
            assert root_dir / pathlib.Path(path_i) in found_toplevel_pathnames
