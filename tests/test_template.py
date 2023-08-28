from utils import bake_in_temp_dir, run_inside_dir


def test_make_docs(cookies):
    with bake_in_temp_dir(cookies) as result:
        run_inside_dir('make docs', str(result.project_path)) == 0


def test_bake_with_apostrophe_and_run_tests(cookies):
    """Ensure that a `full_name` with apostrophes does not break setup.py"""
    with bake_in_temp_dir( cookies, extra_context={'authors': "O'connor"}) as result:
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
# def test_bake_without_travis_pypi_setup(cookies):
#     with bake_in_temp_dir(
#         cookies,
#         extra_context={'use_pypi_deployment_with_travis': 'n'}
#     ) as result:
#         result_travis_config = yaml.load(
#             result.project.join(".travis.yml").open(),
#             Loader=yaml.FullLoader
#         )
#         assert "deploy" not in result_travis_config
#         assert "python" == result_travis_config["language"]
#         # found_toplevel_files = [f.basename for f in result.project.listdir()]
#
#
# def test_bake_without_author_file(cookies):
#     with bake_in_temp_dir(
#         cookies,
#         extra_context={'create_author_file': 'n'}
#     ) as result:
#         found_toplevel_files = [f.basename for f in result.project.listdir()]
#         assert 'AUTHORS.rst' not in found_toplevel_files
#         doc_files = [f.basename for f in result.project.join('docs').listdir()]
#         assert 'authors.rst' not in doc_files
#
#         # Assert there are no spaces in the toc tree
#         docs_index_path = result.project.join('docs/index.rst')
#         with open(str(docs_index_path)) as index_file:
#             assert 'contributing\n   history' in index_file.read()
#
#         # Check that
#         manifest_path = result.project.join('MANIFEST.in')
#         with open(str(manifest_path)) as manifest_file:
#             assert 'AUTHORS.rst' not in manifest_file.read()
#
#
# def test_bake_selecting_license(cookies):
#     license_strings = {
#         'MIT license': 'MIT ',
#         'BSD license': 'Redistributions of source code must retain the ' +
#                        'above copyright notice, this',
#         'ISC license': 'ISC License',
#         'Apache Software License 2.0':
#             'Licensed under the Apache License, Version 2.0',
#         'GNU General Public License v3': 'GNU GENERAL PUBLIC LICENSE',
#     }
#     for license, target_string in license_strings.items():
#         with bake_in_temp_dir(
#             cookies,
#             extra_context={'open_source_license': license}
#         ) as result:
#             assert target_string in result.project.join('LICENSE').read()
#             assert license in result.project.join('setup.py').read()
#
#
# def test_bake_not_open_source(cookies):
#     with bake_in_temp_dir(
#         cookies,
#         extra_context={'open_source_license': 'Not open source'}
#     ) as result:
#         found_toplevel_files = [f.basename for f in result.project.listdir()]
#         assert 'setup.py' in found_toplevel_files
#         assert 'LICENSE' not in found_toplevel_files
#         assert 'License' not in result.project.join('README.rst').read()
#
#
# def test_using_pytest(cookies):
#     with bake_in_temp_dir(
#         cookies,
#         extra_context={'use_pytest': 'y'}
#     ) as result:
#         assert result.project.is_dir()
#         test_file_path = result.project.join(
#             'tests/test_python_boilerplate.py'
#         )
#         lines = test_file_path.readlines()
#         assert "import pytest" in ''.join(lines)
#         # Test the new pytest target
#         run_inside_dir('pytest', str(result.project)) == 0
#
#
# def test_not_using_pytest(cookies):
#     with bake_in_temp_dir(cookies) as result:
#         assert result.project.is_dir()
#         test_file_path = result.project.join(
#             'tests/test_python_boilerplate.py'
#         )
#         lines = test_file_path.readlines()
#         assert "import unittest" in ''.join(lines)
#         assert "import pytest" not in ''.join(lines)
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
# def test_bake_with_no_console_script(cookies):
#     context = {'command_line_interface': "No command-line interface"}
#     result = cookies.bake(extra_context=context)
#     project_path, project_slug, project_dir = project_info(result)
#     found_project_files = os.listdir(project_dir)
#     assert "cli.py" not in found_project_files
#
#     setup_path = os.path.join(project_path, 'setup.py')
#     with open(setup_path, 'r') as setup_file:
#         assert 'entry_points' not in setup_file.read()
#
#
#         project_slug])
#     assert noarg_output in noarg_result.output
#     help_result = runner.invoke(cli.main, ['--help'])
#     assert help_result.exit_code == 0
#     assert 'Show this message' in help_result.output
#
#
# def test_bake_with_argparse_console_script_cli(cookies):
#     context = {'command_line_interface': 'argparse'}
#     result = cookies.bake(extra_context=context)
#     project_path, project_slug, project_dir = project_info(result)
#     module_path = os.path.join(project_dir, 'cli.py')
#     module_name = '.'.join([project_slug, 'cli'])
#     spec = importlib.util.spec_from_file_location(module_name, module_path)
#     cli = importlib.util.module_from_spec(spec)
#     spec.loader.exec_module(cli)
#     runner = CliRunner()
#     noarg_result = runner.invoke(cli.main)
#     assert noarg_result.exit_code == 0
#     noarg_output = ' '.join([
#         'Replace this message by putting your code into',
#         project_slug])
#     assert noarg_output in noarg_result.output
#     help_result = runner.invoke(cli.main, ['--help'])
#     assert help_result.exit_code == 0
#     assert 'Show this message' in help_result.output
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
