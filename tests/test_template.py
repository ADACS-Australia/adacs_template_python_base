from utils import bake_in_temp_dir, run_inside_dir


def test_make_docs(cookies):
    with bake_in_temp_dir(cookies) as result:
        run_inside_dir("make docs", str(result.project_path)) == 0


def test_bake_with_apostrophe_and_run_tests(cookies):
    """Ensure that a `full_name` with apostrophes does not break setup.py"""
    with bake_in_temp_dir(cookies, extra_context={"authors": "O'connor"}) as result:
        assert result.project_path.is_dir()
        assert result.exit_code == 0
        assert result.exception is None


# def test_bake_withspecialchars_and_run_tests(cookies):
#     """Ensure that a `full_name` with double quotes does not break setup.py"""
#     with bake_in_temp_dir(
#         cookies,
#         extra_context={'full_name': 'name "quote" name'}
#     ) as result:
#         assert result.project.is_dir()
#         run_inside_dir('python setup.py test', str(result.project)) == 0
#
#
# def test_bake_with_apostrophe_and_run_tests(cookies):
#     """Ensure that a `full_name` with apostrophes does not break setup.py"""
#     with bake_in_temp_dir(
#         cookies,
#         extra_context={'full_name': "O'connor"}
#     ) as result:
#         assert result.project.is_dir()
#         run_inside_dir('python setup.py test', str(result.project)) == 0
#
#
# # def test_bake_and_run_travis_pypi_setup(cookies):
# #     # given:
# #     with bake_in_temp_dir(cookies) as result:
# #         project_path = str(result.project)
# #
# #         # when:
# #         travis_setup_cmd = ('python travis_pypi_setup.py'
# #                             ' --repo audreyr/cookiecutter-pypackage'
# #                             ' --password invalidpass')
# #         run_inside_dir(travis_setup_cmd, project_path)
# #         # then:
# #         result_travis_config = yaml.load(
# #             result.project.join(".travis.yml").open()
# #         )
# #         min_size_of_encrypted_password = 50
# #         assert len(
# #             result_travis_config["deploy"]["password"]["secure"]
# #         ) > min_size_of_encrypted_password
#
#
# # def test_project_with_hyphen_in_module_name(cookies):
# #     result = cookies.bake(
# #         extra_context={'project_name': 'something-with-a-dash'}
# #     )
# #     assert result.project is not None
# #     project_path = str(result.project)
# #
# #     # when:
# #     travis_setup_cmd = ('python travis_pypi_setup.py'
# #                         ' --repo audreyr/cookiecutter-pypackage'
# #                         ' --password invalidpass')
# #     run_inside_dir(travis_setup_cmd, project_path)
# #
# #     # then:
# #     result_travis_config = yaml.load(
# #         open(os.path.join(project_path, ".travis.yml"))
# #     )
# #     assert "secure" in result_travis_config["deploy"]["password"],\
# #         "missing password config in .travis.yml"
#
#
#
# @pytest.mark.parametrize("use_black,expected", [("y", True), ("n", False)])
# def test_black(cookies, use_black, expected):
#     with bake_in_temp_dir(
#         cookies,
#         extra_context={'use_black': use_black}
#     ) as result:
#         assert result.project.is_dir()
#         requirements_path = result.project.join('requirements_dev.txt')
#         assert ("black" in requirements_path.read()) is expected
#         makefile_path = result.project.join('Makefile')
#         assert ("black --check" in makefile_path.read()) is expected
