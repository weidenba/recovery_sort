from common_helper_process import execute_shell_command_get_return_code
from common_helper_files import get_dir_of_file
from tempfile import TemporaryDirectory
import os


SRC_DIR = os.path.join(get_dir_of_file(__file__), '../../')
TEST_DATA_DIR = os.path.join(get_dir_of_file(__file__), '../data')
MAINSCRIPT = os.path.join(SRC_DIR, 'recovery_sort.py')


def test_help():
    output, return_code = execute_shell_command_get_return_code('{} -h'.format(MAINSCRIPT), timeout=5)
    assert return_code == 0
    assert 'usage: recovery_sort.py' in output


def test_no_filter():
    tmp_dir = TemporaryDirectory()
    output, return_code = execute_shell_command_get_return_code('{} -i thumbnail -i not_existing {} {}'.format(MAINSCRIPT, TEST_DATA_DIR, tmp_dir.name), timeout=10)
    assert return_code == 0
    assert '[ERROR]: Filter "not_existing" is not available' in output
    assert '[recovery_sort][INFO]: Re-organizing complete' in output
    assert '[ReOrganizer][INFO]: 1 files ignored -> duplicate' in output
    assert '[ReOrganizer][INFO]: 0 files ignored -> thumbnail' in output
    tmp_dir.cleanup()


def test_all_filter_and_debug():
    tmp_dir = TemporaryDirectory()
    output, return_code = execute_shell_command_get_return_code('{} -I -R -d {} {}'.format(MAINSCRIPT, TEST_DATA_DIR, tmp_dir.name), timeout=10)
    assert return_code == 0
    assert '[DEBUG]' in output
    assert 'rename filters: [\'mp3\']'
    assert '[recovery_sort][INFO]: Re-organizing complete' in output
    tmp_dir.cleanup()
